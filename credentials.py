import os
import logging
import dotenv

# create logger
logger = logging.getLogger('credentials')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

logger.info("Loading Username")
FB_USERNAME = os.getenv("FB_USERNAME") if os.getenv("FB_USERNAME") else dotenv.dotenv_values(".env")["FB_USERNAME"]
logger.info("Loading Password")
FB_PASSWORD = os.getenv("FB_PASSWORD") if os.getenv("FB_PASSWORD") else dotenv.dotenv_values(".env")["FB_PASSWORD"]
logger.info("Loading Groupe")
FB_GROUPE = os.getenv("FB_GROUPE") if os.getenv("FB_GROUPE") else dotenv.dotenv_values(".env")["FB_GROUPE"]
logger.info("Loading Name")
FB_NAME = os.getenv("FB_NAME") if os.getenv("FB_NAME") else dotenv.dotenv_values(".env")["FB_NAME"]

if __name__ == '__main__':
    print(f"USERNAME: {FB_USERNAME}")
    print(f"PASSWORD: {FB_PASSWORD}")
    print(f"GROUPE: {FB_GROUPE}")
    print(f"NAME: {FB_NAME}")
