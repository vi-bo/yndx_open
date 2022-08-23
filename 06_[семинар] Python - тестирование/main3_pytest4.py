import pytest

@pytest.fixture
def init_db():
    print('\ninit_db')

@pytest.fixture
def run_migrations(init_db):
    print('run_migrations')

@pytest.fixture
def superuser(run_migrations):
    print('create superuser')

def test_one(superuser):
    print('test one')

def test_two(run_migrations):
    print('test two')