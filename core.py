from handlelist import handle_list
import scrape
from settings import *
import sys
import time
import update


def iterate_handles(i, msg):
    while i < len(handle_list) and len(msg) < TWEET_LEN and len(
            msg +
            handle_list[i] +
            ' ') < TWEET_LEN:
        msg += handle_list[i] + ' '
        i += 1

    iterate_handles.index = i
    update.tweet(msg)

raw_list = api.GetUserTimeline(screen_name='puyalluppd')
status_list = [s.text for s in raw_list]
street_name = scrape.parse_string(status_list)
if street_name < 0:
    sys.exit(1)
this_week_date = time.strftime("%m/%d")
sotw = "SOTW:"

message = "{}'s {} {} ".format(this_week_date, sotw, street_name)
iterate_handles.index = 0

while iterate_handles.index < len(handle_list):
    iterate_handles(iterate_handles.index, message)
