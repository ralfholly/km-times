#! /usr/bin/env python3

import math
import sys


def hours_to_hhmmss(hours):
    hh = math.trunc(hours)
    hours -= hh
    mm = math.trunc(hours * 60.0)
    hours -= mm / 60.0
    secs = hours * 60.0 * 60.0
    ss = math.trunc(hours * 60.0 * 60.0)
    if secs - ss >= 0.5:
        ss += 1
        if ss >= 60:
            ss = 0
            mm += 1
            if mm >= 60:
                mm = 0
                hh += 1
    return (hh, mm, ss)


def main():
    if len(sys.argv) != 1 + 1:
        print("Usage:", sys.argv[0], "<time for 1 km mm:ss>")
        sys.exit(1)
    else:
        (mm, ss) = sys.argv[1].split(':')
        km_time = (int(mm) + int(ss) / 60.0) / 60.0

    for km in range(1, 43):
        hours = km * km_time
        (hh, mm, ss) = hours_to_hhmmss(hours)
        print("km %2d   %02d:%02d:%02d" % (km, hh, mm, ss))


if __name__ == '__main__':
    main()
