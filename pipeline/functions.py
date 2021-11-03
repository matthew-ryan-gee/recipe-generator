"""
Write your reusable code here.
Main method stubs corresponding to each block is initialized here. Do not modify the signature of the functions already
created for you. But if necessary you can implement any number of additional functions that you might think useful to you
within this script.

Delete "Delete this block first" code stub after writing solutions to each function.

Write you code within the "WRITE YOUR CODE HERE vvvvvvvvvvvvvvvv" code stub. Variable created within this stub are just
for example to show what is expected to be returned. You CAN modify them according to your preference.
"""
            #######################
            # Matthew Gee         #
            # c479 - assignment 1 #
            #######################

# def readData():
#     dataframe = pd.read_csv('bonappetit_data.csv')
#     print(dataframe.to_string())
#     # createTDImatrix(dataframe['ingredients'])
    
# def createTDImatrix(column):
#     count = 0
#     for row in column:
#             for tupl in list(literal_eval(row)):
#                 print(tupl)
            
#             print(count)
#             count +=1
#     print("create Term Document Index")
    
# def queryMachine():
#      print("Query Machine")

def block_reader(path):

    import os
    import pandas as pd
    files_content = []
    
    #This block opens the pipeline's data directory and finds all files that end with .csv
    #It then reads each file and appends the content to a separate entry in a list
    
    for file in os.listdir(path):
        if file.endswith(".csv"):
            # filename = os.path.join("reuters21578", file)
            f = pd.read_csv(file)
            files_content.append(f)
        
    #Each item of the list contains the entire content of a single sgm file
    for item in files_content:
          yield(item)


def block_document_segmenter(INPUT_STRUCTURE):

    # doc_list = []
    # document = ""
    
    # #These two loops concatenate all sgm content into a single item
    # for file in INPUT_STRUCTURE:
    #     doc_list.append(file) #so i can ignore this structure garbage 
    # for item in doc_list:
    #     document+=item
    
    # #This removes the 22 instances of <!Doctype... from the text collection
    # document = document.replace("<!DOCTYPE lewis SYSTEM \"lewis.dtd\">", "")

    # #The String containing the sgm files is then split by </REUTERS> so that each
    # #entry of the list corresponds with one news article
    # document = document.split("</REUTERS>")
    # document = document[0:-1] #This removes some junk from the end of the file
    # for item in document:
    #     item+="</REUTERS>" #This appends </REUTERS> back onto each article for the asserts
    #     yield(item)
    
    # for line in INPUT_STRUCTURE:
    #     yield(line)
    yield(INPUT_STRUCTURE)
    

def block_extractor(INPUT_STRUCTURE):
    # import pandas as pd
    # # dataframe = pd.read_csv(INPUT_STRUCTURE)
    # content_dict = []
    # ID = 1
    
    # #This loop finds the index of <BODY> and </BODY> for each article and
    # #then takes splices the content from between those indices and stores it in
    # #a dictionary
    # for f in INPUT_STRUCTURE:
    #     start = f.find("<BODY>")+6
    #     end = f.find("</BODY>")
    #     TEXT = f[start:end]
    #     entry = {
    #         "ID": ID,
    #         "TEXT": TEXT
    #         }
    #     content_dict.append(entry)
    #     ID +=1
    


    # for item in content_dict:
    #     yield(item)
    
    # yield(INPUT_STRUCTURE)
        
    for item in INPUT_STRUCTURE:
         yield(item)     
    


def block_tokenizer(INPUT_STRUCTURE):
    # from nltk.tokenize import word_tokenize
    
    # #This loop iterates through each mass of text of the dictionary and then
    # #creates ID/word tuples for every word found in the text
    # for item in INPUT_STRUCTURE:
    #     id = item['ID']
    #     text = item['TEXT']
    #     text = word_tokenize(text)
    #     for word in text:
    #         word_tuple = (id, word)
    #         yield word_tuple
    
    # for line in INPUT_STRUCTURE:
    #     id = item['ID']
    #     text = item['TEXT']
    #     text = word_tokenize(text)
    #     for word in text:
    #         word_tuple = (id, word)
    #         yield word_tuple



def block_stemmer(INPUT_STRUCTURE):
    from nltk.stem import PorterStemmer
    ps = PorterStemmer()
    
    #This loop applies NLTK's porter stemmer to each word of each dictionary
    for item in INPUT_STRUCTURE:
        id = item[0]
        word = ps.stem(item[1])
        word_tuple = (id, word)
        yield word_tuple


