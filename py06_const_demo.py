# 导包
import jsonschema

# 待测试数据
data = {
    "success": True,
    "name": "李四",
    "height": 1.93,
    "addr": None
}

# 校验规则
schema = {
    "type": "object",
    "properties": {
        "success": {"const": True},
        "name": {"const": "李四"},
        "height": {"const": 1.93},
        "addr": {"const": None}
    }
}

# 调用方法
res = jsonschema.validate(instance=data, schema=schema)

# 查看结果
print(res)
