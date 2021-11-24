from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.wqfvz.mongodb.net/pytech?retryWrites=true&w=majority" 
client = MongoClient(url)
db = client.pytech

students = db.getcollection("students")

found students = sutdent.find({})

print("--Displaying student documents from find () Query--")
for found student in foundstudents:
	print(f"Student ID: {foundstudent ['student_id']}")
	print(f"First Name: {foundstudent ['first_name']}")
	print(f"Last Name:  {foundstudent ['last_name']}")
	print("")

foundonestudent = students.find_one({"student_id":"1007"})

print("--Displaying student documents from find () Query--"
	print(f"Student ID: {foundstudent ['student_id']}")
	print(f"First Name: {foundstudent ['first_name']}")
	print(f"Last Name:  {foundstudent ['last_name']}")

