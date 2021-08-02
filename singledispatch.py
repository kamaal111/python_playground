from functools import singledispatch

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,")
    print(arg)

@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in numbers, eh?")
    print(arg)

@fun.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)

class ComplexClass:
    def doing_stuff(self):
        print("Woooow I am working so hard!")

@fun.register(ComplexClass)
def _(arg: "ComplexClass", verbose=False):
    if verbose:
        print("Doing some complex stuff here!")
    arg.doing_stuff()


class ComplexerClass(ComplexClass):
    def doing_stuff(self):
        print("Okey I am sweating balls")


@fun.register(ComplexerClass)
def _(arg: "ComplexerClass", verbose=False):
    if verbose:
        print("Give me a break")
    arg.doing_stuff()

complex_class = ComplexClass()
fun(complex_class, verbose=True)
complexer_class = ComplexerClass()
fun(complexer_class, verbose=True)