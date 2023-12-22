# description: LRI python bootcamp example module

my_var = 4

def power(x, n):
    return x ** (n)


def contact(first_name, domain="ccf.org"):
    '''
    prints the given name
    '''
    email = f"{first_name}@{domain}"
    print(email)

def multiply2(a, b=1):
    '''
    function to multiply two numbers
    '''
    return a * b