



#Q3 Falling Factorial
def falling(n, k):
    """Compute the falling factorial of n to depth k."""
    result = 1  
    
    while k > 0:
        result *= n  
        n -= 1      
        k -= 1      
    
    return result


print(falling(6, 3)) 
print(falling(4, 3))  
print(falling(4, 1)) 
print(falling(4, 0))

120
24
4
1

#Q4 Sum Digits
def sum_digits(y):
    total = 0

    while y > 0:
        remainder = y % 10   
        total += remainder   
        y //= 10             

    return total

# Test cases
print(sum_digits(10))        
print(sum_digits(4224))      
print(sum_digits(1234567890))
a = sum_digits(123)
print(a)                     




