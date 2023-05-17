import pandas as pd

df = pd.read_excel('position.xlsx')
df.to_csv('position.csv', encoding='utf-8')
import csv
with open('honjab.csv', 'r') as f:
    with open('honjab_real.csv', 'w', encoding='utf-8') as w:
        a= f.readlines()
        for item in a:
            w.write(','.join(item.replace('\"', '').split(',')))