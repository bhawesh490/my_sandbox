# Logging in Python
# import logging 
# logging.basicConfig(filename="txt.log", level = logging.INFO)
# types of logging
# DEBUG
# INFO 
# WARNING 
# ERROR 
# CRITICAL 
# logging.info("This is my infor log ")
# logging.warning("this is my warning log ")
# logging.error("this is my error log")
# logging.debug("this is my debug log")
# logging.shutdown()

import logging
logging.basicConfig(filename="test2.log", level = logging.DEBUG,format = '%(asctime)s %(levelname)s %(message)s')
logging.info("This is my Info log")
logging.debug("This is my Debug log")
logging.warning("This is warning log")
logging.error("This is Error log")

# level hiearchy
# 1-ERROR 
# 2-WARNING 
# 3-INFO 
# 4-DEBUG 

def logging_demo(a,b):
    logging.info("this is the start of my code and i am try to enter %s and %s ",a,b)
    try:
        div=a/b 
        logging.info("executed succ")

    except Exception as e:
        logging.error("Error has happened")
        logging.exception("Exception occured :"+str(e))
        logging.error("Error has happened :"+str(e))
        

logging_demo(1,0)          
