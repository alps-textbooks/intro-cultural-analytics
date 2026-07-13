"""In-browser compatibility shim for ``little_mallet_wrapper``.

The upstream package is a thin wrapper that shells out to the MALLET **Java**
binary, which cannot run in the browser (Pyodide) runtime — there is no JVM.
This module reimplements the functions the Intro-Cultural-Analytics notebooks
use on top of scikit-learn's :class:`~sklearn.decomposition.LatentDirichletAllocation`,
so those notebooks run unchanged.

Behavioural note: this is a different LDA implementation than MALLET, so the
topic *numbering/ordering* and exact word rankings will not match a MALLET run —
but the workflow (preprocess → train → inspect topics → per-document
distributions) and the shape of every return value are the same. Results are
reproducible via a fixed ``random_state``.

``quick_train_topic_model`` writes MALLET-shaped ``mallet.topic_keys.<k>`` and
``mallet.topic_distributions.<k>`` files to the output directory, exactly where
the notebooks then read them from with ``load_topic_keys`` /
``load_topic_distributions``.
"""

import os
import re
import string

# scikit-learn backs the LDA in ``quick_train_topic_model``. It is imported at
# module top level, as a plain (unguarded) import, so the in-browser runtime's
# import scanner sees it as a dependency and installs scikit-learn before this
# module runs. The scanner only detects direct top-level imports — an import
# nested in a function or wrapped in try/except is invisible to it, so those
# forms would leave scikit-learn uninstalled and fail at call time.
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# Top words kept per topic when writing the topic-keys file (MALLET default is 20).
_WORDS_PER_TOPIC = 20

_STOPWORDS = None


def _english_stopwords():
    """English stopword set, from NLTK if its corpus is present, else a small builtin."""
    global _STOPWORDS
    if _STOPWORDS is None:
        try:
            from nltk.corpus import stopwords
            _STOPWORDS = set(stopwords.words("english"))
        except Exception:
            # Minimal fallback so preprocessing still runs if the corpus is absent.
            _STOPWORDS = {
                "the", "a", "an", "and", "or", "but", "if", "of", "to", "in", "on",
                "for", "with", "as", "is", "are", "was", "were", "be", "been", "being",
                "it", "its", "this", "that", "these", "those", "at", "by", "from",
                "he", "she", "they", "we", "you", "i", "his", "her", "their", "our",
                "not", "no", "so", "than", "then", "there", "here", "what", "which",
                "who", "whom", "will", "would", "can", "could", "should", "do", "does",
                "did", "have", "has", "had", "about", "into", "over", "after", "up",
            }
    return _STOPWORDS


def process_string(text, lowercase=True, remove_short_words=True,
                   remove_stop_words=True, remove_punctuation=True,
                   numbers="remove", stop_words=None):
    """Clean a single document string for topic modeling.

    Mirrors ``little_mallet_wrapper.process_string``: lowercase, strip
    punctuation, optionally drop numbers/short words/stopwords, collapse
    whitespace, and return the cleaned string.
    """
    if text is None:
        return ""
    text = str(text)
    if lowercase:
        text = text.lower()
    if remove_punctuation:
        text = re.sub("[%s]" % re.escape(string.punctuation), " ", text)
    if numbers == "remove":
        text = re.sub(r"\d+", " ", text)

    if stop_words is not None:
        sw = set(stop_words)
    elif remove_stop_words:
        sw = _english_stopwords()
    else:
        sw = set()

    tokens = []
    for tok in text.split():
        if remove_stop_words and tok in sw:
            continue
        if remove_short_words and len(tok) <= 2:
            continue
        tokens.append(tok)
    return " ".join(tokens)


def print_dataset_stats(training_data):
    """Print corpus stats (document count, mean length, vocabulary size)."""
    docs = list(training_data)
    n = len(docs)
    lengths = [len(d.split()) for d in docs]
    vocab = set()
    for d in docs:
        vocab.update(d.split())
    mean_len = (sum(lengths) / n) if n else 0
    print("Number of Documents:", n)
    print("Mean Number of Words per Document:", round(mean_len, 1))
    print("Vocabulary Size:", len(vocab))


def _write_lines(path, lines):
    parent = os.path.dirname(path)
    if parent and not os.path.isdir(parent):
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        for line in lines:
            fh.write(line + "\n")


