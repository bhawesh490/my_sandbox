import logging
import employee_modify

logger = logging.getLogger(__name__)
# logger = logging.getLogger("main_modify")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("main_modify.log")
stream_handler = logging.StreamHandler()
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logger.error("Division by zero")


logger.info("Calling division function..")
logger.debug("Division result: %s", division(1, 0))
logger.info("Division function called successfully.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")

# you will notice that since default level is set to DEBUG, all messages are displayed.
