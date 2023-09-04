from bs4 import BeautifulSoup as bs
import logging, datetime
import requests

source = 'https://hololive.hololivepro.com/talents/'

with open('./text/talents.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        modified_lines = [line.replace('\n', '') for line in lines]

#Setting log
def setting_log(logpath):
    
    formatter = '%(levelname)s : %(asctime)s : %(message)s'

    # Chage log level to DEBUG
    logging.basicConfig(level=logging.DEBUG, format=formatter, handlers=[logging.FileHandler(logpath, 'w', 'utf-8')])

    logger = logging.getLogger(__name__)

    return logger

def scraping(url, word, logger):
    link = url+ word
    logger.info(url)
    req = requests.get(link)
    req.encoding = req.apparent_encoding
    soup = bs(req.text, 'html.parser')

    return soup


def excecute(url, query_list):
    txt_path = './text/talent_id.txt'
    exec_datetime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    logger = setting_log(f"./log/{exec_datetime}.log")
    logger.info("-----------------START-------------------")
                
    logger.info(f"Creating text file: {txt_path}")
    with open(txt_path, 'w') as f:
        for word in query_list:
            logger.info("Search Name:" + word)
            soup = scraping(url, word, logger)
            div = soup.find_all('div', class_='right_box')
            href_list = []
            for talent in div:
                _talent = talent.find_all('a')
                for a_tag in _talent:
                    if 'href' in a_tag.attrs and 'www.youtube.com' in a_tag['href']:
                        href_list.append(a_tag['href'])
                    else:
                        pass
                for  href in href_list:
                    f.write(str(href + '\n'))
            logger.info(f'Writing to {txt_path} completed.')
    logger.info("-----------------END-------------------")

if __name__ == '__main__':
    excecute(source, modified_lines)