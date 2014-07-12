from threading import Thread
import time


class DummyFeedback(Thread):
    def __init__(self, feedback_queue):
        Thread.__init__(self)
        self.feedback_queue = feedback_queue
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            time.sleep(0)
        print "Stopping dummy feedback"
