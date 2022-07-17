import logging
#logging.basicConfig(filename="teset2.log",level=logging.DEBUG,format='%(asctime)s %(message)s')
logging.basicConfig(filename="test2.log",level=logging.DEBUG,format='%(levelName)s %(name)s %(asctime)s,%(message)s')
logging.info("this is mylog in timestmp")
