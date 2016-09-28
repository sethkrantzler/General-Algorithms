#A function that returns the Fibonacci series for any number

def fibonacci(number):
    if number==0:
        return number
    elif number==1:
        return number
    elif number<0:
        print "Please Enter a number greater than or equal to zero"
    elif type(number) is not int:
        print "Please Enter a number greater than or equal to zero"
    else:
        return fibonacci(number-1)+fibonacci(number-2)





 def fibonacci (num):
	Fib1=0
	Fib2=1
	fibValue=0
	if num ==0:
		return Fib1
	if num ==1:
		return Fib2

	for i in range(2,num):
		fibValue = fib1 + fib2
		fib1 = fib2
		fib2=fib2+fib1
	
	return fibValue
