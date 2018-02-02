# coding=utf-8
# json串转dict示例

import json

if __name__ == "__main__":
    print("json转dict")

    json_str = '{"用户名": "susanhonly", "兴趣": "阅读", "民族": "汉"}'

    # 原类型
    print("原类型:", type(json_str))

    # 转成dict对象
    # 会被转换成字典类型
    json_dict = json.loads(json_str)
    print("转换后的类型:", type(json_dict))

    # 遍历字典
    for k, v in json_dict.items():
        print(k, ":", v)