# -*- coding:utf8 -*-
import pika

print(pika)
import time
from download_lofter import *
import time, sys
from multiprocessing.managers import BaseManager

if sys.version_info[0] == 3:
    import queue
else:
    import Queue as queue
#starttime = datetime.datetime.now()


# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
QueueManager.register('get_fail_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '120.24.190.4'
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
fail = m.get_fail_queue()

flag = True

img = Img()
getImg = img.getImg

while flag:
    try:
        r = getImg(task, fail)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        r = 'q'
        result.put(r)
        print('task queue is empty.')
        flag = False
print('\a')
# do something
# endtime = datetime.datetime.now()
# interval = (endtime - starttime).seconds
# #print(interval)
