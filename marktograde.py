def marktograde(m):
  grade = ""
  if m>=70:grade="A"
  elif m>=60 and m<=69:grade="B"
  elif m>=50 and m<59:grade="C"
  elif m>=40 and m<=49:grade="D"
  return(grade)
mark = int(input("Input mark: "))
print(marktograde(mark))