# Challenge 078

tv_programs = ['TED', 'BBC', 'Deep Tech', 'Science Fantastic']
for i in tv_programs: print(i)
show = input("Enter another TV show: ")
idx = int(input("Enter a position inserted into the list [0-3]: "))
tv_programs.insert(idx, show)
for i in tv_programs: print(i)