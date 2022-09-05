import time

def new_get_text(delay, text):
    time.sleep(delay)
    return text

def new_say_text():
    task1 = new_get_text(5, 'hello')
    task2 = new_get_text(5, 'world')
    return ', '.join([task1, task2])

result = new_say_text()
print(result) # hello, world