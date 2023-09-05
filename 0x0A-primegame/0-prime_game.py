def isWinner(x, nums):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def calculate_primes():
        primes = []
        for i in range(2, 10001):
            if is_prime(i):
                primes.append(i)
        return primes

    def calculate_winner(n):
        primes = calculate_primes()
        if n < 2:
            return "Ben"
        if n % 2 == 0:
            return "Maria"
        return "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = calculate_winner(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage
x = 3
nums = [4, 5, 1]
print("Winner: {}".format(isWinner(x, nums)))

