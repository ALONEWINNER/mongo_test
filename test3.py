import logging
logging.basicConfig(filename="test3.log",level=logging.INFO ,format='%(levelname)s %(asctime)s %(name)s %(message)s')

def divide(a,b):
    logging.info("the no entered by u is %s and %s",a,b)
    try:
        logging.info("in function")
        div=a/b
        logging.info("complte div")
        logging.info("reult of the code is %s",div)   #%s is place holder everything ehich will u try to replace it by vale
    except Exception as e:
        logging.exception(e)

print(divide(3,13))