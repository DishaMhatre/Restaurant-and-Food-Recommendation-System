# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 21:46:46 2020

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

    
input_file = 'zomato_res_final.csv'
dataset = pd.read_csv(input_file)
df = pd.DataFrame(dataset)
   
    

def getCuisinesList():
    cuisinesList=[]
    for i in range (6526):
        string=str(df.loc[i,'Cuisines'])
        li = string.split (",")
        for item in li:
            if(item not in cuisinesList):
                cuisinesList.append(item)
   # print(cuisinesList)
   # print(len(cuisinesList))
    return cuisinesList

def getVegList():
    vegList=[]
    for i in range(6526):
        string=str(df.loc[i,'Veg only'])
        li=string.split(",")
        
        for item in li:
            
                vegList.append(item)
                
                
                
   
   
   # print(len(vegList))
                
    # listToStr=''.join([str(elem) for elem in vegList])
    new_list=list(map(float,vegList))
    
    # finalList=int(listToStr)
##  print(finalList)
    print(new_list)
    return new_list



def getResTypeList():
    resTypeList=[]
    for i in range (6526):
        string=str(df.loc[i,'Restaurant_Type'])
        li = string.split (",")
        for item in li:
            if(item not in resTypeList):
                resTypeList.append(item)
    return resTypeList

cuisines=getCuisinesList()
resTypes=getResTypeList()
#print(resTypes)



    
def getCuisines():
    
    cuisine={} 
     
    cuisinevector=[] 
    cuisinevect={}
        
    for i in range (6526):
        cuisine_list=[]
        res_name=df.loc[i,'Restaurant_Name']
        
        string=str(df.loc[i,'Cuisines'])
        cuisine.update( {res_name :string } )
        
    return cuisine


def getResTypes():
    
    resType={} 
     
    resTypevector=[] 
    resTypevect={}
        
    for i in range (6526):
        resType_list=[]
        res_name=df.loc[i,'Restaurant_Name']
        
        string=str(df.loc[i,'Restaurant_Type'])
        resType.update( {res_name :string } )
        
    return resType
        
    
def getPrices():
   
    price={} 
   
        
    for i in range (6526):
        cuisine_list=[]
        res_name=df.loc[i,'Restaurant_Name']
        pricefortwo=df.loc[i,'Cost_for_two(Rs.)']
        
        price.update( {res_name :pricefortwo } )
       
    return price


def getCuisineVector():
   
    cuisine={} 
   
    cuisinevector=[] 
    cuisinevect={}
        
    for i in range (6526):
        cuisine_list=[]
        res_name=df.loc[i,'Restaurant_Name']
       
        string=str(df.loc[i,'Cuisines'])
        cuisine.update( {res_name :string } )
       
        cuisinelist=string.split(",")
        cuisinevector=[0] * 195
           
                       
                       
        for item in cuisinelist:
            cuisine_list.append(item)
        for items in cuisine_list:
            for i in cuisines:
                   
                if(cmp(items,i)):
                    cuisinevector[cuisines.index(i)]=1
                    break
                       
        cuisinevect.update( {res_name :cuisinevector } )    
           
    return cuisinevect

def getVeg():
     VegOnly={}
    
     for i in range (6526):
              cusine_list=[]
              res_name=df.loc[i,'Restaurant_Name']
              veg=df.loc[i,'Veg only']
              VegOnly.update({res_name :veg})
              
              
     return VegOnly
         

# def getLongitude():
#      longitude={}
    
#      for i in range (6526):
#          cusine_list=[]
#          res_name=df.loc[i,'Restaurant_Name']
#          longitudes=df.loc[i,'Longitude']
#          longitude.update({res_name :longitudes})
        
        
#      return longitude
def getResTypeVector():
   
    resType={} 
   
    resTypevector=[] 
    resTypevect={}
        
    for i in range (6526):
        resType_list=[]
        res_name=df.loc[i,'Restaurant_Name']
       
        string=str(df.loc[i,'Restaurant_Type'])
        resType.update( {res_name :string } )
       
        resTypelist=string.split(",")
        resTypevector=[0] * 23
           
                       
                       
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
vegonly=getVeg()



inputCuisines=input('Enter cuisines separated by commas: \n')
inputResType=input('Enter Restaurant Type: \n')
inputPrice=int(input('Enter your budget for two:\n'))
inputVeg=float(input('Enter 1 for veg only \n'))




def computePriceSimilarity(inputPrice,prices):
    simPriceDict={}
    simPrices={}
    simPriceList=[]
    for i in range (6526):
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
    inputCuisineVector=[0] * 195
    for items in listInputCuisines:
            for i in cuisines:
                   
                if(cmp(items,i)):
                    inputCuisineVector[cuisines.index(i)]=1
                    break
    #print(inputCuisineVector)
    for i in range(6526):
        res_name=df.loc[i,'Restaurant_Name']
        restCuisineVector=cuisineVector[res_name]
        sumxx, sumxy, sumyy = 0, 0, 0
       
        for r in range(len(restCuisineVector)-1):
            x=inputCuisineVector[r]
            
            y=restCuisineVector[r]
            
            sumxx += x * x
            sumyy += y * y
            sumxy += x * y
            
        simScore= sumxy/float((sumxx*sumyy)**0.5)
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
    inputResTypeVector=[0] * 23
    for items in listInputResType:
            for i in resTypes:
                   
                if(cmp(items,i)):
                    inputResTypeVector[resTypes.index(i)]=1
                    break
    #print(inputResTypeVector)
    for i in range(6526):
        res_name=df.loc[i,'Restaurant_Name']
        restResTypeVector=resTypeVector[res_name]
        sumxx, sumxy, sumyy = 0, 0, 0
        
        for r in range(len(restResTypeVector)):
            x=inputResTypeVector[r]
            y=restResTypeVector[r]
            sumxx += x * x
            sumyy += y * y
            sumxy += x * y
     
        simScore1= sumxy/float((sumxx*sumyy)**0.5)
       
        simScoreList1.append(simScore1)
        simScoreDict1.update( {res_name :simScore1 } )
        
        
    a1_sorted_keys = sorted(simScoreDict1, key=simScoreDict1.get, reverse=True)
    for r in a1_sorted_keys:
        simScores1.update( {r :simScoreDict1[r] } )
        
   
   
    return simScoreList1

cuisineSimilarityList=computeCuisineSimilarity(inputCuisines,cuisine)
priceSimilarityList=computePriceSimilarity(inputPrice,prices)
resTypeSimilarityList=computeResTypeSimilarity(inputResType,resTypes)
veglist=(getVegList())


finalSimList=[]
finalSimDict={}
finalSimi={}
for i in range(6526):
    if(inputVeg == 1):
        similarity=cuisineSimilarityList[i]*priceSimilarityList[i]*resTypeSimilarityList[i]*veglist[i]
        
        
        
    else:
        similarity=cuisineSimilarityList[i]*priceSimilarityList[i]*resTypeSimilarityList[i]
        
        
    finalSimList.append(similarity)
    res_name=df.loc[i,'Restaurant_Name']
    finalSimDict.update( {res_name :similarity } )
a1_sorted_keys = sorted(finalSimDict, key=finalSimDict.get, reverse=True)
for r in a1_sorted_keys:
    finalSimi.update( {r :finalSimDict[r] } )

out = dict(itertools.islice(finalSimi.items(),10)) 

#inputLat=input('Enter Latitude  \n')
#inputLong=input('Enter Longitude  \n')

#print(finalSimi)

# newlist=list()
# for i in out.keys():
#     newlist.append(i)
    
# #(newlist)

print('We Recommend:\n')
print(out.keys())
 
