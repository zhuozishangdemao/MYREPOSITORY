# async def fetch_data():
#     print("start request")
#     return "data"
# #return is not a direct result, but a coroutine,which have to be executed by await or asyncio.run()
# async def main():
#     result = await fetch_data()# suspend main(),until fetch_dat finish its movement
#     print(result)

import asyncio

asyncio.run(main())

async def task1():
    await asyncio.sleep(1)
    return "A"
async def task2():
    await asyncio.sleep(2)
    return "B"
async def main():
    results = await asyncio.gather(task1(),task2())
    #when it comes to activate more than A task,the efficiency is its advvantage
    print(results) #use only two seconds
    
