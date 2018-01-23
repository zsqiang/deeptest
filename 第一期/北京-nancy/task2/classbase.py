# -* coding:utf-8 *-
__author__ = 'nancy'

class demo:

    def __init__(self):
        print("init")

    def output(self, test):
        print(test)

    def output_none(self):
        print("no para")

class childdemo(demo):
    def __init__(self):
        print("child init")

    def output_none(self):
        print("child no para")

if __name__ == "__main__":
    demo_obj = demo()
    demo_obj.output("para")
    demo_obj.output_none()

    childdemo_obj = childdemo()
    childdemo_obj.output("child obj")
    childdemo_obj.output_none()