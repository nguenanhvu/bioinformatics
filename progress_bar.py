import sys
import time

def main():
	i = 1
	while i<=1000000001:
		sys.stdout.write('\r['+str(i)+']')
		#sys.stdout.flush()
		i+=1
	print

main()
