def generate_prime_numbers(start,end):
    prime_numbers = []
    for number in range(start,end+1):
        if number > 1:
            for item in range(2, int(number/2)+1):
                if (number % item) == 0:
                    break
            else:
                prime_numbers.append(number)
    return prime_numbers


prime_numbers = generate_prime_numbers(10,50)
print(prime_numbers)
            
