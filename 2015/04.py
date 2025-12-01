import hashlib

def read_file() -> str:
    """
    Reads the secret key from the file as a string

    Returns:
        The secret key as a string
    """
    with open("2015/4.txt", "r") as f:
        for i in f:
            return i

def find_zeroes(secret_key: str, zeros: int) -> int:
    """
    Hashes the secret_key with positive numbers to find hashes begnning with zeros

    Args:
        secret_key: The first half of the hash
        zeros: How many zeros should be at the beginning of the hash

    Returns:
        The smallest positive number that needs to be hashed with the secret key
    """
    for i in range(1, 1000000000):
        hash_value = hashlib.md5((secret_key + str(i)).encode())
        if hash_value.hexdigest()[:zeros] == '0' * zeros:
            return i
    return -1

if __name__ == "__main__":
    secret_key = read_file()
    print("Part 1:", find_zeroes(secret_key, 5))
    print("Part 2:", find_zeroes(secret_key, 6))