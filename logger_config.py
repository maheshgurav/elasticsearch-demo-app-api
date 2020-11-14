import logging

from jsonformatter import JsonFormatter

# `format` can be `json`, `OrderedDict`, `dict`.
# If `format` is `dict` and python version < 3.7.0, the output order is sorted keys, otherwise will same as defined order.
# key: string, can be whatever you like.
# value: `LogRecord` attribute name.
STRING_FORMAT = '''{
    "Name":            "name",
    "Levelno":         "levelno",
    "Levelname":       "levelname",
    "Pathname":        "pathname",
    "Filename":        "filename",
    "Module":          "module",
    "Lineno":          "lineno",
    "FuncName":        "funcName",
    "Created":         "created",
    "Asctime":         "asctime",
    "Msecs":           "msecs",
    "RelativeCreated": "relativeCreated",
    "Thread":          "thread",
    "ThreadName":      "threadName",
    "Process":         "process",
    "Message":         "message"
}'''

def get_logger(name):
    root_logger = logging.getLogger(name)
    root_logger.setLevel(logging.DEBUG)

    formatter = JsonFormatter(STRING_FORMAT)

    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    sh.setLevel(logging.DEBUG)

    root_logger.addHandler(sh)
    return root_logger
