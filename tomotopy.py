"""In-browser compatibility shim for ``tomotopy``.

Upstream ``tomotopy`` is a compiled C++ extension with no WebAssembly wheel, so
it cannot install in the browser (Pyodide) runtime. This module provides the
small ``LDAModel`` surface the Intro-Cultural-Analytics "Topic Modeling Without
MALLET" notebook uses, backed by scikit-learn's
:class:`~sklearn.decomposition.LatentDirichletAllocation`, so the notebook runs
unchanged.

Supported: ``tp.LDAModel(k=...)``, ``model.add_doc(words)``, ``model.train(n)``,
``model.ll_per_word``, ``model.get_topic_words(topic_id, top_n)``,
``model.docs`` and ``doc.get_topic_dist()``. The model is (re)fit lazily. Because
this is a variational sklearn LDA rather than tomotopy's Gibbs sampler, the exact
topic numbering and log-likelihood values differ, but the API and result shapes
match. ``random_state`` is fixed for reproducibility.
"""

# scikit-learn backs the LDA fit. It is imported at module top level, as a plain
# (unguarded) import, so the in-browser runtime's import scanner sees it as a
# dependency and installs scikit-learn before this module runs. The scanner only
# detects direct top-level imports — one nested in a method or wrapped in
# try/except is invisible to it and would leave scikit-learn uninstalled.
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation


class _Doc:
    """A trained document; ``get_topic_dist()`` returns its topic probabilities."""

    def __init__(self, topic_dist, words):
        self._topic_dist = topic_dist
        self.words = words

    def get_topic_dist(self):
        return list(self._topic_dist)


class LDAModel:
    def __init__(self, k=10, **kwargs):
        self.k = int(k)
        self._raw_docs = []          # list[list[str]]
        self._iterations = 0
        self._dirty = True
        self._docs = []
        self._components = None
        self._vocab = None
        self._ll_per_word = 0.0
        self._dtm = None             # cached document-term matrix (rebuilt only when docs change)

    def add_doc(self, words):
        """Add a document as a list (or space-joined string) of tokens."""
        if isinstance(words, str):
            words = words.split()
        self._raw_docs.append(list(words))
        self._dirty = True
        self._dtm = None             # documents changed → drop the cached vectorization
        return len(self._raw_docs) - 1

    def train(self, iterations=10, **kwargs):
        """Accumulate training iterations; the fit happens lazily on next read."""
        self._iterations += int(iterations)
        self._dirty = True

    def _fit(self):
        if not self._dirty:
            return
        # Vectorize once and cache: the notebooks call train() in a loop and read
        # a property after each call, so this refits repeatedly on the same docs.
        if self._dtm is None:
            vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
            self._dtm = vectorizer.fit_transform([" ".join(d) for d in self._raw_docs])
            self._vocab = vectorizer.get_feature_names_out()

        lda = LatentDirichletAllocation(
            n_components=self.k, random_state=0, learning_method="batch",
            # Cap the iteration count: scikit-learn's batch LDA converges quickly
            # for topic modeling, while the notebooks accumulate up to ~100
            # "iterations" (a Gibbs-sampling notion) that would make each in-browser
            # refit needlessly slow.
            max_iter=min(max(10, self._iterations), 30),
        )
        doc_topics = lda.fit_transform(self._dtm)
        row_sums = doc_topics.sum(axis=1, keepdims=True)
        row_sums[row_sums == 0] = 1.0
        doc_topics = doc_topics / row_sums

        self._components = lda.components_
        self._docs = [_Doc(doc_topics[i], self._raw_docs[i]) for i in range(len(self._raw_docs))]

        total_words = self._dtm.sum()
        self._ll_per_word = float(lda.score(self._dtm) / total_words) if total_words else 0.0
        self._dirty = False

    @property
    def docs(self):
        self._fit()
        return self._docs

    @property
    def ll_per_word(self):
        self._fit()
        return self._ll_per_word

    @property
    def num_vocabs(self):
        self._fit()
        return len(self._vocab)

    def get_topic_words(self, topic_id, top_n=10):
        """Return the ``top_n`` ``(word, probability)`` pairs for a topic."""
        self._fit()
        component = self._components[topic_id]
        total = component.sum()
        total = total if total else 1.0
        order = component.argsort()[::-1][:top_n]
        return [(str(self._vocab[i]), float(component[i] / total)) for i in order]

    def summary(self):
        self._fit()
        print("LDAModel (sklearn-backed shim)")
        print("  topics (k):", self.k)
        print("  docs:", len(self._raw_docs))
        print("  vocab:", len(self._vocab) if self._vocab is not None else 0)
        print("  log-likelihood per word:", round(self._ll_per_word, 4))
