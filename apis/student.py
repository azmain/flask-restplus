from flask_restplus import Namespace, Resource, fields
from flask_pymongo import PyMongo
from bson.json_util import dumps
import json
from bson import json_util

from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.nishan

api = Namespace('students', description="Student Details")

student = api.model(
    'Student',
    {
        'roll': fields.String(required=True, description="The student identifier."),
        'name': fields.String(required=True, description="The student name.")
    }
)

STUDENTS = [
    {'roll': '111', 'name': 'Felix'},
]


@api.route('/')
class studentList(Resource):

    @api.doc('student_list')
    @api.marshal_list_with(student)
    def get(self):
        '''List all students'''
        studentList = list(db.student.find_one())
        print(studentList)
        print(json.dumps(studentList))
        return json.dumps(studentList)

