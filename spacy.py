"""In-browser compatibility shim for spaCy.

spaCy depends on compiled C-extensions (blis, thinc, cymem, preshed,
murmurhash) with no WebAssembly wheels, so it cannot install in the browser
(Pyodide) runtime. This module provides an APPROXIMATE spaCy backed by NLTK
(bundled) for the API surface the Intro-Cultural-Analytics notebooks use:
``spacy.load``, ``nlp(text)``, token/span attributes (``.text``, ``.pos_``,
``.tag_``, ``.lemma_``, ``.dep_``, ``.is_alpha``), ``.ents``, ``.sents``,
``nlp.pipe``, ``nlp.get_pipe``, and ``displacy``.

Results are APPROXIMATE and differ from spaCy's trained models:
  * English (``en_core_web_sm``) is real NLTK POS tagging + NER + sentence
    segmentation, with a light rule-based lemmatizer (WordNet is too large to
    ship, so ``.lemma_`` is approximate) and no dependency parse (``.dep_``).
  * Non-English models (es/da/pt/ru/zh) have no NLTK equivalent, so they
    degrade to whitespace/character tokenization with no POS/NER, and announce
    that clearly. This is a run-only stand-in, not a replacement.

The required NLTK corpora (averaged_perceptron_tagger_eng, punkt_tab,
maxent_ne_chunker_tab, words) ship as curriculum content under ``nltk_data/``;
this module points ``nltk.data.path`` at ``/textbook/nltk_data`` so NLTK finds
them.
"""

import re

import nltk

# The NLTK corpora ride along as a SINGLE tarball (nltk_data.tar.gz) shipped as
# curriculum content. Shipping the corpora as hundreds of individual files would
# make each one its own curriculum item and overwhelm the import's per-file
# fan-out. Extract the tarball once into the in-memory FS and point
# nltk.data.path at it; the tarball is fetched from /textbook on first read.
def _load_spacy_corpora():
    import os
    import tarfile
    dest = "/nltk_data_spacy"
    if dest in nltk.data.path:
        return
    try:
        if not os.path.isdir(os.path.join(dest, "taggers")):
            with tarfile.open("/textbook/nltk_data.tar.gz", "r:gz") as _tar:
                _tar.extractall(dest)
        nltk.data.path.insert(0, dest)
    except Exception as _e:
        print("[spacy-shim] NLTK corpora unavailable (%s); POS/NER limited." % _e)


_load_spacy_corpora()

__version__ = "3.7.0"  # advertise a plausible spaCy version for cells that check

# ---- language handling -------------------------------------------------------
# spaCy model name -> ISO language. Only English is backed by real NLTK models.
_MODEL_LANG = {
    "en_core_web_sm": "en", "en_core_web_md": "en", "en_core_web_lg": "en",
    "en": "en", "english": "en",
    "es_core_news_md": "es", "es_core_news_sm": "es",
    "da_core_news_md": "da", "pt_core_news_md": "pt",
    "ru_core_news_md": "ru", "zh_core_web_md": "zh", "zh_core_web_sm": "zh",
}

# Penn Treebank -> Universal POS (spaCy's coarse ``.pos_``).
_PTB_TO_UPOS = {
    "NN": "NOUN", "NNS": "NOUN", "NNP": "PROPN", "NNPS": "PROPN",
    "VB": "VERB", "VBD": "VERB", "VBG": "VERB", "VBN": "VERB", "VBP": "VERB",
    "VBZ": "VERB", "MD": "AUX",
    "JJ": "ADJ", "JJR": "ADJ", "JJS": "ADJ",
    "RB": "ADV", "RBR": "ADV", "RBS": "ADV", "WRB": "ADV",
    "PRP": "PRON", "PRP$": "PRON", "WP": "PRON", "WP$": "PRON", "EX": "PRON",
    "DT": "DET", "PDT": "DET", "WDT": "DET",
    "IN": "ADP", "CC": "CCONJ", "CD": "NUM", "RP": "PART", "TO": "PART",
    "POS": "PART", "UH": "INTJ", "FW": "X", "LS": "X", "SYM": "SYM",
    "$": "SYM", "#": "SYM",
}

