a = ['My', 'deliverable', 'is', 'due', 'in', 'May']

print("{0}".format(" ".join(a)))
#strip
string = " Remove unwanted characters    from this string.\t\t    \n"
print(string.lower())
print(string.upper())
print(string.capitalize())

string4 = "$$Here's another string that has unwanted characters.__---++"
print("Output #30: {0:s}".format(string4))
string4 = "$$The unwanted characters have been removed.__---++"
string4_strip = string4.strip('$_-+')
print("Output #31: {0:s}".format(string4_strip))

# replace

string5 = "Let's replace the spaces in this sentence with other characters."
string5_replace = string5.replace(" ", "!@!")
print("Output #32 (with !@!): {0:s}".format(string5_replace))
string5_replace = string5.replace(" ", ",")
print("Output #33 (with commas): {0:s}".format(string5_replace))