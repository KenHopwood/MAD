__author__ = 'kenhopwood'

# EWC Main
# 25-JAN-2016
# K.Hopwood
# Copyright (c) 2016 All rights reserved.

from Task_hour import Task_hour
import eyeo
from Task_second import Task_second
import time
from Task_flow import Task_flow
import webserver


def main():
    # init I/O
    #eyeo.init_io()

    print "starting flow count task"
    t_f = Task_flow()
    t_f.setName('t_f')

    print "starting second task"
    t_v = Task_second()
    t_v.setName('t_v')

    print "starting hour task"
    t_h = Task_hour()
    t_h.setName('t_h')

    # start threads
    t_f.start()
    t_v.start()
    t_h.start()

    """
    opts = webserver.getopts()
    if opts.daemonize:
        webserver.daemonize(opts)
    webserver.logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                                  level=webserver.get_logging_level(opts))
    webserver.httpd(opts)
    """

    loop_cnt = 0
    print "start loop"
    # Loop indefinitely
    while True:
        loop_cnt += 1
        print loop_cnt
        time.sleep(60)
        # web server

    # Ask threads to die and wait for them to do it
    t_f.join()
    t_v.join()
    t_h.join()
    return


if __name__ == '__main__':
    main()
