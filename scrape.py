from keywords import keywords
import re
from settings import *
import string


def parse_string(recent_statuses):
    """
    Parses recent statuses to find the 'Street of the Week' status and then
    attempts to extract the correct street name from the status.
    """

    # The following can be used for testing
    """recent_statuses = [u'If you\'re a driver on 13 AVE NW from 18 ST NW to the City limits watch out for us as you are on the Street of the Week starting tomorrow!',
         u'What street are we looking for speeders on this week? Highlands BLVD is our Street of the Week. 25 mph on this street! Slow Down!',
         u'Street of the Week is 18th, 15th, & 7th ST NW from W Stewart to River RD. All are residential streets. Slow down or you could be out $124.',
         u'This week our Street of the Week is 14 ST SW from 7 AV SW to 15 AV SW & 7 AV SW from S Fruitland to S Meridian ST. Slow Down!',
         u'It\'s Monday! And we have a new Street of the Week. Actually several streets as we work in the NE area this week. 5 ST NE & 2 AVE NE.',
         u'31 AVE SW between 9 ST SW & S Fruitland is our Street of the Week this week. Slow down!',
         u'Are you a Shaw RD driver? If so, watch for us this week as you are on the Street of the Week! 10 over is a $124 fine! Slow Down!',]"""

    # Takes the most [0]th (most recent) status
    try:
        s = [
            s for s in recent_statuses if 'street of the week' in s.lower()][0]
    except IndexError:
        return -1

    # Redefine string.punctuation because we want to exclude ampersandss
    string.punctuation = """!"#$%'()*+,-./:;<=>?@[\]^_`{|}~"""

    # Strip all punctuation
    n_s = s.encode('utf-8').translate(None, string.punctuation)

    regex = re.compile(r'(\d)(th|rd|nd)')  # 5th, 4th, 2nd, 3rd, etc.

    # Strip all ordinal suffixes but keep the numbers
    correct_status = re.sub(regex, r'\1', n_s)
    # print correct_status

    split_list = correct_status.split()

    # Take all of the street names from the status
    word_list = [
        w for w in split_list if w.upper() in (
            kw.upper() for kw in keywords)]

    wl_len = len(word_list)
    tmp_string = ""
    rand_arr = []  # Primarily for error checking on my part

    """
    Start creating strings from our word list. As long as the string is still
    found in the status, we keep adding to it. Once we find that it isn't, we
    return what we have, which we hope is the correct street name.
    """

    for i in xrange(wl_len):
        if tmp_string + word_list[i] in correct_status:
            if i == wl_len - 1:
                return tmp_string + word_list[i]
            else:
                tmp_string += word_list[i] + ' '
        elif len(tmp_string.split()) is 1:
            rand_arr.append(word_list[i])
            tmp_string = word_list[i] + ' '
        else:
            return tmp_string.rstrip()