def quick_train_topic_model(path_to_mallet, output_directory_path, num_topics,
                            training_data, training_ids=None, **kwargs):
    """Train an LDA topic model (scikit-learn) and write MALLET-shaped outputs.

    ``path_to_mallet`` is accepted for signature compatibility and ignored — there
    is no MALLET binary in the browser. Writes::

        <output_directory_path>/mallet.topic_keys.<num_topics>
        <output_directory_path>/mallet.topic_distributions.<num_topics>

    which ``load_topic_keys`` / ``load_topic_distributions`` read back.
    Returns ``(topic_keys, topic_distributions)``.
    """
    docs = [d if isinstance(d, str) else " ".join(d) for d in training_data]
    num_topics = int(num_topics)

    vectorizer = CountVectorizer(token_pattern=r"(?u)\b\w+\b")
    dtm = vectorizer.fit_transform(docs)
    vocab = vectorizer.get_feature_names_out()

    lda = LatentDirichletAllocation(
        n_components=num_topics, random_state=0,
        learning_method="batch", max_iter=int(kwargs.get("iterations", 20)),
    )
    doc_topics = lda.fit_transform(dtm)

    # Row-normalize the document-topic matrix to probabilities.
    row_sums = doc_topics.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1.0
    doc_topics = doc_topics / row_sums

    topic_keys = []
    for component in lda.components_:
        top_idx = component.argsort()[::-1][:_WORDS_PER_TOPIC]
        topic_keys.append([str(vocab[i]) for i in top_idx])

    topic_distributions = [[float(p) for p in row] for row in doc_topics]

    if output_directory_path:
        _write_lines(
            "%s/mallet.topic_keys.%s" % (output_directory_path, num_topics),
            [" ".join(words) for words in topic_keys],
        )
        _write_lines(
            "%s/mallet.topic_distributions.%s" % (output_directory_path, num_topics),
            [" ".join("%.6f" % p for p in row) for row in topic_distributions],
        )

    return topic_keys, topic_distributions


def load_topic_keys(topic_keys_path):
    """Read a ``mallet.topic_keys.*`` file → list of per-topic word lists."""
    topics = []
    with open(topic_keys_path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            # MALLET writes "<topic>\t<alpha>\t<words>"; our writer writes just words.
            words = parts[-1].split() if len(parts) > 1 else line.split()
            topics.append(words)
    return topics


def load_topic_distributions(topic_distributions_path):
    """Read a ``mallet.topic_distributions.*`` file → list of per-doc prob lists."""
    distributions = []
    with open(topic_distributions_path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            values = parts[-1].split() if len(parts) > 1 else line.split()
            distributions.append([float(x) for x in values])
    return distributions


def get_top_docs(training_data, topic_distributions, topic_index, n=5):
    """Return the ``n`` documents most associated with ``topic_index``.

    List of ``(probability, document)`` sorted by that topic's probability,
    matching the upstream signature the notebooks iterate over.
    """
    paired = list(zip(topic_distributions, training_data))
    paired.sort(key=lambda pair: pair[0][topic_index], reverse=True)
    return [(dist[topic_index], doc) for dist, doc in paired[:n]]


def plot_categories_by_topics_heatmap(labels, topic_distributions, topic_keys=None,
                                      output_path=None, target_labels=None, dim=None):
    """Heatmap of mean topic probability per category label.

    ``labels`` is parallel to ``topic_distributions`` (one label per document).
    Aggregates the mean topic distribution for each unique label and renders a
    category-by-topic heatmap (seaborn), matching the upstream helper.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    try:
        import seaborn as sns
    except Exception:
        sns = None

    labels = list(labels)
    dist = np.asarray(topic_distributions, dtype=float)
    num_topics = dist.shape[1]

    unique = target_labels if target_labels else sorted(set(labels))
    matrix = []
    for lab in unique:
        rows = [dist[i] for i, l in enumerate(labels) if l == lab]
        matrix.append(np.mean(rows, axis=0) if rows else np.zeros(num_topics))
    matrix = np.asarray(matrix)

    if topic_keys:
        col_labels = ["Topic %d\n%s" % (i, " ".join(topic_keys[i][:3])) for i in range(num_topics)]
    else:
        col_labels = ["Topic %d" % i for i in range(num_topics)]

    fig_w, fig_h = (dim if dim else (max(8, num_topics), max(4, len(unique) * 0.6)))
    plt.figure(figsize=(fig_w, fig_h))
    if sns is not None:
        sns.heatmap(matrix, xticklabels=col_labels, yticklabels=unique,
                    cmap="Blues", annot=False)
    else:
        plt.imshow(matrix, aspect="auto", cmap="Blues")
        plt.xticks(range(num_topics), col_labels, rotation=90)
        plt.yticks(range(len(unique)), unique)
        plt.colorbar()
    plt.tight_layout()
    if output_path:
        plt.savefig(output_path)
    plt.show()


def divide_training_data(training_data, num_chunks=10):
    """Split a corpus into ``num_chunks`` contiguous chunks (upstream helper)."""
    docs = list(training_data)
    if num_chunks <= 0:
        return [docs]
    size = max(1, len(docs) // num_chunks)
    return [docs[i:i + size] for i in range(0, len(docs), size)]


def infer_topics(*args, **kwargs):
    raise NotImplementedError(
        "little_mallet_wrapper.infer_topics is not supported in the browser runtime; "
        "retrain with quick_train_topic_model instead."
    )
