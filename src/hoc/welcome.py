from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.padding import Padding
from rich.align import Align
import pyfiglet
import keyboard

class Welcome:
    def __init__(self) -> None:
        self.options = ["BTC", "ETH", "USDT", "SOL", "BNB", "XRP", "DOGE", "USDC", "ADA", "TON"]
        self.selected_index = 0
        self.console = Console()

    def send_welcome(self, text) -> None:
        figlet_text = pyfiglet.figlet_format(text, font="bloody")
        panel = Panel(figlet_text, style="green")

        vertical_padding = (self.console.size.height - figlet_text.count("\n")) // 2
        padded_panel = Padding(panel, (vertical_padding, 0))
        aligned_panel = Align.center(padded_panel)

        self.console.print(aligned_panel)

    def display_menu(self) -> str:
        menu = []
        for i, option in enumerate(self.options):
            if i == self.selected_index:
                menu.append(f"> [bold green]{option}[/bold green]")
            else:
                menu.append(f"  {option}")
        return "\n".join(menu)
    
    def update_selection(self, key_event) -> bool:
        if key_event.name == "up" and self.selected_index > 0:
            self.selected_index -= 1
        elif key_event.name == "down" and self.selected_index < len(self.options) - 1:
            self.selected_index += 1
        elif key_event.name == "enter":
            return False
        return True
    
    def start(self) -> str:
        with Live(self.display_menu(), refresh_per_second=10, screen=True) as live:
            while True:
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    if not self.update_selection(event):
                        break
                    live.update(self.display_menu())

        self.console.clear()
        return self.options[self.selected_index]