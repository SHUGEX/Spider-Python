import asyncio,time


"""
async没有限制并发量的时候，默认为系统最大并发
"""
CONCURRENCY = 20 # 常量，表示定义最大的协程数据
t1 = time.time()
urls = [i for i in range(1,101)]
semaphore = asyncio.Semaphore(CONCURRENCY)  # 限制并发量之后的async协程对象


async def GetResponse(url):
    async with semaphore:    # 控制当前函数的并发量
        # 使用多任务异步协程时，要注意任务任务中不要出现同步的代码块，如果出现同步代码块，就会直接中断异步任务，变成同步任务
        # time.sleep(1)  # 是一个同步操作
        print(url)
        await asyncio.sleep(1)  # 异步中的sleep使用，模拟阻塞操作
        # 在多任务异步协程中，当代码运行遇到阻塞时，需要使用await进行手动挂起

async def funa(url):
    await GetResponse(url)  # 协程对象函数的调用视作一个阻塞操作
    pass

if __name__ == '__main__':
    tasks = []
    for url in urls:
        # task = asyncio.create_task(GetResponse(url))  # 任务创建
        task = asyncio.ensure_future(funa(url))
        tasks.append(task)
    # task = asyncio.ensure_future(GetResponse(999)) # 创建单个任务
    loop = asyncio.get_event_loop()  # 实例化事件循环对象
    loop.run_until_complete(asyncio.wait(tasks))  # 开始执行任务，直到任务结束，如果是多任务
                                                    # 需要asyncio.wait(tasks)方法来执行多个任务
    # loop.run_until_complete(asyncio.wait(task))  # 如果是单任务
    # 单个任务时直接把任务传入事件循环中即可，不用使用wait方法
    t2 = time.time()
    print('代码运行时长为:',t2-t1)  # 单线程运行时长为100秒