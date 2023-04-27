from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.style import Style
from rich.color import Color

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Name")
table.add_column("Favorite Color")

color = Color.from_rgb(100, 100, 100)
text = Text("John", style=Style(bold=True, color=color)) + " " + Text("Smith", style="bold green") + " " + Text("Doe", style="bold blue")
table.add_row("First Name\nLast Name", text)

console.print(table)


# ansi color
console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Color idx")
table.add_column("Name")

color = Color.from_rgb(100, 100, 100)
for id in range(50):
    text = Text("John", style=Style(bold=True, color=color)) + " " + Text("Color", style=Style(bold=True, color=Color.from_ansi(id)))
    table.add_row(f"ID {id}", text)

console.print(table)


