# coding=utf-8
import codecs
import csv

#
# with codecs.open('books.csv', 'w', 'utf-8') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(["书名", "作者", "描述", "出版社", "价格"])
#     # 写书信息
#
#     spamwriter.writerow(["title",
#                          ",".join("['john','haven']"),
#                          "summary",
#                          "publisher",
#                          "price"])

'''
 delimiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    doublequote = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    escapechar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lineterminator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quotechar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quoting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skipinitialspace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    strict = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

'''
print(help(csv))
with codecs.open("books.csv", "w", "utf-8") as  csvfile:
    spamwriter=csv.writer(csvfile, dialect='excel',delimiter=",",escapechar=None,
                          doublequote=True,skipinitialspace=False,quoting=csv.QUOTE_MINIMAL
                          ,quotechar="|")
    spamwriter =csv.writer(csvfile)
    spamwriter.writerow(["dialect","delimiter","escapechar","doublequote","skipinitialspace"])

  # spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["1","2","3","4","5"])




