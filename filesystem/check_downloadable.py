"""

Concept/Code: Hem Raj Regmi (sangamsyabil@gmail.com)
github repository: https://github.com/sangamsyabil/hemAutomation

Happy coding !!!
"""
import requests
from shutil import copyfile


def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


print(is_downloadable('https://www.youtube.com/watch?v=9bZkp7q19f0'))  # >> False
print(is_downloadable('http://google.com/favicon.ico'))  # >> True


# Download the file from `url` and save it locally under `file_name`:
def download_file_from_url(url, file_name):
    with open(file_name, "wb") as file:
        response = requests.get(url)
        file.write(response.content)


def copy_file(src, dst):
    copyfile(src, dst)
