def DecToBin(number): # number is input, binary is output.
  binary = []
  print(hex(id(number)))
  if number.isdecimal(): # if statement checks if the value of n is decimal to prevent text from being entered and causing issues.
    number = int(number); # now that we definitively know n is a valid integer we can explicitly convert it to an integer and avoid runtime error.
    while number:binary.append(number % 2);number >>= 1; # while n, append the modulo of n (our input) to b - the list containing the binary output. then bitshift right by one place, as we took one place from the input and moved it to out.
    binary.reverse();binary=''.join(map(str, binary));return(int(binary)); # reverse b to make it correct binary, convert to integer using join then return b as an integer so further operations can be used on it. 
print(DecToBin(input("Enter a number: ")))


