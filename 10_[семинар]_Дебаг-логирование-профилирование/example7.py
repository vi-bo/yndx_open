from ctypes import string_at

class Foo:
        def bar(self):
                string_at(0xDEADBEEF) # Здесь будет Seqfault

if __name__ == '__main__':
        f = Foo()
        f.spam = 42
        f.bar()