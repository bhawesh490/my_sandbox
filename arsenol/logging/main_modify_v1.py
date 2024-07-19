import set_log
import employee_modify_v1

logger = set_log.setup_logging(__name__, "main_modify_v1.log")


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
