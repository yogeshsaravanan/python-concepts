import time
import asyncio

# importing asyncio to run this functions parallely

async def make_cofee():
    print('started preparing cofee')
    await asyncio.sleep(3)
    print('cofee is ready')
    # return 1
    
async def boil_egg():
    print('started preparing egg')
    await asyncio.sleep(2)
    print('egg is ready')
    # return 2
    
async def main():
    start_time=time.time()
    # make_cofee()
    # boil_egg()
    # gather the fnctions which we are going to run
    
    batch = asyncio.gather(make_cofee(),boil_egg())
    await batch
    # re1,re2 = await batch
    endtime =time.time()-start_time
    print('execution time: ',endtime)
    
if __name__ == '__main__':
    asyncio.run(main())
    
    