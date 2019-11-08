import one
print("TOP LEVEL TWO.PY")
one.func()

if __name__ == '__main__':
  print("two.py being run directly")
else:
  print("two is being imported")