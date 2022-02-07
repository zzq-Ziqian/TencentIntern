import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#公司层面
df_doc = pd.read_table('D:/BA实习项目/data visualization/user_coverage_analysis/doc_user_freq.txt',usecols = [0,1,2,5]).drop_duplicates(subset=['vid_'])
df_drive = pd.read_table('D:/BA实习项目/data visualization/user_coverage_analysis/drive_user_freq.txt',usecols = [0,1,2,5]).drop_duplicates(subset=['vid_'])
df_doc_c2 = pd.DataFrame(df_doc.groupby('corpid_')._c2.sum()).reset_index()
df_doc_corp_member = pd.DataFrame(df_doc.groupby('corpid_').corp_member.max()).reset_index()
df_doc1 = df_doc.drop_duplicates(subset=['corpid_']).reset_index(drop=True)
df_doc_new = pd.concat([df_doc1['corpid_'],df_doc_c2['_c2'],df_doc_corp_member['corp_member']],axis=1)
df_doc_new['average_c2'] = df_doc_new.apply(lambda x:x['_c2']/x['corp_member'],axis=1)

df_drive_c2 = pd.DataFrame(df_drive.groupby('corpid_')._c2.sum()).reset_index()
df_drive_corp_member = pd.DataFrame(df_drive.groupby('corpid_').corp_member.max()).reset_index()
df_drive1 = df_drive.drop_duplicates(subset=['corpid_']).reset_index(drop=True)
df_drive_new = pd.concat([df_drive1['corpid_'],df_drive_c2['_c2'],df_drive_corp_member['corp_member']],axis=1)
df_drive_new['average_c2'] = df_drive_new.apply(lambda x:x['_c2']/x['corp_member'],axis=1)

df_corp_all = pd.merge(df_doc_new,df_drive_new,how='outer',on='corpid_',suffixes=('_doc','_drive')).fillna(value=0)
print(df_corp_all)
df_corp_overlap = pd.merge(df_doc_new,df_drive_new,how='inner',on='corpid_',suffixes=('_doc','_drive'))
print(df_corp_overlap)
x = df_corp_all['average_c2_doc'].tolist()
y = df_corp_all['average_c2_drive'].tolist()
pcc_doc_drive = np.corrcoef(x,y)
print(pcc_doc_drive)
#画图
sns.set(style="white", color_codes=True)
sns.regplot(x='average_c2_doc',y='average_c2_drive',data=df_corp_all,scatter_kws={'alpha':0.5},fit_reg=False)
plt.show()
sns.regplot(x='average_c2_doc',y='average_c2_drive',data=df_corp_all,scatter_kws={'alpha':0},line_kws={'color':'r'})
plt.show()
sns.set(style="white", color_codes=True)
sns.regplot(x='average_c2_doc',y='average_c2_drive',data=df_corp_overlap,scatter_kws={'alpha':0.5},fit_reg=False)
plt.show()
sns.regplot(x='average_c2_doc',y='average_c2_drive',data=df_corp_overlap,scatter_kws={'alpha':0},line_kws={'color':'r'})
plt.show()

#行业层面
user_cols = ['industry','industryid','industry_name','field']
df_industry = pd.read_table('D:/BA实习项目/data visualization/user_coverage_analysis/wwindustry_corpscale.txt',sep=',',header=None,names=user_cols,usecols=[0,1,2])
#print(df_industry)
df_unique_corp_doc = pd.read_table('D:/BA实习项目/data visualization/user_coverage_analysis/doc_user_freq.txt',usecols = [1,7]).drop_duplicates(subset=['corpid_']).reset_index(drop=True)
#print(df_unique_corp_doc)
df_unique_corp_drive = pd.read_table('D:/BA实习项目/data visualization/user_coverage_analysis/drive_user_freq.txt',usecols = [1,7]).drop_duplicates(subset=['corpid_']).reset_index(drop=True)
#print(df_unique_corp_drive)
df_corp_industryid = pd.concat([df_unique_corp_doc,df_unique_corp_drive]).drop_duplicates(subset=['corpid_']).reset_index(drop=True)
df_corp_industry = pd.merge(df_corp_industryid,df_industry,on='industryid')
#print(df_corp_industry)
df_corp_all_industry = pd.merge(df_corp_all,df_corp_industry,on='corpid_')
pd.set_option('display.max_columns', None)
print(df_corp_all_industry)
df_industry_c2_doc = pd.DataFrame(df_corp_all_industry.groupby('industry_name')._c2_doc.sum()).reset_index()
df_industry_member_doc = pd.DataFrame(df_corp_all_industry.groupby('industry_name').corp_member_doc.sum()).reset_index()
df_industry_c2_drive = pd.DataFrame(df_corp_all_industry.groupby('industry_name')._c2_drive.sum()).reset_index()
df_industry_member_drive = pd.DataFrame(df_corp_all_industry.groupby('industry_name').corp_member_drive.sum()).reset_index()
df_final = pd.merge(pd.merge(df_industry_c2_doc,df_industry_member_doc,on='industry_name'),pd.merge(df_industry_c2_drive,df_industry_member_drive,on='industry_name'),on='industry_name')
df_final['average_doc'] = df_final.apply(lambda x:x['_c2_doc']/x['corp_member_doc'],axis=1)
df_final['average_drive'] = df_final.apply(lambda x:x['_c2_drive']/x['corp_member_drive'],axis=1)
#print(df_final)

# 画图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False# 这两行代码解决 plt 中文显示的问题

industry_name = df_final['industry_name'].tolist()
average_doc = df_final['average_doc'].tolist()
average_drive = df_final['average_drive'].tolist()
bar_width = 0.3
index_doc = np.arange(len(industry_name))
index_drive = index_doc + bar_width
plt.bar(index_doc, height=average_doc, width=bar_width, color='b', label='doc')
plt.bar(index_drive, height=average_drive, width=bar_width, color='g', label='drive')
plt.legend()
plt.xticks(index_doc + bar_width/2,industry_name)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.ylabel('行业平均使用率')  # 纵坐标轴标题
plt.title('行业使用产品情况')  # 图形标题

plt.show()

