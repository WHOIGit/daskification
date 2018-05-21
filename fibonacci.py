
from distributed import Client

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    client = Client()

    x = [6, 7, 8, 9]
    futures = client.map(fib, x)
    y = client.gather(futures)
