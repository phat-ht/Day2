def printdiamond(height):

  # top half diamond
  for i in range(1, height + 1):
    spaces = ' ' * (height - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

  # Bottom half diamond
  for i in range(height - 1, 0, -1):
    spaces = ' ' * (height - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

# Input height
height = int(input("Enter the height of the diamond: "))

# Print diamond
printdiamond(height)
