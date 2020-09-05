"""
  Counting Cubes multiprocessing
"""

import multiprocessing
import time

def get_cube(num):
  """
  function to print cube of given num
  """
  return num**3

def get_cubes(nums):
  for i in range(100000000):
    pass
  print([get_cube(num) for num in nums])

def get_range(length, amount):
  start = 0
  while start != length:
    end = length//amount + start
    yield start, end
    start = end


numbers = range(30)

if __name__ == "__main__":
  gen = get_range(30, 3)
  start, end = next(gen)
  # creating thread
  x = time.perf_counter()
  t1 = multiprocessing.Process(target=get_cubes, args=(numbers[start:end],))
  start, end = next(gen)
  t2 = multiprocessing.Process(target=get_cubes, args=(numbers[start:end],))
  start, end = next(gen)
  t3 = multiprocessing.Process(target=get_cubes, args=(numbers[start:end],))

  # starting thread 1
  t1.start()
  # starting thread 2
  t2.start()
  # starting thread 3
  t3.start()

  # wait until thread 1 is completely executed
  t1.join()
  # wait until thread 2 is completely executed
  t2.join()
  # wait until thread 3 is completely executed
  t3.join()

  # both threads completely executed
  print("Done!")
  print(f'{time.perf_counter() - x}')