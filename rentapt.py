import time
import urllib
from lxml import html
from twilio.rest import Client

def sendMessage():
    # Your Account SID from twilio.com/console
    account_sid = "AC5554fc17f070137914xxxxxxxxxxxxxx"
    # Your Auth Token from twilio.com/console
    auth_token  = "01166a0bc0d683a241xxxxxxxxxxxxxx"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
          to='+1917xxxxxxx',
          from_="+1970xxxxxxx",
          body='Studio Vacancy!!')

    print(message.sid)


def sleep_time(time_hour, time_min, time_second):
    return time_hour * 3600 + time_min * 60 + time_second

url = 'https://www.235grand.com/floorplans'
header= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
      'AppleWebKit/537.11 (KHTML, like Gecko) '
      'Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}


if __name__ == '__main__':
    second = sleep_time(0, 5, 0)

    while True:
        time.sleep(second)
        req = urllib.request.Request(url, headers=header)
        # req = urllib.request.Request(url)
        # req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36")
        request_url = urllib.request.urlopen(req)
        a = request_url.read()
        tree = html.fromstring(a)
        word = tree.xpath('//a[@data-floorplan-name="Studio"]/text()')[0].strip()
        # tree.xpath('//a[@data-floorplan-name="1 Bedroom - 1 Bathroom"]/text()')[0].strip()
        # tree.xpath("//*[@id='desktop_qualifiedBuyBox']")
        if word == 'Availability':
            sendMessage()
            print('yes')
            break