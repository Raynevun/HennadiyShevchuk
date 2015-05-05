# example how to run file from cmd:
# summarize_beacon.py --time_from 3 months 1 day 1 hour ago --time_to 1 month 1 hour ago

import argparse
import datetime
from time import gmtime, strftime
import time
import requests
from xml.etree import ElementTree

def get_args():
    parser = argparse.ArgumentParser(
        description='Script retrieves time from the given url')
    parser.add_argument(
        '-f', '--time_from', type=str, help='Time from ',nargs='*')
    parser.add_argument(
        '-t', '--time_to', type=str, help='Time to', nargs='*')
    args = parser.parse_args()
    time_from = args.time_from
    time_to = args.time_to
    return time_from, time_to

time_from, time_to = get_args()

def parse_time(time_from):
    months,days,hours = 0,0,0
    names=time_from[1::2]
    numbers = time_from[0::2]
    for i,j in enumerate(names):
        if j.startswith('m'):
            months=int(numbers[i])
        elif j.startswith('d'):
            days=int(numbers[i])
        elif j.startswith('h'):
            hours=int(numbers[i])
    year = int(strftime("%Y", gmtime()))
    month = int(strftime("%m", gmtime())) - months
    day = int(strftime("%d", gmtime())) - days
    hour = int(strftime("%H", gmtime()))-hours
    minute = int(strftime("%M", gmtime()))
    dt = datetime.datetime(year,months,day,hour,minute)
    return time.mktime(dt.timetuple())

def send_request(timestamp):
    url = 'https://beacon.nist.gov/rest/record/%s'%int(timestamp)
    r = requests.get(url)
    return r.content

timestamp_one = int(parse_time(time_from))
timestamp_two = int(parse_time(time_to))

def parse_response(content):
    tree = ElementTree.fromstring(send_request(content))
    return tree[6].text

x = parse_response(timestamp_one) +parse_response(timestamp_two)

def get_result(line):
        for i in set(list(line)):
            print "{0:s},{1:d}".format(i,line.count(i))
get_result(x)


