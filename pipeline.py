import re
import csv
import pandas as pd
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
from ast import literal_eval
import pdpipe as pdp


# writer.writerow([title, url, author, servings, list(ingredients), steps])


#dataframe:['title', 'url', 'author', 'servings', 'ingredients', 'steps']
#dataframeProcessed: ['title', 'url', 'author', 'servings', 'ingredients', 'steps', 'ingredientsCleaned']
#TDI: (term, docID)
#invertedIndex: ([term, frequency, [docID's]], tag)

def readData(file):
    return pd.read_csv(file)

def getColumn(dataframe, column):
    return dataframe[column]



# # NOT FUNCTIONAL
# def processInvertedIndex(frame,column,invertedIndex):
#     from nltk import pos_tag
#     processedIndex = []
#     for entry in invertedIndex:
#         word = entry[0]
#         tag = pos_tag([word])[0][1]
#         entry.append(tag)
#         # print("\n", term, pos_tag([term]))
#         print(entry)
#     print(len(invertedIndex))
    

def BSBI_index(frame, column, TDI):
    import time
    start = time.time()
    
    TDI = sorted(TDI)
    inverted_index = dict()
    for pair in TDI:
        term = pair[0]
        docID = pair[1]
        
        #if invertedIndex is not empty AND the term is the last item in the index
        if len(inverted_index) > 0 and term in inverted_index:
            
            #if last document listed in list of terms is the same as the new one
            if docID in inverted_index[term]:
                inverted_index[term][docID] = inverted_index[term][docID] + 1
                
            #if last document listed in list of terms is NOT the same as the new one, then add the new document and set value to 1
            else:
                inverted_index[term][docID] = 1
            
            
        #if term not in the list, then just make dict[term]'s value a new dict containing its frequency in the document.
        else:
            inverted_index[term] = dict()
            inverted_index[term][docID] = 1

    
    import pprint 
    output_s = pprint.pformat(dict(inverted_index))
    
    with open('BSBI_index.txt','w') as f:
        f.write(output_s)
    
    
    print("BSBI: ", len(inverted_index.keys()))
    end = time.time()
    print("BSBI time: ", end - start)
    
#     # processInvertedIndex(frame,column,invertedIndex)
    
#dict(term, dict(id: freq))
def SPIMI_index(frame,column,TDI):
    import time
    start = time.time()
    
    from mergedeep import merge
    block_list = []
    new_block = dict()
    block_size = 500
    block_index = 0
    
    def search_block_list(key, value):
        for block in block_list:
            if key in block:
                if value in block[key]:
                    block[key][value] = block[key][value] + 1
                else:
                    block[key][value] = 1
                return True
        return False
    
    for pair in TDI:
        term = pair[0] #key
        docID = pair[1] #value
        

        
        if term in new_block:  
            if docID in new_block[term]:
                new_block[term][docID] = new_block[term][docID] + 1
            else:
                new_block[term][docID] = 1
        else:
            #if not in block list, do the following (other upates are in the function)
            if search_block_list(term, docID) == False:
                if len(new_block) <= block_size:
                    new_block[term] = dict()
                    new_block[term][docID] = 1
                    
                else:
                    block_list.append(new_block)
                    block_index = block_index + 1
                    new_block = dict()
                    new_block[term] = dict()
                    new_block[term][docID] = 1
                    # print("new block", block_index, "!")
                    
                    
                    
    block_list.append(new_block)
    inverted_index = dict()
    
    print("BLOCK LIST: ", len(block_list))
    for block in block_list:
        merge(inverted_index, block)
        

    import pprint 
    output_s = pprint.pformat(dict(inverted_index))
    with open('SPIMI_index.txt','w') as f:
        f.write(output_s)
        
    
    print("SPIMI: ", len(inverted_index.keys()))
    end = time.time()
    print("SPIMI time: ", end - start)
    
    
    # processIndex(frame, column, inverted_index)
    
    
def createTDI(frame, column):
    docID = 0
    TDI = []
    for row in frame[column]:
        for word in row:
            TDI.append( (word, docID) )
        docID = docID + 1

    
    BSBI_index(frame,column,TDI)
    SPIMI_index(frame,column, TDI)
    
    



# #IS THIS EVEN NECESSARY?
# def sortColumn(frame, column):
#     sortedColumn = []
    
#     for row in frame[column]:
#         row = sorted(set(row))
#         sortedColumn.append(row)
   
#     frame[column] = sortedColumn
#     # print("sortedColumn")
#     # print(frame)
#     createTDI(frame, column)
    
    
    
    
    

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
    
    # sortColumn(frame, column)
    createTDI(frame,column)
    
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
    
def title_pipeline(frame):
    print("not implemented")
    
    # for row in frame:
    #     tokenize(frame,'title')
    
def steps_pipeline(frame):
    print("not implemented")
    # for row in frame:
    #     tokenize(frame,'title')
    
def pipelineStart(dataframe):
    ingredient_pipeline(dataframe)
    title_pipeline(dataframe)
    steps_pipeline(dataframe)



dataframe = readData("bonappetit_data.csv")
# print(dataframe)
print(dataframe)
ingredients = ingredient_pipeline(dataframe)
# title = title_pipeline('title')



     
