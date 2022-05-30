morning = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon = ['Java', 'C', 'Ruby', 'Python', 'C#']

# possible_courses = set(morning) ^ set(afternoon)
possible_courses = set(morning).symmetric_difference(afternoon)
print(possible_courses)

possible_courses = set(afternoon).symmetric_difference(morning)
print(possible_courses)
