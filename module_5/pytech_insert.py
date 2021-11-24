from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.wqfvz.mongodb.net/pytech?retryWrites=true&w=majority" 
client = MongoClient(url)
db = client.pytech

students = db.getcollection("students")

fred = {
	"student_id":"1007"
	"first_name":"Fred"
	"last_name":"Smith"
	}

	nelson = {
	"student_id":"1008"
	"first_name":"Nelson"
	"last_name":"Morales"
	}

	Danie = {
	"student_id":"1009"
	"first_name":"Danie"
	"last_name":"Carr"
	}

print("--INSERT STATEMENTS--")

fred_inserted_id = students.insert_one(fred).inserted_id
print(f"Inserted student record {fred"['first_name']}{fred"['last_name']} into the students collection with document id {fred_inserted}")

nelson_inserted_id = students.insert_one(nelson).inserted_id
print(f"Inserted student record {nelson"['first_name']}{nelson"['last_name']} into the students collection with document id {nelson_inserted}")

danie_inserted_id = students.insert_one(danie).inserted_id
print(f"Inserted student record {danie"['first_name']}{danie"['last_name']} into the students collection with document id {nelson_inserted}")
