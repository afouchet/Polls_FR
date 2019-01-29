import csv
from gensim.models import KeyedVectors
import numpy as np

from analysis import clean_text

def get_x_by_line(filename, model_file):
    with open(filename) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    clean_suggs = sum(
        (clean_text.get_clean_suggestion(row['reponse']) for row in rows if row['theme'] == 'Contribution libre'),
        [])

    model = KeyedVectors.load_word2vec_format(model_file)
    X_by_line = dict()
    for sugg in clean_suggs:
        vector = np.zeros(300)
        for word in sugg.split():
            try:
                vector += model.get_vector(word)
            except KeyError:
                continue
        X_by_line[sugg] = vector

    return X_by_line
