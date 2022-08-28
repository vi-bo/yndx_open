import logging

class NoPingFilter(logging.Filter):

        def filter(self, record) -> bool:
                return '/api/v1/ping' not in record.getMessage()
