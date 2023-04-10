# Challenge 072

subjects = ["math", "literature", "physics", "chemistry", "biology", "history"]
print(subjects)
subject = input("Which subject you don't like? ").lower()
subjects.remove(subject)
print(subjects)
