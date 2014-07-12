from threading import Thread
import time


class CommandLine(Thread):
    def __init__(self, command_queue):
        Thread.__init__(self)
        self.command_queue = command_queue
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            self.command_queue.put(raw_input('Command: '))
            time.sleep(0)
        print "Stopping command line input"
