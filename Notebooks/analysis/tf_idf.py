"""
Try to group propositions by TF-IDF
Take all corpus to count DF
Then group only propositions from "Contribution libre"
"""
from collections import Counter, defaultdict
import csv
import nltk

from analysis import clean_text

# French Stopwords and stemmer
STOPWORDS = nltk.corpus.stopwords.words('french')
STEMMER = nltk.SnowballStemmer('french')


def get_lines_tf_idf(filename, stemmer=STEMMER, stopwords=STOPWORDS):
    with open(filename) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    corpus = [row['reponse'] for row in rows]
    idf_by_token = get_inverse_doc_frequency(corpus, stemmer, stopwords)

    clean_suggs = sum(
        (clean_text.get_clean_suggestion(row['reponse']) for row in rows if row['theme'] == 'Contribution libre'),
        [])
    tf_idf_by_line = calc_tf_idf(clean_suggs, idf_by_token, stemmer, stopwords)
    return tf_idf_by_line


def calc_tf_idf(suggestions, token_idf, stemmer, stopwords):
    tf_idf_by_line = dict()
    token_index = defaultdict(int)
    token_index.default_factory = token_index.__len__

    # Keeping only word seen in 10 documents
    for tok, count in token_idf.items():
        # if count <= 1. / 10:
        token_index[tok]

    for line in suggestions:
        toks = _tokenize(line, stemmer, stopwords)
        tf_idf = [0] * len(token_index)
        for tok in toks:
            if tok in token_index:
                tf_idf[token_index[tok]] += token_idf[tok]

        tf_idf_by_line[line] = tf_idf

    return tf_idf_by_line
    

def get_inverse_doc_frequency(suggestions, stemmer, stopwords):
    token_count = Counter()
    for sugg in suggestions:
        sugg = clean_text.get_clean_text(sugg)
        tok_seen = Counter()
        for tok in _tokenize(sugg, stemmer, stopwords):
            tok_seen[tok] = 1

        token_count += tok_seen

    return {tok: 1 / nb_doc for tok, nb_doc in token_count.items()}


def _tokenize(text, stemmer, stopwords):
    return [stemmer.stem(token) for token in text.split() if token not in stopwords]

