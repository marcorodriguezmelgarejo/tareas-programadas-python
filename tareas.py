import sched
import time

scheduler = sched.scheduler(timefunc=time.time, delayfunc=time.sleep)

scheduler.run()