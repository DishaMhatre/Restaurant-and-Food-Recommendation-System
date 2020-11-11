# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 20:36:15 2020

@author: Admin
"""

import itertools 
import csv
import numpy
import pandas as pd
import math
import numpy as np




def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros
def cmp(a, b):
    return [c for c in a if c.isalpha()] == [c for c in b if c.isalpha()]

    
input_file = 'zomatoFinal.csv'
dataset = pd.read_csv(input_file)
df = pd.DataFrame(dataset)

def getOccasions():
    
    occasion={} 
     
    occasionvector=[] 
    occasionvect={}
        
    for i in range (6405):
        occasion_list=[]
        res_name=df.loc[i,'Restaurant_Name']
        
        string=str(df.loc[i,'Occasion'])
        occasion.update( {res_name :string } )
        
    #print(occType)
        
    return occasion
   
    

def getCuisinesList():
    cuisinesList=[]
    for i in range (6405):
        string=str(df.loc[i,'Cuisines'])
        li = string.split (",")
        for item in li:
            if(item not in cuisinesList):
                cuisinesList.append(item)
    
    return cuisinesList

def getResTypeList():
    resTypeList=[]
    for i in range (6405):
        string=str(df.loc[i,'Restaurant_Type'])
        li = string.split (",")
        for item in li:
            if(item not in resTypeList):
                resTypeList.append(item)
    return resTypeList


def getOccasionTypeList():
    occTypeList=[]
    for i in range (6405):
        string=str(df.loc[i,'Occasion'])
        li = string.split (",")
        for item in li:
            if(item not in occTypeList):
                occTypeList.append(item)
                
                
   # print(occTypeList)
    #print(len(occTypeList))
    return occTypeList

cuisines=getCuisinesList()

resTypes=getResTypeList()

occasions=getOccasionTypeList()


    
def getCuisines():
    
    cuisine={} 
     
    cuisinevector=[] 
    cuisinevect={}
        
    for i in range (6405):
        cuisine_list=[]
        res_name=df.loc[i,'Restaurant_Name']
        
        string=str(df.loc[i,'Cuisines'])
        cuisine.update( {res_name :string } )
        
    return cuisine


def getResTypes():
    
    resType={} 
     
    resTypevector=[] 
    resTypevect={}
        
    for i in range (6405):
        resType_list=[]
        res_name=df.loc[i,'Restaurant_Name']
        
        string=str(df.loc[i,'Restaurant_Type'])
        resType.update( {res_name :string } )
        
    return resType
        
    
def getPrices():
   
    price={} 
   
        
    for i in range (6405):
        cuisine_list=[]
        res_name=df.loc[i,'Restaurant_Name']
        pricefortwo=df.loc[i,'Cost_for_two(Rs.)']
        
        price.update( {res_name :pricefortwo } )
       
    return price

def getOccasionVector():
   
    occasion={} 
   
    occasionvector=[] 
    occasionvect={}
        
    for i in range (6405):
        occasion_list=[]
        res_name=df.loc[i,'Restaurant_Name']
       
        string=str(df.loc[i,'Occasion'])
        occasion.update( {res_name :string } )
       
        occasionlist=string.split(",")
        occasionvector=[0] * 13
           
                       
                       
        for item in occasionlist:
            occasion_list.append(item)
        for items in occasion_list:
            for i in occasions:
                   
                if(cmp(items,i)):
                    occasionvector[occasions.index(i)]=1
                    break
                       
        occasionvect.update( {res_name :occasionvector } )    
           
    return occasionvect


def getCuisineVector():
   
    cuisine={} 
   
    cuisinevector=[] 
    cuisinevect={}
        
    for i in range (6405):
        cuisine_list=[]
        res_name=df.loc[i,'Restaurant_Name']
       
        string=str(df.loc[i,'Cuisines'])
        cuisine.update( {res_name :string } )
       
        cuisinelist=string.split(",")
        cuisinevector=[0] * 193
           
                       
                       
        for item in cuisinelist:
            cuisine_list.append(item)
        for items in cuisine_list:
            for i in cuisines:
                   
                if(cmp(items,i)):
                    cuisinevector[cuisines.index(i)]=1
                    break
                       
        cuisinevect.update( {res_name :cuisinevector } )    
           
    return cuisinevect


def getResTypeVector():
   
    resType={} 
   
    resTypevector=[] 
    resTypevect={}
        
    for i in range (6405):
        resType_list=[]
        res_name=df.loc[i,'Restaurant_Name']
       
        string=str(df.loc[i,'Restaurant_Type'])
        resType.update( {res_name :string } )
       
        resTypelist=string.split(",")
        resTypevector=[0] * 25
           
                       
                       
        for item in resTypelist:
            resType_list.append(item)
        for items in resType_list:
            for i in resTypes:
                   
                if(cmp(items,i)):
                    resTypevector[resTypes.index(i)]=1
                    break
                       
        resTypevect.update( {res_name :resTypevector } )    
           
    return resTypevect

resType=getResTypes()
cuisine=getCuisines()
prices=getPrices()
cuisineVector=getCuisineVector()
resTypeVector=getResTypeVector()
occasion=getOccasions()
occasionVector=getOccasionVector()
#print(resType)
#print(resTypeVector)

inputCuisines=input('Enter cuisines: \n')
inputResType=input('Enter Restaurant Type: \n')
inputOccasions=input('Enter Occasion Type: \n')
inputPrice=int(input('Enter your budget for two:\n'))

def computePriceSimilarity(inputPrice,prices):
    simPriceDict={}
    simPrices={}
    simPriceList=[]
    for i in range (6405):
        res_name=df.loc[i,'Restaurant_Name']
        thisprice=prices[res_name]
        diff = abs(thisprice - inputPrice)
        sim = math.exp(-diff / 10.0)
        simPriceList.append(sim)
        simPriceDict.update( {res_name :sim } )
    #print(simPriceDict)
    a1_sorted_keys = sorted(simPriceDict, key=simPriceDict.get, reverse=True)
    for r in a1_sorted_keys:
        simPrices.update( {r :simPriceDict[r] } )
        #r, simScoreDict[r]
    return simPriceList
        

def computeCuisineSimilarity(inputCuisines,cuisine):
    simScoreDict={}
    simScores={}
    simScoreList=[]
    list = inputCuisines.split (",")
    listInputCuisines = []
    for i in list:
    	listInputCuisines.append((i))
    #print(listInputCuisines)
    inputCuisineVector=[0] * 193
    for items in listInputCuisines:
            for i in cuisines:
                   
                if(cmp(items,i)):
                    inputCuisineVector[cuisines.index(i)]=1
                    break
    #print(inputCuisineVector)
    for i in range(6405):
        res_name=df.loc[i,'Restaurant_Name']
        restCuisineVector=cuisineVector[res_name]
        sumxx, sumxy, sumyy = 0, 0, 0
       
        for r in range(len(restCuisineVector)-1):
            x=inputCuisineVector[r]
            y=restCuisineVector[r]
            sumxx += x * x
            sumyy += y * y
            sumxy += x * y
       
        simScore= sumxy/((sumxx*sumyy)**0.5)
        simScoreList.append(simScore)
        simScoreDict.update( {res_name :simScore } )
        
    a1_sorted_keys = sorted(simScoreDict, key=simScoreDict.get, reverse=True)
    for r in a1_sorted_keys:
        simScores.update( {r :simScoreDict[r] } )
        
    return simScoreList

def computeResTypeSimilarity(inputResType,resType):
    simScoreDict1={}
    simScores1={}
    simScoreList1=[]
    list = inputResType.split (",")
    listInputResType = []
    for i in list:
    	listInputResType.append((i))
    #print(listInputCuisines)
    inputResTypeVector=[0] * 25
    for items in listInputResType:
            for i in resTypes:
                   
                if(cmp(items,i)):
                    inputResTypeVector[resTypes.index(i)]=1
                    break
    #print(inputResTypeVector)
    for i in range(6405):
        res_name=df.loc[i,'Restaurant_Name']
        restResTypeVector=resTypeVector[res_name]
        sumxx, sumxy, sumyy = 0, 0, 0
        
        for r in range(len(restResTypeVector)):
            x=inputResTypeVector[r]
            y=restResTypeVector[r]
            sumxx += x * x
            sumyy += y * y
            sumxy += x * y
       
        simScore1= sumxy/((sumxx*sumyy)**0.5)
        simScoreList1.append(simScore1)
        simScoreDict1.update( {res_name :simScore1 } )
        
        
    a1_sorted_keys = sorted(simScoreDict1, key=simScoreDict1.get, reverse=True)
    for r in a1_sorted_keys:
        simScores1.update( {r :simScoreDict1[r] } )
        
    return simScoreList1


def computeOccasionSimilarity(inputOccasions,occasion):
    simScoreDict2={}
    simScores2={}
    simScoreList2=[]
    list = inputOccasions.split (",")
    listInputOccasions = []
    for i in list:
    	listInputOccasions.append((i))
    #print(listInputOccasions)
    inputOccasionVector=[0] * 13
   
    for items in listInputOccasions:
            for i in occasions:
                   
                if(cmp(items,i)):
                    inputOccasionVector[occasions.index(i)]=1
                    break
   # print(inputOccasionVector)
    for i in range(6405):
        res_name=df.loc[i,'Restaurant_Name']
        restOccasionVector=occasionVector[res_name]
        #print(restOccasionVector)
        sumxx, sumxy, sumyy = 0, 0, 0
       
        for r in range(len(restOccasionVector)):
            x=inputOccasionVector[r]
            
            y=restOccasionVector[r]
            
            sumxx += x * x
            sumyy += y * y
            sumxy += x * y
        
        simScore2= sumxy/float((sumxx*sumyy)**0.5)
        simScoreList2.append(simScore2)
        simScoreDict2.update( {res_name :simScore2 } )
        
    a1_sorted_keys = sorted(simScoreDict2, key=simScoreDict2.get, reverse=True)
    for r in a1_sorted_keys:
        simScores2.update( {r :simScoreDict2[r] } )
        
    #print(simScoreDict2)
    return simScoreList2



cuisineSimilarityList=computeCuisineSimilarity(inputCuisines,cuisine)
priceSimilarityList=computePriceSimilarity(inputPrice,prices)
resTypeSimilarityList=computeResTypeSimilarity(inputResType,resTypes)
sal=computeOccasionSimilarity(inputOccasions,occasion)


finalSimList=[]
finalSimDict={}
finalSimi={}

for i in range(6405):
    similarity=cuisineSimilarityList[i]*priceSimilarityList[i]*resTypeSimilarityList[i]*sal[i]
    if (similarity>0):
        
        finalSimList.append(similarity)
        res_name=df.loc[i,'Restaurant_Name']
        finalSimDict.update( {res_name :similarity } )
a1_sorted_keys = sorted(finalSimDict, key=finalSimDict.get, reverse=True)
for r in a1_sorted_keys:
    finalSimi.update( {r :finalSimDict[r] } )
   
if(len(finalSimList)>5):
    out = dict(itertools.islice(finalSimi.items(), 5)) 
else:
    out=finalSimi

#print(out)
#recRestList=out.keys()
#print(recRestList)
 
l1=float(input("Enter value of latitude"))
l2=float(input("Enter value of longitude\n\n"))

length=len(out)
finalFinal={}
def computeLoc(out,l1,l2):
    lat=[]
    long=[]
    for x in out:
        for i in range(6405):
            thisRest=df.loc[i,'Restaurant_Name']
            if(x == thisRest):
                lat.append(df.loc[i,'Latitude'])
                long.append(df.loc[i,'Longitude'])
    locDist=[]
    for i in range(length):
        dist=math.sqrt((l1-lat[i])**2+(l2-long[i])**2)
        locDist.append(dist)
    locDistDict={}
    i=0
    for x in out:
        locDistDict.update({x:locDist[i]})
        i+=1
    locDist = sorted(locDistDict, key=locDistDict.get, reverse=False)
    for z in locDist:
        finalFinal.update({z:locDistDict[z]})
        
    locDistList=finalFinal.keys()
    #print(locDistList)
    
    return locDistList
print('We Recommend:\n')
print(computeLoc(out,l1,l2))
