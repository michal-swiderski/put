from math import floor


def sizeof_fmt(num, suffix='B'):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Yi', suffix)


def to_coords(shape, n):
    height, width, channels = shape

    k = n % channels
    j = floor(n / channels) % width
    i = floor(n / channels / width) % height
    return i, j, k
