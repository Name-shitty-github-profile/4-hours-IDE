def save(Code: str):
  print(f'Saving to {Code.file}\nOpening the file')
  with open(Code.file, 'w') as f:
    print("File opened\nWritting the code")
    f.write(Code.content)
  print("Code saved")
  return None
