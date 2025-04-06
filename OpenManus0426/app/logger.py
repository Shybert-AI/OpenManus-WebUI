import sys
from datetime import datetime
import queue
from loguru import logger as _logger

from app.config import PROJECT_ROOT


_print_level = "INFO"

# 创建线程安全的队列用于存储日志
log_queue = queue.Queue()

# 自定义 Sink 将日志写入队列
def log_sink(message):
    """将 loguru 日志消息推送到队列"""
    log_queue.put(message)

def define_log_level(print_level="INFO", logfile_level="DEBUG", name: str = None):
    """Adjust the log level to above level"""
    global _print_level
    _print_level = print_level

    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y%m%d")
    log_name = "root"
    _logger.remove()
    _logger.add(sys.stderr, level=print_level)
    _logger.add(log_sink, level=print_level)
    _logger.add(PROJECT_ROOT / f"logs/{log_name}.log", level=logfile_level)
    return _logger


logger = define_log_level()


if __name__ == "__main__":
    logger.info("Starting application")
    logger.debug("Debug message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")

    try:
        raise ValueError("Test error")
    except Exception as e:
        logger.exception(f"An error occurred: {e}")
