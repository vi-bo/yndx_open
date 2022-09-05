import logging

logging.basicConfig(level=logging.DEBUG)

for i in range(1000):
    logging.info("Iteration %s", i)