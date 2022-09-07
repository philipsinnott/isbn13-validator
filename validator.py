def isbn13(n):
    # Save check digit
    check = n % 10
    # Convert each digit in the integer to a respective element in a list
    n_list = [int(x) for x in str(n)]
    # Exclude the check digit
    n_list = n_list[:12]

    counter = 1
    total = 0

    # Loop through each element and add its value to the total
    # Multiply every second element by 3
    for i in n_list:
        if counter % 2 == 0:
            total += 3 * i
        else:
            total += i
        counter += 1

    # Do mod 10 division on the total and save remainder
    rem = total % 10
    # If the remainder is zero, the check digit is also zero
    if (rem == 0 and check == 0):
        print("Valid")
    # If the remainder isn't zero, we subtract it with 10 and compare the result with the check digit
    if (10 - rem == check):
        return "Valid"
    else:
        return "Invalid"