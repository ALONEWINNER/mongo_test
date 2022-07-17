import logging
print("hello")
#logging.basicConfig(filename="test.log")
logging.basicConfig(filename="test.log",level=logging.INFO)
logging.info("this is first code")
logging.warning(("this is warning"))
logging.info("lallu lal  is a good")
logging.error("this is system error")
l=[1,2,3,4]
for i in l:
    if i==2:
        logging.info(l)
        logging.warning("this is waringfor the user for 2 times")
logging.shutdown()
