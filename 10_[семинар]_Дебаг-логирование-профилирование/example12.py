import os, logging, json

class JSONFormatter(logging.Formatter):
        def format(self, record):
                return json.dumps(
                        {
                                'args': record.args,
                                'file': record.filename,
                                'func': record.funcName,
                                'line': record.lineno,
                                'message': record.getMessage(),
                        },
                        ensure_ascii=False
                )