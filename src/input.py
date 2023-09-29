import keyboard

class Input:
  def detect(self, key, action):
    if keyboard.is_pressed(key):
      action()
      break
