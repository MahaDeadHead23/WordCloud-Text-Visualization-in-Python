#! python3 
#WordCloud-Creates a Word Cloud png



from pathlib import Path
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud

TXT_FILE = Path.cwd() / "WordCloud.txt"

# Read text
text = open(TXT_FILE, mode="r", encoding="utf-8").read()
stopwords = STOPWORDS

wc = WordCloud(background_color="black", stopwords=stopwords, height=600, width=400)
wc.generate(text)

# store to file
wc.to_file("wordcloud_output.png")