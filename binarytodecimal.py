def BinaryToDecimal(binary):
    decimal = 0 # Decimal, this is what we return
    count = 0 # count for power
    while binary: # while binary is not equal to zero
        digit = binary % 10 # digit = binary mod 10 (10 for decimal)
        decimal = decimal + digit * pow(2 , count)
        binary = binary//10 # integer divide by 10
        count += 1 # add 1 to count for power operator
    return decimal
binary = int(input("Enter a binary number: "))
print(BinaryToDecimal(binary))

