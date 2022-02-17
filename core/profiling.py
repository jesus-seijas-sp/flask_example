import cProfile
import pstats
import time
from io import StringIO

class Logs:
    def __init__(self):
        self.logs = "None"

    def set(self, value):
        self.logs = value

    def get(self):
        return self.logs

logs = Logs()

def startProfiling():
    start = time.time()
    pr = cProfile.Profile()
    pr.enable()
    return {"start": start, "pr": pr}


def stopProfiling(prof):
    print('START PROFILING')
    pr = prof["pr"]
    start = prof["start"]
    pr.disable()
    s = StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
    ps.print_stats()
    end = time.time()
    elapsed = end - start
    logs.set(s.getvalue() + "\nTOTAL ELAPSED TIME: {}\n".format(elapsed))
    # print(lastlogs)
