import re
import csv
import pandas as pd
from nltk import PorterStemmer
from ast import literal_eval
import pdpipe as pdp



# writer.writerow([title, url, author, servings, list(ingredients), steps])

def readData(file):
    return pd.read_csv(file)

def getColumn(dataframe, column):
    return dataframe[column]
    
    

def removeStopWords(element):
    print("removeStopWords not implemented")
    
def porterStemmer(element):
    print("porterStemmer not implemented")
    
def tokenize(element):
    print("tokenize not implemented")



    
def createTDI(column):
    print("createTDI not implemented")
    
def queryMachine(dframe):
    print("Query Machine")
     
def searchTDImatrix(column):
    print("searchTDImatrix not implemented")
    
def createDictionary(column):
    print('whatever')
     
def ingredient_pipeline(frame):
    frame['ingredientsClean'] = ""
    column = frame['ingredients']
    # ingredient_text
    index = 0
    for row in column:
        ingredientsAsString = ""
        for pair in list(literal_eval(row)):
            ingredientsAsString += "h"# pair[1]
        frame.at['ingredientsClean', index] = ingredientsAsString
        index += 1

    print(frame['ingredientsClean'])
    
    # column = createDictionary(column)
    
def title_pipeline(column):
    print("not implemented")



dataframe = readData("input.csv")
# print(dataframe)
ingredients = ingredient_pipeline(dataframe)
# title = title_pipeline('title')



     
