from bot import CONFIG
import logging

# This is global logging config for bot?
logging.basicConfig(**CONFIG.log_config)
