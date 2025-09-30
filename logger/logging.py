import logging
import sys
from typing import Optional

def get_logger(name: Optional[str] = None, level: int = logging.INFO) -> logging.Logger:
      """
    Create and return a logger with the given name.

    Args:
        name (str): Name of the logger (usually your app name or module).
        level (int): Logging level. Defaults to INFO.
    """
      logger = logging.getLogger(name)
      logger.setLevel(level)
      handler = logging.StreamHandler(sys.stdout)
      handler.setLevel(level)
      formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
      handler.setFormatter(formatter)
      logger.addHandler(handler)
      return logger