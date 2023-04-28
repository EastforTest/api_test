import logging

"""
logging库提供了多个组件：Logger、Handler、Filter、Formatter。Logger对象提供应用程序可直接使用的接口

Handler发送日志到适当的目的地，

Filter提供了过滤日志信息的方法，

Formatter指定日志显示格式。另外，可以通过：logger.setLevel(logging.Debug)设置级别

日志我们一般写代码的时候会添加,部分公司和部分项目要求不一样,

info一般都是记录一些消费信息,操作信息,转账信息

info以上的级别就是在程序出现错误的时候会记录
"""

logger = logging.getLogger()
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test1.log',encoding='utf-8')
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
logger.setLevel(logging.DEBUG)# 设置日志的级别
fh.setFormatter(formatter)#设置的日志的输出
ch.setFormatter(formatter)
logger.addHandler(fh) #logger对象可以添加多个fh和ch对象
logger.addHandler(ch)
logger.debug('logger debug message')#写入日志的信息
logger.info('logger info message')
logger.warning('logger warning message')
logger.error('logger error message')
logger.critical('logger critical message')
