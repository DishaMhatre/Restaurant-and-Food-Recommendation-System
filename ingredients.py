import itertools 
import csv
import numpy
import pandas as pd
import math
import numpy as np

input_file = 'ingredients.csv'
dataset = pd.read_csv(input_file)
df = pd.DataFrame(dataset)

nonvegList=['eggs', 'chicken', 'egg','prawns','bacon','meat','sausage','sausages','buffalo',
            'goat cheese','mutton','crab','fish','lamb','steak','beef','pork','turkey','squid',
            'ham','lobster','duck','broth']


inputCuisine=input("Enter the cuisine: \n")
inputIngr=input("Enter the ingredients separated by commas: \n")

list = inputIngr.split (",")
listInputIngr = []
for i in list:
    listInputIngr.append((i))
        
rows=len(df.axes[0])
columns=len(df.axes[1])

#print(listInputIngr)
scoreList=[]
scoreDict={}
scores={}
for i in range(982):
    summ=0
    cuisine=df.loc[i,'Cuisine']
    dish=df.loc[i,'Dish']
    if(cuisine==inputCuisine):
        thisIngr=df.loc[i,'Ingredients']
        list1=thisIngr.split(",")
        listThisIngr=[]
        for j in list1:
            listThisIngr.append(j)
        length=len(listThisIngr)
        for item in listThisIngr:
            if item in nonvegList and item not in listInputIngr:
                summ=0
                break
                
            else:
                if item in listInputIngr:
                    summ=summ+1
        
        score=summ/length
        if (score>0):
            scoreList.append(score)
            scoreDict.update( {dish :score } )
        #print(df.loc[i,'Dish'],summ/length)
#print(scoreDict)
a1_sorted_keys = sorted(scoreDict, key=scoreDict.get, reverse=True)
for r in a1_sorted_keys:
     scores.update( {r :scoreDict[r] } )
list1=scores.keys()
print("We recommend: \n")        
print(list1)