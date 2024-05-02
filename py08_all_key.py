"""
综合案例
"""
import jsonschema

data = {
    "success": False,
    "code": 10000,
    "message": "xxx登录成功",
    "data": {
        "age": 20,
        "name": "lily"
    }
}

schema = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "code": {"type": "integer"},
        "message": {"pattern": "登录成功$"},
        "data": {
            "type": "object",
            "properties": {
                "name": {"const": "lily"},
                "age": {"const": 20}
            },
            "required": ["name", "age"]
        }
    },
    "required": ["success", "code", "message", "data"]
}
jsonschema.validate(instance=data, schema=schema)