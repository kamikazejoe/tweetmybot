from threading import Thread
import time


class CommandParser(Thread):
    def __init__(self, command_queue, action_queue, feedback_queue):
        Thread.__init__(self)
        self.command_queue = command_queue
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            time.sleep(0)
        print "Stopping command parser"
