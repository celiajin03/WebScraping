import time
import urllib
import ast
from twilio.rest import Client

def sendMessage():
    # Your Account SID from twilio.com/console
    account_sid = "AC5554fc17f070137914xxxxxxxxxxxxxx"
    # Your Auth Token from twilio.com/console
    auth_token  = "01166a0bc0d683a241xxxxxxxxxxxxxx"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
          to='+1917xxxxxxx',                  # receiving phone no.
          from_="+1970xxxxxxx",               # twilio phone no.
          body='Sign Up!!!')                  # msg content

    print(message.sid)


def sleep_time(time_hour, time_min, time_second):
    return time_hour * 3600 + time_min * 60 + time_second

url = 'https://www.newyorkbartendingschool.com/wp-admin/admin-ajax.php'
values = {'action': 'fetch_fooevents_bookings_dates',
          'selected': 'txzvcjqttkcfbtxnkoob_6221'}


if __name__ == '__main__':
    second = sleep_time(0, 5, 0)

    while True:
        time.sleep(second)
        data = urllib.parse.urlencode(values).encode('ascii')
        req = urllib.request.Request(url, data)
        a = urllib.request.urlopen(req).read()
        b = ast.literal_eval(a.decode('UTF-8'))
        next_day = next(iter(b.items()))[1]
        if next_day == 'May 16, 2022':
            sendMessage()
            break