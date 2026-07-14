"""In-browser stub for the spaCy model package ``es_core_news_md``.

The real spaCy model packages cannot install in the Pyodide (in-browser)
runtime. Notebooks load a model two ways — ``spacy.load("es_core_news_md")`` and
``import es_core_news_md; nlp = es_core_news_md.load()``. The ``spacy`` shim handles the first; this
module handles the second by delegating to it. Only English is backed by real
NLTK models; this non-English model degrades to whitespace tokenization (the
shim prints a note when loaded).
"""

import spacy


def load(**kwargs):
    return spacy.load("es_core_news_md")
