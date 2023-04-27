import difflib
from rich.console import Console
from rich.syntax import Syntax

# Define the two strings to compare
string1 = "Hello, world!"
string2 = "Hello, everyone!"

# Compute the difference between the two strings using difflib
diff = difflib.unified_diff(string1.splitlines(), string2.splitlines())

# Create a Console object to display the difference
console = Console()

# Display the difference using rich Syntax highlighting
# console.print(Syntax('\n'.join(diff), "diff"))





import difflib
from rich.console import Console
# from rich.syntax import Syntax

def Syntax(s, color):
    return f'[{color}]{s}[/{color}]'

# Define the two strings to compare
string1 = "Hello, world!"
string2 = "Hello, everyone!"

# Split the strings into words
words1 = string1.split()
words2 = string2.split()

# Compute the difference between the two sequences of words using difflib
diff = difflib.SequenceMatcher(None, words1, words2).get_opcodes()

# Create a Console object to display the difference
console = Console()

# Display the difference using rich Syntax highlighting
output = []
for opcode, i1, i2, j1, j2 in diff:
    if opcode == 'equal':
        output.append(' '.join(words1[i1:i2]))
    elif opcode == 'replace':
        output.append(str(Syntax(' '.join(words1[i1:i2]), "red")) + ' ' + str(Syntax(' '.join(words2[j1:j2]), "green")))
    elif opcode == 'delete':
        output.append(str(Syntax(' '.join(words1[i1:i2]), "red")))
    elif opcode == 'insert':
        output.append(str(Syntax(' '.join(words2[j1:j2]), "green")))

console.print(' '.join(output))


import difflib
from rich.console import Console
from rich.table import Table
from rich.text import Text

# Define the two strings to compare
string1 = "halo Hello, world! hey. same one"
string2 = "Hello, your world! everyone! same world!"

# Split the strings into words
words1 = string1.split()
words2 = string2.split()

# Compute the difference between the two sequences of words using difflib
diff = difflib.SequenceMatcher(None, words1, words2).get_opcodes()

# Create a Console object to display the difference
console = Console()

# Create a table to display the two strings side by side
table = Table(show_header=False, show_lines=True)
table.add_column()
table.add_column()

# Create a Text object for the first string
text1, text2 = [], []

def add_color(s: str, color: str):
    return f'[{color}]{s}[/{color}]'
# Highlight the different words in the Text objects
colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]
colors = ["red", "yellow", "white", "green", "magenta", "cyan", "white"]
color_index = 0
for opcode, i1, i2, j1, j2 in diff:
    if opcode == 'equal':
        text1.extend(words1[i1:i2])
        text2.extend(words2[j1:j2])
    elif opcode == 'replace':
        for old, new in zip(words1[i1:i2], words2[j1:j2]):
            text1.append(add_color(old, colors[0]))
            text2.append(add_color(new, colors[1]))
    elif opcode == 'delete':
        for i, word in enumerate(words1[i1:i2]):
            text1.append(add_color(word, colors[2]))
    elif opcode == 'insert':
        for i, word in enumerate(words2[j1:j2]):
            text2.append(add_color(word, colors[3]))

table.add_row(" ".join(text1), " ".join(text2))
# Print the table
console.print(table)
