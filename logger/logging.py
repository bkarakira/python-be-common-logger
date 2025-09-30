import logging
import sys
from typing import Optional

def get_logger(name: Optional[str] = None, level: int = logging.INFO) -> logging.Logger:
  logger = logging.getLogger(name)
  logger.setLevel(level)
  
  handler = logging.StreamHandler(sys.stdout)
  handler.setLevel(level)

  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  
  print("new version 0.2.1")

  return logger