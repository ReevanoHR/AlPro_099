import csv
#Membaca file CSV dengan menggunakan nested list
FILE_NAME = 'FILE/nilaiKuliah.csv'
listNilai = []
with open(FILE_NAME, 'r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    line_count = 0
    
    for baris in readCSV:
        if line_count == 0:
            print(f'Nama Kolom : {baris}')
            line_count += 1
        else:
            print(baris)
            listNilai.append(baris)
            line_count += 1
            
    print(f'Total {line_count} baris')
    
csvfile.close()
print ("isi nested list yang dibuat: ")
print (listNilai)

#Menulis file CSV dengan menggunakan nested list
FILE_NAME = 'FILE/nilaiKuliah.csv'
with open(FILE_NAME, 'w', newline='') as csvfile:
    writeCSV = csv.writer(csvfile, delimiter=',')
    writeCSV.writerow(['Nama', 'NIM', 'Nilai'])
    
    for baris in listNilai:
        writeCSV.writerow(baris)
        
csvfile.close()