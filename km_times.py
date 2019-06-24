#! /usr/bin/env python3

import math
import sys


def hoursToHHMMSS(hours):
    hh = math.trunc(hours)
    hours -= hh
    mm = math.trunc(hours * 60.0)
    hours -= mm / 60.0
    ss = round(hours * 60.0 * 60.0)
    return (hh, mm, ss)

if __name__ == '__main__':
    if len(sys.argv) != 1 + 1:
        print("Usage:", sys.argv[0], "<time for 1 km mm:ss>")
        sys.exit(1)
    else:
        (mm, ss) = sys.argv[1].split(':')
        km_time = (int(mm) + int(ss) / 60.0) / 60.0

    for km in range(1, 43):
        hours = km * km_time
        (hh, mm, ss) = hoursToHHMMSS(hours)
        print("km %2d   %02d:%02d:%02d" % (km, hh, mm, ss))
