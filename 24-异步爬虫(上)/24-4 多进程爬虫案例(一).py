import requests
from fake_useragent import FakeUserAgent
import multiprocessing
# 目标网站:https://sc.chinaz.com/tupian/
user_agent_demo = FakeUserAgent().random
result = []
urls = ["https://scpic2.chinaz.net/Files/pic/pic9/202206/bpic26343_s.jpg",
        "https://scpic1.chinaz.net/Files/pic/pic9/202206/apic41370_s.jpg",
        "https://scpic3.chinaz.net/Files/pic/pic9/202206/bpic26347_s.jpg",
        "https://scpic2.chinaz.net/Files/pic/pic9/202206/bpic26348_s.jpg",
        "https://scpic3.chinaz.net/Files/pic/pic9/202206/hpic5515_s.jpg",
        "https://scpic2.chinaz.net/Files/pic/pic9/202206/hpic5520_s.jpg"
]

def GetResponse(url,queue):
    # 获取响应
    queue.put(url)
    response_ = requests.get(url,headers={'User-Agent':user_agent_demo})
    data = response_.content
    with open(url.split('/')[-1].split('.')[0] + '.jpg','wb') as f:
        f.write(data)
    return data


if __name__ == '__main__':
    jobs = []
    queues = []
    for url in urls:
        queue = multiprocessing.Queue()
        queues.append(queue)
        p = multiprocessing.Process(target=GetResponse,args=(url,queue))
        jobs.append(p)
        p.start()
    for i,t in enumerate(jobs):
        t.join()
        result.append(queues[i].get())