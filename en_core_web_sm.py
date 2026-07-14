"""In-browser stub for the spaCy model package ``en_core_web_sm``.

The real spaCy model packages cannot install in the Pyodide (in-browser)
runtime. Notebooks load a model two ways — ``spacy.load("en_core_web_sm")`` and
``import en_core_web_sm; nlp = en_core_web_sm.load()``. The ``spacy`` shim
handles the first; this module handles the second by delegating to it. English
is backed by real NLTK part-of-speech tagging and named-entity recognition.
"""

import spacy


def load(**kwargs):
    return spacy.load("en_core_web_sm")
