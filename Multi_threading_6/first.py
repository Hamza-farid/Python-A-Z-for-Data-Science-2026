import time
import random
from concurrent.futures import ThreadPoolExecutor



def my_func(p_x):

    wait = random.randint(1,4)
    time.sleep(wait)
    print(f"i am {p_x}. i took wait {wait} seconds ")

my_func(101)
