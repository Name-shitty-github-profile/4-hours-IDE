from .esc import exite
from .remove import remove
from .save import save
def liste(Code):
  print("Here's the commands")
  for i in commands:
    print('/' + i)

commands: dict = {
  'esc': exite,
  'escape': exite,
  'exit': exite,
  'save': save,
  'resume': lambda Code : 'end',
  'list': liste,
  'help': liste,
  'project': lambda Code : print(f'File : {Code.file}\nCode {"{"}\n {Code.content} \n{"}"}'),
  'remove': remove
}
