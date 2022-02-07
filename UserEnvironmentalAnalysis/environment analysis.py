import pandas as pd
import numpy as np
import gensim
import jieba
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from Bio.Cluster import kcluster
from Bio.Cluster import clustercentroids
from sklearn.metrics import silhouette_score
from collections import Counter

df1 = pd.read_csv('D:/BA实习项目/user environment analysis/data/raw_data_1/1.csv')
df2 = pd.read_csv('D:/BA实习项目/user environment analysis/data/raw_data_1/2.csv')
df3 = pd.read_csv('D:/BA实习项目/user environment analysis/data/raw_data_1/3.csv',error_bad_lines=False)
df4 = pd.read_csv('D:/BA实习项目/user environment analysis/data/raw_data_1/4.csv')
df5 = pd.read_csv('D:/BA实习项目/user environment analysis/data/raw_data_1/5.csv')
df6 = pd.read_csv('D:/BA实习项目/user environment analysis/data/raw_data_1/6.csv')
df7 = pd.read_csv('D:/BA实习项目/user environment analysis/data/raw_data_1/7.csv',error_bad_lines=False)
df8 = pd.read_csv('D:/BA实习项目/user environment analysis/data/raw_data_1/8.csv',error_bad_lines=False)
df9 = pd.read_csv('D:/BA实习项目/user environment analysis/data/raw_data_1/9.csv',error_bad_lines=False)
df10 = pd.read_csv('D:/BA实习项目/user environment analysis/data/raw_data_1/10.csv')
df11 = pd.read_csv('D:/BA实习项目/user environment analysis/data/raw_data_1/11.csv')
df12 = pd.read_csv('D:/BA实习项目/user environment analysis/data/raw_data_1/12.csv',error_bad_lines=False)
df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12],axis=0,ignore_index = True)
df_data = df[['corpid','create_vid','docid','name']]
#print(df_data)
df_index = pd.read_table('D:/BA实习项目/user environment analysis/data/raw_data_2/idex_1581056559197_9734.txt',usecols=[2,3,0,4,6]).rename(columns={'corpid_':'corpid','docid_':'docid'})
#print(df_index)
df_raw = pd.merge(df_data,df_index,how='left',on=['corpid','docid'])
#print(df_raw)
#精确模式分词,去停用词
doc_name = df_raw['name'].tolist()
stopwords = {}.fromkeys([line.rstrip() for line in open('D:/BA实习项目/stopword.txt',encoding='utf8')])
after_divide_name = list()

for i in doc_name:
    e = []
    element = jieba.cut(i)
    for j in element:
        if j not in stopwords and j!=' ':
            e.append(j)
    after_divide_name.append(e)
#print(after_divide_name)
'''
#计算词频，找出模板词，将模板词加入停用词表
all_word = ''.join('%s' %i for i in after_divide_name)
all_words = all_word.split()
c=Counter()
for x in all_words:
    if len(x) > 1 and x != '\r\n':
        c[x] += 1
print('\n词频统计结果:')
for (k,v) in c.most_common(15):# 输出词频最高的前10个词
    print("%s:%d"%(k,v))
#print(after_divide_name)
'''

#corpus:百度百科800w+,搜狐新闻400w+,小说229G+
#model param：window=5,min_count=10,size=128(维度),hs=1,negative=0,iter=5
model = gensim.models.KeyedVectors.load_word2vec_format('D:/BA实习项目/pre-train model/baike_26g_news_13g_novel_229g.bin', binary=True)

#将词语转化为词向量并求每个句子的向量均值
vecs_sentence = []
for sentence in after_divide_name:
    vecs_word = np.zeros(128)
    count = 0
    for word in sentence:
        try:
            count = count+1
            vecs_word = model[word]+vecs_word
        except KeyError:
            continue
    if count!=0:
        vecs_word = vecs_word/count
    if vecs_word.all()==0:continue
    vecs_sentence.append(vecs_word)
data_input = np.array(vecs_sentence)
#print(data_input)
#Kmeans聚类
#data_input = data_input[data_input!=0]
#print(data_input)
#df_data = pd.DataFrame(vecs_sentence)
#coef = []

(clusterid, error, nfound) = kcluster(data_input,nclusters=2,dist='u')
for x in clusterid:
    cdata = clustercentroids(data_input)

#(cdata, cmask) = vecs_sentence.clustercentroid()
#print((cdata,cmask))
coef = []
x = range(3,20)
for clusters in x:
    clusterid, error, nfound = kcluster(data_input,clusters,dist='u',npass=10)
    silhouette_avg = silhouette_score(data_input, clusterid, metric='cosine')
    coef.append(silhouette_avg)

e =[i+2 for i,j in enumerate(coef) if j == max(coef)]
print(e)
print(coef)
plt.plot(x,coef)
plt.show()
'''
estimator = KMeans(init='k-means++', n_clusters=5, n_init=5)
estimator.fit(data_input)
label_color = ['r','g','b','c','y']
colors = [label_color[i] for i in clusterid.labels_]
def show_scatter(data,colors):
    x,y = dat
    plt.scatter(x,y,c=colors)
    plt.axis()
    plt.title("scatter")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()
show_scatter(data_input,colors)
'''
'''
from nltk.cluster.kmeans import KMeansClusterer
import nltk
kclusterer = KMeansClusterer(num_means=5, distance=nltk.cluster.util.cosine_distance,avoid_empty_clusters=True)
cluster = kclusterer.cluster(data_input,assign_clusters=True)
centroids = kclusterer.means()
#print(centroids)

for i in centroids:
    key_vector = model.similar_by_vector(i, topn=5)
    print(key_vector)



for x in range(0,4):
    centroid = kclusterer._centroid(data_input,mean=x)
    key_vector = model.similar_by_vector(centroid,topn=10)
    relate_words.append(key_vector)
print(relate_words)
'''

