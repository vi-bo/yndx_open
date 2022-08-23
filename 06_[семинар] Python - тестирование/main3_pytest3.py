import pytest

@pytest.fixture(scope='module')
def call_me_once_use_when_needed():
    print('\ncall me once use when needed')

@pytest.fixture()
def call_me_every_time():
    print('call me every time')

@pytest.fixture(autouse=True)
def call_me_everywhere():
    print('YOU\'LL CALL ME EVEN IF YOU DON\'T WANNA TO')

def test_one(call_me_once_use_when_needed, call_me_every_time):
    print('test one')

def test_two(call_me_once_use_when_needed, call_me_every_time):
    print('test two')