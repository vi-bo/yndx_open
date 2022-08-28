import os

def main():
    print(f'PID = {os.getpid()}')
    with open('bar.txt', 'w') as f:
        f.write('Bar')
        print(f'Файловый дескриптор '
                f'{f.fileno()}')
        print(f'Статус файлового дескриптора '
                f'{os.stat(f.fileno())}')
        input()
    
if __name__ == '__main__':
    main()