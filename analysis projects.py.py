#!/usr/bin/env python
# coding: utf-8

# In[1]:


from csv import reader
of=open('googleplaystore.csv',encoding="utf-8")
rf=reader(of)
android=list(rf)
android_header=android[0]
android=android[1:]
def explore_data(dataset,end,start=0,count_rows_columns=False):
    for i in dataset[start:end]:
        print(i)
        print('\n')
    if count_rows_columns:
        print("Number of rows:",len(dataset))
        print("Number of columns:",len(dataset[0]))
print(android_header)
print("\n")
explore_data(android,540,544,count_rows_columns=True)
unique_apps=[]
duplicate_apps=[]
for row in android:
    name=row[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
print("Number of unique apps:",len(unique_apps))
print("Number of duplicate apps:",len(duplicate_apps))
def convert_million(s):
    if s.endswith('M'):
        s=s.rstrip('M')
        return float(s)*1000000
    else:
        return float(s)
reviews_max={}
for row in android:
    name=row[0]
    n_review=convert_million(row[3])
    if name in reviews_max and reviews_max[name]<n_review:
        reviews_max[name]=n_review
    elif name not in reviews_max:
        reviews_max[name]=n_review
android_clean=[]
already_added=[]
for row in android:
    name=row[0]
    n_review=convert_million(row[3])
    if n_review==reviews_max[name]and name not in already_added:
        android_clean.append(row)
        already_added.append(name)
def check_eng(name):
    non_ascii=0
    for ch in name:
        if ord(ch)>127:
            non_ascii+=1
        if non_ascii>3:
            return False
        else:
            return True
android_english=[]
for row in android_clean:
    name=row[0]
    if check_eng(name):
        android_english.append(row)
print(len(android_english))
android_final=[]
for row in android_english:
    price=row[7]
    if price=='0':
        android_final.append(row)
print(len(android_final))
print(android_header)
print('\n')
print(explore_data(android_final,0,3))
def freq_table(dataset,index):
    freq_dict={}
    total=0
    for row in dataset:
        total+=1
        genre=row[index]
        if genre in freq_dict:
            freq_dict[genre]+=1
        else:
            freq_dict[genre]=1
    freq_dict_perc={}
    for key in freq_dict:
        percent=freq_dict[key]/total*100
        freq_dict_perc[key]=percent
    return freq_dict_perc
freq_table(android_final,1)


# In[78]:


from csv import reader
of=open('AppleStore.csv',encoding="utf-8")
rf=reader(of)
ios=list(rf)
ios_header=ios[0]
ios=ios[1:]
def explore_data(dataset,end,start=0,count_rows_columns=False):
    for i in dataset[start:end]:
        print(i)
        print('\n')
    if count_rows_columns:
        print("Number of rows:",len(dataset))
        print("Number of columns:",len(dataset[0]))
        print(ios_header)
        print('\n')
        explore_data(ios,540,544,count_rows_columns=True)
unique_apps=[]
duplicate_apps=[]
for row in ios:
    name=row[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
print("Number of unique apps:",len(unique_apps))
print("Number of duplicate appps:",len(duplicate_apps))
def check_eng(name):
    non_ascii=0
    for ch in name:
        if ord(ch)>127:
            non_ascii+=1
        if non_ascii>3:
            return False
        else:
            return True
ios_final=[]
for row in ios_english:
    price==[4]
    if price=='0.0':
        ios_final.append(row)
print(len(ios_final))
print(ios_header)
print('\n')
print(explore_data(ios_final,0,3))
def freq_table(dataset,index):
    freq_dict={}
    total=0
    for row in dataset:
        total+=1
        genre=row[index]
        if genre in freq_dict:
            freq_dict[genre]+=1
        else:
            freq_dict[genre]=1
    freq_dict_perc={}
    for key in freq_dict:
        percent = freq_dict[key]/total*100
        freq_dict_perc[key]=percent
    return freq_dict_perc
freq_table(ios_final, -5)


# In[ ]:




