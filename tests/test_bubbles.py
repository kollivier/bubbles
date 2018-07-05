import pytest
import os
from slackclient import SlackClient
import pdb
import bubbles
from tests.test_fake_slack import fake_user_message

# a few example tests

def test_minutes():
    words = ['m', 'min', 'minute', 'minutes']
    for word in words:
        message = fake_user_message("@bubbles in 3 {} okay".format(word))
        assert bubbles.understand_message(message).get('minutes') == 3

    message = fake_user_message("@bubbles in 3 millenia")
    assert bubbles.understand_message(message).get('minutes') == 0

def test_seconds():
    words = ['s', 'sec', 'second', 'seconds']
    for word in words:
        message = fake_user_message("@bubbles in 3 {} okay".format(word))
        assert bubbles.understand_message(message).get('seconds') == 3

    message = fake_user_message("@bubbles in 3 sarlocs")
    assert bubbles.understand_message(message).get('seconds') == 0

def test_hours():
    words = ['h', 'hour', 'hours']
    for word in words:
        message = fake_user_message("@bubbles in 3 {} okay".format(word))
        assert bubbles.understand_message(message).get('hours') == 3

    message = fake_user_message("@bubbles in 3 hamburgers")
    assert bubbles.understand_message(message).get('hours') == 0

def test_group_size():
    message = fake_user_message("@bubbles of 5")
    assert bubbles.understand_message(message).get('size') == 5

def test_group_tabulation():
    message = fake_user_message("@bubbles of 2 in 10s")
    size = bubbles.understand_message(message).get('size')
    users = ['a','b','c','d','e','f','g']
    groups = bubbles.tabulate_bubbles_for_users(users, size)
    print(groups)

    assert True

