import time
import random
from concurrent.futures import ThreadPoolExecutor

tables = ["order","product","customer"]

def my_func(p_x):

    wait = random.randint(1,4)
    time.sleep(3)
    print(f"i am {p_x}. i took wait {wait} seconds ")

with ThreadPoolExecutor(max_workers=len(tables)) as executor:

    futures = executor.map(my_func,tables)