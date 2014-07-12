#!/usr/bin/env python

from distutils.core import setup

setup(
    name='TweetMyBot',
    scripts=['scripts/tweetmybot'],
    packages=[
        'tweetmybot',
        'tweetmybot.input',
        'tweetmybot.output',
        'tweetmybot.feedback',
    ],
    package_dir={
        '': 'src',
    },
    version='1.0.0',
    description='Controller for a twitter controlled robot',
    author='Joe Cathell',
    author_email='kamikazejoe@gmail.com')
