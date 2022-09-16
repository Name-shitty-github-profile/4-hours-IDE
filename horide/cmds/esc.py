from .save import save
def exite(Code: str):
  if input('Do you want to save your current work ? [y,n]').lower() == 'y':
    save(Code)
  exit()
