import multiprocessing

def factorize_number(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return divisors

def factorize(*numbers):
    num_processes = multiprocessing.cpu_count() # finding number of available cores
    pool = multiprocessing.Pool(processes=num_processes) # creating pull process
    divisors = pool.map(factorize_number, numbers) # parallel calculation
    pool.close() # closing
    pool.join() # and combining pool processes
    return divisors

#test
a, b, c, d = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
