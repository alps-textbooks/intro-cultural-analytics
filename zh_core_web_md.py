"""In-browser stub for the spaCy model package ``zh_core_web_md``.

The real spaCy model packages cannot install in the Pyodide (in-browser)
runtime. Notebooks load a model two ways — ``spacy.load("zh_core_web_md")`` and
``import zh_core_web_md; nlp = zh_core_web_md.load()``. The ``spacy`` shim handles the first; this
module handles the second by delegating to it. Only English is backed by real
NLTK models; this non-English model degrades to whitespace tokenization (the
shim prints a note when loaded).
"""

import spacy


def load(**kwargs):
    return spacy.load("zh_core_web_md")
