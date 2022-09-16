from .cmds import commands
from os import name, system

def clear():
  if name in ('nt', 'dos'):
    system('cls')
    return None
  system('clear')

class Code:
  def __init__(self, file: str):
    self.content: str = ''
    self.file: str = file

  def add_line(self, line: str):
    self.content += '\n' + line

  def remove_line(self, line: int):
    e = ''
    li: list = self.content.split("\n")
    le = len(li)
    if line == -1: line = le
    for i in range(le):
      if i != line and i != '':
        e += '\n' + li[i]
    self.content = e

def runcmd(code: Code):
  command = input("COMMAND INTERUPT, /resume to resume : /")
  while True:
    try:
      if commands[command](code) == 'end':
        break
    except KeyError:
      print("Unknown command")
    command = input("Command : /")

def run(*, file: str = None):
  if file is None: file = input("File path : ")
  code = Code(file)
  with open(file, 'r') as f:
    code.content = f.read()
    print(code.content)
  while True:
    clear()
    print(code.content)
    try:
      while True:
        code.add_line(input())
    except KeyboardInterrupt:
      runcmd(code)
