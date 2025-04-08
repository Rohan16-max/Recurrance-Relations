
# Question:-

def myfunction1(n):
    if(n>0):
        return
    for i in range (0,n+1):
        print("Codingal")
    myfunction1(n/2)
    myfunction1(n/3)


def myfunction2(n):
    if(n<=1):
         return 
    print("Codingal") 

    myfunction2(n-1)

# Answer :-


def myfunction1(n):
    if n <= 0:
        return
    # The loop part (O(n))
    for i in range(0, n + 1):
        print("Codingal")
    
    # Recursive calls (T(n/2) and T(n/3))
    myfunction1(n / 2)
    myfunction1(n / 3)




def myfunction2(n):
    if n <= 1:
        return
    # This is constant time (O(1))
    print("Codingal")
    
    # Recursive call (T(n - 1))
    myfunction2(n - 1)


