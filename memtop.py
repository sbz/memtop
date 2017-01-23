#!/usr/bin/env python

import psutil
import sys

pids = psutil.pids()

class MemObject(object):
    def __init__(self):
        self.pid = None
        self.mem_usage = None
        self.cmdline = None

objs = []


def main():
    for p in pids:
        process = psutil.Process(pid=p)
        pid = process.pid
        # Only Resident Set Size (RSS)
        # https://en.wikipedia.org/wiki/Resident_set_size
        percent = '{0:2.1f}'.format(process.memory_percent(memtype="rss"))
        cmdline_str = ' '.join(process.cmdline())
        cmdline_str = cmdline_str[:70] + '...' if len(cmdline_str) > 70 \
                    else cmdline_str
        mem_obj = MemObject()
        mem_obj.pid = pid
        mem_obj.mem_usage = float(percent)
        mem_obj.cmdline = cmdline_str
        objs.append(mem_obj)

    header = "Process (Pid) | Memory Used (%) | Command (cmdline)"
    print(header)
    print("-"*len(header))
    for m in sorted(objs, key=lambda x: x.mem_usage, reverse=True):
        print("{0:^14} {1:^16} {2:^20}".format(m.pid, m.mem_usage, m.cmdline))

    return 0

if __name__ == '__main__':
    sys.exit(main())
