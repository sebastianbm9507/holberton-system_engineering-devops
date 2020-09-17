#!/usr/bin/python3
""" Consume reddit API """

import requests


def top_ten(subreddit):
    """ Get number_of_subscribers """
    URL = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    header = {'User-Agent': 'PostmanRuntime/7.26.5'}
    data = requests.get(URL, headers=header).json()
    if data.get('error') == 404:
        print(None)
    else:
        detailed_data = data.get('data').get('children')
        for index, each_dict in enumerate(detailed_data):
            if index == 10:
                break
            print(each_dict.get('data').get('title'))
