# Kylee Gordon Lab-16 04/08/2022

# This program gets user input and uses it to generate a html file containing the code required to
# create a simple website containing the user's input

def main():
    # Input
    name = input("Enter your name: ")
    description = input("Describe yourself: ")

    # Processing
    create_file()
    html = generate_html(name, description)

    # Output
    write_file(html)
    print("You webpage has been created, the HTML can be viewed in the file: webpage.html")


def create_file():
    file = open("webpage.html", "w")
    file.close()


def write_file(html):
    file = open("webpage.html", "w")
    file.write(html)


def generate_html(name, description):
    html = "<html>\n<head>\n</head>\n<body>\n<center>\n<h1>\n" + name + "\n</h1>\n</center>\n<hr />\n" + description + "\n<hr />\n</body>\n</html> "
    return html


main()
