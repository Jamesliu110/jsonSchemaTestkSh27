# 导包
import jsonschema
# 校验规则
schema = {
    "type": "object",
    "properties": {
        "success": {"type": "boolean"},
        "code": {"type": "integer"},
        "message": {"type": "string"},
        "money": {"type": "number"},
        "address": {"type": "null"},
        "data": {"type": "object"},
        "luckyNumber": {"type": "array"}
    }
}
# 测试数据
json_data = {
    "success": True,
    "code": 10000,
    "message": "操作成功",
    "money": 6.66,
    "address": None,
    "data": {
        "name": "tom"
    },
    "luckyNumber": [6, 8, 9]
}
# 调用方法校验
res = jsonschema.validate(instance=json_data, schema=schema)
# 查看校验结果
print("校验结果：", res)
