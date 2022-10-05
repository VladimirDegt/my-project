def make_readable(seconds):
    if seconds > 0:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return '{:02}:{:02}:{:02}'.format(h, m, s)

    return f"00:00:00"


print(make_readable(5))
