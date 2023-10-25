from base_program import is_prime, primes, checksum, pipeline

def test_is_prime():
    assert is_prime(5) == True

def test_primes():
    primes_list = primes(1000)
    length = 0
    for num in primes_list:
        if is_prime(num) == True:
            length += 1
    assert length == 1000

def test_checksum():
    assert checksum(primes(1000)) == 7785816

def test_pipeline():
    assert pipeline() == 7785816

def main():
    test_is_prime()
    test_primes()
    test_checksum()
    test_pipeline

if __name__ == '__main__':
    main()
