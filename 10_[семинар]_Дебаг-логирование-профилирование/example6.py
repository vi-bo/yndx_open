def calculate_rps(requests, seconds):
        breakpoint()
        return requests / seconds

while True:
        print('Requests:', end='')
        request = float(input())
        print('Seconds:', end='')
        seconds = float(input())
        rps = calculate_rps(request, seconds)
        print(f'{rps} requests per seconds')
