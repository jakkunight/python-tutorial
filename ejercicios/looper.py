#!/usr/bin/python

end = False
while(end != True):
	ans = input("End? [Y/n]")
	while(ans != "y" and ans != "n" and ans != "Y" and ans != "N"):
		ans = input("End? [Y/n]")
	if(ans == "N" or ans == "n"):
		end = False
	else:
		end = True
