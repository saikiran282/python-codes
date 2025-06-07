def fun(n):
    
    if n==1:
        print(n)
        return
    print(n)
    fun(n-1)
    print(n)

fun(5)
