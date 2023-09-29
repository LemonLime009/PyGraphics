import pygame

class Input:
    def __init__(self, start):
        self.start = start
    
    def detect(self, key, action):
        keys = pygame.key.get_pressed()

        if keys[key]:
            action()