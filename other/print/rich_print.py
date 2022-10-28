from rich import print
from rich.console import Console
from rich.table import Table
from rich.progress import track
from time import sleep
import os
import sys
from rich.columns import Columns
from rich.markdown import Markdown
from rich.syntax import Syntax

# print
print("Hello, [bold red]World[/bold red]!")
print("Hello, [italic red]World[/italic red]!")

# Console
console = Console()
console.print("Hello", "World!")
console.print("Hello", "World!", style="italic magenta")
console.print("Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")

# Emojis
console.print(":smiley: :vampire: :pile_of_poo: :thumbs_up: :raccoon: :cry: :thumbs_down: :kiss: :cool:")


# Table
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Date", style="dim", width=12)
table.add_column("Title")
table.add_column("Production Budget", justify="right")
table.add_column("Box Office", justify="right")
table.add_row(
    "Dev 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
)
table.add_row(
    "May 25, 2018",
    "[red]Solo[/red]: A Star Wars Story",
    "$275,000,000",
    "$393,151,347",
)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VIII: The Last Jedi",
    "$262,000,000",
    "[bold]$1,332,539,889[/bold]",
)
console.print(table)

# Markdown
for i in 'i am best programmer'.split():
    markdown = Markdown(i)
    console.print(markdown)



# %%
from rich.tree import Tree
from rich import print as rprint
tree = Tree("Family Tree")
tree.add("Mom")
tree.add("Dad")
tree.add("Brother").add("Wife")
tree.add("[red]Sister").add("[green]Husband").add("[blue]Son")

rprint(tree)


# Rich Print Table
table = Table(show_header=True, header_style="bold magenta")
# table.add_column("Date", style="dim", width=12)
table.add_column("Name")
table.add_column("Your input")
table.add_column("Output")
table.add_column("Expected")
table.add_column("Status")
table.add_column("Elapsed time")
# table.add_column("Production Budget", justify="right")
# table.add_column("Box Office", justify="right")
table.add_row(
    "Dev 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
)
table.add_row(
    "Dev 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
)
table.add_row(
    "May 25, 2018",
    "[red]Solo[/red]: A Star Wars Story",
    "$275,000,000",
    "$393,151,347",

)
table.add_row(
    "Dec 15, 2017",
    "Star Wars Ep. VIII: The Last Jedi",
    "$262,000,000",
    "[bold]$1,332,539,889[/bold]",
)
console.print(table)

