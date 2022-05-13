import requests
from bs4 import BeautifulSoup

# resp = requests.get("https://www.wp.pl/")
# soup = BeautifulSoup(resp.text, 'html.parser')
# # print(soup.prettify())
# print(soup.a)
# for link in soup.find_all('a'):
#     print(link.get('href'), link)
#
# # print(soup.get_text())

import csv

# with open('q.csv') as f:
#     for n, line in enumerate(f):
#         if n:  # nie drukuj naglowka
#             print(line.rstrip().split(';'))

csv.register_dialect('warsztatowy', delimiter=';')
# with open('q.csv') as f:
#     reader = csv.reader(f, 'warsztatowy')
#     for row in reader:
#         print(row)

csv.register_dialect('warsztatowy2', delimiter=',')
with open('b.csv') as f:
    reader = csv.reader(f, 'warsztatowy2')
    for row in reader:
        print(row)

import pandas as pd
df = pd.read_csv("q.csv", sep=';', decimal=",", parse_dates=['_date'])