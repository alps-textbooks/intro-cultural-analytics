# ALPS Compatibility Review
This file lists notebook snippets from `book/_toc.yml` that may still need human review for ALPS/Pyodide compatibility after the mechanical fixes.
## Mechanical Changes Applied
- Converted pip install commands to `%pip install`: 37
- Commented unsupported shell/local commands: 57
- Added `import matplotlib.pyplot as plt` before `.plot(...)` usage in cells: 31

## Missing TOC Notebooks
- `book/08-LLMs-and-AI/00-LLMs-and-AI.ipynb`
- `book/08-LLMs-and-AI/01-Local-LLMs.ipynb`
- `book/08-LLMs-and-AI/02-Word-Document-Embeddings.ipynb`
- `book/08-LLMs-and-AI/03-Text-Classification.ipynb`

## Unsupported Commands Commented Out
### `book/01-Command-Line/01-The-Command-Line.ipynb` cell 28
- Original: `!curl -O https://www.gutenberg.org/files/1952/1952-0.txt`
- Replacement: `# ALPS unsupported shell command: !curl -O https://www.gutenberg.org/files/1952/1952-0.txt`
### `book/01-Command-Line/01-The-Command-Line.ipynb` cell 30
- Original: `!wget https://www.gutenberg.org/files/1952/1952-0.txt`
- Replacement: `# ALPS unsupported shell command: !wget https://www.gutenberg.org/files/1952/1952-0.txt`
### `book/01-Command-Line/01-The-Command-Line.ipynb` cell 46
- Original: `!wc -w The-Yellow-Wallpaper.txt`
- Replacement: `# ALPS unsupported shell command: !wc -w The-Yellow-Wallpaper.txt`
### `book/01-Command-Line/01-The-Command-Line.ipynb` cell 49
- Original: `!wc -l The-Yellow-Wallpaper.txt`
- Replacement: `# ALPS unsupported shell command: !wc -l The-Yellow-Wallpaper.txt`
### `book/01-Command-Line/01-The-Command-Line.ipynb` cell 54
- Original: `!cat The-Yellow-Wallpaper.txt`
- Replacement: `# ALPS unsupported shell command: !cat The-Yellow-Wallpaper.txt`
### `book/01-Command-Line/01-The-Command-Line.ipynb` cell 56
- Original: `!head The-Yellow-Wallpaper.txt`
- Replacement: `# ALPS unsupported shell command: !head The-Yellow-Wallpaper.txt`
### `book/01-Command-Line/01-The-Command-Line.ipynb` cell 59
- Original: `!head -50 The-Yellow-Wallpaper.txt`
- Replacement: `# ALPS unsupported shell command: !head -50 The-Yellow-Wallpaper.txt`
### `book/01-Command-Line/01-The-Command-Line.ipynb` cell 61
- Original: `!tail The-Yellow-Wallpaper.txt`
- Replacement: `# ALPS unsupported shell command: !tail The-Yellow-Wallpaper.txt`
### `book/01-Command-Line/01-The-Command-Line.ipynb` cell 66
- Original: `!grep "yellow" -n The-Yellow-Wallpaper.txt`
- Replacement: `# ALPS unsupported shell command: !grep "yellow" -n The-Yellow-Wallpaper.txt`
### `book/01-Command-Line/01-The-Command-Line.ipynb` cell 69
- Original: `!grep "yellow" -n --color The-Yellow-Wallpaper.txt`
- Replacement: `# ALPS unsupported shell command: !grep "yellow" -n --color The-Yellow-Wallpaper.txt`
### `book/01-Command-Line/01-The-Command-Line.ipynb` cell 71
- Original: `!grep -wc "yellow" The-Yellow-Wallpaper.txt`
- Replacement: `# ALPS unsupported shell command: !grep -wc "yellow" The-Yellow-Wallpaper.txt`
### `book/01-Command-Line/01-The-Command-Line.ipynb` cell 72
- Original: `!grep -wc "paper" The-Yellow-Wallpaper.txt`
- Replacement: `# ALPS unsupported shell command: !grep -wc "paper" The-Yellow-Wallpaper.txt`
### `book/01-Command-Line/01-The-Command-Line.ipynb` cell 74
- Original: `!grep "wallpaper" -B 2 -A 2 -n --color The-Yellow-Wallpaper.txt`
- Replacement: `# ALPS unsupported shell command: !grep "wallpaper" -B 2 -A 2 -n --color The-Yellow-Wallpaper.txt`
### `book/02-Python/02-How-to-Use-Jupyter-Notebooks.ipynb` cell 26
- Original: `jupyter lab`
- Replacement: `# ALPS unsupported local command: jupyter lab`
### `book/02-Python/03-Anatomy-Python-Script.ipynb` cell 51
- Original: `!python word_frequency_Yellow_Wallpaper.py`
- Replacement: `# ALPS unsupported shell command: !python word_frequency_Yellow_Wallpaper.py`
### `book/02-Python/03-Anatomy-Python-Script.ipynb` cell 55
- Original: `!python word_frequency.py ../texts/literature/Grimms-Fairy-Tales.txt`
- Replacement: `# ALPS unsupported shell command: !python word_frequency.py ../texts/literature/Grimms-Fairy-Tales.txt`
### `book/02-Python/03-Anatomy-Python-Script.ipynb` cell 57
- Original: `!python word_frequency.py ../texts/literature/Little-Women_Louisa-May-Alcott.txt`
- Replacement: `# ALPS unsupported shell command: !python word_frequency.py ../texts/literature/Little-Women_Louisa-May-Alcott.txt`
### `book/02-Python/04-Variables.ipynb` cell 50
- Original: `!ls ../texts/music/`
- Replacement: `# ALPS unsupported shell command: !ls ../texts/music/`
### `book/04-Data-Collection/04-Git-GitHub.ipynb` cell 10
- Original: `!git --version`
- Replacement: `# ALPS unsupported shell command: !git --version`
### `book/04-Data-Collection/04-Git-GitHub.ipynb` cell 15
- Original: `!git clone https://github.com/melaniewalsh/Intro-Cultural-Analytics-Notebooks.git`
- Replacement: `# ALPS unsupported shell command: !git clone https://github.com/melaniewalsh/Intro-Cultural-Analytics-Notebooks.git`
### `book/04-Data-Collection/04-Git-GitHub.ipynb` cell 23
- Original: `!git pull`
- Replacement: `# ALPS unsupported shell command: !git pull`
### `book/04-Data-Collection/11-Twitter-API-Setup.ipynb` cell 13
- Original: `!twarc2 configure`
- Replacement: `# ALPS unsupported shell command: !twarc2 configure`
### `book/04-Data-Collection/12-Twitter-Data.ipynb` cell 20
- Original: `!twarc2 counts "David Foster Wallace bro is:verified" --csv --archive --granularity day > twitter-data/tweet-counts.csv`
- Replacement: `# ALPS unsupported shell command: !twarc2 counts "David Foster Wallace bro is:verified" --csv --archive --granularity day > twitter-data/tweet-counts.csv`
### `book/04-Data-Collection/12-Twitter-Data.ipynb` cell 29
- Original: `!twarc2 search "David Foster Wallace is:verified"`
- Replacement: `# ALPS unsupported shell command: !twarc2 search "David Foster Wallace is:verified"`
### `book/04-Data-Collection/12-Twitter-Data.ipynb` cell 31
- Original: `!twarc2 search "David Foster Wallace is:verified" twitter-data/dfw_last_week.jsonl`
- Replacement: `# ALPS unsupported shell command: !twarc2 search "David Foster Wallace is:verified" twitter-data/dfw_last_week.jsonl`
### `book/04-Data-Collection/12-Twitter-Data.ipynb` cell 33
- Original: `!twarc2 search "\"David Foster Wallace\" is:verified" twitter-data/dfw_exact.jsonl`
- Replacement: `# ALPS unsupported shell command: !twarc2 search "\"David Foster Wallace\" is:verified" twitter-data/dfw_exact.jsonl`
### `book/04-Data-Collection/12-Twitter-Data.ipynb` cell 39
- Original: `!twarc2 search "David Foster Wallace bro is:verified" --archive twitter-data/dfw_bro.jsonl`
- Replacement: `# ALPS unsupported shell command: !twarc2 search "David Foster Wallace bro is:verified" --archive twitter-data/dfw_bro.jsonl`
### `book/04-Data-Collection/12-Twitter-Data.ipynb` cell 44
- Original: `!twarc2 csv twitter-data/dfw_bro.jsonl twitter-data/dfw_bro.csv`
- Replacement: `# ALPS unsupported shell command: !twarc2 csv twitter-data/dfw_bro.jsonl twitter-data/dfw_bro.csv`
### `book/04-Data-Collection/12-Twitter-Data.ipynb` cell 92
- Original: `!twarc2 hashtags twitter-data/dfw.jsonl twitter-data/dfw_hashtags.csv`
- Replacement: `# ALPS unsupported shell command: !twarc2 hashtags twitter-data/dfw.jsonl twitter-data/dfw_hashtags.csv`
### `book/04-Data-Collection/12-Twitter-Data.ipynb` cell 95
- Original: `!twarc2 hashtags --group year --limit 10 twitter-data/dfw.jsonl twitter-data/dfw_hashtags_year.csv`
- Replacement: `# ALPS unsupported shell command: !twarc2 hashtags --group year --limit 10 twitter-data/dfw.jsonl twitter-data/dfw_hashtags_year.csv`
### `book/04-Data-Collection/13-Twitter-Data-Sharing.ipynb` cell 13
- Original: `!twarc2 dehydrate twitter-data/dfw_bro.jsonl > twitter-data/dfw_bro.txt`
- Replacement: `# ALPS unsupported shell command: !twarc2 dehydrate twitter-data/dfw_bro.jsonl > twitter-data/dfw_bro.txt`
### `book/04-Data-Collection/13-Twitter-Data-Sharing.ipynb` cell 21
- Original: `!twarc2 hydrate twitter-data/dfw_bro.txt > twitter-data/dfw_bro_REHYDRATED.jsonl`
- Replacement: `# ALPS unsupported shell command: !twarc2 hydrate twitter-data/dfw_bro.txt > twitter-data/dfw_bro_REHYDRATED.jsonl`
### `book/05-Text-Analysis/Multilingual/Chinese/01-Preprocessing-Chinese.ipynb` cell 7
- Original: `!python -m spacy download zh_core_web_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download zh_core_web_md`
### `book/05-Text-Analysis/Multilingual/Chinese/02-Named-Entity-Recognition-Chinese.ipynb` cell 19
- Original: `!python -m spacy download zh_core_web_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download zh_core_web_md`
### `book/05-Text-Analysis/Multilingual/Chinese/03-POS-Keywords-Chinese.ipynb` cell 16
- Original: `!python -m spacy download zh_core_web_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download zh_core_web_md`
### `book/05-Text-Analysis/Multilingual/Danish/01-Preprocessing-Danish.ipynb` cell 7
- Original: `!python -m spacy download da_core_news_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download da_core_news_md`
### `book/05-Text-Analysis/Multilingual/Danish/02-Named-Entity-Recognition-Danish.ipynb` cell 19
- Original: `!python -m spacy download da_core_news_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download da_core_news_md`
### `book/05-Text-Analysis/Multilingual/Danish/03-POS-Keywords-Danish.ipynb` cell 16
- Original: `!python -m spacy download da_core_news_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download da_core_news_md`
### `book/05-Text-Analysis/Multilingual/Portuguese/01-Preprocessing-Portuguese.ipynb` cell 7
- Original: `!python -m spacy download pt_core_news_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download pt_core_news_md`
### `book/05-Text-Analysis/Multilingual/Portuguese/02-Named-Entity-Recognition-Portuguese.ipynb` cell 19
- Original: `!python -m spacy download pt_core_news_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download pt_core_news_md`
### `book/05-Text-Analysis/Multilingual/Portuguese/03-POS-Keywords-Portuguese.ipynb` cell 16
- Original: `!python -m spacy download pt_core_news_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download pt_core_news_md`
### `book/05-Text-Analysis/Multilingual/Russian/01-Preprocessing-Russian.ipynb` cell 7
- Original: `!python -m spacy download ru_core_news_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download ru_core_news_md`
### `book/05-Text-Analysis/Multilingual/Russian/02-Named-Entity-Recognition-Russian.ipynb` cell 19
- Original: `!python -m spacy download ru_core_news_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download ru_core_news_md`
### `book/05-Text-Analysis/Multilingual/Russian/03-POS-Keywords-Russian.ipynb` cell 16
- Original: `!python -m spacy download ru_core_news_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download ru_core_news_md`
### `book/05-Text-Analysis/Multilingual/Spanish/01-Preprocessing-Spanish.ipynb` cell 7
- Original: `!python -m spacy download es_core_news_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download es_core_news_md`
### `book/05-Text-Analysis/Multilingual/Spanish/02-Named-Entity-Recognition-Spanish.ipynb` cell 19
- Original: `!python -m spacy download es_core_news_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download es_core_news_md`
### `book/05-Text-Analysis/Multilingual/Spanish/03-POS-Keywords-Spanish.ipynb` cell 16
- Original: `!python -m spacy download es_core_news_md`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download es_core_news_md`
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 11
- Original: `!echo "export JAVA_HOME=$(/usr/libexec/java_home)" >> ~/.bash_profile`
- Replacement: `# ALPS unsupported shell command: !echo "export JAVA_HOME=$(/usr/libexec/java_home)" >> ~/.bash_profile`
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 13
- Original: `!source ~/.bash_profile`
- Replacement: `# ALPS unsupported shell command: !source ~/.bash_profile`
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 15
- Original: `!javac`
- Replacement: `# ALPS unsupported shell command: !javac`
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 21
- Original: `!javac`
- Replacement: `# ALPS unsupported shell command: !javac`
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 25
- Original: `!echo "export JAVA_HOME=/fill-in-the-path/to/your-java_installation/bin" >> ~/.bashrc`
- Replacement: `# ALPS unsupported shell command: !echo "export JAVA_HOME=/fill-in-the-path/to/your-java_installation/bin" >> ~/.bashrc`
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 27
- Original: `!source ~/.bashrc`
- Replacement: `# ALPS unsupported shell command: !source ~/.bashrc`
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 29
- Original: `!javac`
- Replacement: `# ALPS unsupported shell command: !javac`
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 38
- Original: `!~/mallet-2.0.8/bin/mallet import-file`
- Replacement: `# ALPS unsupported shell command: !~/mallet-2.0.8/bin/mallet import-file`
### `book/05-Text-Analysis/12-Named-Entity-Recognition.ipynb` cell 29
- Original: `!python -m spacy download en_core_web_sm`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download en_core_web_sm`
### `book/05-Text-Analysis/13-POS-Keywords.ipynb` cell 22
- Original: `!python -m spacy download en_core_web_sm`
- Replacement: `# ALPS unsupported shell command: !python -m spacy download en_core_web_sm`

