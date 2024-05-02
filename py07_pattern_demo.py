# 导包
import jsonschema

# 测试数据
data = {
    "message": "操作成功!",
    "mobile": "11800000002"
}

# 校验规则
schema = {
    "type": "object",
    "properties": {
        "message": {"pattern": "^操作成功"},
        "mobile": {"pattern": "^[0-9]{11}$"}
    }
}

# 调用方法
res = jsonschema.validate(instance=data, schema=schema)

# 查看结果
print(res)
