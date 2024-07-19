import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Division by zero")


logging.info("Calling division function..")
logging.debug("Division result: %s", division(1, 0))
logging.info("Division function called successfully.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.critical("This is a critical message.")

# you will notice that since default level is set to DEBUG, all messages are displayed.
