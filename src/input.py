import keyboard

class Input():
  def startRecording(self):
    self.events = keyboard.record(until="esc")

  def event(self, key, action):
    key = self.key
    for event in self.events:
      if event.event_type == keyboard.key:
        action()
