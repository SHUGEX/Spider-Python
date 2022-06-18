import multiprocessing
import time
from multiprocessing import Queue
from multiprocessing.dummy import Pool # 用于创建线程池
# from multiprocessing import Pool  # 进程池创建

t1 = time.time()
urls = [i for i in range(1,4)]  # 假如此处存在1000个url
result = []


# def GetResponse(url,queue):
#     # 多进程模拟
#     res = url*url
#     queue.put(res)
#     time.sleep(2)
#     return res
def GetResponse(url):
    # 线程池使用
    res = url*url
    result.append(res)
    time.sleep(2)
    return res

# if __name__ == '__main__':
#     多进程的使用
#     jobs = []  # 用于存放各个进程的任务
#     queues = []  # 用于存放队列对象
#     for url in urls:
#         queue = Queue()
#         queues.append(queue)
#         p = multiprocessing.Process(target=GetResponse,args=(url,queue))
#         jobs.append(p)
#         p.start()
#     for i,t in enumerate(jobs): # enumerate作用主浊取出列表中元素值以及其对应的下标
#         t.join()
#         result.append(queues[i].get())
#     print(result)
#     t2 = time.time()
#     print('代码运行所耗时长:',t2-t1)

if __name__ == '__main__':
    pool = Pool(4)  # 创建线程池，空间为Pool中传入的数字，数字有多大，创建的池就有多少个线程
    # 线程池以及进程池不要无限创建，根据个人任务需求开建满足标准的进程池或者线程池
    pool.map(GetResponse,urls)  # 把任务以及需要传入任务的参数进行映射，第一个参数传入的是任务(函数或其它逻辑代码块)
    # 映射结束即代表任务结束
    print(result)
    t2 = time.time()
    print('代码运行消耗时长为：',t2-t1)