# NLTK chunker labels -> spaCy entity labels.
_NE_TO_SPACY = {
    "PERSON": "PERSON", "ORGANIZATION": "ORG", "GPE": "GPE",
    "LOCATION": "LOC", "FACILITY": "FAC", "GSP": "GPE", "FAC": "FAC",
}

# spaCy's English NER label inventory (for get_pipe('ner').labels).
_ENGLISH_ENT_LABELS = ("PERSON", "ORG", "GPE", "LOC", "FAC", "NORP", "PRODUCT",
                       "EVENT", "WORK_OF_ART", "LAW", "LANGUAGE", "DATE", "TIME",
                       "PERCENT", "MONEY", "QUANTITY", "ORDINAL", "CARDINAL")

_IRREGULAR = {
    "was": "be", "were": "be", "is": "be", "are": "be", "am": "be", "been": "be",
    "has": "have", "had": "have", "did": "do", "does": "do", "done": "do",
    "men": "man", "women": "woman", "children": "child", "people": "person",
    "went": "go", "gone": "go", "made": "make", "said": "say",
}


def _find_token_offset(text, tok, offset):
    """Locate ``tok`` in ``text`` at/after ``offset``, accounting for the
    substitutions ``word_tokenize`` makes (straight/curly quotes -> `` or '' ;
    brackets -> -LRB-/-RRB- etc.). Returns ``(idx, matched_length)`` so token
    ``.idx`` (and displacy entity highlighting) line up with the source text."""
    subs = {
        "``": ('"', "“", "``"), "''": ('"', "”", "''"),
        "-LRB-": ("(",), "-RRB-": (")",), "-LSB-": ("[",), "-RSB-": ("]",),
        "-LCB-": ("{",), "-RCB-": ("}",),
    }
    best = None
    for cand in subs.get(tok, (tok,)):
        i = text.find(cand, offset)
        if i >= 0 and (best is None or i < best[0]):
            best = (i, len(cand))
    return best if best is not None else (offset, len(tok))


def _lemmatize(word, upos):
    """Light rule-based lemmatizer (approximate — WordNet is too big to ship)."""
    low = word.lower()
    if low in _IRREGULAR:
        return _IRREGULAR[low]
    if upos == "VERB" or upos == "AUX":
        for suf, repl in (("ing", ""), ("ed", ""), ("ies", "y"), ("es", ""), ("s", "")):
            if low.endswith(suf) and len(low) - len(suf) >= 3:
                base = low[: len(low) - len(suf)] + repl
                return base
    if upos in ("NOUN", "PROPN"):
        if low.endswith("ies") and len(low) > 4:
            return low[:-3] + "y"
        if low.endswith("ses") or low.endswith("xes") or low.endswith("zes"):
            return low[:-2]
        if low.endswith("s") and not low.endswith("ss") and len(low) > 3:
            return low[:-1]
    return low


class Token:
    def __init__(self, doc, text, idx, i, tag):
        self.doc = doc
        self.text = text
        self.idx = idx          # char offset
        self.i = i              # token index
        self.tag_ = tag or ""   # fine-grained (Penn for English)
        self.pos_ = _PTB_TO_UPOS.get(tag, "PUNCT" if not any(c.isalnum() for c in text) else "X")
        self.dep_ = ""          # no dependency parse in this shim
        self.ent_type_ = ""
        self.is_alpha = text.isalpha()
        self.is_stop = text.lower() in _STOPWORDS
        self.is_punct = not any(c.isalnum() for c in text)
        self.is_space = text.isspace()
        self.like_num = text.isdigit()

    @property
    def lemma_(self):
        return _lemmatize(self.text, self.pos_)

    @property
    def head(self):
        return self  # no parse; token is its own head

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text


