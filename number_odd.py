#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int=3333
#Print the number of odd digits in the variable "var_int".
print(4-var_int//1000%2+1-var_int//100%2+1-var_int//10%2+1-var_int%2+1)
