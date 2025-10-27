def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# User input
num = int(input("Enter a number: "))
if is_prime(num):
    print("The number is prime.")
else:
    print("The number is not prime.")

# Test cases
assert is_prime(2) == True
assert is_prime(15) == False
assert is_prime(17) == True
