from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter

my_lists = [[123,2,2,444], [22,6,6,444], [354,4,4,678], [236,5,5,678], \
[578,1,1,290], [461,1,1,290]]
my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3, 0))
print("Output #92: {}".format(my_lists_sorted_by_index_3_and_0))