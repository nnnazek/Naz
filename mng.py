import pymongo #GET STARTED

import ssl

client = pymongo.MongoClient("mongodb+srv://Nazerke:pp2password@cluster0-lr7ml.mongodb.net/test?retryWrites=true&w=majority")

mydb = client['mydatabase']

print(client.list_database_names()) #CREATE DATABASE

mydb = client['mydatabase']

mycol = mydb["students"]

mydict = {"name":"Nazerke","surname":"Zhansugirova","id":"19BD"}

x = mycol.insert_one(mydict) #INSERT
#ObjectId('5ea4981538b276059289e468')
x.inserted_id

mydb.list_collection_names() #CREATE COLLECTION
#['students']

#example insert
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
mycol.insert_many(mylist)
#<pymongo.results.InsertManyResult object at 0x0000020906769148>

#FIND
x = mycol.find_one() #find_one возвращает первое значение этой базы
x
#{'_id': ObjectId('5ea4981538b276059289e468'), 'name': 'Nazerke', 'surname': 'Zhansugirova', 'id': '19BD'}
students = mycol.find()
students
#<pymongo.cursor.Cursor object at 0x0000020905D7E988>
for x in students:
    print(x)

#возвращает все данные с базы, можно пробегаться по (x['name'])
students = mycol.find({}, {"_id": 0, "name": 1, "address": 1})
for x in students:
    x #выходит все значения без айдишки
    #нельзя имя 0, адрес 1

#QUERY
query = {"name": "Nazerke"} 
students = mycol.find(query)
for x in students:
    x
#выводит соответствующее значение 

query = {"address": {"$gt": 'S'}}
query
students = mycol.find(query)
for x in students:
    print(x)
#выводит все адреса которые больше чем S

query = {"address": {"$regex": "^S"}}
query
students = mycol.find(query)
for x in students:
    x
#выводит все адреса которые начинаются с буквы S

#SORT
students = mycol.find().sort("name")
for x in students:
    x
#отсортировать студентов по имени(по алфавитном порядке)
#если наоборот то ...sort("name",-1)

#DELETE
myquery = {"address": "Mountain 21"}
mycol.delete_one(myquery)
for x in mycol.find():
    x
#удаляет указанное значение
#delete_many({}) удаляет все документы с collection

#DROP COLLECTION
#полностью удаляет collection students

#UPDATE
myquery = {"address": "Valley 345"}
newvalues = {"$set":{"address": "Canyon 123"}}
mycol.update_one(myquery, newvalues)
for x in students:
    x
#заменяет старые данные с новыми данными
#update_one обновляет только первую запись
#update_many может обновлять множество записов

#LIMIT
for x in mycol.find().limit(3)
    x
#выводит первые три записи




