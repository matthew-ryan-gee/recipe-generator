from functions import read_Dom, readData, queryMachine

#main
print("Hello. This program scrapes the BonAppetit website for recipes and",
      "allows the user to query and apply statistics to the data.")

hasData = input("Do you already have the data in a csv format? Y/N: ")

if hasData.lower() == "n":
    print("Scraping the whole website takes forever TBH - there are 15000 recipes.")
    percent = input("Please enter a number between 0 and 100 to determine what percentage of the data you wish to scrape. ")
    dom = "site.txt"
    read_Dom(dom, percent)
    
readData()

queryMachine()


