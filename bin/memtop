#!/usr/bin/env python

import os
import psutil
import sys

class MemObject(object):
    def __init__(self):
        self.pid = None
        self.mem_usage = None
        self.cmdline = None

    def _linux_get_kernel_thread_name(self):
        # TODO: Check Parent Pid is equal 2
        cmd = 'grep Name: /proc/{0}/status'.format(self.pid)
        data = os.popen(cmd).read()
        th_name = data.split()[-1]
        return "[{0}]".format(th_name)

    def get_kernel_thread_name(self):
        if 'linux' in sys.platform:
            return self._linux_get_kernel_thread_name()
        else:
            return self.cmdline


objs = []


def main():
    pids = psutil.pids()

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
        if cmdline_str == '':
            mem_obj.cmdline = mem_obj.get_kernel_thread_name()
        else:
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
