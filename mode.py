from math import exp, log, sqrt
import re

string = "The quick brown fox jumps over the lazy dog"
string_list = string.split()
pattern = re.compile(r"The", re.I)
count = 0
for word in string_list :
    if pattern.search(word):
        count += 1

print("count:{0:d}".format(count))

pattern2 = re.compile(r"(?PThe)", re.I)
print("#39:")
for word in string_list :
    if pattern.search(word) :
        print("{:s}".format(pattern2.search(word).group('match_word')))