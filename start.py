import time
from labylib import Cape

cookie = input("Paste your PHPSESSID here:\n")

vis = Cape.Visibility(cookie)
temp = Cape.Template(cookie)

i = False

print("\nRunning..")
while(True):
	if(i):
		temp.update("christmas2010")
	else:
		temp.update("newyear")

	i = not i
	vis.update("show")
	time.sleep(1)