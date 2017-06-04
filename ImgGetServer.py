# -*- coding:utf8 -*-
from download_lofter import *
import time, sys
from multiprocessing.managers import BaseManager

if sys.version_info[0] == 3:
    import queue
else:
    import Queue as queue
# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()
# 失败结果的队列:
fail_queue = queue.Queue()


# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
QueueManager.register('get_fail_queue', callable=lambda: fail_queue)
# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.start()
# 获取Queue的对象:

task = m.get_task_queue()
result = m.get_result_queue()
fail = m.get_fail_queue()

names = ['sys-peter', 'madebai', 'vx-sw201572','1598373634','heydouga','tiantianquan45','zhgw866','xiayuzhu']

page = 0
for name in names:
    print(name)
    page = 0
    while getUrlImg(page, task, name):
        page += 1
        if page > 50:
            break
        pass

flag = True
while flag:
    try:
        n = result.get(timeout=10)

        if n == 'q':
            flag = False
        else:
            print(n)
    except queue.Empty:
        print('no result')
flag = True
while flag:
    try:
        n = fail.get(timeout=10)
        if n == 'q':
            flag = False
        else:
            print(n)
    except queue.Empty:
        print("no filed")

m.shutdown()
print('master exit.')
