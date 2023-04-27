from itertools import zip_longest

from rich.color import Color
from rich.style import Style
from rich.console import Console
from rich.table import Table
from rich.markup import escape
import difflib

from rich.text import Text


def compare_outputs_old(output, target):
    """
    已弃用.
    比较输出结果和目标结果中的单词，将不同的单词用不同颜色标出
    """
    output_words = output.split()
    target_words = target.split()
    diff_output = []
    diff_target = []
    for word in output_words:
        if word not in target_words:
            diff_output.append(f"[bold][red]{escape(word)}[/red][/bold]")
        else:
            diff_output.append(word)
    for word in target_words:
        if word not in output_words:
            diff_target.append(f"[bold][green]{escape(word)}[/green][/bold]")
        else:
            diff_target.append(word)
    return " ".join(diff_output), " ".join(diff_target)


from show_string_difference import get_string_difference, add_color


def compare_outputs(output, target):
    """
        比较输出结果和目标结果中的单词，将不同的单词用不同颜色标出
    """
    return get_string_difference(output, target)


def display_diff_table(debug_infos, outputs, targets, title=None, caption=None, caption_style=None):
    """
    使用Rich模块生成n*3的表格，并将输出结果和目标结果中的不同的单词用不同颜色标出
    """
    console = Console()
    if not title:
        table = Table(show_header=True, header_style="bold magenta")
    else:
        # title_style = Style(color="yellow", bold=True, size=1)

        # table = Table(title=title, title_style=title_style, show_header=True, header_style="bold magenta")
        # title = Text(title, style=Style(color="red", bold=True, size=20))
        table = Table(
            title=title, title_justify='left', title_style='bold cyan',
            caption=caption, caption_justify='right', caption_style=caption_style,
            header_style="bold magenta", show_header=True, show_lines=False,
        )
    table.add_column("Debug Info")
    table.add_column("Output")
    table.add_column("Target")
    same_cnt = 0
    total_row = max(map(len, [outputs, targets]))
    for debug_info, output, target in zip_longest(debug_infos, outputs, targets, fillvalue=""):
        diff_output, diff_target, is_same = compare_outputs(output, target)
        table.add_row(debug_info, diff_output, diff_target)
        same_cnt += is_same
    table.add_row()
    # table.add_row("Error Count:", f"{same_cnt}/{total_row}")
    color = "green" if same_cnt == total_row else "red"
    table.add_row(
        f"[{color}][bold]Error Count:[/][/]",
        f"[{color}][bold]{total_row - same_cnt}[/][/]",
        f"[{color}][bold]{total_row - same_cnt}[/][/]",
    )

    console.print(table)
    return same_cnt == total_row


if __name__ == '__main__':
    # 测试代码
    debug_infos = ["Debug 1", "Debug 2", "Debug 3"]
    outputs = ["This is the output 1.", "This is the output 2.", "This is the output 3."]
    targets = ["This is the target 1.", "This is the target 2.", "This is the target 3."]
    display_diff_table(debug_infos, outputs, targets)
