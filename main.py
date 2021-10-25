import re
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import csv



# remove lines not containing '/bonappetit.com/recipe/'
# remove lines containing /recipe/recipe


### Reads file and cleans data ###
file = open("site.txt", encoding='utf-8')
lines = file.readlines()

urls = []
count = 0
limit = 10
for line in lines:
    if count < limit:
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
                        count += 1
urls.sort()

# output = open('bonappetit_data.csv', 'w+', encoding='utf-8', newline='')
# writer = csv.writer(output, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
# writer.writerow(['title','url', 'author', 'servings', 'ingredients','instructions'])
for url in urls:
    recipe_page = url
    page = urlopen(recipe_page)
    soup = bs(page, 'html.parser')    
    name_box = soup.find('h1')
    title = name_box.text.strip()
    print(title)
    # print(url)
    
    author_box = soup.find('span', {'itemprop': 'name'})
    author = author_box.text.strip()
    # print(author)
    
    
    
    
    
    
    ingredients = []
    ingredient_box = soup.find('div',  {'data-testid': 'IngredientList'})
    servings = ingredient_box.p.text
    amount = []
    item = []
    p_tags = ingredient_box.div.find_all('p')
    for p in p_tags:
        amount.append(p.text)
        print(p.text)
    div_tags = ingredient_box.div.find_all('div')
    for div in div_tags:
        item.append(div.text)
        print(div.text)
    ingredients = zip (amount, item)
    print("SERVINGS: ", servings)
    print(ingredients, "\n")
    
    # ingredient_box = soup.find('div',  {'data-testid': 'IngredientList'})
    # ingredients = ingredient_box.text
    # ingredients = ingredients[11:]
    # servings = ""
    # if "servings" in ingredients[:15].lower():
    #     s_index = ingredients.lower().index("servings") + 8
    #     servings = ingredients[:s_index]
    #     ingredients = ingredients[s_index:]
    # print("servings ", servings)
    # print(ingredients, "\n")
    
    preparation_box = soup.find('div',  {'data-testid': 'InstructionsWrapper'})
    preparation = preparation_box.text
    # print(preparation,  "\n")
    
    # writer.writerow([title, url, author, servings, ingredients, preparation])
    
# output.close()
 