#!/usr/bin/env python

import sys
from time import sleep

def bePatient(name, step, seconds):
    """Display ``name`` and ``step`` N times, and wait 0.5 second
    in between. N being equal to seconds / 0.5.
    """
    timestepInMs = 0.5
    elapsed = 0.0
    for idx in range(1, int(seconds / timestepInMs)):
        sleep(timestepInMs)
        elapsed = elapsed + timestepInMs
        print("[%s] [%s] is waiting %ss [%s/%s]" % (name, step, timestepInMs, elapsed, seconds))

if __name__ == '__main__':
    if len(sys.argv) != 4:
        raise Exception("Missing parameters ! - Usage: %s <name> <seconds>" % sys.argv[0])
    name = sys.argv[1]
    step = sys.argv[2]
    seconds = int(sys.argv[3])
    bePatient(name, step, seconds)

