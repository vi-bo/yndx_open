import signal
import time

def on_signt(signo, stack_frame):
    print(f'Поймал сигнал {signo}')

signal.signal(signal.SIGINT, on_signt)

while True:
    time.sleep(1)