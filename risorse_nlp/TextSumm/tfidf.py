import nltk
import math 

def create_df_table(dic,corpus_frequencies):
    # create a df table as a dictionary (term, document frequency) 
    df_table = {}
    for word in dic:
        df_table[word]=0
        for doc_id in corpus_frequencies.keys():
            doc_freq=corpus_frequencies[doc_id]
            if doc_freq[word]>0:
                df_table[word] += 1
    return df_table

def create_idf_table(df_table, total_documents):
    # create a df table as a dictionary (term, document frequency) 
    idf_table = {}
    for word in df_table.keys():
        idf_table[word]=math.log(total_documents / float(df_table[word]))
    return idf_table

def create_tfidf_table(f_distr, idf_table):
    # create a tf*idf table (term, tf*idf score) from a doc frequency distribution
    tf_idf_table = {}
    for word in f_distr:
        tf_idf_table[word]= float(f_distr.freq(word) * idf_table[word])
    return tf_idf_table

def compute_avg_tfidfscore(tf_idf_column):
    # computing document relevance as avg. of tf*idf scores
    doc_score=0
    for word in tf_idf_column.keys():
        doc_score+=tf_idf_column[word]
    return doc_score / len(tf_idf_column)

def compute_docvect_length(tf_idf_column):
    # computing length of document vector
    coordsum=0
    for word in tf_idf_column.keys():
        coordsum+=tf_idf_column[word]**2
    return math.sqrt(coordsum)

def compute_lenghtnorm_vectors(tf_idf_matrix):
    # produces a length-normalized tf*idf matrix
    norm_tf_idf_matrix = {}
    for doc_id in tf_idf_matrix.keys():
        column=tf_idf_matrix[doc_id]
        vec_length=compute_docvect_length(column)
        for word in column.keys():
            column[word]=column[word]/vec_length
        norm_tf_idf_matrix[doc_id]=column
    return norm_tf_idf_matrix

def compute_docweight_incorpus_table(scoring_table):
    # computing document relevance in a corpus from a scoring table (doc, score) 
    all_weights=0
    weight_table = {}
    for doc_id in scoring_table.keys():
        all_weights+=scoring_table[doc_id]
    for doc_id in scoring_table.keys():
        weight_table[doc_id]=(scoring_table[doc_id] / all_weights)
        # normalized scores
    return weight_table

def compute_cos_similarity(norm_vec1, norm_vec2):
    # computing cosine similarity between 2 normalized vectors
    common_words=[w for w in norm_vec1 if w in norm_vec2]
    sim_score=0
    for w in common_words:
        sim_score+=norm_vec1[w]*norm_vec2[w]
    return sim_score

def compute_centroid(voc, tf_idf_matrix):
    # produces the centroid of vectors in a tf*idf matrix
    centroid = {}
    length=len(tf_idf_matrix.keys())
    for word in voc:
        centroid[word]=0
    for doc_id in tf_idf_matrix.keys():
        column=tf_idf_matrix[doc_id]
        for word in column.keys():
            centroid[word]+=column[word]/length
    return centroid

def normalize_vector(vector):
    # produces a length-normalized vector
    norm_vect = {}
    vec_length=compute_docvect_length(vector)
    for word in vector.keys():
        norm_vect[word]=vector[word]/vec_length
    return norm_vect
