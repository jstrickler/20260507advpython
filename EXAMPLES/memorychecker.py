import os
import psutil

class MemoryChecker():
    """
    Callable class to get current memory use of program.

    Instances of this class may be called, at which time
    they will return current memory use.
    """

    def __init__(self, pid):
        self.process = psutil.Process()  # Get PID of current process

    def __call__(self):
        return self.process.memory_info().rss  # Return memory use for PID

if __name__ == '__main__':
    process_id = os.getpid()
    mc = MemoryChecker(process_id)   # mc is a "smart function"
    print(mc())  # can call at any time to get current memory use
    big_list = [1] * 100_000_000
    print(mc())
    del big_list
    print(mc())