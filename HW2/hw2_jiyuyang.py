#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 00:02:44 2019

@author: jiyuyang
"""



raw_input=[]
trans=0
data={}
min_sup=2
'''
my_input=['good grilled fish sandwich and french fries , but the service is bad',
          'disgusting fish sandwich , but good french fries',
          'their grilled fish sandwich is the best fish sandwich , but pricy',
          'A B A B A B A']
for row in my_input:
    raw_input.append(row.split())
    for i,item in enumerate(raw_input[-1]):
        if item not in data:
            data[item] = set()
        data[item].add((trans,i))
    trans += 1
'''

while True:
    try:
        row = input()
    except EOFError:
        break
    raw_input.append(row.split())
    for i,item in enumerate(raw_input[-1]):
        if item not in data:
            data[item] = set()
        data[item].add((trans,i))
    trans += 1
    
    
def check(data):
    new_data={}
    for item in data:
        if len(data[item])>=2:
            new_data[item]=data[item]
    return new_data
data=check(data)
c1={}
c3={}
c2={}
c4={}
for i,itids in data.items():
  itids=set([(e[0], e[1]+1) for e in itids])
  next_list=[]
  for j in itids:
      if(j[1]<len(raw_input[j[0]]) and (not raw_input[j[0]][j[1]] in next_list)):
          next_list.append(raw_input[j[0]][j[1]])
  for j in next_list:
      if j in data:
          jtids = itids & data[j]
          if len(jtids) >= 2:
              c1[str(i+' '+j)]=(jtids)
              
for i,itids in c1.items():
  itids=set([(e[0], e[1]+1) for e in itids])
  next_list=[]
  for j in itids:
      if(j[1]<len(raw_input[j[0]]) and (not raw_input[j[0]][j[1]] in next_list)):
          next_list.append(raw_input[j[0]][j[1]])
  for j in next_list:
      if j in data:
          jtids = itids & data[j]
          if len(jtids) >= 2:
              c2[str(i+' '+j)]=(jtids)
              
for i,itids in c2.items():
  itids=set([(e[0], e[1]+1) for e in itids])
  next_list=[]
  for j in itids:
      if(j[1]<len(raw_input[j[0]]) and (not raw_input[j[0]][j[1]] in next_list)):
          next_list.append(raw_input[j[0]][j[1]])
  for j in next_list:
      if j in data:
          jtids = itids & data[j]
          if len(jtids) >= 2:
              c3[str(i+' '+j)]=(jtids)
for i,itids in c3.items():
  itids=set([(e[0], e[1]+1) for e in itids])
  next_list=[]
  for j in itids:
      if(j[1]<len(raw_input[j[0]]) and (not raw_input[j[0]][j[1]] in next_list)):
          next_list.append(raw_input[j[0]][j[1]])
  for j in next_list:
      if j in data:
          jtids = itids & data[j]
          if len(jtids) >= 2:
              c4[str(i+' '+j)]=(jtids)
res=[]
for key, value in c4.items():
    res.append([len(value),key])
for key, value in c3.items():
    res.append([len(value),key])
for key, value in c2.items():
    res.append([len(value),key])
for key, value in c1.items():
    res.append([len(value),key])
res=sorted(res,key=lambda x:x[1])
res=sorted(res,key=lambda x:x[0],reverse=True)
for row in res[:20]:
    print (row)