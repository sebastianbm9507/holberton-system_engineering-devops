#!/usr/bin/python3
""" Consume reddit API """

import requests


def number_of_subscribers(subreddit):
    """ Get number_of_subscribers """
    URL = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'PostmanRuntime/7.26.5'}
    data = requests.get(URL, headers=header).json()
    result = None
    if data.get('error') == 404:
        result = 0
    else:
        data1 = data.get('data').get('subscribers')
        result = data1
    return result
