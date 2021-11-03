import re
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import csv
import pandas as pd
from nltk import PorterStemmer
from ast import literal_eval

def read_Dom(input_dom, percentage):
    urls = []
    file = open(input_dom, encoding='utf-8')
    lines = file.readlines()
    
    count = 0
    limit = 10
    for line in lines:
        if count <= limit:
            break
        if line.startswith("<url>"):
            if "bonappetit.com/recipe/" in line:
                if "recipe/recipe" not in line:
                    start = line.index("<loc>") + len("<loc>")
                    end = line.index("</loc>")
                    newLine = line[start:end]
                    titleStart = len("https://www.bonappetit.com/recipe/")
                    if re.match("[a-zA-Z0-9-]*$", newLine[titleStart:]):
                        # urls.append(newLine[titleStart:])
                        urls.append(newLine)
                        count =+ 1
    end = (len(urls))*(percentage/100)
    urls = urls[:end]
    urls.sort()
    extract_Data(urls)
             
def extract_Data(urls):
    output = open('bonappetit_data2.csv', 'w+', encoding='utf-8-sig', newline='')
    writer = csv.writer(output, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['title','url', 'author', 'servings', 'ingredients','steps'])
    
    for url in urls:
        try:
            recipe_page = url
            page = urlopen(recipe_page)
            soup = bs(page, 'html.parser')    
            name_box = soup.find('h1')
            if (name_box != None):
                title = name_box.text.strip()   
            # print(title)
            # print(url)
            
            author_box = soup.find('span', {'itemprop': 'name'})
            if (author_box != None):
                author = author_box.text.strip()
            
            # print(author)
            
            
            ingredients = []
            ingredient_box = soup.find('div',  {'data-testid': 'IngredientList'})
            if(ingredient_box != None):
                if (ingredient_box.p != None):
                    servings = ingredient_box.p.text
                amount = []
                item = []
                
                last_tag = 'div'
                
                ingredient_box = ingredient_box.find('div')
                if ingredient_box != None:
                    ingredient_box = ingredient_box.find_all()
                    if ingredient_box != None:
                        for tag in ingredient_box:
                            if tag.name == last_tag:
                                amount.append("Sub Recipe:")
                            if tag.name == 'div':
                                item.append(tag.text)
                                last_tag = 'div'
                            if tag.name == 'p':
                                amount.append(tag.text)
                                last_tag = 'p'
                
                ingredients = zip (amount, item)
                # print("SERVINGS: ", servings)
                ingredients = [l for l in ingredients]
            
        
            
            steps = []
            preparation_box = soup.find('div',  {'data-testid': 'InstructionsWrapper'})
            if(preparation_box != None):
                preparation_box = preparation_box.find_all('p')
                if preparation_box != None:
                    for p in preparation_box:
                        steps.append(p.text)
            # print(steps)
        
            
            writer.writerow([title, url, author, servings, list(ingredients), steps])
        except:
            continue
    output.close()
    
def readData():
    dataframe = pd.read_csv('bonappetit_data.csv')
    print(dataframe.to_string())
    # createTDImatrix(dataframe['ingredients'])
    
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
 