import logging
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO

from pandora.vectorization import Vectorizer
from pandora.parameters import Settings

def main():
    logging.info('Box of Pandora open...')

    s = Settings(config_path='config/12c.json')
    print(s)

    vectorizer = Vectorizer(settings=s)
    s = vectorizer.fit()
    print(s)

    logging.info('Box of Pandora closed!')


if __name__ == '__main__':
    main()