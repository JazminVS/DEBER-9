import time
hour=0
seg=0
m=0

for hour in range (0,24):
	for m in range (0,60):
		for seg in range (0,60):
			print (str(hour)+":"+str(m)+":"+str(seg))
			time.sleep(1)

	
