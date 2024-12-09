import pytest

from tasks.database import Database


@pytest.fixture(scope='session')
def base():
    return Database()