# coding = utf-8
# 使用函数strftime格式化日期时间示例

import time

if __name__ == "__main__":
    # 先看下当前默认格式化的时间
    localtime = time.asctime(time.localtime())
    print("当前默认日期时间格式: %s" % localtime)

    # 格式化为:年-月-日 时:分:秒 星期几
    print("24小时制全格式:", time.strftime("%Y-%m-%d %H:%M:%S %A", time.localtime()))
    print("12小时制缩写格式:", time.strftime("%y-%m-%d %I:%M:%S %a", time.localtime()))

    # 带a.m或p.m标识时间格式
    print("带a.m或p.m 24小时制全格式:", time.strftime("%Y-%m-%d %H:%M:%S %p %A", time.localtime()))

    # 带时区显示
    print("带时区显示:", time.strftime("%Y-%m-%d %H:%M:%S %p %A %z", time.localtime()))

    # 格式乱排下试试
    print("随意排格式：", time.strftime("%A %Y-%d-%m %p %H:%M:%S %z", time.localtime()))