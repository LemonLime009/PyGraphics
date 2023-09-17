from matrix import matrix
import time

# Initializing display
display = matrix()

# Drawing rectangle (2x3), starting at 2,3
display.rectangle(2,3,2,3)

# Updating screen
display.update()

# Waiting 3 seconds
time.sleep(3)

# Clearing screen
display.clear()
