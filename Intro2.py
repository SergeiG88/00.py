import requests as rq
import logging.config
from log_settings import log_config

logging.config.dictConfig(log_config)
logger = logging.getLogger('RequestsLogger')

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        site_code = response.status_code
        if response.status_code == 200:
            log_suc = logging.getLogger('success')
            log_suc.info(f'{site}, response - {site_code}')
        elif response.status_code != 200:
            log_bad = logging.getLogger('bad')
            log_bad.warning(f'{site}, response - {site_code}')
    except Exception:
        logging.exception(f'NO CONNECTION')
