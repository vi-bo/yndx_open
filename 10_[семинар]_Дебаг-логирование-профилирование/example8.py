import logging
import os
logging.basicConfig(level=logging.INFO)

logging.info(
        'Worker with PID %s has been started',
        os.getpid(),
)
