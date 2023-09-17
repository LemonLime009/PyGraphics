class matrix():

  def __init__(self):
    self.a = [" ", " ", " ", " ", " "]
    self.b = [" ", " ", " ", " ", " "]
    self.c = [" ", " ", " ", " ", " "]
    self.d = [" ", " ", " ", " ", " "]
    self.e = [" ", " ", " ", " ", " "]

  def update(self):
    print(f"{self.a[0]}{self.a[1]}{self.a[2]}{self.a[3]}{self.a[4]}")
    print(f"{self.b[0]}{self.b[1]}{self.b[2]}{self.b[3]}{self.b[4]}")
    print(f"{self.c[0]}{self.c[1]}{self.c[2]}{self.c[3]}{self.c[4]}")
    print(f"{self.d[0]}{self.d[1]}{self.d[2]}{self.d[3]}{self.d[4]}")
    print(f"{self.e[0]}{self.e[1]}{self.e[2]}{self.e[3]}{self.e[4]}")

  def rectangle(self, length, width):
    lines = 0
    while lines != width:
      lines += 1
      for i in range(length):
        if lines == 1:
          self.a[i] = "O"
        elif lines == 2:
          self.b[i] = "O"
        elif lines == 3:
          self.c[i] = "O"
        elif lines == 4:
          self.d[i] = "O"
        elif lines == 5:
          self.e[i] = "O"
