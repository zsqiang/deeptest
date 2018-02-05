# coding=utf-8

import logging
import logging

logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')

'''

filename  Specifies that a FileHandler be created, using the specified
              filename, rather than a StreamHandler.
    filemode  Specifies the mode to open the file, if filename is specified
              (if filemode is unspecified, it defaults to 'a').
    format    Use the specified format string for the handler.
    datefmt   Use the specified date/time format.
    style     If a format string is specified, use this to specify the
              type of format string (possible values '%', '{', '$', for
              %-formatting, :meth:`str.format` and :class:`string.Template`
              - defaults to '%').
    level     Set the root logger level to the specified level.
    stream    Use the specified stream to initialize the StreamHandler. Note
              that this argument is incompatible with 'filename' - if both
              are present, 'stream' is ignored.
    handlers  If specified, this should be an iterable of already created
              handlers, which will be added to the root handler. Any handler
              in the list which does not have a formatter assigned will be
              assigned the formatter created in this function.


'''


class LYMLogging:
    LOGGING_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s %(message)s'

    def __init__(self, level=logging.DEBUG,
                 format=LOGGING_FORMAT,
                 datefmt='%a, %d %b %Y %H:%M:%S',
                 filename='LYM.log',
                 filemode='w'):
        self.level = level
        self.datefmt = datefmt
        self.format = format
        self.filename = filename
        self.filemode = filemode
        # 初始化日志同时输出到console和日志文件

        logging.basicConfig(level=logging.DEBUG,
                            format=self.format,
                            datefmt=self.datefmt,
                            filename=self.filename,
                            filemode=self.filemode)



        '''
        
        方案二:
        console = logging.StreamHandler()
        console.setLevel(level)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s%(message)s')
        logging.Formatter(formatter)
        logging.getLogger("appName").addHandler(console)
        self.log = logging.getLogger("LYMLogger")
        '''
        # 日志输出

    def output(self, msg, level=logging.DEBUG):
        if level == logging.DEBUG:
            # 调试信息
            self.log.debug(msg)
        elif level == logging.INFO:
            # 一般的信息
            self.log.info(msg)
        elif level == logging.WARNING:
            # 警告信息
            self.log.warning(msg)
        elif level == logging.ERROR:
            # 错误信息
            self.log.error(msg)
        else:
            # 尼玛
            self.log.critical(msg)

    def set_level(self, level=logging.DEBUG):
        self.log.set_level(level)


if __name__ == '__main__':
    log = LYMLogging(format='%(name)-12s: %(levelname)-8s%(message)s')
    log.output("it's debug msg", level=logging.DEBUG)
    log.output("it's info msg", level=logging.INFO)
    log.output("it's warning msg", level=logging.WARNING)
    log.output("it's error msg", level=logging.ERROR)
    log.output("it's fuck msg", level=logging.CRITICAL)

if __name__ != "__main__":
    print("python logging实例")
    log = LYMLogging()

    log.output("it's debug msg", level=logging.DEBUG)
    log.output("it's info msg", level=logging.INFO)
    log.output("it's warning msg", level=logging.WARNING)
    log.output("it's error msg", level=logging.ERROR)
    log.output("it's fuck msg", level=logging.CRITICAL)
