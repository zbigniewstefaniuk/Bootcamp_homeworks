"""
    counting cubes with threads
"""

import time
import threading

def get_cube(num: int) -> int:
    return num**3

def get_cubes(nums: list):
    for i in range(100000000):
        pass
    print([get_cube(num) for num in nums])
    # return None

numbers = range(30)

def get_range(length: int, amount: int) -> tuple: # 30, 3
    start = 0
    while start != length:
        end = length // amount + start
        yield start, end
        start = end

gen = get_range(len(numbers), 3)

start, end = next(gen)
t1 = threading.Thread(target=get_cubes, args=(numbers[start:end],))
start, end = next(gen)
t2 = threading.Thread(target=get_cubes, args=(numbers[start:end],))
start, end = next(gen)
t3 = threading.Thread(target=get_cubes, args=(numbers[start:end],))

time1 = time.perf_counter()
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
time2 = time.perf_counter()

get_cubes(numbers)
time3 = time.perf_counter()

print(f'Czas watki: {time2-time1}')
