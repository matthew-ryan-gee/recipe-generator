import re
import csv
import pandas as pd
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
from ast import literal_eval
import pdpipe as pdp
import re


# writer.writerow([title, url, author, servings, list(ingredients), steps])


#dataframe:['title', 'url', 'author', 'servings', 'ingredients', 'steps']
#dataframeProcessed: ['title', 'url', 'author', 'servings', 'ingredients', 'steps', 'ingredientsCleaned']
#TDI: (term, docID)
#invertedIndex: ([term, frequency, [docID's]], tag)

def readData(file):
    return pd.read_csv(file)

def getColumn(dataframe, column):
    return dataframe[column]

def processInvertedIndex(frame,column,invertedIndex):
    from nltk import pos_tag
    processedIndex = []
    for entry in invertedIndex:
        word = entry[0]
        tag = pos_tag([word])[0][1]
        entry.append(tag)
        # print("\n", term, pos_tag([term]))
        print(entry)
    print(len(invertedIndex))
    

def createInvertedIndex(frame, column, TDI):
    TDI = sorted(TDI)
    invertedIndex = []
    for pair in TDI:
        term = pair[0]
        docID = pair[1]
        if len(invertedIndex) > 0 and pair[0] == invertedIndex[-1][0]:
        #if invertedIndex is not empty AND the word of thre Row is not equal to the last row entered in the iIndex
            #increase the frequency of that word
            invertedIndex[-1][1] = invertedIndex[-1][1] + 1
            #add the docID of the pair to the posting list
            invertedIndex[-1][2].append(pair[1])
        else:
            postingList = []
            postingList.append(docID)
            invertedIndex.append( [term, 1, postingList] )
    # for row in invertedIndex:
    #     print("\n", row)
    processInvertedIndex(frame,column,invertedIndex)
def createTDI(frame, column):
    docID = 0
    TDI = []
    for row in frame[column]:
        for word in row:
            TDI.append( (word, docID) )
        docID = docID + 1
        # print("\n ", docID)
    
    
    # print("createTDI ")
    
    createInvertedIndex(frame,column,TDI)
    # for row in TDI:
    #     print("\n", row)

def sortColumn(frame, column):
    sortedColumn = []
    
    for row in frame[column]:
        row = sorted(set(row))
        sortedColumn.append(row)
   
    frame[column] = sortedColumn
    # print("sortedColumn")
    # print(frame)
    createTDI(frame, column)

def removeStopWords(frame, column):
    from nltk.corpus import stopwords
    stopwords = set(stopwords.words('english'))
    
    columnNoStops = []
    for row in frame[column]:
        rowNoStops = []
        for token in row:
            if token not in stopwords:
                if re.match("[a-zA-Z-]*$", token):
                    rowNoStops.append(token)
        columnNoStops.append(rowNoStops)
    frame[column] = columnNoStops
    
    # print("removeStopWords")
    # print(frame[column])
    
    sortColumn(frame, column)
    
def porterStemmer(frame, column):
    stemmer = PorterStemmer()
    column_stemmed = []
    for row in frame[column]:
        row_stemmed = []
        for token in row:
            row_stemmed.append(stemmer.stem(token))
        column_stemmed.append(row_stemmed)
    frame[column] = column_stemmed
    # print("Porter Stemmer")
    # print(frame[column])
    
    removeStopWords(frame, column)
            
    
def tokenize(frame, column):
    column_tokenized = []
    for row in frame[column]:
        column_tokenized.append(word_tokenize(row))
    
    # print("Tokenize")
    # print(column_tokenized)
    
    frame[column] = column_tokenized
    
    #must choose between using porterStemmer or skipping directly to removeStopWords
    # porterStemmer(frame, column)
    
    removeStopWords(frame,column)
    # return(frame, column)
    


    
def queryMachine(dframe):
    print("Query Machine")
     
def searchTDImatrix(column):
    print("searchTDImatrix not implemented")


        
     
def ingredient_pipeline(frame):
    ingredientsConcatenated = []
    column = frame['ingredients']
    # ingredient_text
    for row in column:
        ingredientsAsString = ""
        for pair in list(literal_eval(row)):
            ingredientsAsString = ingredientsAsString + pair[1] + " "
        ingredientsConcatenated.append(ingredientsAsString)
    frame['ingredientsCleaned'] = ingredientsConcatenated
    # print(frame['ingredientsCleaned'])
    

    # print("Ingredients Pipeline")
    # print(frame)
    
    # return(frame)
    
    tokenize(frame, 'ingredientsCleaned')
    
def title_pipeline(column):
    print("not implemented")
    
def pipelineStart(dataframe):
    ingredient_pipeline(dataframe)
    title_pipeline(dataframe)



dataframe = readData("bonappetit_data.csv")
# print(dataframe)
print(dataframe)
ingredients = ingredient_pipeline(dataframe)
# title = title_pipeline('title')



     
