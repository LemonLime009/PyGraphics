from matrix import Matrix
from clock import Clock
from console import Console
from input import Input

display = Matrix()
clock = Clock(120)
console = Console()
input = Input()

gameCondition = True

def rectangle():
    display.clear()
    display.rectangle(2,2,2,2)
    display.update()

while gameCondition:
    clock.startTicker()

    display.clear()
    display.rectangle(4,4,0,0)
    display.update()

    input.detect("K_LEFT", rectangle())

    clock.endTicker()
