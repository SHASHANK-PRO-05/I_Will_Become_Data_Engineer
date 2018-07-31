# I have 2 spark nodes and 1 hdfs node with around 600MB of data
# you can change accordingly
from pyspark import SparkConf, SparkContext
from sys import argv
import os, re, random, string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# This is optional. If your both system have same python no need
# also you can add this in bashrc which is upto you.
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.6'

# Some constants for everywhere
regex = re.compile('[%s]' % re.escape(string.punctuation))
stop_words_english = set(stopwords.words('english') + [''])


# doing a range partition. hash partition seems out to be more
# fast. Plus this is not considering distribution. You should
# know distribution of data if you want to use range partitions
# That way it will be faster.
def ranged(word):
    if ord(word[0]) < 97:
        return random.choice([1, 3])
    return random.choice([2, 4])


# This function remove the punctuation characters
def remove_punctuations(word):
    return regex.sub('', word)


# This function will do the case conversion
def case_conversion(word, case='lower'):
    if case == 'lower':
        return word.lower()
    else:
        return word.upper()


# this function will remove the stop words in the
def filter_stop_words_english(word):
    if word in stop_words_english:
        return False
    else:
        return True


if __name__ == '__main__':
    # Spark speculation will make sure that is some of your task is stuck it will be
    # relaunched. YARN may also do that for you. I have a standalone cluster.
    conf = SparkConf().set('spark.speculation', True).setAppName('Chap1-Tokennize')
    sc = SparkContext()
    text = sc.textFile(argv[1])
    words_tokenized = text.flatMap(sent_tokenize).flatMap(word_tokenize)
    punctuations_removed = words_tokenized.map(remove_punctuations)
    case_convert = punctuations_removed.map(case_conversion).persist()
    removed_stop_words = case_convert.filter(filter_stop_words_english).persist()
    # This is not the best way. A better way would be to use the final_list output
    # but let's go with this for now
    word_chosen_ratio = removed_stop_words.count() / case_convert.count()
    final_list = removed_stop_words.map(
        lambda x: (x, 1)).partitionBy(8).reduceByKey(lambda x, y: x + y).partitionBy(
        8).sortBy(
        lambda x: -x[1])

    print(f'Words ratio not including stop words is :{word_chosen_ratio}')
    final_list.saveAsTextFile(argv[2])
    sc.stop()
