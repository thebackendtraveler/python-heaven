minutes = int(input("Please enter the amount of (whole) minutes you have worked this month: "))

hours = int(minutes / 60)
minutes = int(minutes % 60)
days = int(hours / 8)
hours = int(hours % 8)

print("{0}:{1}:{2}".format(days, hours, minutes))