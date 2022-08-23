from freezegun import freeze_time
import datetime

#Freeze time for a pytest test:

@freeze_time("2022-01-14")
def test():
    now = datetime.datetime.now()
    assert now == datetime.datetime(2022, 1, 14)