class Span:
    def __init__(self, doc, start, end, label=""):
        self.doc = doc
        self.start = start      # token index
        self.end = end
        self.label_ = label

    @property
    def text(self):
        toks = self.doc._tokens[self.start:self.end]
        return " ".join(t.text for t in toks)

    @property
    def ents(self):
        # Entities of the parent doc that fall within this span. Notebooks
        # usually re-parse a sentence via nlp(sentence.text), but support
        # sentence.ents too for robustness.
        return tuple(
            e for e in self.doc._ents
            if e.start >= self.start and e.end <= self.end
        )

    def __iter__(self):
        return iter(self.doc._tokens[self.start:self.end])

    def __len__(self):
        return self.end - self.start

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text


class Doc:
    def __init__(self, nlp, text):
        self.text = text
        self._nlp = nlp
        self._tokens = []
        self._sents = []       # list[Span]
        self._ents = []        # list[Span]
        nlp._analyze(self, text)

    def __iter__(self):
        return iter(self._tokens)

    def __len__(self):
        return len(self._tokens)

    def __getitem__(self, i):
        return self._tokens[i]

    @property
    def ents(self):
        return tuple(self._ents)

    @property
    def sents(self):
        return iter(self._sents)

    @property
    def noun_chunks(self):
        # Approximate: contiguous NOUN/PROPN/ADJ runs.
        chunks = []
        i, n = 0, len(self._tokens)
        while i < n:
            if self._tokens[i].pos_ in ("NOUN", "PROPN"):
                j = i
                while j < n and self._tokens[j].pos_ in ("NOUN", "PROPN", "ADJ"):
                    j += 1
                chunks.append(Span(self, i, j, ""))
                i = j
            else:
                i += 1
        return iter(chunks)

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text


class _NERPipe:
    labels = _ENGLISH_ENT_LABELS


class Language:
    def __init__(self, lang, model):
        self.lang = lang
        self.model_name = model
        self._is_english = lang == "en"
        self.pipe_names = ["tagger", "parser", "ner"]
        if not self._is_english:
            print(
                "[spacy-shim] '%s' has no NLTK model in the in-browser runtime; "
                "tokenization only, no POS/NER (results are approximate)." % model
            )

    def _analyze(self, doc, text):
        if self._is_english:
            self._analyze_english(doc, text)
        else:
            self._analyze_degraded(doc, text)

    def _analyze_english(self, doc, text):
        # sentence + word tokenize, POS tag, NER via NLTK.
        offset = 0
        tokens = []
        sent_spans = []
        for sent in nltk.sent_tokenize(text):
            s_start = len(tokens)
            words = nltk.word_tokenize(sent)
            tagged = nltk.pos_tag(words)
            for (w, tag) in tagged:
                idx, wlen = _find_token_offset(text, w, offset)
                offset = idx + wlen
                tokens.append(Token(doc, w, idx, len(tokens), tag))
            sent_spans.append((s_start, len(tokens), tagged))
        doc._tokens = tokens
        doc._sents = [Span(doc, a, b) for (a, b, _t) in sent_spans]
        # NER: run ne_chunk per sentence, map char/token spans.
        ents = []
        ti = 0
        for (a, b, tagged) in sent_spans:
            try:
                tree = nltk.ne_chunk(tagged)
            except Exception:
                ti = b
                continue
            k = a
            for node in tree:
                if hasattr(node, "label"):
                    span_len = len(node.leaves())
                    label = _NE_TO_SPACY.get(node.label(), node.label())
                    ents.append(Span(doc, k, k + span_len, label))
                    for t in doc._tokens[k:k + span_len]:
                        t.ent_type_ = label
                    k += span_len
                else:
                    k += 1
        doc._ents = ents

    def _analyze_degraded(self, doc, text):
        # No POS/NER for unsupported languages: whitespace/char tokenize only.
        tokens = []
        if self.lang == "zh":
            # Chinese has no spaces; approximate one token per character.
            for ch in text:
                if ch.strip():
                    idx = text.find(ch)
                    tokens.append(Token(doc, ch, idx, len(tokens), ""))
        else:
            offset = 0
            for w in re.findall(r"\w+|[^\w\s]", text, re.UNICODE):
                idx = text.find(w, offset)
                offset = idx + len(w)
                tokens.append(Token(doc, w, idx, len(tokens), ""))
        doc._tokens = tokens
        doc._sents = [Span(doc, 0, len(tokens))] if tokens else []
        doc._ents = []

    def __call__(self, text):
        return Doc(self, text)

    def pipe(self, texts, **kwargs):
        for t in texts:
            yield Doc(self, t)

    def get_pipe(self, name):
        return _NERPipe()

    @property
    def vocab(self):
        return _Vocab()


