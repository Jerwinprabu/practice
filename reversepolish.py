#!/usr/bin/pypy
# reverse polish notation evaluator
# Functions that define the operators and how to evaluate them.
# This example assumes binary operators, but this is easy to extend.
ops = {
  "+" : (lambda a, b: a + b),
  "-" : (lambda a, b: a - b),
  "*" : (lambda a, b: a * b)
}
  
def eval(tokens):
  stack = []
  
  for token in tokens:
    if token in ops:
      arg2 = stack.pop()
      arg1 = stack.pop()
      result = ops[token](arg1, arg2)
      stack.append(result)
    else:
      stack.append(int(token))
  
  return stack.pop()
  
print "Result:",  eval("7 2 3 + -".split())
