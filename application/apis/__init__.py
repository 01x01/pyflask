from flask_restx import Api
from .index import ns as index_ns

api = Api(
    doc="/doc",
    title='index api',
    version='1.0',
    description='A description'
)

api.add_namespace(index_ns)