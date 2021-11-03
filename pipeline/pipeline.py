import re
import csv
import pandas as pd
from nltk import PorterStemmer
from ast import literal_eval
import pdpipe as pdp



# writer.writerow([title, url, author, servings, list(ingredients), steps])

def readData():
    dataframe = pd.read_csv('input.csv')
    createTDImatrix(dataframe['ingredients'])
    #
    
def createTDImatrix(column):
    count = 0
    for row in column:
            for tupl in list(literal_eval(row)):
                print(tupl)
            
            print(count)
            count +=1
    print("create Term Document Index")
    
def queryMachine():
     print("Query Machine")
     
readData()
     
