import requests

url = "https://www.lumendatabase.org/notices/search?term=%s"

def _makerequest(url):

    headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'DNT': '1',
                'Cookie': 'advanced_search_visibility=1; lumen_authenticated=0; _lumen_session=L3pVUGEzZUF5YkZIaHFBQmd6Q0JJQW1GcTFiNTJMa0Z1aGVLU0Q5ZVMydXY3VkRyQzBTcG5Sb3BDK2pwVWlDTENsTEg5aURySGtvbGtQYjBndXBBd1E3S3RUKzF6ejRpVVhXM1JPTnhHN3pWbndtdVZRZUx4b2VoTE11NjBaalZ6RFd0dnNJR0dIbTRYVzMzdHEzRmNLdHFSdGVZWWJwT29WMUNGU254Ny9MVkxBSjBHblVTdVJSNWpzWEZVc2JCeFVzTW94b3MrcEJQSUxOcWxsOUlTOVJiRGl1UGRVMCtZcndNWERMK2hUZz0tLXNsTzBSMTJvam5yTk82Y1NxOEpMOXc9PQ%3D%3D--c14f39a927e4134ff04e3e7c40cf75f645c9d669',
                'Cache-Control': 'max-age=0'
               }

    resp = requests.get(url, headers=headers)
    return resp.content.decode()

def _parseresponce(html):
    links = []

    html = html.splitlines()

    for num, line in enumerate(html):
        if line.strip('            ') == '<li class="excerpt">':
            couldbe = html[num + 1]
            if couldbe.strip('            ') != '<em>Joker</em>':
                links.append(html[num + 1].replace('            ', '').replace('[REDACTED]', ''))

    return links


if __name__ == "__main__":
    # this just for testing without the UI
    film = input("FILM >>> ")
    resp = _makerequest(url % (film))
    links = _parseresponce(resp)

    print(links)