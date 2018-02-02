# coding=utf-8
# dict字典转换json串示例

import json

if __name__ == "__main__":
    print("字典转json串:")

    json_dict = {"用户名": "susanhonlly", "兴趣": "阅读", "民族": "汉"}
    print("原类型:", type(json_dict))

    # 将字典转换成json串
    # 会被转换成字符串类型
    json_str = json.dumps(json_dict)
    print("转换后的类型:", type(json_str))
    print(json_str)