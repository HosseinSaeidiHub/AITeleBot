import pytest
from bot.core import BotCore

def test_botcore_init():
    core = BotCore("dummy-token")
    assert core.app is not None
