from nltk.corpus import stopwords
from string import punctuation
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import defaultdict
from heapq import nlargest
from pyspark import SparkConf, SparkContext
from sys import argv
import os
from nltk import pos_tag, ne_chunk, extract_rels
import shutil
import json

os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.6'

stopwords = set(
    stopwords.words('english') + list(punctuation) + ['TITLE', 'NRC', 'enclosure', 'nuclear', 'arkansas', 'inspection',
                                                      'report', 'docu', 'entergy', 'nrc', 'DOCUMENT', 'CONTAINS',
                                                      'SAFEGUARDS', 'INFORMATION'])


def summarize_texts(text, count=15, min_cut=0.6, max_cut=0.8):
    sentences = sent_tokenize(text)
    new_sentences = []
    sentences = new_sentences
    word_sent = [word_tokenize(sentence) for sentence in sentences]
    freq = defaultdict(lambda: 0.)
    m = 0
    for s in word_sent:
        for w in s:
            if w not in stopwords and not w.isupper():
                freq[w] += 1
                m = max(m, freq[w])

    not_this = set()
    for w in freq:
        freq[w] /= m
        if freq[w] > max_cut or freq[w] < min_cut:
            not_this.add(w)

    ranking = defaultdict(lambda: 0.)
    for i, sent in enumerate(word_sent):
        for w in sent:
            if w in freq and w not in not_this:
                ranking[i] += freq[w]
    sent_ids = nlargest(count, ranking, key=ranking.get)
    return [sentences[i] for i in sent_ids]


if __name__ == '__main__':
    conf = SparkConf().setAppName('TextSummary').set('spark.speculation', True).setMaster('[*]')
    sc = SparkContext()
    files = sc.textFile(argv[1]).map(summarize_texts).collect()
    dir = './output-result/'
    if os.path.isdir(dir):
        shutil.rmtree(dir)
    os.mkdir(dir)
    for i, file in enumerate(files):
        if len(file) > 4:
            f = open(f'{dir}/{i}.json', 'w')
            f.write(json.dumps(file))
            f.flush()
            f.close()
    sc.stop()
