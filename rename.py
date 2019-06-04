#
# rename file
# from ext4 file sysytem
# to ..for example ntfs, fat
# ext4: file-Name.txt, file-name.txt
# ntfs: file-Name.txt, file-name.txt ~ is similar name!
# after use
# ```
# python2 rename.py
# << file-Name.txt, file-name.txt
# >> file-name.txt, file-name-fx-dd.txt
# ```
#
from os import rename
from os import getcwd
from os import listdir
from os import path
from time import time

#pit install natsort
from natsort import natsorted

def renameFile(src, target):
  print(src, ' ~> ', target)
  print(' ')
  #@todo add simulate mode, add exception
  rename(src, target)

def getPathToFiles():
  path =  getcwd()
  #@tood add test
  # subDir = '/files'
  subDir = ''
  pathToFiles = path + subDir
  # print(path, pathToFiles)
  print('path:' + pathToFiles)
  return pathToFiles

def getFiles(pathToFiles):
  files = listdir(pathToFiles)
  # print(files)
  files = natsorted(files, reverse=True)
  # print(files)
  return files

def convert(src):
  target = src.replace(" ", '-')
  target = src.replace('_', '-')
  target = target.lower()
  #print(src, ' :> ', target)
  return target

def isExist(list, item):
  return False

def isExistFile(file):
  # print('F:'+ file )
  # if ((os.path.isfile(file) )):
  #   print('+')
  # else:
  #   print('-')
  #@fixme stub
  # return 0 != 1
  return path.exists(file)

def existExtension(src, splitter):
  parts = src.split(splitter)
  countparts = len(parts)
  # print('parts=', countparts)
  return 1 < countparts

def updateName(src):
  #postfix = '_time_01'
  splitter = '.'
  uniqfix = str(time()).split(splitter)[-1]
  #uniqfix = str(time.time()).replace(splitter, '')
  postfix = '-fx-' + uniqfix
  parts = src.split(splitter)
  if existExtension(src, splitter):
    extension = parts[ len(parts) - len(splitter) ]
    name = src[ :len(src) - len(extension) - len(splitter) ]
    #print(len(parts), name, '.', extension)
    target = name + postfix + splitter + extension
  else:
    target = src + postfix
  #+ between name and extension.
  #+ prefix does not keep origin sorting
  #print(src, ' ~>> ', target)
  return target

def updateFileName(src, path):
  namefilenew = convert(src)
  #@fixme use join
  # print('|', path, '/', namefilenew)
  if isExistFile(path + '/' + namefilenew): #fixme after stub, to while
    # print('yes')
    updatedName = updateName(namefilenew)
    namefilenew = updatedName
    # updateFileName(updatedName)
  # else:
    # print('no')
  prepath = path + '/'
  #@fixme filename, check name with space
  renameFile(prepath+ src, prepath+ namefilenew)
  return namefilenew

def isValidName(name):
  if ' ' in name:
    return 0!=0
  return 0==0

def isValidFileName(name, pathall):
  #@fixme check isdir
  pathfull = path.join(pathall, name)
  if path.isdir(pathfull):
    print('::is-dir ~ ' + name)
    return True
  return name == convert(name)


pathToFiles = getPathToFiles()
filenames = getFiles(pathToFiles)
for filename in filenames:
  # if not path.isdir(filename):
  if not isValidFileName(filename, pathToFiles):
    print('update...(' + filename + ')')
    updateFileName(filename, pathToFiles)

print('done')
