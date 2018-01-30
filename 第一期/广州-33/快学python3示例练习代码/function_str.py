# coding=utf-8
# 函数参数传递示例之，字符串传递，定义函数将字符串联合起来


def str_join(str1, str2, str3):
    return str1 + str2 + str3


if __name__ == "__main__":
    str1 = "今天"
    str2 = "是"
    str3 = "星期日"
    str4 = str_join(str1, str2, str3)
    print(str4)