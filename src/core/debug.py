from functools import wraps
import logging
import time
import traceback
from typing import Any, Callable, Dict, Optional
from .logging_config import LogConfig

logger = LogConfig.get_component_logger("debug")

class DebugMode:
    """Debug mode configuration and utilities"""
    
    def __init__(self):
        self.enabled = False
        self.trace_calls = False
        self.trace_api = False
        self.trace_performance = False
    
    def enable(self, trace_calls: bool = True, trace_api: bool = True, 
               trace_performance: bool = True):
        """Enable debug mode with specified tracing options"""
        self.enabled = True
        self.trace_calls = trace_calls
        self.trace_api = trace_api
        self.trace_performance = trace_performance
        logger.debug(f"Debug mode enabled with settings: calls={trace_calls}, "
                    f"api={trace_api}, performance={trace_performance}")
    
    def disable(self):
        """Disable debug mode"""
        self.enabled = False
        self.trace_calls = False
        self.trace_api = False
        self.trace_performance = False
        logger.debug("Debug mode disabled")

# Global debug mode instance
DEBUG_MODE = DebugMode()

def debug_trace(func: Callable) -> Callable:
    """Decorator to trace function calls in debug mode"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if not DEBUG_MODE.trace_calls:
            return await func(*args, **kwargs)
        
        func_name = func.__name__
        logger.debug(f"Entering {func_name}")
        logger.debug(f"Args: {args}")
        logger.debug(f"Kwargs: {kwargs}")
        
        try:
            start_time = time.time()
            result = await func(*args, **kwargs)
            end_time = time.time()
            
            if DEBUG_MODE.trace_performance:
                duration = end_time - start_time
                logger.debug(f"{func_name} execution time: {duration:.4f} seconds")
            
            logger.debug(f"{func_name} returned: {result}")
            return result
        except Exception as e:
            logger.error(f"Error in {func_name}: {str(e)}")
            logger.error(f"Traceback: {traceback.format_exc()}")
            raise
    
    return wrapper

def api_debug_trace(func: Callable) -> Callable:
    """Decorator to trace API calls in debug mode"""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if not DEBUG_MODE.trace_api:
            return await func(*args, **kwargs)
        
        func_name = func.__name__
        logger.debug(f"API Call: {func_name}")
        
        try:
            start_time = time.time()
            result = await func(*args, **kwargs)
            end_time = time.time()
            
            if DEBUG_MODE.trace_performance:
                duration = end_time - start_time
                logger.debug(f"API {func_name} response time: {duration:.4f} seconds")
            
            logger.debug(f"API {func_name} response: {result}")
            return result
        except Exception as e:
            logger.error(f"API Error in {func_name}: {str(e)}")
            logger.error(f"API Traceback: {traceback.format_exc()}")
            raise
    
    return wrapper

def log_error(error: Exception, context: Optional[Dict[str, Any]] = None):
    """Log an error with context in debug mode"""
    if not DEBUG_MODE.enabled:
        logger.error(str(error))
        return
    
    error_type = type(error).__name__
    error_msg = str(error)
    stack_trace = traceback.format_exc()
    
    logger.error(f"Error Type: {error_type}")
    logger.error(f"Error Message: {error_msg}")
    
    if context:
        logger.error(f"Error Context: {context}")
    
    logger.error(f"Stack Trace:\n{stack_trace}")

def performance_log(operation: str, duration: float):
    """Log performance metrics in debug mode"""
    if not DEBUG_MODE.trace_performance:
        return
    
    logger.debug(f"Performance - {operation}: {duration:.4f} seconds")
