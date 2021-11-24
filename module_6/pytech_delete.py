from pymongo import MongoClient
import certifi
ca = certifi.where()

url = "mongodb+srv://admin:admin@cluster0.wqfvz.mongodb.net/pytech?retryWrites=true&w=majority" 
client = MongoClient(url, tlsCAFile=ca)
db = client.pytech


studentCollection = db['students']
foundStudents = studentCollection.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find () Query --")
for foundStudent in foundStudents:
	print(f"Student ID: {foundStudent['student_id']}")
	print(f"First Name: {foundStudent['first_name']}")
	print(f"Last Name:  {foundStudent['last_name']}")
	print("")
steve = {
	
 	"student_id":"1010",
	"first_name":"Steve",
	"last_name":"Marty",
	}

steve_inserted_id = studentCollection.insert_one(steve).inserted_id
print("--INSERT STATEMENTS--")
print(f"Inserted student record into the students collection with document id {steve_inserted_id}")




print("-- DISPLAYING STUDENT TEST DOC --")
filter = { 'student_id': '1010' } 
#findone method 
print(studentCollection.find_one(filter))

#delete one method 
studentCollection.delete_one(filter)

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find () Query --")
foundStudents = studentCollection.find({})
for foundStudent in foundStudents:
	print(f"Student ID: {foundStudent['student_id']}")
	print(f"First Name: {foundStudent['first_name']}")
	print(f"Last Name:  {foundStudent['last_name']}")
	print("")

 
