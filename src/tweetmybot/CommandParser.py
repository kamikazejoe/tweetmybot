from threading import Thread
import time
from Queue import Empty


class CommandParser(Thread):
    def __init__(self, command_queue, action_queue, feedback_queue):
        Thread.__init__(self)
        self.command_queue = command_queue
        self.action_queue = action_queue
        self.feedback_queue = feedback_queue
        self.running = True

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            try:
                command = self.command_queue.get_nowait()

                action = self.parse_command(command)

                if action is not None:
                    self.action_queue.put(action)
                    self.feedback_queue.put(action)

            except Empty:
                pass

            time.sleep(0)
        print "Stopping command parser"

    def parse_command(self, command_string):
        command_string = command_string.upper()

        command = None
        direction = None
        duration = 10

        if "FORWARD" in command_string:
            command = "move"
            direction = 1
        elif "BACKWARDS" in command_string:
            command = "move"
            direction = 2
        elif "LEFT" in command_string:
            command = "move"
            direction = 3
        elif "RIGHT" in command_string:
            command = "move"
            direction = 4

        if command is not None:
            self.action_queue.put((command, direction, duration))
            self.feedback_queue.put((command, direction, duration))
