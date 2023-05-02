import logging

log_file = './cf.log'

# Create a FileHandler for logging a file
# The default mod is 'a', that is append
file_handler = logging.FileHandler(log_file, mode='a')

# Create a list of handlers for the logger
handlers = [file_handler]

# Name of the logger, otherwise 'root'
logger = logging.getLogger('search-app')

# Configure  the root logger with the handlers list
# Named loggers inherit the properties of root logger
logging.basicConfig(handlers=handlers, level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")

nums = [1, 2, 3, 4, 5]
num_to_find = 20

try:
    index = nums.index(num_to_find)
    print("Found")
except ValueError as e:
    logger.error(f"{e}", exc_info=True)