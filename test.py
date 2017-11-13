import bs4
def get_html(url):
    import urllib.request
    req = urllib.request.Request(url)
    #req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    #req.add_header('User-Agent', '')
    try:
        with urllib.request.urlopen(req,\
         timeout = 10) as html:
            return html.read().decode()
    except:
        print('Error')
        return ''

#soup = bs4.BeautifulSoup(get_html('http://www.baidu.com'), 'html.parser')
#print(get_html('http://poj.org/userstatus?user_id=ooc'))
print(get_html('http://fanyi.niutrans.com'))
