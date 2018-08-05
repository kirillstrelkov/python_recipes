from datetime import datetime


def timestamp2isotime(timestamp):
    return datetime.utcfromtimestamp(timestamp/1000.0).isoformat()[:-3]


def get_timestamp(date=datetime.now()):
    epoch = datetime.utcfromtimestamp(0)
    return int((date - epoch).total_seconds() * 1000)  # milliseconds since epoch


def get_ms_since_epoch(time_as_str, time_format='%d-%m-%Y %H:%M:%S.%f'):
    msg_time = datetime.strptime(time_as_str, time_format)
    epoch = datetime.utcfromtimestamp(0)

    return int((msg_time - epoch).total_seconds() * 1000)  # milliseconds since epoch
