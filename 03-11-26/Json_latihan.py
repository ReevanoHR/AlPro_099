import json

FILE_NAME = 'FILE/history_city_list.json'

with open(FILE_NAME, 'r', encoding='Latin1') as jsonfile: #untuk encoding bisa menggunakan utf-8 atau latin1 maupun coba-coba encoding lain jika error
    data = json.load(jsonfile)

print(type(data))
#print(data[0])
print(len(data))

#print data sesuai indeks
#print(json.dumps(data[764], indent=4)) #atau dengan cara
#print(data[764])#lebih rapih menggunakan cara di atas

#cara menampilkan data sesuai key
print(json.dumps(data[764]['city']['coord']['lon'], indent=4))