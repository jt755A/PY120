class A:
  def __init__(self):
      self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)

'''
Line 10 would throw an AttributeError. class A's __init__ method is never
called, since the `super` function is not included in class B's __init__ 
method. As a result, the class B instance will not have a `var_a` instance
variable.
'''