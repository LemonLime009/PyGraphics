from matrix import Matrix
from clock import Clock
from console import Console
from input import Input

display = Matrix()
clock = Clock(60)
console = Console()
input = Input()

def action():
    display.rectangle(4,4,0,0)
    display.update()

while True:
    input.detect("a", action())
