import myModules 

myTime = myModules.create_time()
print("create time ", myTime)

print("Local time ", myModules.output_local_time(myTime))
input("Press any key to continue: ")
myTime2 = myModules.create_time()
print("The time difference ", myModules.calculate_difference(myTime, myTime2))

print("Generate random ", myModules.generate_random(10))