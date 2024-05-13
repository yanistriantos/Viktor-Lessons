# Default (named) argument
def greet(poslanie, person="Whoever"):
    # string formatiing
    # print(poslanie + ' ' +  person + "!")
    # f-strings
    print(f"{poslanie} - {person}!")

# regular function call
greet('Dobri Pojelaniq')

# function call keyword argument
# greet(poslanie="moeto poslanie", person="Whoever")
