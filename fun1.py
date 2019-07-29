
def add_number():
    total=0
    for number in range (1,10+1):
        print(number)
        total = total + number
    return(total)   
"""
answer=add_number()
print(answer)
"""
def add_numbers(start,end):
    test=0
    for i in range(start,end+1):
        test+=i
    return(test)
x=add_numbers(1,10)                
print(x)        
