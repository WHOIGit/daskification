# to simulate task load, time.sleep is used
import time

#functions for testing
def inc(x):
    time.sleep(5)
    return x + 1

def dec(x):
    time.sleep(3)
    return x - 1

def add(x, y):
    time.sleep(7)
    return x + y

def whitespace(input):
    spaced = " ".join(input)
    time.sleep(10)
    return spaced
