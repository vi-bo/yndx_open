import os

def main():
    print(f'{os.getpid()}: Давайте создадим процесс')

    res = os.fork()

    if res !=0:
        print(f'{os.getpid()}: Новый процесс с pid={res} создан')
    else:
        print(f'{os.getpid()}: Я дочерний процесс')
        print(f'{os.getpid()}: pid родительского процесса (ppid) = '
                f'{os.getppid()}')
    
    input()

if __name__ == '__main__':
    main()