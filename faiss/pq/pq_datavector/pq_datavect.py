import faiss
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
data=pd.read_csv("logtable.csv",names=['date','message'],sep=" - ")

df_y=data['date']

df_x=data['message']
tf=CountVectorizer()
data_2=tf.fit_transform(df_x).toarray()
dim=data_2.shape[1]
m=1
n_bits=8
index=faiss.IndexPQ(dim,m,n_bits)
index.train(data_2)
index.add(data_2)
arr=faiss.vector_to_array(index.codes)

dic={}
for i,val in enumerate(arr):
    if val not in dic:
        dic[val] =[i]
    else:
        dic[val].append(i)

        
# for i in dic.keys():
#     name=str(i)+'_clusternumber.csv'
#     arra=[]
#     numb=[]
#     deta=[]
#     for j in dic[i]:
#         arra.append(df_y[j])
#         numb.append(j)
#         deta.append(df_x[j])
#     dict={'log_no':numb,'date':arra,'time':deta}
#     data_f=pd.DataFrame(dict)
#     data_f.to_csv(name)        
