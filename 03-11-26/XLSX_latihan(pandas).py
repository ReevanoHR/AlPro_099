import pandas as pd

FILECSV = 'FILE/nilaiKuliah.csv'

dfCSV = pd.read_csv(FILECSV, delimiter=',', encoding='Latin1')
dfCSV.to_csv('FILE/nilaiKuliah.csv', index=False, sep=',', encoding='Latin1') #index=False untuk menghilangkan index pada file csv
print(dfCSV) 

# (dfCSV.head()) = 5 data pertama
# (dfCSV.sample()) = data secara acak
# (dfCSV.tail()) = 5 data terbawah
# (dfCSV.describe()) = Menjelaskan rerata etc.

#untuk menulis file exel

dfXLSX = pd.read_excel('FILE/Nilai_KelasA.xlsx', sheet_name='Sheet1')
print(dfXLSX)