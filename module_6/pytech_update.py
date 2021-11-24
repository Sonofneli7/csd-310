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





filter = { 'student_id': '1007' } 
newvaluesToUpdate = { "$set": { 'last_name': 'Stevens' } } 
studentCollection.update_one(filter, newvaluesToUpdate) 

print("-- DISPLAYING STUDENT DOCUMENT 1007 --") 
print(studentCollection.find_one(filter))
