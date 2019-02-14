# Poll analysis

The goal of this project was, from a poll asking people their political
suggestion, to automatically extract the ideas that were popular.

TL;DR: Didn't work. Some people gave 3 ideas in a sentence, other needed
several sentences to express one idea. So it was very hard to isolate ideas.
Also, the dataset was way too small for text analysis.
Besides, sentences can be very short or very long. The clustering methods would
rather group together small sentences (because they differ in few words, as
they have few words), rather than group together sentences that shared words.

Long version:
We tried several methods to find group of sentences talking about the same subject:
- TF-IDF
- Word2Vec: summing words of a sentence.


In both cases, DBScan either:
- found no cluster
- or (with bigger epsilon), made 1 big cluster with every short sentence.

IMO, the best solution is simply, for particular words ('ISF', 'taxe'), to be
able to find what people were saying. We tried using sentiment analysis to
know, for a subject, what is the distribution of sentiment around a topic.


# Ressources used

## Sentiment analysis
Used French lexicon from:
http://advanse.lirmm.fr/feel.php

## Word2Vec
Used word representation from Facebook
https://fasttext.cc/docs/en/crawl-vectors.html