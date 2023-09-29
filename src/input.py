import pygame

pygame.init()

class Input:
  def acceptInput(self, key, action):
    keysPressed = pygame.key.get_pressed()
    if keysPressed[self.key]:
      self.action()
