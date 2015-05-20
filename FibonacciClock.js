var t=[5,3,2,1,1];
var output_hour=[0,0,0,0,0];
var output_minute=[0,0,0,0,0];
var output_colour=[0,0,0,0,0];
var i;
function minute(a)
{
	var sum=0;
	var i=0;
	while(sum<a[1])
	{
		if((sum+t[i]*5)<=a[1])
		{
			output_minute[i]=t[i];
			sum+=t[i]*5;
		}
		i+=1;
	}
	return a;
}
function normalise_min(a)
{
	if(a[1]%5>2)
		a[1]+= (5-a[1]%5);
	else
		a[1]-= a[1]%5;
	return a;
}
function hour(a)
{
	var sum=0;
	var i=0;
	while(sum<a[0])
	{
		if(sum+t[i]<=a[0])
		{
			output_hour[i]=t[i];
			sum+=t[i];
		}
		i+=1;
	}
	return a;
}
function main() 
{
	var d = new Date(); 
		a1=d.getHours();
		if(a1===0)
			a1=12;
		else
			a1=a1%12;
		a2=d.getMinutes();  
		var a=[a1,a2];
		a=hour(a);
    	a=normalise_min(a);
    	a=minute(a);
    	var i;
    	for (i=0; i<5; i++) 
		{        
			if(output_hour[i]===0 && output_minute[i]===0)
    			output_colour[i]='W';
    		else if(output_minute[i]===output_hour[i])
    			output_colour[i]='G';
    		else if(output_hour[i]===0)
    			output_colour[i]='B';
    		else if(output_minute[i]===0)
    			output_colour[i]='R';   
		}   
	console.log(output_colour);	
}
function myFunction() {
    myVar = setInterval(main, 5000);
}
myFunction();
