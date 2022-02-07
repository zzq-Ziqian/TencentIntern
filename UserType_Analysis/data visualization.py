import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#用户层面
df_doc = pd.read_table('D:/BA实习项目/data visualization/user_coverage_analysis/doc_user_freq.txt',usecols = [0,2]).drop_duplicates(subset=['vid_'])
df_drive = pd.read_table('D:/BA实习项目/data visualization/user_coverage_analysis/drive_user_freq.txt',usecols = [0,2]).drop_duplicates(subset=['vid_'])
df_all = pd.merge(df_doc,df_drive,how='outer',on='vid_',suffixes=('_doc','_drive')).fillna(value=0)
print(df_all)
df_overlap = pd.merge(df_doc,df_drive,how='inner',on='vid_',suffixes=('_doc','_drive'))
print(df_overlap)

x = df_all['_c2_doc'].tolist()
y = df_all['_c2_drive'].tolist()
#print(x,y)
pcc_doc_drive = np.corrcoef(x,y)
print(pcc_doc_drive)

#df_overlap.groupby([1],[2]).count()

sns.set(style="white", color_codes=True)
sns.regplot(x='_c2_doc',y='_c2_drive',data=df_overlap,scatter_kws={'alpha':0.05},fit_reg=False)
plt.show()
sns.regplot(x='_c2_doc',y='_c2_drive',data=df_overlap,scatter_kws={'alpha':0},line_kws={'color':'r'})
plt.show()

