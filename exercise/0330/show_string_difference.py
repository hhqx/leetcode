import difflib
from functools import reduce

from rich.color import Color
from rich.console import Console
from rich.style import Style
from rich.table import Table
from rich.text import Text

colors_map = [
    [200, 200, 200],
    [255, 0, 0],
    [255, 0, 10],
    [150, 150, 150],
    [0, 200, 0],
]
colors = list(map(lambda x: Color.from_rgb(x[0], x[1], x[2]), colors_map))


def add_color(s: str, color: Color) -> Text:
    return Text(s, style=Style(bold=True, color=color))


def get_string_difference(string1, string2):
    global colors
    words1, words2 = string1.split(), string2.split()
    text1, text2 = [], []
    # Compute the difference between the two sequences of words using difflib
    diff = difflib.SequenceMatcher(None, words1, words2).get_opcodes()
    is_same = all(row[0] == 'equal' for row in diff)
    for opcode, i1, i2, j1, j2 in diff:
        if opcode == 'equal':
            for i, word in enumerate(words1[i1:i2]):
                text1.append(add_color(word, colors[0]))
                text2.append(add_color(word, colors[0]))
        elif opcode == 'replace':
            for old, new in zip(words1[i1:i2], words2[j1:j2]):
                text1.append(add_color(old, colors[1]))
                text2.append(add_color(new, colors[2]))
        elif opcode == 'delete':
            for i, word in enumerate(words1[i1:i2]):
                text1.append(add_color(word, colors[3]))
        elif opcode == 'insert':
            for i, word in enumerate(words2[j1:j2]):
                text2.append(add_color(word, colors[4]))

    # text1, text2 = reduce(lambda x, y: x+" "+y, text1), reduce(lambda x, y: x+" "+y, text2)
    text1, text2 = map(lambda text: reduce(lambda x, y: x + " " + y, text), [text1, text2])
    return text1, text2, is_same


def visualize_string_difference(old, new):
    # Create a Console object to display the difference
    console = Console()

    # Create a table to display the two strings side by side
    table = Table(
        title="Visualize the Difference between Two Strings.", title_justify='center', title_style='bold magenta',
        show_header=True, show_lines=True, header_style="bold cyan")
    table.add_column("Old string")
    table.add_column("New string")

    # get the string difference
    text1, text2 = get_string_difference(old, new)[:2]
    table.add_row(text1, text2)

    # Print the table
    console.print(table)


if __name__ == '__main__':
    # Define the two strings to compare
    s1 = "halo Hello, world! hey. same one"
    s2 = "Hello, your world! everyone! same world!"
    visualize_string_difference(s1, s2)

