#!/usr/bin/env python

import argparse

config_file_locations = [
    '~/.tweetmybot.yaml',
    '/etc/tweetmybot.yaml']

args_parser = argparse.ArgumentParser(
    description="Controls a robot by accepting instructions from twitter")

args_parser.add_argument(
    'config',
    type=str,
    help='Path to a config file with some or all of the options specified')

args_parser.add_argument(
    'api_key',
    type=str,
    help='The twitter OAuth API key')
args_parser.add_argument(
    'api_secret',
    type=str,
    help='The twitter OAuth API secret')
args_parser.add_argument(
    'access_token_key',
    type=str,
    help='The twitter OAuth access token key')
args_parser.add_argument(
    'access_token_secret',
    type=str,
    help='The twitter OAuth access token secret')


args_parser.add_argument(
    'serial_device',
    type=str,
    help='The serial device to send commands to')
args_parser.add_argument(
    'local_control',
    type=bool,
    help='Control the motors locally instead of sending commands via serial')
args_parser.add_argument(
    'fake_control',
    type=bool,
    help='Control the motors locally instead of sending commands via serial')

args_parser.add_argument(
    'raspi_camera',
    type=str,
    help='Use the Raspberry Pi camera to take pictures')
args_parser.add_argument(
    'usb_camera',
    type=str,
    help='Use a usb webcam to take pictures')
