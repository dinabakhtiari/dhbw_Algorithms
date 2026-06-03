def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)
    
#print(f"Factorial of 3: {recursive_factorial(3)}")   
#print("-----------------------") 
#print(f"Factorial of 5: {recursive_factorial(5)}") 
#print("-----------------------") 
#print(f"Factorial of 6: {recursive_factorial(6)}") 


def loop_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    series = [0, 1]
    
    while len(series) < n:
        next_number = series[-1] + series[-2]
        series.append(next_number)
        
    return series[:n]

#print(f"Fibonacci sequence for n=2: {loop_fibonacci(2)}") 
#print("----------------------------------------") 
#print(f"Fibonacci sequence for n=7: {loop_fibonacci(7)}")


#PART 2 :
# What fundamental piece of recursion is missing from this function?
# The function is missing a Base Case. Without a base case, the function has no condition to stop execution, leading to infinite recursive calls until the computer's memory is exhausted and a RecursionError occurs.
def countdown(n):
    # Base Case: Stop the recursion when n is less than 1
    if n < 1:
        return

    print(n)
    countdown(n - 1)  # Recursive Call

countdown(10)
print("-----------------------") 
countdown(20)