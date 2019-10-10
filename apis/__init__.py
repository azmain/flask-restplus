from flask_restplus import Api

from .student import api as student_api


api = Api(
    title= 'Learn python',
    version = '1.0',
    description= 'Learning Api with Flask & Rest Plus'
)

api.add_namespace(student_api)