def block_stopwords_removal(INPUT_STRUCTURE, stopwords):

    #This loop vefifies whether the user gave a stopwords file. If stopwords=None,
    #then the file imports NLTK's stopword file and then use it in the final step.
    #As block-6-stopwords-removal opens and reads the path location, if a path is given
    #by the user, the contents of stopwords needs only be assigned to stop_words to proceed
    if stopwords is None:
        from nltk.corpus import stopwords
        stop_words = set(stopwords.words('english'))
    else:
        stop_words = stopwords

        
    #this loop scans each touple for stop words and removes the item if it is in fact a stopword
    for item in INPUT_STRUCTURE:
        id = item[0]
        word = item[1]
        if word not in stop_words:
            word_tuple = (id, word)
            yield(word_tuple)
            


#             #######################
#             # Matthew Gee         #
#             # c479 - assignment 1 #
#             #######################


# def block_reader(path):

#     import os
#     import panda as pd
#     files_content = []
    
#     #This block opens the reuters directory and finds all files that end with .sgm
#     #It then reads each file and appends the content to a separate entry in a list
    
#     for file in os.listdir(path):
#         if file.endswith(".csv"):
#             # filename = os.path.join("reuters21578", file)
#             f = pd.read_csv(file)
#             files_content.append(f)
            
#     #Each item of the list contains the entire content of a single sgm file
#     for item in files_content:
#           yield(item)


# def block_document_segmenter(INPUT_STRUCTURE):

#     doc_list = []
#     document = ""
    
#     #These two loops concatenate all sgm content into a single item
#     for file in INPUT_STRUCTURE:
#         doc_list.append(file) #so i can ignore this structure garbage 
#     for item in doc_list:
#         document+=item
    
#     #This removes the 22 instances of <!Doctype... from the text collection
#     document = document.replace("<!DOCTYPE lewis SYSTEM \"lewis.dtd\">", "")

#     #The String containing the sgm files is then split by </REUTERS> so that each
#     #entry of the list corresponds with one news article
#     document = document.split("</REUTERS>")
#     document = document[0:-1] #This removes some junk from the end of the file
#     for item in document:
#         item+="</REUTERS>" #This appends </REUTERS> back onto each article for the asserts
#         yield(item)
    
    

# def block_extractor(INPUT_STRUCTURE):
#     content_dict = []
#     ID = 1
    
#     #This loop finds the index of <BODY> and </BODY> for each article and
#     #then takes splices the content from between those indices and stores it in
#     #a dictionary
#     for f in INPUT_STRUCTURE:
#         start = f.find("<BODY>")+6
#         end = f.find("</BODY>")
#         TEXT = f[start:end]
#         entry = {
#             "ID": ID,
#             "TEXT": TEXT
#             }
#         content_dict.append(entry)
#         ID +=1
    


#     for item in content_dict:
#         yield(item)


# def block_tokenizer(INPUT_STRUCTURE):
#     from nltk.tokenize import word_tokenize
    
#     #This loop iterates through each mass of text of the dictionary and then
#     #creates ID/word tuples for every word found in the text
#     for item in INPUT_STRUCTURE:
#         id = item['ID']
#         text = item['TEXT']
#         text = word_tokenize(text)
#         for word in text:
#             word_tuple = (id, word)
#             yield word_tuple


# def block_stemmer(INPUT_STRUCTURE):
#     from nltk.stem import PorterStemmer
#     ps = PorterStemmer()
    
#     #This loop applies NLTK's porter stemmer to each word of each dictionary
#     for item in INPUT_STRUCTURE:
#         id = item[0]
#         word = ps.stem(item[1])
#         word_tuple = (id, word)
#         yield word_tuple


# def block_stopwords_removal(INPUT_STRUCTURE, stopwords):

#     #This loop vefifies whether the user gave a stopwords file. If stopwords=None,
#     #then the file imports NLTK's stopword file and then use it in the final step.
#     #As block-6-stopwords-removal opens and reads the path location, if a path is given
#     #by the user, the contents of stopwords needs only be assigned to stop_words to proceed
#     if stopwords is None:
#         from nltk.corpus import stopwords
#         stop_words = set(stopwords.words('english'))
#     else:
#         stop_words = stopwords

        
#     #this loop scans each touple for stop words and removes the item if it is in fact a stopword
#     for item in INPUT_STRUCTURE:
#         id = item[0]
#         word = item[1]
#         if word not in stop_words:
#             word_tuple = (id, word)
#             yield(word_tuple)
            
