from datetime import datetime

######
# Truncate strings to Safe Length
######
def truncate(string, max_chars=36):
    return (string[:max_chars-3] + '...') if len(string) > max_chars else string
 
######
# Truncate strings to Safe Length
######
def line_count( string, line_limitt=75 ):
    if ( len(string) < line_limitt ):
        return 1.4
    else:
        return 1.5 + ( len(string) / line_limitt )

######
# Strip Non ASCII
######
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)



######
# Create friendly time string
# @see http://stackoverflow.com/questions/1551382/user-friendly-time-format-in-python
######
def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    now = datetime.now()
    if type(time) is int or type(time) is float:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "*"
        if second_diff < 60:
            return str(second_diff) + "s"
        if second_diff < 120:
            return "m~"
        if second_diff < 3600:
            return str(second_diff / 60) + "m"
        if second_diff < 7200:
            return "h~"
        if second_diff < 86400:
            return str(second_diff / 3600) + "h"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff / 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff / 30) + " months ago"
    return str(day_diff / 365) + " years ago"