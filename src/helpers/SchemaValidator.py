from jsonschema import validate
from jsonschema.exceptions import ValidationError


def schema_validator(response, schema):
    try:
        validate(instance=response, schema=schema)
        return True
    except ValidationError:
        return False
