"""using Python3"""
from collections import namedtuple

Club = namedtuple("club",['name','ucl','league'])

best_team = Club('Real Madrid',11,32)
print (best_team)
print ('{} has {} UCL Trophy till 2017'.format(best_team.name,best_team.ucl))

print ("----------------")
#_make() create new table from existing list
another_team = ["AC Millan",7,18]
another_team = Club._make(another_team)
print(another_team)

print ("----------------")
#_asdict() create new table from existing list
get_dict = best_team._asdict()
print(get_dict)

print ("----------------")
#_replace() replacing specified fields
best_team = best_team._replace(name="Royal Madrid",league=33)
print(best_team)

print ("----------------")
#_fields() extract all fields
print(best_team._fields)
