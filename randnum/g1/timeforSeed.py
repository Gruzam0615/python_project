from datetime import datetime, timedelta, timezone

def TimeForSeed() :
    '''
    now - nDay == 어제
    현재시간서 nDay timedelta(days=n) 만큼 감소
    now() - timedelta(days=1)은 현재시간보다 하루이전 값을 출력
    '''
    now = datetime.now()

    '''
    기준일 선언을 위한 값
    값이 -5 는 5일 전
    값이 5 는 5일 후
    '''
    timedeltaValue = 0

    # 기준일 선언
    standardDay = now + timedelta(timedeltaValue)
    timeZoneName = timezone(timedelta(hours=9))

    # time = datetime(standardDay.year, standardDay.month, standardDay.day, standardDay.hour, standardDay.minute, standardDay.second, standardDay.microsecond, tzinfo=timeZoneName)
    time = datetime(standardDay.year, standardDay.month, standardDay.day, standardDay.hour, standardDay.minute, standardDay.second, standardDay.microsecond)

    return time

