import logging


def test_print_logs():
    Logger = logging.getLogger(__name__)

    Logger.info("This is information logs")
    Logger.error("This is error logs")
    Logger.critical("This is critical logs")
    Logger.warning("This is warning logs")
