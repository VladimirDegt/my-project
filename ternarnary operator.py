s = "helloWorld"

generator = (" " + i if i.isupper() else i for i in s)
print("".join(generator))

"""
Complete the solution so that the function will break up camel casing, using a space between words.
Example

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"""
