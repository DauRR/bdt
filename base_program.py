import random

def is_prime(x: int) -> bool:
    delim = 2
    while x % delim != 0:
        delim += 1
    return x == delim

def primes(count: int) -> list[int]:
    prime_numbers_list = []
    i = 2
    while len(prime_numbers_list) != count:
        if is_prime(i) == True:
            prime_numbers_list.append(i)
        i += 1
    return prime_numbers_list

def checksum(x: list[int]) -> int:
    random.seed(100)
    random.shuffle(x)
    control_sum = 0
    for number in x:
        number += control_sum
        number *= 113
        control_sum = number % 10000007
    return control_sum

def pipeline() -> int:
    return checksum(primes(1000))

def main():
    print(pipeline())

if __name__ == '__main__':
    main()
