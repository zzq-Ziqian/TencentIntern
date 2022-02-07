import pandas as pd
import numpy as np

df1 = pd.read_csv("D:/BA实习项目/data/first_view_doc.csv",usecols=[3,4])

#after_create留存分析
df2_create = pd.read_table("D:/BA实习项目/data/after_create.txt")
df3_create = pd.merge(df1, df2_create, how='inner', on='docid')
df4_create = df3_create[df3_create['name'] != '欢迎使用微文档']
new_vid_create = df4_create.groupby('ds')
df5_create = new_vid_create.get_group(20191223).drop_duplicates(subset=['vid'])
df6_create = new_vid_create.get_group(20191224).drop_duplicates(subset=['vid'])
df7_create = df5_create[df5_create['20191226'] != '\\N']
df8_create = df6_create[df6_create['20191227'] != '\\N']
new_user_create = len(df5_create) + len(df6_create)
remain_user_create = len(df7_create) + len(df8_create)
rate_create = remain_user_create / new_user_create
print('有create行为的用户留存率为'+str(rate_create))

#after_view留存分析
df2_view = pd.read_table("D:/BA实习项目/data/after_view.txt")
df3_view = pd.merge(df1, df2_view, how='inner', on='docid')
df4_view = df3_view[df3_view['name'] == '欢迎使用微文档']
df5_view = df3_view[df3_view['name'] != '欢迎使用微文档']
new_vid1_view = df4_view.groupby('ds')#带有1后缀的为微文档用户
df6_view = new_vid1_view.get_group(20191223).drop_duplicates(subset=['vid'])
df7_view = new_vid1_view.get_group(20191224).drop_duplicates(subset=['vid'])
new_vid2_view = df5_view.groupby('ds')#带有2后缀的为其他用户
df8_view = new_vid2_view.get_group(20191223).drop_duplicates(subset=['vid'])
df9_view = new_vid2_view.get_group(20191224).drop_duplicates(subset=['vid'])
df10_view = df6_view[df6_view['20191226'] != '\\N']
df11_view = df7_view[df7_view['20191227'] != '\\N']
df12_view = df8_view[df8_view['20191226'] != '\\N']
df13_view = df9_view[df9_view['20191226'] != '\\N']
new_user1_view = len(df7_view) + len(df6_view)
remain_user1_view = len(df10_view) + len(df11_view)
new_user2_view = len(df8_view) + len(df9_view)
remain_user2_view = len(df12_view) + len(df13_view)
rate1_view = remain_user1_view / new_user1_view
#print(rate1_view)
rate2_view = remain_user2_view / new_user2_view
print('有view行为的用户留存率为'+str(rate2_view))

#after_edit留存分析
df2_edit = pd.read_table("D:/BA实习项目/data/after_edit.txt")
df3_edit = pd.merge(df1, df2_edit, how='inner', on='docid')
df4_edit = df3_edit[df3_edit['name'] == '欢迎使用微文档']
df5_edit = df3_edit[df3_edit['name'] != '欢迎使用微文档']
new_vid1_edit = df4_edit.groupby('ds')
df6_edit = new_vid1_edit.get_group(20191223).drop_duplicates(subset=['vid'])
df7_edit = new_vid1_edit.get_group(20191224).drop_duplicates(subset=['vid'])
new_vid2_edit = df5_edit.groupby('ds')
df8_edit = new_vid2_edit.get_group(20191223).drop_duplicates(subset=['vid'])
df9_edit = new_vid2_edit.get_group(20191224).drop_duplicates(subset=['vid'])
df10_edit = df6_edit[df6_edit['20191226'] != '\\N']
df11_edit = df7_edit[df7_edit['20191227'] != '\\N']
df12_edit = df8_edit[df8_edit['20191226'] != '\\N']
df13_edit = df9_edit[df9_edit['20191226'] != '\\N']
new_user1_edit = len(df7_edit) + len(df6_edit)
remain_user1_edit = len(df10_edit) + len(df11_edit)
new_user2_edit = len(df8_edit) + len(df9_edit)
remain_user2_edit = len(df12_edit) + len(df13_edit)
rate1_edit = remain_user1_edit / new_user1_edit
#print(rate1_edit)
rate2_edit = remain_user2_edit / new_user2_edit
print('有edit行为的用户留存率为'+str(rate2_edit))
'''
#after_forward留存分析
df2_forward = pd.read_table("D:/BA实习项目/data/after_forward.txt")
df3_forward = pd.merge(df1, df2_forward, how='inner', on='docid')
df4_forward = df3_forward[df3_forward['name']=='欢迎使用微文档']
df5_forward = df3_forward[df3_forward['name']!='欢迎使用微文档']
new_vid1_forward = df4_forward.groupby('ds')
df6_forward = new_vid1_forward.get_group(20191223).drop_duplicates(subset=['vid'])
df7_forward = new_vid1_forward.get_group(20191224).drop_duplicates(subset=['vid'])
new_vid2_forward = df5_forward.groupby('ds')
df8_forward = new_vid2_forward.get_group(20191223).drop_duplicates(subset=['vid'])
df9_forward = new_vid2_forward.get_group(20191224).drop_duplicates(subset=['vid'])
df10_forward = df6_forward[df6_forward['20191226'] != '\\N']
df11_forward = df7_forward[df7_forward['20191227'] != '\\N']
df12_forward = df8_forward[df8_forward['20191226'] != '\\N']
df13_forward = df9_forward[df9_forward['20191226'] != '\\N']
rate1_forward = ((len(df10_forward) + len(df11_forward))) / ((len(df7_forward) + len(df6_forward)))
#print(rate1_forward)
rate2_forward = ((len(df12_forward) + len(df13_forward))) / ((len(df8_forward) + len(df9_forward)))
print(rate2_forward)
'''
#用户漏斗模型
convert_view_to_create = new_user_create/new_user2_view
print('view行为到create行为的转化率为'+str(convert_view_to_create))
convert_create_to_edit = new_user2_edit/new_user_create
print('create行为到edit行为的转化率为'+str(convert_create_to_edit))
#convert_edit_to_forward = new_user2_forward/new_user2_edit
#print('edit行为到forward行为的转化率为'+str(convert_edit_to_forward))