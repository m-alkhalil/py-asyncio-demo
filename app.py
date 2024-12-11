import time
import asyncio


def wash_Dishes():
    print ("start washing dishes")
    time.sleep(3)
    print (" washing dishes completed")

def fill_water():
    print ("filling water..")
    time.sleep(2)
    print("cup is full")


def main():
    start_time = time.time()
    wash_Dishes()
    fill_water()
    end_time = time.time()
    
    exec_time = end_time -  start_time 

    print(f"execution time = {exec_time:.2f} Seconds")

if __name__ == "__main__":
    print("start")
    main()
