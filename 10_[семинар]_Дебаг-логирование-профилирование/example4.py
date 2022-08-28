import base64

def main():
        with open('/dev/urandom', 'rb') as urand:
                rand_bytes = urand.read(128)
        with open('/tmp/mypass.txt', 'wb') as mypass:
                mypass.write(base64.a85encode(rand_bytes))
        
if __name__ == '__main__':
        main()