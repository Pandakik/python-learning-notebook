#异步操作
#The waiting is the hardest part
'''
#Some operations take a long time
Web calls
Network IO
Complex data processing
#We don't want to stop everything just because
one process is taking foreever
'''
#Concurrency and parallelism is a broad topic
'''
All languages offer mutople options for managing long running operations
Python is no exception
We're going to focus on a common scenario - web requests
'''

#Introducing the asyncio module
'''
-New in Pythoon 3.4
Undergoing regular updates
"Grafts" asynchronous development into Python
Streams
async/await
Synchronization(locks)
Exception management
'''

#Running our aiohttp demo
async def main():
    strat_time = default_timer()

    async with aiohttp.ClientSession() as session:
        two_task = asyncio.create_tasl(load_data(session, 2)
        three_task = asyncio.create_tasl(load_data(session, 3)

        print('Doing other work')

        two_result = await two_task
        three_result = await three_task

        elapsed_time = default_timer() - strat_time
        print(f'The operation took {elapsed_time:.2} secondes')

#Asynchronous using aiohttp
# install aiohttp
import aiohttp
from timeit impor default_timer

async def load_data(session, delay):
    async with session.get(f'https://httpbin.org/delay/{delay}') as resp:
        await resp.text()
#continued...