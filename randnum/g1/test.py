from datetime import datetime, timedelta, timezone

now = datetime.now()

timedeltaValue = -5

standardDay = now + timedelta(timedeltaValue)

KST = timezone(timedelta(hours=9))

for i in range(6):
    time = datetime(standardDay.year, standardDay.month, standardDay.day, standardDay.hour, standardDay.minute + i, standardDay.second, tzinfo=KST)
    print("time3:", time)
