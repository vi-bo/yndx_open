import logging

root_log = logging.getLogger()
print(root_log.name)
foo_log = logging.getLogger('foo')
print(foo_log.name)
foo_bar_log = logging.getLogger('foo.bar')
print(foo_bar_log.name)
