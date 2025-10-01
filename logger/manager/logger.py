import logging
import sys
from typing import Optional

from colorama import Fore, Style, init as colorama_init

from ..config.logger import LoggerConfig


# Initialize colorama
colorama_init(autoreset=True)

class ColoredFormatter(logging.Formatter):
    """
    Custom formatter to add colors based on log level.
    """
    COLORS = {
        "DEBUG": Fore.CYAN,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.MAGENTA,
    }

    def format(self, record: logging.LogRecord) -> str:
        color = self.COLORS.get(record.levelname, "")
        formatted = super().format(record)
        return f"{color}{formatted}{Style.RESET_ALL}"

class LoggerManager:
    """
    Handles initialization and retrieval of loggers.
    Provides flexible configuration for console/file outputs.
    """

    @staticmethod
    def init_logger(config: LoggerConfig) -> None:
        """
        Initialize root logger with chosen configuration.
        Prevents reinitialization if already configured.
        """
        root_logger = logging.getLogger()
        
        # Prevent duplicate handlers if called multiple times
        if root_logger.hasHandlers():
            root_logger.handlers.clear()

        log_format = config.fmt.build_format()
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(ColoredFormatter(config.fmt.build_format()))
        handlers = [console_handler]
        
        if config.file_path:
            file_handler = logging.FileHandler(config.file_path)
            handlers.append(file_handler)

        logging.basicConfig(
            level=config.get_level(),
            format=log_format,
            handlers=handlers,
        )

        root_logger.propagate = config.propagate

    @staticmethod
    def get_logger(name: Optional[str] = None) -> logging.Logger:
        """Return a named logger for a specific module."""
        return logging.getLogger(name)