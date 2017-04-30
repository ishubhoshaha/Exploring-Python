import textwrap
string = "This is a very very very very very long string."
# divide original string in multiple paragraph with 7 ch long and return list where each paragraph treat as a list element
getlist = textwrap.wrap(string,7)
print (type(getlist))
print (getlist)
print ("-----------------")
# divide original string in multiple paragraph with 7 ch long and return as a single string
get_as_string = textwrap.fill(string,7) 
print (type(get_as_string)) 
print (get_as_string)
