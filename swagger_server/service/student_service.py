import os
import os
import time
from pymongo import MongoClient
from bson.objectid import ObjectId

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")

#Logic for Github action correct testing

client = None
for _ in range(10):
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
        client.server_info()
        break
    except Exception:
        time.sleep(2)

if client is None:
    raise Exception("MongoDB not available")

db = client.student_db


def add(student=None):
    # Check for duplicates
    if db.students.find_one({"first_name": student.first_name, "last_name": student.last_name}):
        return 'already exists', 409

    student_dict = student.to_dict()
    result = db.students.insert_one(student_dict)

    return str(result.inserted_id), 200


def get_by_id(student_id=None, subject=None):
    try:
        oid = ObjectId(student_id)
    except:
        return 'invalid id format', 400

    student = db.students.find_one({"_id": oid})
    if not student:
        return 'not found', 404

    # Format response for JSON serialization
    student['student_id'] = str(student['_id'])
    del student['_id']

    return student


def delete(student_id=None):
    try:
        oid = ObjectId(student_id)
    except:
        return 'invalid id format', 400

    result = db.students.delete_one({"_id": oid})
    if result.deleted_count == 0:
        return 'not found', 404

    return student_id