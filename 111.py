# Challenge 111

data = ['Book,Author,Year Released',
        'To Kill A Mockingbird,Harper Lee,1960',
        'A Brief History of Time,Stephen Hawking,1988',
        'The Great Gatsby,F. Scott Fitzgerald,1922',
        'The Man Who Mistook His Wife for a Hat,Oliver Sacks,1985',
        'Pride and Prejudice,Jane Austen,1813'
        ]

with open("Books.csv", 'w') as file:
    for row in data:
        file.write(row + '\n')