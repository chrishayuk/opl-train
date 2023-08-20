Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Write a Python program that prints the first 10 Fibonacci numbers.

### Response:def Fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 

print("First 10 Fibonacci numbers:") 
for i in range(1,11): 
    print(Fibonacci(i), end=' ')</s>