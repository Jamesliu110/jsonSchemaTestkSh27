# 导包
import jsonschema

# 待测数据
json_data = {
    "success": True,
    "code": 10000,
    "message": "操作成功",
    "money": 6.66,
    "address": None,
    "data": {
        "name": "tom",
        "age": "18",
        "height": 1.81
    },
    "luckyNumber": [6, 8, 9]
}

# 校验规则
schema = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "code": {"type": "integer"},
        "message": {"type": "string"},
        "money": {"type": "number"},
        "address": {"type": "null"},
        "data": {
            "type": "object",
            "required": ["name", "age", "height"]
        },
        "luckyNumber": {"type": "array"},
    },
    "required": ["success", "code", "message", "money", "address", "data", "luckyNumber"]
}

# 调用方法
res = jsonschema.validate(instance=json_data, schema=schema)

# 查看结果
print("校验结果：", res)
