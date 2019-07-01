#! /usr/bin/env python3

import math
import sys
import argparse

MARATHON_KM = 42.195
HALF_MARATHON_KM = MARATHON_KM / 2.0


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


def print_time_at_km(km, km_time):
    hours = km * km_time
    (hh, mm, ss) = hours_to_hhmmss(hours)
    print("km %6.3f   %02d:%02d:%02d" % (km, hh, mm, ss))


def fatal(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="A Runner's Calculator", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--km-time", type=str, help="Time for a single km (kilometer) MM:SS", default="6:00")
    parser.add_argument("--marathon", action="store_true", help="Show marathon (" + str(MARATHON_KM) + " km) \
        and half-marathon (" + str(HALF_MARATHON_KM) + " km) times")
    args = parser.parse_args()

    if args.km_time:
        try:
            (mm, ss) = args.km_time.split(':')
            km_time = (int(mm) + int(ss) / 60.0) / 60.0
        except ValueError:
            fatal("Time format must be 'MM:SS'")

        km = 1.0
        while km < 43.0:
            print_time_at_km(km, km_time)
            if args.marathon:
                if math.trunc(km) == math.trunc(HALF_MARATHON_KM):
                    print_time_at_km(HALF_MARATHON_KM, km_time)
                elif math.trunc(km) == math.trunc(MARATHON_KM):
                    print_time_at_km(MARATHON_KM, km_time)
            km += 1.0

if __name__ == '__main__':
    main()
