import time


class Clock():

  def __init__(self, fps):
    self.fps = fps
    self.frame_duration = 1 / self.fps

  def startTicker(self):
    self.startTime = time.time()

  def endTicker(self):
    self.exeTime = time.time() - self.startTime
    self.remainingTime = self.frame_duration - self.exeTime
    if self.remainingTime > 0:
      time.sleep(self.remainingTime)
