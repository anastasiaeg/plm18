# vim: set filetype=python ts=2 sw=2 sts=2 expandtab: 
# note above: enforce indentation standards

# Timm's rule. Python is not a language. 
# Rather, it is a language laboratory.

y = [x/2 for x in range(0,100) if x > 60]

lst = [ 1,2 ,3]
d = dict(name=1, zebras=3, showsize=4)

def me(x): return -1*x

print(me)

def ordered(lst,key=me):
  print(">",lst.sort(key=key))
  return lst

def score(pair): return pair[0]

def unscore(pair): return -1*score(pair)
def what(pair):  return pair[1]

print( ordered([ [3, "dog"],[4,"cat"],[1,"dog"]],
               key=score))

print(ordered([k for k in d.keys()]))

print(ordered([k for k in d.values()]))

print("B4 ", d)
print("Adter ", {d[k] :k for k in d} )
   


#print(232000001111111) 

#print("hello","gooodbye",sep=".... ",end=""); print("goodbye")

def eg1():
  old=[10,20,30,40, 50,60,70]
  old[0] = 100
  old[-1]= "rd"
  print(old[2:])
  new=old[:]
  old[0]= 99999
  print(new)
  #assert new[0] ==101,"i expcted %5.3f" % 100
#  print(old)
  
#eg1()

def odds(lst):
  for i in lst:
    if i % 2:
      yield  i
 
for x in odds([1,2,3,4,5]):
  print("X? ", x)
  
#def lines(str):
 # for line in words(str):
  ##     yield line
     
def person(x):  
  return str(x) and x[0].isupper()


print("ST ",str( person("Tim")))
print(9999)

import re
def words(str): return re.split("[\n\t \r]+",str)
      
def people(src):
  for s in src:
    for w in words(s):
      if person(w):
        yield w
  
def linesFromString(str):
  for line in str.split('\n'):
     yield line
      
def linesFromFile(file):
  with open(file) as f:
    x= f.readline()
    while x:
      yield x
      x = f.readline()

# Timm
it= """
asd
as asd
  asdasd
  
  
  asd Tim  """

print(111)
for x in people(linesFromFile("idiom.py")):
  print("F> %s " % x)
  
print(333)
#print([s for s in 
 #      people("idiom.py")])


#print("upper ", person("Tim"))

#for i in odds(range(0,50)):
 # print("I> ", i)
  
# =======================
#print([x/2 for x in range(0,9) if x % 2])
import re

def cells(str, out):
   str = re.sub(r'([\n\t\r ]|#.*)', '', str)
   if str != '':
      lst = [z.strip() for z in str.split(",")]
      if len(lst) > 0:
        out += [lst]  

def filterEachLine(f=cells):
  out=[]
  line = input()
  while line:
    f(line, out)
    line=input()
  return out
    
#for line in filterEachLine():
#  print("\t",line)
#------------------------------------------------------
# decorators
# For example, functions can be things to call, but
# they can also be places to comment on things.
import re, traceback, time

def go(f):
  print("\n-----| %s |-----------------------" % f.__name__)
  if f.__doc__:
    print("# "+ re.sub(r'\n[ \t]*',"\n# ",f.__doc__))
  f()
  return f

#@go
def go1():
  """Isn't it great we can
  use the function doco string to
  document the test? """
  print("going!")
 
#go1()
#-------------------------------------------------------
# World's shortest unit test engine

TRY=FAIL=0

def ok(f):
  global TRY,FAIL 
  try:     
    TRY  += 1; go(f); print("# pass");  
  except:  
    FAIL += 1; print(traceback.format_exc());  
  return f

#@ok
def ok1(): 1/1

#@ok
def ok2(): 1/0

#@ok
def ok3(): 
  "note how we get to ok3, even after ok2 crashes"
  assert 1==0, "i thought one was zero %s " % "today"

#------------------------------------------------------
# closures

def visit(x,f):
  if isinstance(x,list):
    for y in x:
      visit(y,f)
  else:
    f(x)

def visitEg():
  lst = [10, 20, [30, [40, 50]], [60, 70], 80]
  class worker:
    def __init__(i)   : i.n=0
    def __call__(i,x) : i.n += x*100 
  w = worker()
  visit(lst, w)
  return w.n

#print(visitEg())

#-----------------------------------------------------
# memoisation via decoration
def memo(f):
  cache={}
  def g(*lst, **dic):  
    if lst in cache:
      return cache[lst]
    new = cache[lst] = f(*lst, **dic)
    return new
  return g

@memo
def fib(n):
  return n if n < 2 else fib(n-2) + fib(n-1)

#@go
def fibEg():
  "without memoization, this will never terminate"
  print(fib(200))

  
#-----------------------------------------------------
# list comprehensions

