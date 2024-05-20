import time

def make_cofee():
    print('started preparing cofee')
    time.sleep(3)
    print('cofee is ready')
    
def boil_egg():
    print('started preparing egg')
    time.sleep(2)
    print('egg is ready')
    
if __name__ == '__main__':
    start_time=time.time()
    make_cofee()
    boil_egg()
    endtime =time.time()-start_time
    print('execution time: ',endtime)
    
    