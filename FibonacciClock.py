from time import ctime
import time
t=[5,3,2,1,1]
output_hour=[0,0,0,0,0]
output_minute=[0,0,0,0,0]
output_colour=[0,0,0,0,0]
# OUTPUT FORMAT- output_colour, a list of length 5, the output is the colour on the respective sized square tile. t shows the sizes.
def hour(a):
	sum=0
	i=0
	while(sum<a[0]):
		if(sum+t[i]<=a[0]):
			output_hour[i]=t[i]
			sum+=t[i]
		i+=1
	return a
def minute(a):

	sum=0
	i=0
	while(sum<a[1]):
		if((sum+t[i]*5)<=a[1]):
			output_minute[i]=t[i]
			sum+=t[i]*5
		i+=1
	return a
def normalise_min(a):
	if(a[1]%5>2):
		a[1]+= (5-a[1]%5)
	else:
		a[1]-= a[1]%5
	return a
def main():
    while True:
    	a= ctime().split()[3]
    	a=a.split(":")
    	a[0]=int(a[0])%12
    	if(int(a[0])==0):
    		a[0]=12
    	a[1]=int(a[1])
    	a[2]=int(a[2])
    	a=hour(a)
    	a=normalise_min(a)
    	a=minute(a)
    	for i in range(0,5):
    		if(output_hour[i]==0 and output_minute[i]==0):
    			output_colour[i]='W'
    		elif(output_minute[i]==output_hour[i] and output_minute[i]!=0 and output_hour[i]!=0):
    			output_colour[i]='G'
    		elif(output_hour[i]==0):
    			output_colour[i]='B'
    		elif(output_minute[i]==0):
    			output_colour[i]='R'
    	print a,output_hour,output_minute,output_colour

        time.sleep(5) #1 minute
 
if __name__ == "__main__":
    main()
