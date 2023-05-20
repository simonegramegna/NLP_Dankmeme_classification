import cleaning
import tfidf
import nltk
import re
import string
import math
import show
import operator
from nltk import sent_tokenize
from nltk.corpus import inaugural
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from itertools import groupby, combinations

# load text

corpus={}
for doc_id in nltk.corpus.inaugural.fileids():
        corpus[doc_id]=inaugural.raw(doc_id)

# apply the pipeline on each doc to build a frequency table


total_documents = len(corpus)
stop_words = stopwords.words('english')
frequencies = {}
vocabulary=set()
vocabularysize=0
for doc_id in corpus.keys():
        tokens=cleaning.wordmatch(corpus[doc_id])
        waste = cleaning.onlypunct(corpus[doc_id])
        cleaned_tokens = [t for t in tokens if not t in waste]
        nostop_tokens = [t for t in cleaned_tokens if not t in stop_words]
        norm_tokens = [t.lower() for t in nostop_tokens]
        #porter = PorterStemmer()
        #stemmed_tokens = [porter.stem(t) for t in norm_tokens]
        wnl=nltk.WordNetLemmatizer()
        lemmas = [wnl.lemmatize(t) for t in norm_tokens]
        docvocabulary=set(lemmas)
        vocabulary=vocabulary.union(docvocabulary)
        vocabularysize=vocabularysize+len(docvocabulary)
        docfdist = nltk.FreqDist(t for t in lemmas)      
        frequencies[doc_id]=docfdist
# building a df table (term, #sentences that contain term)
df_table=tfidf.create_df_table(vocabulary, frequencies)
# building an idf table (term, idf score) based on a df_table
idf_table=tfidf.create_idf_table(df_table, total_documents)
#show.printdict(idf_table)

# Now we build a tf*idf_table for each sentence
# building a tf*idf table from: 1) a frequency distribution 2) an idf_table
#               doc1    doc2    ...     docN
# term1         w11     w12     ...     w1N
# term2         w21     w22     ...     w2N
# ...           ...     ...     ...     ...
# termM         wM1     wM2     ...     wMN

# A tf_idf_table corresponds to a column of the classic term-doc matrix
# We build the whole matrix indexed by docs

tf_idf_tables={}
for doc_id in frequencies.keys():
        tf_idf_table=tfidf.create_tfidf_table(frequencies[doc_id], idf_table)
        tf_idf_tables[doc_id]=tf_idf_table

#### we want to length-normalize the tf-idf vectors ###
tf_idf_tables=tfidf.compute_lenghtnorm_vectors(tf_idf_tables)

pairs=combinations(tf_idf_tables.keys(), 2)
all_pairs=list(pairs)
sim_table={}
for w in all_pairs:
        key=""
        # take the two vectors
        words1=tf_idf_tables[w[0]]
        words2=tf_idf_tables[w[1]]
        sim=tfidf.compute_cos_similarity(words1,words2)
        key=w[0][:len(w[0])-4]+"---"+w[1][:len(w[1])-4]
        sim_table[key]=sim

sorted_sim_table = dict( sorted(sim_table.items(), key=operator.itemgetter(1),reverse=True))
# take only top-k similarities
print ("TOP-K COSINE SIMILARITIES")
K=5
sorted_topk = dict(list(sorted_sim_table.items())[0: K])
show.printdict(sorted_topk)
sorted_lastk = dict(list(sorted_sim_table.items())[len(sorted_sim_table)-K:])
print ("LAST-K COSINE SIMILARITIES")
show.printdict(sorted_lastk)
print ("SPECIFIC COMPARISONS")
key="2009-Obama---2013-Obama"
print (key, sim_table[key])
key="2013-Obama---2017-Trump"
print (key, sim_table[key])
key="2005-Bush---2013-Obama"
print (key, sim_table[key])
key="2005-Bush---2017-Trump"
print (key, sim_table[key])
