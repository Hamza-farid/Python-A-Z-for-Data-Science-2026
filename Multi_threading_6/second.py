import time
import random
from concurrent.futures import ThreadPoolExecutor

tables = ["order","product","customer"]

def my_func(p_x):

    wait = random.randint(1,4)
    time.sleep(wait)
    print(f"i am {p_x}. i took wait {wait} seconds ")

for i in tables:
    my_func(i)