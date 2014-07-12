from threading import Thread
import time
from Queue import Empty


class Console(Thread):
    def __init__(self, action_queue):
        Thread.__init__(self)
        self.action_queue = action_queue
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            try:
                action = self.action_queue.get_nowait()

                print action

            except Empty:
                pass

            time.sleep(0)

        print "Stopping Console Output"