## Snippets Needing Review
### `book/03-Data-Analysis/03-Pandas-Basics-Part3.ipynb` cell 117: Bokeh rendering dependency
```python
#Import necessary Bokeh modules from bokeh.plotting import figure, show from bokeh.models import ColumnDataSource, NumeralTickFormatter from bokeh.io import output_notebook, show from bokeh.palettes import RdBu from bokeh.transform import linear_cmap, jitter
```
### `book/03-Data-Analysis/03-Pandas-Basics-Part3.ipynb` cell 118: Bokeh rendering dependency
```python
#Set up Bokeh to work in Jupyter notebook output_notebook()
```
### `book/03-Data-Analysis/03-Pandas-Basics-Part3.ipynb` cell 120: Bokeh rendering dependency (tags=['hide-input'])
```python
#Make groupby into a new DataFrame dialogue_df = women_film_df.groupby(['title', 'release_year'])[['proportion_of_dialogue']].sum()\ .sort_values(by='proportion_of_dialogue', ascending=False).reset_index() # Set up the source data that will suppply the x,y columns and the film title hover text source = ColumnDataSource(dialogue_df) # Set the hover 
```
### `book/04-Data-Collection/02-Web-Scraping-Part1.ipynb` cell 21: external web request/API call
```python
response = requests.get("http://www.scifiscripts.com/scripts/Ghostbusters.txt")
```
### `book/04-Data-Collection/02-Web-Scraping-Part1.ipynb` cell 26: external web request/API call
```python
bad_response = requests.get("http://www.scifiscripts.com/scripts/Ghostboogers.txt")
```
### `book/04-Data-Collection/02-Web-Scraping-Part1.ipynb` cell 39: external web request/API call
```python
def scrape_screenplay(url): response = requests.get(url) html_string = response.text return html_string
```
### `book/04-Data-Collection/02-Web-Scraping-Part1.ipynb` cell 50: external web request/API call (tags=['output_scroll', 'hide-output'])
```python
response = requests.get("https://genius.com/Missy-elliott-the-rain-supa-dupa-fly-lyrics") html_string = response.text print(html_string)
```
### `book/04-Data-Collection/02-Web-Scraping-Part1.ipynb` cell 56: external web request/API call
```python
response = requests.get("http://static.decontextualize.com/kittens.html") html_string = response.text print(html_string)
```
### `book/04-Data-Collection/02-Web-Scraping-Part1.ipynb` cell 67: external web request/API call
```python
response = requests.get("http://static.decontextualize.com/kittens.html") html_string = response.text document = BeautifulSoup(html_string, "html.parser")
```
### `book/04-Data-Collection/02-Web-Scraping-Part1.ipynb` cell 102: external web request/API call
```python
response = requests.get("https://genius.com/Missy-elliott-the-rain-supa-dupa-fly-lyrics") html_str = response.text document = BeautifulSoup(html_str, "html.parser")
```
### `book/04-Data-Collection/03-Web-Scraping-Part2.ipynb` cell 13: external web request/API call
```python
response = requests.get("https://genius.com/albums/Missy-elliott/Under-construction") html_string = response.text
```
### `book/04-Data-Collection/03-Web-Scraping-Part2.ipynb` cell 82: external web request/API call
```python
def get_all_songs_from_album(artist, album_name): artist = artist.replace(" ", "-") album_name = album_name.replace(" ", "-") response = requests.get(f"https://genius.com/albums/{artist}/{album_name}") html_string = response.text document = BeautifulSoup(html_string, "html.parser") song_title_tags = document.find_all("h3", attrs={"class": "chart_ro
```
### `book/04-Data-Collection/07-Genius-API.ipynb` cell 31: external web request/API call
```python
response = requests.get(genius_search_url) json_data = response.json()
```
### `book/04-Data-Collection/07-Genius-API.ipynb` cell 58: external web request/API call
```python
response = requests.get(genius_search_url) json_data = response.json()
```
### `book/04-Data-Collection/08-Collect-Genius-Lyrics.ipynb` cell 7: compiled or possibly unavailable package
```python
%pip install git+https://github.com/johnwmillr/LyricsGenius.git
```
### `book/04-Data-Collection/08-Collect-Genius-Lyrics.ipynb` cell 7: external web request/API call
```python
%pip install git+https://github.com/johnwmillr/LyricsGenius.git
```
### `book/04-Data-Collection/08-Collect-Genius-Lyrics.ipynb` cell 11: compiled or possibly unavailable package
```python
import lyricsgenius LyricsGenius = lyricsgenius.Genius(client_access_token)
```
### `book/04-Data-Collection/08-Collect-Genius-Lyrics.ipynb` cell 11: external web request/API call
```python
import lyricsgenius LyricsGenius = lyricsgenius.Genius(client_access_token)
```
### `book/04-Data-Collection/08-Collect-Genius-Lyrics.ipynb` cell 14: compiled or possibly unavailable package
```python
artist = LyricsGenius.search_artist("Missy Elliott", max_songs=6)
```
### `book/04-Data-Collection/08-Collect-Genius-Lyrics.ipynb` cell 14: external web request/API call
```python
artist = LyricsGenius.search_artist("Missy Elliott", max_songs=6)
```
### `book/04-Data-Collection/08-Collect-Genius-Lyrics.ipynb` cell 21: compiled or possibly unavailable package
```python
song = LyricsGenius.search_song("Missy Elliott", "Work It")
```
### `book/04-Data-Collection/08-Collect-Genius-Lyrics.ipynb` cell 21: external web request/API call
```python
song = LyricsGenius.search_song("Missy Elliott", "Work It")
```
### `book/04-Data-Collection/08-Collect-Genius-Lyrics.ipynb` cell 28: compiled or possibly unavailable package
```python
from bs4 import BeautifulSoup import re import lyricsgenius import requests from pathlib import Path
```
### `book/04-Data-Collection/08-Collect-Genius-Lyrics.ipynb` cell 32: external web request/API call
```python
def get_all_songs_from_album(artist, album_name): artist = artist.replace(" ", "-") album_name = album_name.replace(" ", "-") response = requests.get(f"https://genius.com/albums/{artist}/{album_name}") html_string = response.text document = BeautifulSoup(html_string, "html.parser") song_title_tags = document.find_all("h3", attrs={"class": "chart_ro
```
### `book/04-Data-Collection/08-Collect-Genius-Lyrics.ipynb` cell 34: compiled or possibly unavailable package
```python
def download_album_lyrics(artist, album_name): # Set up LyricsGenius with your Genius API client access token #client_access_token = Your-Client-Access-Token LyricsGenius = lyricsgenius.Genius(client_access_token) LyricsGenius.remove_section_headers = True # With the function that we previously created, go to Genius.com and get all song titles for 
```
### `book/04-Data-Collection/08-Collect-Genius-Lyrics.ipynb` cell 34: external web request/API call
```python
def download_album_lyrics(artist, album_name): # Set up LyricsGenius with your Genius API client access token #client_access_token = Your-Client-Access-Token LyricsGenius = lyricsgenius.Genius(client_access_token) LyricsGenius.remove_section_headers = True # With the function that we previously created, go to Genius.com and get all song titles for 
```
### `book/04-Data-Collection/11-Twitter-API-Setup.ipynb` cell 9: compiled or possibly unavailable package (tags=['command_line'])
```python
%pip install twarc --upgrade
```
### `book/04-Data-Collection/11-Twitter-API-Setup.ipynb` cell 16: compiled or possibly unavailable package (tags=['command_line'])
```python
Your keys have been written to /Users/melwalsh/Library/Application Support/twarc/config ✨ ✨ ✨ Happy twarcing! ✨ ✨ ✨
```
### `book/04-Data-Collection/12-Twitter-Data.ipynb` cell 12: compiled or possibly unavailable package
```python
# %pip install twarc #!twarc2 configure
```
### `book/04-Data-Collection/12-Twitter-Data.ipynb` cell 42: compiled or possibly unavailable package
```python
%pip install twarc-csv
```
### `book/04-Data-Collection/12-Twitter-Data.ipynb` cell 90: compiled or possibly unavailable package
```python
%pip install twarc-hashtags
```
### `book/04-Data-Collection/14-Reddit-Data.ipynb` cell 6: compiled or possibly unavailable package
```python
%pip install psaw
```
### `book/04-Data-Collection/14-Reddit-Data.ipynb` cell 10: compiled or possibly unavailable package
```python
from psaw import PushshiftAPI # Initialize PushShift api = PushshiftAPI()
```
### `book/05-Text-Analysis/Multilingual/Chinese/01-Preprocessing-Chinese.ipynb` cell 5: spaCy/model download/runtime
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/Multilingual/Chinese/01-Preprocessing-Chinese.ipynb` cell 7: spaCy/model download/runtime
```python
# ALPS unsupported shell command: !python -m spacy download zh_core_web_md
```
### `book/05-Text-Analysis/Multilingual/Chinese/01-Preprocessing-Chinese.ipynb` cell 9: spaCy/model download/runtime
```python
import spacy
```
### `book/05-Text-Analysis/Multilingual/Chinese/01-Preprocessing-Chinese.ipynb` cell 14: spaCy/model download/runtime
```python
#nlp = spacy.load('zh_core_web_md')
```
### `book/05-Text-Analysis/Multilingual/Chinese/01-Preprocessing-Chinese.ipynb` cell 18: spaCy/model download/runtime
```python
filepath = '../texts/zh.txt' # Open and read text text = open(filepath, encoding='utf-8').read() # Process text with spaCy document = nlp(text)
```
### `book/05-Text-Analysis/Multilingual/Chinese/02-Named-Entity-Recognition-Chinese.ipynb` cell 12: spaCy/model download/runtime (tags=['output_scroll'])
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/Multilingual/Chinese/02-Named-Entity-Recognition-Chinese.ipynb` cell 15: spaCy/model download/runtime
```python
import spacy from spacy import displacy from collections import Counter import pandas as pd pd.options.display.max_rows = 600 pd.options.display.max_colwidth = 400
```
### `book/05-Text-Analysis/Multilingual/Chinese/02-Named-Entity-Recognition-Chinese.ipynb` cell 19: spaCy/model download/runtime (tags=['output_scroll'])
```python
# ALPS unsupported shell command: !python -m spacy download zh_core_web_md
```
### `book/05-Text-Analysis/Multilingual/Chinese/02-Named-Entity-Recognition-Chinese.ipynb` cell 25: spaCy/model download/runtime
```python
#nlp = spacy.load('es_core_news_md')
```
### `book/05-Text-Analysis/Multilingual/Chinese/03-POS-Keywords-Chinese.ipynb` cell 9: spaCy/model download/runtime
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/Multilingual/Chinese/03-POS-Keywords-Chinese.ipynb` cell 12: spaCy/model download/runtime
```python
import spacy from spacy import displacy from collections import Counter import pandas as pd pd.set_option("max_rows", 400) pd.set_option("max_colwidth", 400)
```
### `book/05-Text-Analysis/Multilingual/Chinese/03-POS-Keywords-Chinese.ipynb` cell 16: spaCy/model download/runtime
```python
# ALPS unsupported shell command: !python -m spacy download zh_core_web_md
```
### `book/05-Text-Analysis/Multilingual/Chinese/03-POS-Keywords-Chinese.ipynb` cell 20: spaCy/model download/runtime
```python
nlp = spacy.load('zh_core_web_md')
```
### `book/05-Text-Analysis/Multilingual/Danish/01-Preprocessing-Danish.ipynb` cell 5: spaCy/model download/runtime
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/Multilingual/Danish/01-Preprocessing-Danish.ipynb` cell 7: spaCy/model download/runtime (tags=['output_scroll'])
```python
# ALPS unsupported shell command: !python -m spacy download da_core_news_md
```
### `book/05-Text-Analysis/Multilingual/Danish/01-Preprocessing-Danish.ipynb` cell 9: spaCy/model download/runtime
```python
import spacy
```
### `book/05-Text-Analysis/Multilingual/Danish/01-Preprocessing-Danish.ipynb` cell 14: spaCy/model download/runtime
```python
#nlp = spacy.load('da_core_news_md')
```
### `book/05-Text-Analysis/Multilingual/Danish/01-Preprocessing-Danish.ipynb` cell 18: spaCy/model download/runtime
```python
filepath = '../texts/da.txt' # Open and read text text = open(filepath, encoding='utf-8').read() # Process text with spaCy document = nlp(text)
```
### `book/05-Text-Analysis/Multilingual/Danish/02-Named-Entity-Recognition-Danish.ipynb` cell 12: spaCy/model download/runtime (tags=['output_scroll'])
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/Multilingual/Danish/02-Named-Entity-Recognition-Danish.ipynb` cell 15: spaCy/model download/runtime
```python
import spacy from spacy import displacy from collections import Counter import pandas as pd pd.options.display.max_rows = 600 pd.options.display.max_colwidth = 400
```
### `book/05-Text-Analysis/Multilingual/Danish/02-Named-Entity-Recognition-Danish.ipynb` cell 19: spaCy/model download/runtime (tags=['output_scroll'])
```python
# ALPS unsupported shell command: !python -m spacy download da_core_news_md
```
### `book/05-Text-Analysis/Multilingual/Danish/02-Named-Entity-Recognition-Danish.ipynb` cell 25: spaCy/model download/runtime
```python
#nlp = spacy.load('da_core_news_md')
```
### `book/05-Text-Analysis/Multilingual/Danish/03-POS-Keywords-Danish.ipynb` cell 9: spaCy/model download/runtime
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/Multilingual/Danish/03-POS-Keywords-Danish.ipynb` cell 12: spaCy/model download/runtime
```python
import spacy from spacy import displacy from collections import Counter import pandas as pd pd.set_option("max_rows", 400) pd.set_option("max_colwidth", 400)
```
### `book/05-Text-Analysis/Multilingual/Danish/03-POS-Keywords-Danish.ipynb` cell 16: spaCy/model download/runtime
```python
# ALPS unsupported shell command: !python -m spacy download da_core_news_md
```
### `book/05-Text-Analysis/Multilingual/Danish/03-POS-Keywords-Danish.ipynb` cell 20: spaCy/model download/runtime
```python
nlp = spacy.load('da_core_news_md')
```
### `book/05-Text-Analysis/Multilingual/Portuguese/01-Preprocessing-Portuguese.ipynb` cell 5: spaCy/model download/runtime
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/Multilingual/Portuguese/01-Preprocessing-Portuguese.ipynb` cell 7: spaCy/model download/runtime (tags=['output_scroll'])
```python
# ALPS unsupported shell command: !python -m spacy download pt_core_news_md
```
### `book/05-Text-Analysis/Multilingual/Portuguese/01-Preprocessing-Portuguese.ipynb` cell 9: spaCy/model download/runtime
```python
import spacy
```
### `book/05-Text-Analysis/Multilingual/Portuguese/01-Preprocessing-Portuguese.ipynb` cell 14: spaCy/model download/runtime
```python
#nlp = spacy.load('pt_core_news_md')
```
### `book/05-Text-Analysis/Multilingual/Portuguese/02-Named-Entity-Recognition-Portuguese.ipynb` cell 12: spaCy/model download/runtime (tags=['output_scroll'])
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/Multilingual/Portuguese/02-Named-Entity-Recognition-Portuguese.ipynb` cell 15: spaCy/model download/runtime
```python
import spacy from spacy import displacy from collections import Counter import pandas as pd pd.options.display.max_rows = 600 pd.options.display.max_colwidth = 400
```
### `book/05-Text-Analysis/Multilingual/Portuguese/02-Named-Entity-Recognition-Portuguese.ipynb` cell 19: spaCy/model download/runtime (tags=['output_scroll'])
```python
# ALPS unsupported shell command: !python -m spacy download pt_core_news_md
```
### `book/05-Text-Analysis/Multilingual/Portuguese/02-Named-Entity-Recognition-Portuguese.ipynb` cell 25: spaCy/model download/runtime
```python
#nlp = spacy.load('pt_core_news_md')
```
### `book/05-Text-Analysis/Multilingual/Portuguese/03-POS-Keywords-Portuguese.ipynb` cell 9: spaCy/model download/runtime
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/Multilingual/Portuguese/03-POS-Keywords-Portuguese.ipynb` cell 12: spaCy/model download/runtime
```python
import spacy from spacy import displacy from collections import Counter import pandas as pd pd.set_option("max_rows", 400) pd.set_option("max_colwidth", 400)
```
### `book/05-Text-Analysis/Multilingual/Portuguese/03-POS-Keywords-Portuguese.ipynb` cell 16: spaCy/model download/runtime
```python
# ALPS unsupported shell command: !python -m spacy download pt_core_news_md
```
### `book/05-Text-Analysis/Multilingual/Portuguese/03-POS-Keywords-Portuguese.ipynb` cell 20: spaCy/model download/runtime
```python
nlp = spacy.load('pt_core_news_md')
```
### `book/05-Text-Analysis/Multilingual/Russian/01-Preprocessing-Russian.ipynb` cell 5: spaCy/model download/runtime
```python
%pip install -U spacy>=3.0
```
### `book/05-Text-Analysis/Multilingual/Russian/01-Preprocessing-Russian.ipynb` cell 7: spaCy/model download/runtime
```python
# ALPS unsupported shell command: !python -m spacy download ru_core_news_md
```
### `book/05-Text-Analysis/Multilingual/Russian/01-Preprocessing-Russian.ipynb` cell 9: spaCy/model download/runtime
```python
import spacy
```
### `book/05-Text-Analysis/Multilingual/Russian/01-Preprocessing-Russian.ipynb` cell 14: spaCy/model download/runtime
```python
#nlp = spacy.load('ru_core_news_md')
```
### `book/05-Text-Analysis/Multilingual/Russian/01-Preprocessing-Russian.ipynb` cell 18: spaCy/model download/runtime
```python
filepath = '../texts/ru.txt' # Open and read text text = open(filepath, encoding='utf-8').read() # Process text with spaCy document = nlp(text)
```
### `book/05-Text-Analysis/Multilingual/Russian/02-Named-Entity-Recognition-Russian.ipynb` cell 12: spaCy/model download/runtime (tags=['output_scroll'])
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/Multilingual/Russian/02-Named-Entity-Recognition-Russian.ipynb` cell 15: spaCy/model download/runtime
```python
import spacy from spacy import displacy from collections import Counter import pandas as pd pd.options.display.max_rows = 600 pd.options.display.max_colwidth = 400
```
### `book/05-Text-Analysis/Multilingual/Russian/02-Named-Entity-Recognition-Russian.ipynb` cell 19: spaCy/model download/runtime (tags=['output_scroll'])
```python
# ALPS unsupported shell command: !python -m spacy download ru_core_news_md
```
### `book/05-Text-Analysis/Multilingual/Russian/02-Named-Entity-Recognition-Russian.ipynb` cell 25: spaCy/model download/runtime
```python
#nlp = spacy.load('ru_core_news_md')
```
### `book/05-Text-Analysis/Multilingual/Russian/03-POS-Keywords-Russian.ipynb` cell 9: spaCy/model download/runtime
```python
%pip install -U spacy>=3.0
```
### `book/05-Text-Analysis/Multilingual/Russian/03-POS-Keywords-Russian.ipynb` cell 12: spaCy/model download/runtime
```python
import spacy from spacy import displacy from collections import Counter import pandas as pd pd.set_option("max_rows", 400) pd.set_option("max_colwidth", 400)
```
### `book/05-Text-Analysis/Multilingual/Russian/03-POS-Keywords-Russian.ipynb` cell 16: spaCy/model download/runtime
```python
# ALPS unsupported shell command: !python -m spacy download ru_core_news_md
```
### `book/05-Text-Analysis/Multilingual/Russian/03-POS-Keywords-Russian.ipynb` cell 20: spaCy/model download/runtime
```python
nlp = spacy.load('ru_core_news_md')
```
### `book/05-Text-Analysis/Multilingual/Spanish/01-Preprocessing-Spanish.ipynb` cell 5: spaCy/model download/runtime
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/Multilingual/Spanish/01-Preprocessing-Spanish.ipynb` cell 7: spaCy/model download/runtime
```python
# ALPS unsupported shell command: !python -m spacy download es_core_news_md
```
### `book/05-Text-Analysis/Multilingual/Spanish/01-Preprocessing-Spanish.ipynb` cell 9: spaCy/model download/runtime
```python
import spacy
```
### `book/05-Text-Analysis/Multilingual/Spanish/01-Preprocessing-Spanish.ipynb` cell 14: spaCy/model download/runtime
```python
#nlp = spacy.load('es_core_news_md')
```
### `book/05-Text-Analysis/Multilingual/Spanish/01-Preprocessing-Spanish.ipynb` cell 18: spaCy/model download/runtime
```python
filepath = '../texts/es.txt' # Open and read text text = open(filepath, encoding='utf-8').read() # Process text with spaCy document = nlp(text)
```
### `book/05-Text-Analysis/Multilingual/Spanish/02-Named-Entity-Recognition-Spanish.ipynb` cell 12: spaCy/model download/runtime (tags=['output_scroll'])
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/Multilingual/Spanish/02-Named-Entity-Recognition-Spanish.ipynb` cell 15: spaCy/model download/runtime
```python
import spacy from spacy import displacy from collections import Counter import pandas as pd pd.options.display.max_rows = 600 pd.options.display.max_colwidth = 400
```
### `book/05-Text-Analysis/Multilingual/Spanish/02-Named-Entity-Recognition-Spanish.ipynb` cell 19: spaCy/model download/runtime (tags=['output_scroll'])
```python
# ALPS unsupported shell command: !python -m spacy download es_core_news_md
```
### `book/05-Text-Analysis/Multilingual/Spanish/02-Named-Entity-Recognition-Spanish.ipynb` cell 25: spaCy/model download/runtime
```python
#nlp = spacy.load('es_core_news_md')
```
### `book/05-Text-Analysis/Multilingual/Spanish/03-POS-Keywords-Spanish.ipynb` cell 9: spaCy/model download/runtime
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/Multilingual/Spanish/03-POS-Keywords-Spanish.ipynb` cell 12: spaCy/model download/runtime
```python
import spacy from spacy import displacy from collections import Counter import pandas as pd pd.set_option("max_rows", 400) pd.set_option("max_colwidth", 400)
```
### `book/05-Text-Analysis/Multilingual/Spanish/03-POS-Keywords-Spanish.ipynb` cell 16: spaCy/model download/runtime
```python
# ALPS unsupported shell command: !python -m spacy download es_core_news_md
```
### `book/05-Text-Analysis/Multilingual/Spanish/03-POS-Keywords-Spanish.ipynb` cell 20: spaCy/model download/runtime
```python
nlp = spacy.load('es_core_news_md')
```
### `book/05-Text-Analysis/04-Sentiment-Analysis.ipynb` cell 13: compiled or possibly unavailable package
```python
%pip install vaderSentiment
```
### `book/05-Text-Analysis/04-Sentiment-Analysis.ipynb` cell 15: compiled or possibly unavailable package
```python
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer # Initialize VADER so we can use it later sentimentAnalyser = SentimentIntensityAnalyzer()
```
### `book/05-Text-Analysis/04-Sentiment-Analysis.ipynb` cell 63: NLTK data download/runtime
```python
import nltk nltk.download('punkt')
```
### `book/05-Text-Analysis/04-Sentiment-Analysis.ipynb` cell 65: NLTK data download/runtime (tags=['output_scroll'])
```python
nltk.sent_tokenize(text)
```
### `book/05-Text-Analysis/04-Sentiment-Analysis.ipynb` cell 67: NLTK data download/runtime (tags=['output_scroll'])
```python
for number, sentence in enumerate(nltk.sent_tokenize(text)): print(number, sentence)
```
### `book/05-Text-Analysis/04-Sentiment-Analysis.ipynb` cell 70: NLTK data download/runtime
```python
# Break text into sentences sentences = nltk.sent_tokenize(text) # Make empty list sentence_scores = [] # Get each sentence and sentence number, which is what enumerate does for number, sentence in enumerate(sentences): # Use VADER to calculate sentiment scores = sentimentAnalyser.polarity_scores(sentence) # Make dictionary and append it to the pre
```
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 11: Java/MALLET command or path
```python
# ALPS unsupported shell command: !echo "export JAVA_HOME=$(/usr/libexec/java_home)" >> ~/.bash_profile
```
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 15: Java/MALLET command or path (tags=['output_scroll'])
```python
# ALPS unsupported shell command: !javac
```
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 21: Java/MALLET command or path
```python
# ALPS unsupported shell command: !javac
```
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 25: Java/MALLET command or path
```python
# ALPS unsupported shell command: !echo "export JAVA_HOME=/fill-in-the-path/to/your-java_installation/bin" >> ~/.bashrc
```
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 29: Java/MALLET command or path
```python
# ALPS unsupported shell command: !javac
```
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 38: Java/MALLET command or path (tags=['output_scroll'])
```python
# ALPS unsupported shell command: !~/mallet-2.0.8/bin/mallet import-file
```
### `book/05-Text-Analysis/07-Topic-Modeling-Set-Up.ipynb` cell 41: Java/MALLET command or path
```python
%pip install little_mallet_wrapper
```
### `book/05-Text-Analysis/08-Topic-Modeling-Text-Files.ipynb` cell 11: Java/MALLET command or path
```python
path_to_mallet = 'mallet-2.0.8/bin/mallet'
```
### `book/05-Text-Analysis/08-Topic-Modeling-Text-Files.ipynb` cell 14: Java/MALLET command or path
```python
# %pip install little_mallet_wrapper # %pip install seaborn
```
### `book/05-Text-Analysis/08-Topic-Modeling-Text-Files.ipynb` cell 16: Java/MALLET command or path
```python
# %pip install little_mallet_wrapper # %pip install seaborn
```
### `book/05-Text-Analysis/08-Topic-Modeling-Text-Files.ipynb` cell 18: Java/MALLET command or path
```python
import little_mallet_wrapper import seaborn import glob from pathlib import Path
```
### `book/05-Text-Analysis/08-Topic-Modeling-Text-Files.ipynb` cell 32: Java/MALLET command or path
```python
training_data = [] for file in files: text = open(file, encoding='utf-8').read() processed_text = little_mallet_wrapper.process_string(text, numbers='remove') training_data.append(processed_text)
```
### `book/05-Text-Analysis/08-Topic-Modeling-Text-Files.ipynb` cell 41: Java/MALLET command or path
```python
little_mallet_wrapper.print_dataset_stats(training_data)
```
### `book/05-Text-Analysis/08-Topic-Modeling-Text-Files.ipynb` cell 56: Java/MALLET command or path (tags=['output_scroll'])
```python
little_mallet_wrapper.quick_train_topic_model(path_to_mallet, output_directory_path, num_topics, training_data)
```
### `book/05-Text-Analysis/08-Topic-Modeling-Text-Files.ipynb` cell 60: Java/MALLET command or path
```python
topics = little_mallet_wrapper.load_topic_keys(path_to_topic_keys) for topic_number, topic in enumerate(topics): print(f"✨Topic {topic_number}✨\n\n{topic}\n")
```
### `book/05-Text-Analysis/08-Topic-Modeling-Text-Files.ipynb` cell 63: Java/MALLET command or path
```python
topic_distributions = little_mallet_wrapper.load_topic_distributions(path_to_topic_distributions)
```
### `book/05-Text-Analysis/08-Topic-Modeling-Text-Files.ipynb` cell 73: Java/MALLET command or path
```python
little_mallet_wrapper.plot_categories_by_topics_heatmap(obit_titles, topic_distributions, topics, output_directory_path + '/categories_by_topics.pdf', target_labels=target_labels, dim= (13, 9) )
```
### `book/05-Text-Analysis/08-Topic-Modeling-Text-Files.ipynb` cell 81: Java/MALLET command or path
```python
def display_top_titles_per_topic(topic_number=0, number_of_documents=5): print(f"✨Topic {topic_number}✨\n\n{topics[topic_number]}\n") for probability, document in little_mallet_wrapper.get_top_docs(training_data, topic_distributions, topic_number, n=number_of_documents): print(round(probability, 4), training_data_obit_titles[document] + "\n") retur
```
### `book/05-Text-Analysis/08-Topic-Modeling-Text-Files.ipynb` cell 95: Java/MALLET command or path
```python
from IPython.display import Markdown, display import re def display_bolded_topic_words_in_context(topic_number=3, number_of_documents=3, custom_words=None): for probability, document in little_mallet_wrapper.get_top_docs(training_data, topic_distributions, topic_number, n=number_of_documents): print(f"✨Topic {topic_number}✨\n\n{topics[topic_number]
```
### `book/05-Text-Analysis/09-Topic-Modeling-Without-Mallet.ipynb` cell 9: compiled or possibly unavailable package
```python
%pip install tomotopy
```
### `book/05-Text-Analysis/09-Topic-Modeling-Without-Mallet.ipynb` cell 10: Java/MALLET command or path
```python
%pip install little_mallet_wrapper
```
### `book/05-Text-Analysis/09-Topic-Modeling-Without-Mallet.ipynb` cell 13: Java/MALLET command or path
```python
import tomotopy as tp import little_mallet_wrapper import seaborn import glob from pathlib import Path import pandas as pd
```
### `book/05-Text-Analysis/09-Topic-Modeling-Without-Mallet.ipynb` cell 13: compiled or possibly unavailable package
```python
import tomotopy as tp import little_mallet_wrapper import seaborn import glob from pathlib import Path import pandas as pd
```
### `book/05-Text-Analysis/09-Topic-Modeling-Without-Mallet.ipynb` cell 22: Java/MALLET command or path
```python
training_data = [] original_texts = [] titles = [] for file in files: text = open(file, encoding='utf-8').read() processed_text = little_mallet_wrapper.process_string(text, numbers='remove') training_data.append(processed_text) original_texts.append(text) titles.append(Path(file).stem)
```
### `book/05-Text-Analysis/10-Topic-Modeling-CSV.ipynb` cell 12: Java/MALLET command or path
```python
path_to_mallet = 'mallet-2.0.8/bin/mallet'
```
### `book/05-Text-Analysis/10-Topic-Modeling-CSV.ipynb` cell 15: Java/MALLET command or path
```python
# %pip install little_mallet_wrapper # %pip install seaborn #To install the most updated version of little_mallet_wrapper: # %pip install git+https://github.com/maria-antoniak/little-mallet-wrapper.git
```
### `book/05-Text-Analysis/10-Topic-Modeling-CSV.ipynb` cell 18: Java/MALLET command or path
```python
import little_mallet_wrapper import seaborn import glob from pathlib import Path import pandas as pd import random pd.options.display.max_colwidth = 100
```
### `book/05-Text-Analysis/10-Topic-Modeling-CSV.ipynb` cell 29: Java/MALLET command or path
```python
training_data = [little_mallet_wrapper.process_string(text, numbers='remove') for text in reddit_df['selftext']]
```
### `book/05-Text-Analysis/10-Topic-Modeling-CSV.ipynb` cell 36: Java/MALLET command or path
```python
little_mallet_wrapper.print_dataset_stats(training_data)
```
### `book/05-Text-Analysis/10-Topic-Modeling-CSV.ipynb` cell 49: Java/MALLET command or path (tags=['output_scroll'])
```python
little_mallet_wrapper.quick_train_topic_model(path_to_mallet, output_directory_path, num_topics, training_data)
```
### `book/05-Text-Analysis/10-Topic-Modeling-CSV.ipynb` cell 53: Java/MALLET command or path
```python
topics = little_mallet_wrapper.load_topic_keys(path_to_topic_keys) for topic_number, topic in enumerate(topics): print(f"✨Topic {topic_number}✨\n\n{topic}\n")
```
### `book/05-Text-Analysis/10-Topic-Modeling-CSV.ipynb` cell 56: Java/MALLET command or path
```python
topic_distributions = little_mallet_wrapper.load_topic_distributions(path_to_topic_distributions)
```
### `book/05-Text-Analysis/10-Topic-Modeling-CSV.ipynb` cell 63: Java/MALLET command or path
```python
little_mallet_wrapper.plot_categories_by_topics_heatmap(reddit_titles, topic_distributions, topics, output_directory_path + '/categories_by_topics.pdf', target_labels=target_labels, dim= (18, 8) )
```
### `book/05-Text-Analysis/10-Topic-Modeling-CSV.ipynb` cell 70: Java/MALLET command or path
```python
def display_top_titles_per_topic(topic_number=0, number_of_documents=5): print(f"✨Topic {topic_number}✨\n\n{topics[topic_number]}\n") for probability, document in little_mallet_wrapper.get_top_docs(training_data, topic_distributions, topic_number, n=number_of_documents): print(round(probability, 4), training_data_reddit_titles[document] + "\n") ret
```
### `book/05-Text-Analysis/10-Topic-Modeling-CSV.ipynb` cell 84: Java/MALLET command or path
```python
from IPython.display import Markdown, display import re def display_bolded_topic_words_in_context(topic_number=3, number_of_documents=3, custom_words=None): for probability, document in little_mallet_wrapper.get_top_docs(training_data, topic_distributions, topic_number, n=number_of_documents): print(f"✨Topic {topic_number}✨\n\n{topics[topic_number]
```
### `book/05-Text-Analysis/11-Topic-Modeling-Time-Series.ipynb` cell 11: Java/MALLET command or path
```python
path_to_mallet = 'mallet-2.0.8/bin/mallet'
```
### `book/05-Text-Analysis/11-Topic-Modeling-Time-Series.ipynb` cell 14: Java/MALLET command or path
```python
%pip install little_mallet_wrapper %pip install seaborn
```
### `book/05-Text-Analysis/11-Topic-Modeling-Time-Series.ipynb` cell 17: Java/MALLET command or path
```python
import little_mallet_wrapper import seaborn import glob from pathlib import Path import pandas as pd import random pd.options.display.max_colwidth = 100
```
### `book/05-Text-Analysis/11-Topic-Modeling-Time-Series.ipynb` cell 29: Java/MALLET command or path
```python
training_data = [little_mallet_wrapper.process_string(text, numbers='remove') for text in trump_df['text']]
```
### `book/05-Text-Analysis/11-Topic-Modeling-Time-Series.ipynb` cell 33: Java/MALLET command or path
```python
little_mallet_wrapper.print_dataset_stats(training_data)
```
### `book/05-Text-Analysis/11-Topic-Modeling-Time-Series.ipynb` cell 47: Java/MALLET command or path (tags=['output_scroll'])
```python
little_mallet_wrapper.quick_train_topic_model(path_to_mallet, output_directory_path, num_topics, training_data)
```
### `book/05-Text-Analysis/11-Topic-Modeling-Time-Series.ipynb` cell 49: Java/MALLET command or path (tags=['output_scroll'])
```python
topics = little_mallet_wrapper.load_topic_keys(path_to_topic_keys) for topic_number, topic in enumerate(topics): print(f"✨Topic {topic_number}✨\n\n{topic}\n")
```
### `book/05-Text-Analysis/11-Topic-Modeling-Time-Series.ipynb` cell 52: Java/MALLET command or path
```python
topic_distributions = little_mallet_wrapper.load_topic_distributions(path_to_topic_distributions)
```
### `book/05-Text-Analysis/11-Topic-Modeling-Time-Series.ipynb` cell 54: Java/MALLET command or path
```python
def display_top_tweets_per_topic(topic_number=0, number_of_documents=5): print(f"✨Topic {topic_number}✨\n\n{topics[topic_number]}\n") for probability, document in little_mallet_wrapper.get_top_docs(training_data, topic_distributions, topic_number, n=number_of_documents): print(round(probability, 4), tweet_dict[document] + "\n") return
```
### `book/05-Text-Analysis/11-Topic-Modeling-Time-Series.ipynb` cell 57: Java/MALLET command or path
```python
from IPython.display import Markdown, display import re def display_bolded_topic_words_in_context(topic_number=3, number_of_documents=3, custom_words=None): print(f"✨Topic {topic_number}✨\n\n{topics[topic_number]}\n") for probability, document in little_mallet_wrapper.get_top_docs(training_data, topic_distributions, topic_number, n=number_of_docume
```
### `book/05-Text-Analysis/11-Topic-Modeling-Time-Series.ipynb` cell 61: Java/MALLET command or path
```python
topic_distributions = little_mallet_wrapper.load_topic_distributions(path_to_topic_distributions)
```
### `book/05-Text-Analysis/12-Named-Entity-Recognition.ipynb` cell 22: spaCy/model download/runtime (tags=['output_scroll'])
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/12-Named-Entity-Recognition.ipynb` cell 25: spaCy/model download/runtime
```python
import spacy from spacy import displacy from collections import Counter import pandas as pd pd.options.display.max_rows = 600 pd.options.display.max_colwidth = 400
```
### `book/05-Text-Analysis/12-Named-Entity-Recognition.ipynb` cell 29: spaCy/model download/runtime (tags=['output_scroll'])
```python
# ALPS unsupported shell command: !python -m spacy download en_core_web_sm
```
### `book/05-Text-Analysis/12-Named-Entity-Recognition.ipynb` cell 36: spaCy/model download/runtime
```python
#nlp = spacy.load('en_core_web_sm')
```
### `book/05-Text-Analysis/13-POS-Keywords.ipynb` cell 15: spaCy/model download/runtime
```python
%pip install -U spacy
```
### `book/05-Text-Analysis/13-POS-Keywords.ipynb` cell 18: spaCy/model download/runtime
```python
import spacy from spacy import displacy from collections import Counter import pandas as pd pd.options.display.max_rows = 400 pd.options.display.max_colwidth = 400
```
### `book/05-Text-Analysis/13-POS-Keywords.ipynb` cell 22: spaCy/model download/runtime
```python
# ALPS unsupported shell command: !python -m spacy download en_core_web_sm
```
### `book/05-Text-Analysis/13-POS-Keywords.ipynb` cell 26: spaCy/model download/runtime
```python
nlp = spacy.load('en_core_web_sm')
```
### `book/06-Network-Analysis/02-Making-Network-Viz-with-Bokeh.ipynb` cell 9: Bokeh rendering dependency
```python
# %pip install bokeh
```
### `book/06-Network-Analysis/02-Making-Network-Viz-with-Bokeh.ipynb` cell 10: Bokeh rendering dependency
```python
from bokeh.io import output_notebook, show, save
```
### `book/06-Network-Analysis/02-Making-Network-Viz-with-Bokeh.ipynb` cell 12: Bokeh rendering dependency
```python
output_notebook()
```
### `book/06-Network-Analysis/02-Making-Network-Viz-with-Bokeh.ipynb` cell 22: Bokeh rendering dependency
```python
from bokeh.io import output_notebook, show, save from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine from bokeh.plotting import figure from bokeh.plotting import from_networkx
```
### `book/06-Network-Analysis/02-Making-Network-Viz-with-Bokeh.ipynb` cell 27: Bokeh rendering dependency
```python
from bokeh.io import output_notebook, show, save from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine from bokeh.plotting import figure from bokeh.plotting import from_networkx from bokeh.palettes import Blues8, Reds8, Purples8, Oranges8, Viridis8, Spectral8 from bokeh.transform import linear_cmap
```
### `book/06-Network-Analysis/02-Making-Network-Viz-with-Bokeh.ipynb` cell 36: Bokeh rendering dependency
```python
from bokeh.io import output_notebook, show, save from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine from bokeh.plotting import figure from bokeh.plotting import from_networkx from bokeh.palettes import Blues8, Reds8, Purples8, Oranges8, Viridis8, Spectral8 from bokeh.transform import linear_cmap from networkx.algorithms import co
```
### `book/06-Network-Analysis/02-Making-Network-Viz-with-Bokeh.ipynb` cell 50: Bokeh rendering dependency
```python
from bokeh.io import output_notebook, show, save from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine, EdgesAndLinkedNodes, NodesAndLinkedEdges from bokeh.plotting import figure from bokeh.plotting import from_networkx from bokeh.palettes import Blues8, Reds8, Purples8, Oranges8, Viridis8, Spectral8 from bokeh.transform import line
```
### `book/06-Network-Analysis/02-Making-Network-Viz-with-Bokeh.ipynb` cell 60: Bokeh rendering dependency
```python
from bokeh.models import EdgesAndLinkedNodes, NodesAndLinkedEdges #Choose colors for node and edge highlighting node_highlight_color = 'white' edge_highlight_color = 'black' #Choose attributes from G network to size and color by — setting manual size (e.g. 10) or color (e.g. 'skyblue') also allowed size_by_this_attribute = 'adjusted_node_size' colo
```
### `book/06-Network-Analysis/02-Making-Network-Viz-with-Bokeh.ipynb` cell 64: Bokeh rendering dependency
```python
from bokeh.io import output_notebook, show, save from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine, EdgesAndLinkedNodes, NodesAndLinkedEdges, LabelSet from bokeh.plotting import figure from bokeh.plotting import from_networkx from bokeh.palettes import Blues8, Reds8, Purples8, Oranges8, Viridis8, Spectral8 from bokeh.transform i
```
### `book/07-Mapping/01-Mapping.ipynb` cell 50: browser/network map tile dependency (tags=['output_scroll'])
```python
%pip install folium
```
### `book/07-Mapping/01-Mapping.ipynb` cell 51: browser/network map tile dependency
```python
import folium
```
### `book/07-Mapping/01-Mapping.ipynb` cell 54: browser/network map tile dependency
```python
ithaca_map = folium.Map(location=[42.44, -76.5], zoom_start=14) ithaca_map
```
### `book/07-Mapping/01-Mapping.ipynb` cell 57: browser/network map tile dependency
```python
folium.Marker(location=[42.444695, -76.482233], popup="Intro to Cultural Analytics").add_to(ithaca_map) ithaca_map
```
### `book/07-Mapping/01-Mapping.ipynb` cell 60: browser/network map tile dependency
```python
def create_map_markers(row, map_name): folium.Marker(location=[row['lat'], row['lon']], popup=row['place']).add_to(map_name)
```
### `book/07-Mapping/01-Mapping.ipynb` cell 70: browser/network map tile dependency
```python
def create_ICE_map_markers(row, map_name): folium.CircleMarker(location=[row['lat'], row['lon']], raidus=100, fill=True, popup=folium.Popup(f"{row['Name'].title()} <br> {row['City'].title()}, {row['State']}", max_width=200), tooltip=f"{row['Name'].title()} <br> {row['City'].title()}, {row['State']}" ).add_to(map_name)
```
### `book/07-Mapping/01-Mapping.ipynb` cell 72: browser/network map tile dependency
```python
US_map = folium.Map(location=[42, -102], zoom_start=4) US_map
```
### `book/07-Mapping/01-Mapping.ipynb` cell 84: browser/network map tile dependency
```python
US_map = folium.Map(location=[42, -102], zoom_start=4) folium.Choropleth( geo_data = US_districts_geo_json, name = 'choropleth', data = US_districts_csv, columns = ['districtName', 'total_awards'], key_on = 'feature.properties.districtName', fill_color = 'GnBu', line_opacity = 0.2, legend_name= 'Total ICE Money Received' ).add_to(US_map) US_map
```
### `book/07-Mapping/01-Mapping.ipynb` cell 86: browser/network map tile dependency
```python
tooltip = folium.features.GeoJson( US_districts_geo_json, tooltip=folium.features.GeoJsonTooltip(fields=['representative', 'state', 'party', 'total_value'], localize=True) ) US_map.add_child(tooltip) US_map
```
### `book/07-Mapping/02-Custom-Maps.ipynb` cell 4: browser/network map tile dependency
```python
import folium
```
### `book/07-Mapping/02-Custom-Maps.ipynb` cell 7: browser/network map tile dependency
```python
folium.Map(location=[0, 30], zoom_start=4, min_zoom=4, max_zoom=10, max_bounds=True, min_lon=0, max_lon=70, min_lat=-40, max_lat=40, tiles='https://cartocdn-gusc.global.ssl.fastly.net//ramirocartodb/api/v1/map/named/tpl_756aec63_3adb_48b6_9d14_331c6cbc47cf/all/{z}/{x}/{y}.png', attr='Textures and Icons from https://www.textures.com/ & https://theno
```
### `book/07-Mapping/02-Custom-Maps.ipynb` cell 10: browser/network map tile dependency
```python
folium.Map(location=[0, 30], zoom_start=2, tiles='http://c.tile.stamen.com/watercolor/{z}/{x}/{y}.jpg', attr='Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/li
```
### `book/07-Mapping/02-Custom-Maps.ipynb` cell 13: browser/network map tile dependency
```python
folium.Map(location=[0, 30], zoom_start=4, tiles='http://services.arcgisonline.com/arcgis/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}', attr="Sources: National Geographic, Esri, Garmin, HERE, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, INCREMENT P")
```