class _Vocab:
    def __getitem__(self, key):
        return None

    def __contains__(self, key):
        return False


_STOPWORDS = set(
    "a an the and or but if while of to in on at by for with from into is are was "
    "were be been being have has had do does did this that these those i you he she "
    "it we they them his her its our their as not no".split()
)


def load(model="en_core_web_sm", **kwargs):
    lang = _MODEL_LANG.get(model)
    if lang is None:
        # Unknown model name: guess by prefix, default English.
        prefix = model.split("_", 1)[0]
        lang = prefix if prefix in ("es", "da", "pt", "ru", "zh") else "en"
    return Language(lang, model)


def blank(lang="en", **kwargs):
    return Language(lang if lang in ("es", "da", "pt", "ru", "zh") else "en", lang)


# ---- displacy ---------------------------------------------------------------
class _Displacy:
    def render(self, docs, style="dep", jupyter=None, options=None, **kwargs):
        if isinstance(docs, (Doc,)):
            docs = [docs]
        html = "".join(self._render_one(d, style) for d in docs)
        # Match spaCy: when jupyter is None it auto-detects a notebook kernel and
        # renders inline (returning None); only jupyter=False returns the raw HTML
        # string. Rendering inline shows highlighted entities instead of raw markup.
        if jupyter is not False:
            try:
                from IPython.display import HTML, display
                display(HTML(html))
                return None
            except Exception:
                pass
        return html

    def serve(self, *args, **kwargs):
        raise NotImplementedError(
            "displacy.serve starts a web server, unavailable in the browser runtime; "
            "use displacy.render(...) instead."
        )

    def _render_one(self, doc, style):
        if style == "ent":
            return self._render_ents(doc)
        return self._render_dep(doc)

    def _render_ents(self, doc):
        colors = {"PERSON": "#aa9cfc", "ORG": "#7aecec", "GPE": "#feca74",
                  "LOC": "#ff9561", "FAC": "#9cc9cc", "DATE": "#bfe1d9"}
        out = []
        last = 0
        text = doc.text
        for ent in doc._ents:
            start_char = doc._tokens[ent.start].idx
            end_tok = doc._tokens[ent.end - 1]
            end_char = end_tok.idx + len(end_tok.text)
            out.append(_escape(text[last:start_char]))
            bg = colors.get(ent.label_, "#ddd")
            # The label is bracketed as literal text (not just styled) so it stays
            # legible after the runtime's rich-output sanitizer strips inline
            # styles — "Ada Lovelace [PERSON]" rather than a run-together
            # "Ada LovelacePERSON". The colored <mark> is kept for environments
            # that do preserve styles.
            out.append(
                '<mark style="background:%s;padding:0.2em 0.4em;border-radius:0.3em;">'
                '%s <span style="font-size:0.7em;font-weight:bold;margin-left:0.4em;">[%s]</span></mark>'
                % (bg, _escape(text[start_char:end_char]), ent.label_)
            )
            last = end_char
        out.append(_escape(text[last:]))
        return '<div style="line-height:2.2;">%s</div>' % "".join(out)

    def _render_dep(self, doc):
        # No dependency parse in this shim: show the POS-tagged tokens instead.
        cells = "".join(
            '<div style="text-align:center;margin:0 0.4em;">'
            '<div>%s</div><div style="color:#888;font-size:0.8em;">%s</div></div>'
            % (_escape(t.text), t.pos_)
            for t in doc._tokens
        )
        return ('<div style="display:flex;flex-wrap:wrap;">%s</div>'
                '<div style="color:#a00;font-size:0.8em;">(approximate: dependency '
                'parse unavailable in the in-browser runtime)</div>' % cells)


def _escape(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


displacy = _Displacy()
