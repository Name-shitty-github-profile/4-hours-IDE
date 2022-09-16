def remove(Code):
  while True:
    try:
      line = int(input("Line you want to delete [-1 is the last one] "))
      break
    except ValueError:
      print("Invalid value and integer please")
  Code.remove_line(line)
