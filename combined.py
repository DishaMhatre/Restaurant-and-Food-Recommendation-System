# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 22:05:38 2020

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
   
    

def getCuisinesList():
    cuisinesList=[]
    for i in range (6405):
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
    for i in range(6405):
        string=str(df.loc[i,'Veg only'])
        li=string.split(",")
        
        for item in li:
            
                vegList.append(item)
                
                
                
   
   
   # print(len(vegList))
                
    # listToStr=''.join([str(elem) for elem in vegList])
    new_list=list(map(float,vegList))
    
    # finalList=int(listToStr)
##  print(finalList)
   #print(new_list)
    return new_list



def getResTypeList():
    resTypeList=[]
    for i in range (6405):
        string=str(df.loc[i,'Restaurant_Type'])
        li = string.split (",")
        for item in li:
            if(item not in resTypeList):
                resTypeList.append(item)
                
    #print(len(resTypeList))
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
   # print(len(occTypeList))
    return occTypeList


cuisines=getCuisinesList()
resTypes=getResTypeList()
occasions=getOccasionTypeList()

#print(resTypes)





    
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
      
   
def getPrices():
   
    price={} 
   
        
    for i in range (6405):
        cuisine_list=[]
        res_name=df.loc[i,'Restaurant_Name']
        pricefortwo=df.loc[i,'Cost_for_two(Rs.)']
        
        price.update( {res_name :pricefortwo } )
       
    return price


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
    
     for i in range (6405):
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


resType=getResTypes()
cuisine=getCuisines()
prices=getPrices()
cuisineVector=getCuisineVector()
resTypeVector=getResTypeVector()
vegonly=getVeg()
occasion=getOccasions()
occasionVector=getOccasionVector()


inputCuisines=input('Enter cuisines separated by commas: \n')
inputResType=input('Enter Restaurant Type: \n')
inputPrice=int(input('Enter your budget for two:\n'))
inputVeg=float(input('Enter 1 for veg only \n'))
inputOccasions=input('Enter Occasion Type: \n')




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
    inputCuisineVector=[0] * 195
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
     
        simScore1= sumxy/float((sumxx*sumyy)**0.5)
       
        simScoreList1.append(simScore1)
        simScoreDict1.update( {res_name :simScore1 } )
        
        
    a1_sorted_keys = sorted(simScoreDict1, key=simScoreDict1.get, reverse=True)
    for r in a1_sorted_keys:
        simScores1.update( {r :simScoreDict1[r] } )
        
   
   # print(simScoreList1)
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
veglist=(getVegList())


finalSimList=[]
finalSimDict={}
finalSimi={}
for i in range(6405):
    if(inputVeg == 1):
        similarity=cuisineSimilarityList[i]*priceSimilarityList[i]*resTypeSimilarityList[i]*veglist[i]*sal[i]
        
        
        
    else:
        similarity=cuisineSimilarityList[i]*priceSimilarityList[i]*resTypeSimilarityList[i]*sal[i]
        
        
    finalSimList.append(similarity)
    res_name=df.loc[i,'Restaurant_Name']
    finalSimDict.update( {res_name :similarity } )
#print(finalSimDict)
a1_sorted_keys = sorted(finalSimDict, key=finalSimDict.get, reverse=True)
for r in a1_sorted_keys:
    finalSimi.update( {r :finalSimDict[r] } )

print(finalSimi)
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
 

l1=float(input("Enter value of latitude"))
l2=float(input("Enter value of longitude"))


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
    for i in range(10):
        dist=math.sqrt((l1-lat[i])**2+(l2-long[i])**2)
        locDist.append(dist)
    locDistDict={}
    i=0
    for x in out:
        locDistDict.update({x:locDist[i]})
        i+=1
    print(locDistDict)
    return locDistDict
computeLoc(out,l1,l2)