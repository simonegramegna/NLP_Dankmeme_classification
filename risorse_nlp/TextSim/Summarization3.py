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

# load text
#text=inaugural.raw("2013-obama.txt")
text=inaugural.raw("2017-trump.txt")
sentences = sent_tokenize(text) # NLTK function
corpus={}
# our corpus is the set of sentences in the text
# one doc = one sentence

for sent in sentences:
        corpus[sent]=sent

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

###### ANOTHER SOLUTION BASED ON NORMALIZED VECTORS AND k-NN#######


#### we want to length-normalize the tf-idf vectors ###
tf_idf_tables=tfidf.compute_lenghtnorm_vectors(tf_idf_tables)

# Instead of assigning a relevance to a sentence we:
# compute the centroid vector of the document and find most similar sentences


# computing the centroid from a vocabulary and a tf*idf matrix
centroid=tfidf.compute_centroid(vocabulary, tf_idf_tables)
norm_centroid=tfidf.normalize_vector(centroid)
#print ("centroid length:", tfidf.compute_docvect_length(centroid))
#print ("centroid normalized length:", tfidf.compute_docvect_length(norm_centroid))
# generating a summary by selecting k most similar sentences to the centroid  

k=34


def generate_summary(tf_idf_tables, norm_centroid, k):
    summary=""
    sentence_list={}
    for sentence in tf_idf_tables.keys():
        sim=tfidf.compute_cos_similarity(centroid,tf_idf_tables[sentence])
        sentence_list[sentence]=sim
    # rank sentence_list
    sorted_sim_table = dict( sorted(sentence_list.items(), key=operator.itemgetter(1),reverse=True))
    sorted_topk = dict(list(sorted_sim_table.items())[0: k])
    for sentence in sorted_topk:
        summary += " " + sentence
    # select top-k sentences
    return summary

summary=generate_summary(tf_idf_tables, norm_centroid, k)

#sentence_relevance_matrix=tfidf.sentence_relevance(tfidfscoring)
#print (sentence_relevance_matrix)
#threshold=tfidf.find_average_score(sentence_relevance_matrix)
#print ("Avg. relevance score per sentence: ", threshold)
#print ("All sentences above the threshold will be included in the summary")
#summary=tfidf.generate_summary(sentences, sentence_relevance_matrix, threshold)

print ("SUMMARY made of: ", str(k), "sentences\n")
print (summary)

#######################################################




