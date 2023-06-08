#!/usr/bin/python3
"""
Recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces.
"""
from requests import get


def count_words(subreddit, word_list, next="", counters={}):
    """
    Hot posts by subreddit in a recursive way with sorted count
    """
    headers = {"user-agent": "kyeeh"}
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, next)
    if len(counters) == 0:
        for word in word_list:
            counters[word] = 0
    try:
        req_data = get(url, headers=headers, allow_redirects=False).json()
        hot_posts = req_data["data"]["children"]
        for post in hot_posts:
            for word in word_list:
                counters[word] += post["data"]["title"].lower(
                    ).split(' ').count(word.lower())
        next = req_data["data"]["after"]
        if next:
            count_words(subreddit, word_list, next, counters)
        else:
            sorted_counters = sorted(sorted(counters.items(
                ), key=lambda t: t[0]), key=lambda t: (t[1]), reverse=True)
            for (key, value) in sorted_counters:
                if value != 0:
                    print('{}: {}'.format(key, value))
    except Exception:
        return (None)
