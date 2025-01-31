import logging
import logging.handlers
import os
from datetime import datetime
from pathlib import Path

class LogConfig:
    """Logging Configuration"""
    
    LOGGING_LEVELS = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }

    def __init__(self, app_name: str = "sportsbot"):
        self.app_name = app_name
        self.log_dir = Path("logs")
        self.log_dir.mkdir(exist_ok=True)
        
        # Create separate log files for different components
        self.app_log = self.log_dir / f"{app_name}.log"
        self.error_log = self.log_dir / f"{app_name}_error.log"
        self.debug_log = self.log_dir / f"{app_name}_debug.log"
        self.api_log = self.log_dir / f"{app_name}_api.log"

    def setup_logging(self, level: str = "INFO", debug_mode: bool = False):
        """Setup logging configuration"""
        level = self.LOGGING_LEVELS.get(level.upper(), logging.INFO)
        if debug_mode:
            level = logging.DEBUG

        # Create formatters
        standard_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        detailed_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
        )

        # Setup handlers
        handlers = {
            'app': self._setup_file_handler(self.app_log, standard_formatter, level),
            'error': self._setup_file_handler(self.error_log, detailed_formatter, logging.ERROR),
            'debug': self._setup_file_handler(self.debug_log, detailed_formatter, logging.DEBUG),
            'api': self._setup_file_handler(self.api_log, detailed_formatter, level),
            'console': self._setup_console_handler(standard_formatter, level)
        }

        # Setup root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(level)
        
        # Remove existing handlers
        for handler in root_logger.handlers[:]:
            root_logger.removeHandler(handler)
        
        # Add new handlers
        for handler in handlers.values():
            root_logger.addHandler(handler)

        # Create specific loggers
        self.setup_component_logger('api', handlers['api'])
        self.setup_component_logger('error', handlers['error'])
        self.setup_component_logger('debug', handlers['debug'])

        logging.info(f"Logging setup complete. Level: {logging.getLevelName(level)}")
        if debug_mode:
            logging.debug("Debug mode enabled")

    def _setup_file_handler(self, log_file: Path, formatter: logging.Formatter, 
                          level: int) -> logging.Handler:
        """Setup a file handler with rotation"""
        handler = logging.handlers.RotatingFileHandler(
            log_file,
            maxBytes=10485760,  # 10MB
            backupCount=5,
            encoding='utf-8'
        )
        handler.setFormatter(formatter)
        handler.setLevel(level)
        return handler

    def _setup_console_handler(self, formatter: logging.Formatter, 
                             level: int) -> logging.Handler:
        """Setup console handler"""
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        handler.setLevel(level)
        return handler

    def setup_component_logger(self, name: str, handler: logging.Handler) -> logging.Logger:
        """Setup a logger for a specific component"""
        logger = logging.getLogger(f"{self.app_name}.{name}")
        logger.addHandler(handler)
        logger.propagate = False
        return logger

    @staticmethod
    def get_component_logger(component_name: str) -> logging.Logger:
        """Get a logger for a specific component"""
        return logging.getLogger(f"sportsbot.{component_name}")

def setup_debug_mode():
    """Setup debug mode with detailed logging"""
    log_config = LogConfig()
    log_config.setup_logging(level="DEBUG", debug_mode=True)
    return log_config

def setup_production_mode():
    """Setup production mode with standard logging"""
    log_config = LogConfig()
    log_config.setup_logging(level="INFO", debug_mode=False)
    return log_config
