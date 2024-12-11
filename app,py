import time
import asyncio

async def washDishes():
    print("Dish washing machine started...")
    await asyncio.sleep(4)
    print("Dish washing machine finished")
    return "Dish Washing Completed!"

async def openWidnows():
    print("opening the kitchen windows...")
    await asyncio.sleep(2)
    print("opening windows completed...")
    return "Open Window Completed!"

async def main():
    start_time = time.time()
    
    try:
        washer_task = asyncio.create_task(washDishes())
        windows_task = asyncio.create_task(openWidnows())

        washer_returns = await washer_task
        windows_returns = await windows_task 
        end_time = time.time()
        # calculate time diference to obtain the execution time
        execution_time = end_time - start_time
        print (f"Total execution time is {execution_time:.2f}")
        
    except Exception as e:
        print(f"Exception caught, error message: {e}")


if __name__ == "__main__":
    asyncio.run(main())