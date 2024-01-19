from django.utils.timezone import localtime

def get_duration(visit):
    time_now = localtime()
    if visit.leaved_at == None:
        return time_now - visit.entered_at
    return visit.leaved_at - visit.entered_at


def is_visits_long(visit, minutes=60):
    return get_duration(visit).total_seconds() > minutes * 60


def format_duration(duration):
    total_seconds = duration.seconds
    hours, remainder = divmod(total_seconds, 60 * 60)
    minutes, seconds = divmod(remainder, 60)
    return f'{hours:02}:{minutes:02}:{seconds:02}'