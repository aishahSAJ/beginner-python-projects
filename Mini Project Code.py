# %%

import time
import csv

# create a new class
# assign value for time and duration
class Stopwatch:
    def __init__(self, start_time, stop_time, duration):
        self.start_time = start_time
        self.stop_time = stop_time
        self.duration = duration

# %%
    def start(self):
        self.start_time = time.time()

#%%
        
    def stop(self):
        self.end_time = time.time()
        self.duration = self.end_time - self.start_time
        with open("stopwatch_log.csv", "a") as log:
            log_writer = csv.writer(log)
            log_writer.writerow([time.ctime(self.end_time), self.duration])
        return self.duration

# %%

    def reset(self):
        self.start_time = 0
        self.end_time = 0
        self.duration = 0

# %%
import time
import csv

class Stopwatch:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.duration = 0
        self.running = False
# %%
    def start(self):
        if self.running:
            print("Stopwatch is already running!")
        else:
            self.running = True
            self.start_time = time.time()
# %%
    def stop(self):
        if not self.running:
            print("Stopwatch is not running!")
        else:
            self.running = False
            self.end_time = time.time()
            self.duration += self.end_time - self.start_time

            # log the event to a csv file
            with open("stopwatch_log.csv", "a") as log:
                log_writer = csv.writer(log)
                log_writer.writerow([time.ctime(self.end_time), self.duration])

            return self.duration
# %%
    def reset(self):
        self.start_time = 0
        self.end_time = 0
        self.duration = 0
        self.running = False
# %%