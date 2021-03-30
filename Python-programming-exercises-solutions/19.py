from operator import itemgetter
people = [tuple(person.split(',')) for person in input().split(' ')]
people.sort(key=itemgetter(0,1,2))
print(people)