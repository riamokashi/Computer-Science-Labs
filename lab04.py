def leap_year(year):
    year = int(year)
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    elif year % 4 == 0:  
        return True


def rotate(s,n):
    s = str(s)
    n = int(n)
    return s[-n:] + s[:-n]

def digit_count(n):
    n = str(n)
    zero_count = 0
    odd_count = 0
    even_count = 0
    for x in n:
        if x == ".":
            break
        if not int(x) % 2 and int(x) != 0:            
        	    even_count += 1
        if int(x) != 0 and int(x) % 2:
        	     odd_count += 1 
    if n.count('0'):
        zero_count = n.count('0')    
    if n[:-2] == "." and n.count('0'):
        zero_count = zero_count - 1

    return (even_count, odd_count, zero_count)
                
print(digit_count(1234567890123))

def float_check(s):
    s = str(s)
    if s.count(".") == 2:
        return False
    if s.count(".") == 1:
        return True
    if s.isdigit() == True:
        return True
    else:
        return False 
