# -*- coding:utf-8 -*-
import hashlib

sha = hashlib.sha256()

sha.update("这个世界很疯狂".encode())  # updat 还可以对数据进行串接进行加密
sha.update("second world is crazy".encode())
print(sha.digest())  # 二进制
print(sha.hexdigest())  # 十六进制

sha2 = hashlib.sha256()
sha2.update("这个世界很疯狂second world is crazy".encode())
print(sha2.hexdigest())

import hmac

hm = hmac.new("世界".encode())
print(hm.hexdigest())

import logging

logging.basicConfig(filename="example.log", level=logging.DEBUG,
                    format='%(asctime)s %(message)s %(pathname)s %(lineno)d',
                    datefmt='%m/%d/%Y %I:%M:%S %p')  # #level设置级别时需要大写
# logging.basicConfig(filename='example.log',level=logging.INFO)
logging.warning("this is warning")
logging.critical("this is critical")
logging.error("this is error")
print("------------")
logging.debug("this is debug")
logging.info("this is info")

logger = logging.getLogger("Test-log")
logger.setLevel(logging.DEBUG)
