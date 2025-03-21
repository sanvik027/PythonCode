import logging


import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Decorator definition
def log_info(func):
    def wrapper(*args, **kwargs):
        # Log the input arguments
        logging.info(f"The arguments passed are: {args}")
        # Call the original function and store the result
        result = func(*args, **kwargs)
        # Log the output result
        logging.info(f"Result: {result}")
        return result  # Return the result of the original function
    return wrapper  # Return the wrapper function

# Decorator applied
@log_info
def add_val(inp1, inp2):
    return inp1 + inp2

# Function call
total = add_val(4, 6)
logging.info(total)  # Output: 10
