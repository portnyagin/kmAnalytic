from json import JSONEncoder


from marshmallow import Schema, fields

from dataclasses_json import dataclass_json
from dataclasses import dataclass

@dataclass_json
@dataclass
class Client:
    id: int
    client_type: str
    is_ip: int


client_schema = Client.schema()
client_schemas = Client.schema(many=True)