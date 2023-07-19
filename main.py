from flask import Flask, render_template

class Link:
    def __init__(self, name, url):
        # Initialises a Link object with a name and URL
        self.name = name
        self.url = url

    def __str__(self):
        # Returns a string representation of the Link object
        return f"{self.name}: {self.url}"

class LinkTree:
    def __init__(self):
        # Initialises a LinkTree object with an empyty list to store links
        self.links = []
    
    def add_link(self, name, url):
        # Creates a new Link to object with the provided name and URL 
        link = Link(name, url)

        # Appends the link to the list of links in the Linktree
        self.links.append(link)

    def get_links(self):
        return self.links   
    
    def print_links(self):
        # Iterates over each link in the LinkTree and prints its string representation
        for links in self.links:
            print(links)

# Creating a Flask application 
app = Flask(__name__)


# Creating a sample LinkTree Instance
my_linktree = LinkTree()

# Adding links to the LinkTree
my_linktree.add_link("Linkedin", "https://www.linkedin.com/in/vincent-chow-339577260/")
my_linktree.add_link("GitHub", "https://github.com/chowvb")
my_linktree.add_link("Personal Instagram", "https://www.instagram.com/vinnie_chow99/")
my_linktree.add_link("Fitness Instagram", "https://www.instagram.com/vchow_alt/")

# Displaying the link in the LinkTree in the CLI
# my_linktree.print_links()

# Route to dusplay the Linktree in a web browser 
@app.route('/')
def display_linkstree():
    links = my_linktree.get_links()
    return render_template('linktree.html', links=links)

if __name__ == '__main__':
    app.run()