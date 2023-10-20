import concurrent.futures
import time
import random

def myFunc(myparam): 
    time.sleep(random.randint(1, 5))
    print(myparam)

if __name__ == '__main__':
    print('hello world')
    _params = [1, 2, 3, 4, 5]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(myFunc, myparam) for myparam in _params]