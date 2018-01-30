# -* coding:utf-8 *-
__author__ = 'nancy'

import configparser

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.add_section("addsection")
    config.set("addsection", "option1", "value1")
    config.set("addsection", "option2", "value2")

    config.add_section("addsection2")

    with open('readini.ini', 'w') as f:
        config.write(f)

    config.read('readini.ini')
    sections = config.sections()
    print(sections)

    for opt in sections:
        options = config.options(opt)
        print(options)

    for opt in sections:
        for val in config.options(opt):
            print("[%s] %s = %s" % (opt, val, config.get(opt, val)))