#@go
def compEg():
  s = [x**2 for x in range(10)]
  v = [2**i for i in range(13) ]
  m = [x/10 for x in s if x % 2]
  print(dict(s=s,v=v,m=m))

#-----------------------------------------------------
# iterators
def items(x):
  if isinstance(x,(list,tuple)):
    for y in x:
      for z in items(y):
        yield z
  else:
    yield x

#@go
def items1():
  for i in items([10, 20, [30, [40, 50]], [60, 70], 80]):
    print(i)

#-----------------------------------------------------
# context manager
from contextlib import contextmanager
@contextmanager
def tag(s):
  print("<"+s+">",end="")
  yield;
  print("</"+s+">",end="")

#@go
def tagEg():
  with tag("h1"):
    print( "hello",end="")
    with tag("em"):
      print("timm",end="")

#-----------------------------------------------------
# abstraction
def str2lines(str):
  for line in str.splitlines():
    yield line

def file2lines(file):
  with open(file) as fs: # context manager
    for line in fs:
      yield line.rstrip('\n')

import zipfile
def zip2lines(file):
  with zipfile.ZipFile(file) as z:    
    with z.open(file) as f:
      for line in f:
        yield line.rstring('\n')

def lines(str):
  "returns an iterator"
  def ext()  : return str[-3:]
  def zip()  : return ext() == "zip"
  def file() : return ext() in [".py", "csv", "txt"]
  # --- begin main ------------------
  if  file() : return file2lines(str)
  elif zip() : return zip2lines(str)
  else       : return str2lines(str)

#@go
def linesEg1():
  for n,line in enumerate(lines("""111 
                    222
                    333""")):
    print(n,"\t",line)

#@go
def linesEg2():
  for n,line in enumerate(lines("idiom.py")):
    print(n,"\t",line)

#-----------------------------------------------------
# csv reader
def csv(src):
  """kill whitespace, comments, skip blanklines, 
     return list of cells, one per line"""
  for line in lines(src):
    line = re.sub(r'([\n\t\r ]|#.*)', '', line)
    if line:
      line= [z.strip() for z in line.split(",")]
      if line:
        yield  line

str001="""forecast,temp,humidity, ?windy, play
          #------- ---- --------  -----  -----
          ?,     85, ?,  false, no
          sunny, 72, 95.0, false, no
          sunny, 80, 90, true,  no # comments
          rainy, 65, 70, true,  no
          rainy, 71, 91, true,  no
          overcast, 83, 86, false, yes
          rainy, 70, ?, false, yes

          rainy, 68, 80, false, yes
          # another comment
          overcast, 64, 65, true, yes
          sunny, 69, 70, false, yes
          rainy, 75, 80, false, yes
          sunny, 75, 70, true, yes
          overcast, 72, 90, true, yes
          overcast, 81, 75, false, yes"""

#@go
def csvEg():
  for cells in csv(str001):
    print(cells)

def thing(x):
  def sym(x): return x
  #sym = lambda x: x
  try:    
    return int(x), int
  except: 
    try:    return float(x),float
    except: return x,sym

x,_= thing('7')
print('TH>', x)

class Fred:
  def __init__(i,x):
    i.name= x

f=Fred(3)
print(f.name)

class Struct:
    "A structure that can have any fields defined."
    def __init__(self, **entries): 
        self.__dict__.update(entries)
    def __repr__(self):
        keys=self.__dict__.keys()
        keys = [k for k in keys]
        keys.sort()
        return str(["%s=%s" %  (k,self.__dict__[k]) for k in keys])
    def __getitem__(self,x):
        return self.__dict__[x]
        
s= Struct(name="tim",age="some lie")
print("W> ",s)
print("W> ",s.name)
print("W> ",s.__dict__["name"])
print("W3> ",s["name"])

#-----------------------------------------------------
# columns reader
def cols(src):
  """ Cols have meta-knowledge. Meta-K starts life as
      'None'. Then, when the first non empty cells shows up,
      they are converted to 'int' or 'sym' or 'float'.
  """
  meta = None
  # --- utils -----------------
  def cols1(line,c, cell, f):
    if line == 0   : return cell
    if cell == "?" : return cell
    if f           : return f(cell)
    cell, meta[c] = thing(cell)
    return cell 
  # --- main ------------------
  for line,cells in enumerate(csv(src)):
    meta = meta or { 
            c:None for c,cell in enumerate(cells) if cell[0] != "?" }
    yield [ cols1(line, c, cells[c], meta[c]) for c in meta ]

#@go
def colsEg():
  for cells in cols(str001):
    print(cells)

if __name__ == "__main__": 
   print("\n# %s TRY= %s ,FAIL= %s ,%%PASS= %s"  % (
          time.strftime("%d/%m/%Y, %H:%M:%S,"),
          TRY, FAIL, int(round((TRY-FAIL)*100/(TRY+0.001)))))
