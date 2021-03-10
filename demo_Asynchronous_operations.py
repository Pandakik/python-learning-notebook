#sync
#调用一个web服务 去delay
from timeit import default_timer#快速和容易去看花费多长时间
import requests#最常用发起HTTP/HTTPS的库

def load_data(delay):#delay可以设置延迟的时间
    print(f'Starting {delay} second timer')
    text = requests.get(f'https://httpbin.org/delay/{dealy}').text
    print(f'Completed {delay} second timer')
    return text

def run_demo():
    start_time =default_timer

    two_data = load_data(2)
    three_data = load_data(3)

    elapsed_time = default_timer() - start_time
    print(f'The operation took {elapsed_time:.2} seconds')

def main():    
    run_demo()

main()    


#async
#demo2
from timeit import default_timer#快速和容易去看花费多长时间
import aiohttp#是异步发起http的库
import asyncio

async def load_data(delay):#delay可以设置延迟的时间
        print(f'Starting {delay} second timer')
        async with session.get(f'https://httpbin.org/delay/{dealy}') as resp:
            text = await resp.text()
            print(f'Completed {delay} second timer')
            return text

async def main():
    #Start the timer
    start_time = default_timer()

    #Creating a single session
    async  with aiohttp.ClienSession() as session:
        #Setup our tasks and get them running
        two_task = asyncio.create_task(load_data(session,2))
        three_task = asyncio.create_task(load_data(session,3))