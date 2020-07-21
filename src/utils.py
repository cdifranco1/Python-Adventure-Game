import sys
import time

def slow_print(*textlines, newline=True):
    for l in textlines:
        if newline:
            print("\n")
        for x in l:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(0.005)