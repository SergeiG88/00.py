def is_prime(func):

    def wrapper(*n):
        print('Простое')
        func(*n)
        # print('Составное')
    return wrapper

@is_prime
def sum_three(x,y,z):
    print(x + y + z)

sum_three(2,3,6)






