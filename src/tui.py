from rich.console import Console
from rich.panel import Panel

console = Console()

def display_welcome():
    console.print(Panel.fit("[bold green]Welcome to carnaI![/]", title="🤖"))

if __name__ == "__main__":
    display_welcome()
