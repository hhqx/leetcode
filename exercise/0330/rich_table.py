from rich.console import Console
from rich.table import Table

# 生成n*3的表格
def generate_table():
    table = Table(title="Table Title")
    table.add_column("Header 1")
    table.add_column("Header 2")
    table.add_column("Header 3")
    for i in range(1, 4):
        table.add_row(f"Row {i} Column 1", f"Row {i} Column 2", f"Row {i} Column 3")
    return table

# 生成m个n*3的嵌套表
def generate_nested_table(m, n):
    nested_table = []
    for i in range(m):
        table = generate_table()
        nested_table.append(table)
    return nested_table

# 使用Rich模块显示嵌套表
def display_nested_table(nested_table):
    console = Console()
    for i, table in enumerate(nested_table):
        console.print(f"Table {i + 1}", style="bold red")
        console.print(table)

# 生成包含两个n*3的嵌套表
nested_table = generate_nested_table(2, 3)

# 使用Rich模块显示嵌套表
display_nested_table(nested_table)
