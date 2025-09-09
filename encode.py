# hanifx_menu.py
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import track
from datetime import datetime
from hanifx_secure_encode import encode_text, encode_file

console = Console()
LOG_FILE = "hanifx_logs.txt"

def save_log(data_type, input_value, encoded_result):
    """Save encoded output to log file with timestamp"""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]")
        f.write(f"\nType: {data_type}")
        f.write(f"\nInput: {input_value}")
        f.write(f"\nEncoded: {encoded_result}")
        f.write("\n" + "-"*40 + "\n")

def encode_string():
    text = Prompt.ask("[bold cyan]Enter the text you want to encode[/bold cyan]")
    with console.status("[green]Encoding text...[/green]"):
        result = encode_text(text)
    console.print(Panel(result, title="[green]âœ… Encoded String[/green]"))

    save_log("STRING", text, result)
    console.print("[bold blue]ðŸ“Œ Saved to log file[/bold blue]")

def encode_file_path():
    path = Prompt.ask("[bold cyan]Enter file path[/bold cyan]")
    with console.status("[green]Encoding file...[/green]"):
        for step in track(range(10), description="Processing..."):
            pass
        result = encode_file(path)
    console.print(Panel(f"[bold green]{result}[/bold green]", title="âœ… Encoded File"))

    save_log("FILE", path, result)
    console.print("[bold blue]ðŸ“Œ Saved to log file[/bold blue]")

def main():
    console.print(Panel("[bold magenta]ðŸ”¥ HanifX Encoder v24.0.0 ðŸ”¥[/bold magenta]", expand=False))

    while True:
        console.print("\n[bold yellow]Choose an option:[/bold yellow]")
        console.print(" [cyan]1)[/cyan] Encode Text")
        console.print(" [cyan]2)[/cyan] Encode File")
        console.print(" [cyan]3)[/cyan] Exit")

        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3"], default="1")

        if choice == "1":
            encode_string()
        elif choice == "2":
            encode_file_path()
        elif choice == "3":
            console.print("[bold red]Exiting... Goodbye![/bold red]")
            break

if __name__ == "__main__":
    main()
