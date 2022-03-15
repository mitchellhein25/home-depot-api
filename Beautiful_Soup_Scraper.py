import requests
from bs4 import BeautifulSoup as bs
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class soup_initiator:
    """This Class takes a URL and grabs the soup object from the
    HTML of the site, using the get_soup() method"""

    def __init__(self, url):
        self._url = url

    def requests_retry_session(
        retries=3,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504),
        session=None,
    ):
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session
    def get_soup(self):

        header ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        print('Retrieving info from', self._url, '\n...')
        try:
            r = self.requests_retry_session().get(self._url, headers=header, timeout=15, verify=False)
        except:
            print("Timeout occurred")
            r = self.requests_retry_session().get(self._url, headers=header, timeout=15, verify=False)
        soup = bs(r.content.decode('utf-8', 'ignore'), 'lxml')
        return soup
