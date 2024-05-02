"""
入门案例
"""
# 1. 导包
import jsonschema

# 2. 创建 校验规则
schema = {
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "code": {
            "type": "number"
        },
        "message": {
            "type": "string"
        }
    },
    "required": ["success", "code", "message"]
}

# 3. 准备 待校验数据（用 python语法，表示的 json数据）
json_data = {
    "success": True,
    "code": 100.3,
    "message": "操作成功"
}

# 4. 调用方法 进行校验
res = jsonschema.validate(instance=json_data, schema=schema)

# 5. 查看校验结果
print("校验结果：", res)
