import requests
import csv 
import pandas as pd
import numpy as np

df = pd.read_csv('movies_data.csv')

titles = df['title'].tolist()
test = titles[0:5001]

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0) Gecko/20100101 Firefox/39.0"}
base = "http://www.omdbapi.com/?apikey=PlsBanMe&t="

with open(r"box_office_data.csv", "a") as csv_file:
    writer = csv.writer(csv_file, delimiter =",", quoting=csv.QUOTE_MINIMAL)

    for i in range(len(test)):
        if test[i][-3:] == 'The' or test[i][-3:] == "Die" or test[i][-3:] == "Das" or test[i][-3:] == "Der":
            title = test[i][:-5]
        elif test[i][-2:] == "L'":
            title = test[i][:-4]
        else:
            title = test[i]
        
        print(title)

        url = base + title
        res = requests.get(url, headers = header).json()

        if res["Response"] == "True" and "BoxOffice" in res.keys():
            revenue = res["BoxOffice"]
            print(revenue)
            writer.writerow([test[i],revenue])

        elif res["Response"] == "True" and "BoxOffice" not in res.keys():
            writer.writerow([test[i],"NA"])

        elif res["Response"] == "False":
            writer.writerow([test[i],"NA"])
       


