import logging
logging.basicConfig(filename="test4.log",level=logging.INFO ,format='%(levelname)s %(asctime)s %(name)s %(message)s')


try:
    logging.info("i am read a file")
    with open("su.txt","r"):
        logging.info("success")
except Exception as e:
    logging.critical("this is a situation for us")
    logging.error(e)
    logging.exception(e)