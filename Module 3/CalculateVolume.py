length = float(input("Please enter the length: "))
width = float(input("Please enter the width: "))
height = float(input("Please enter the height: "))

volume = (length * width * height)
volume = (volume * 0.1) + volume

print("Volume with 1% :", volume)
