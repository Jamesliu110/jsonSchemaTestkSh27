# 导包
import jsonschema

# 校验规则 (json语法)
schema = {
    "type": "object"
}

# 数据
# json_data = 100
# json_data = 100.2
# json_data = "hello"
# json_data = [1, 2, 3, 4]
# json_data = None
# json_data = True
json_data = {"a": 1, "b": 2}

# 调用方法
res = jsonschema.validate(instance=json_data, schema=schema)

# 查看结果
print("校验结果：", res)
