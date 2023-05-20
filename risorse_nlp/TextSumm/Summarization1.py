import cleaning
import tfidf
import nltk
import re
import string
import math
from nltk import sent_tokenize
from nltk.corpus import inaugural
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# load text
text=inaugural.raw("2013-obama.txt")
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

# Now we need to assign a relevance to a sentence

# computing a table containing a score for each doc in the corpus (from each tfidf_table)
tfidf_sentence_score_table={}
for sent in tf_idf_tables.keys():
        tfidf_sentence_score_table[sent]=tfidf.compute_avg_tfidfscore(tf_idf_tables[sent])


# computing a table containing a relevance score for each sentence (from a scoring table)
relevance_table=tfidf.compute_docweight_incorpus_table(tfidf_sentence_score_table)

# generating a summary based on some criteria on relevance table
# selection criterion --> relevance score of sentence > avg. relevance 
def generate_summary(relevance_table):
    summary=""
    n_sentences=len(relevance_table.keys())
    sentence_count = 0
    total_rel=0
    for sentence in relevance_table.keys():
        total_rel+=relevance_table[sentence]
    avgrel=total_rel/n_sentences
    for sentence in relevance_table.keys():
        if relevance_table[sentence]>=avgrel:
            #print ("taken!", relevance_table[sentence], avgrel)
            summary += " " + sentence
            sentence_count+=1
    #used=int((sentence_count / n_sentences)*100)    
    summary += "\n Used: "+str(sentence_count)+" out of "+str(n_sentences)+" sentences."
    return summary

summary=generate_summary(relevance_table)

print ("SUMMARY\n")
print (summary)





