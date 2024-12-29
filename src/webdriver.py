from rich.console import Console
from rich.panel import Panel
from src.crypto import Crypto
from src.hoc.memory import Memory
from src.hoc.system import system_clear
from datetime import datetime
import requests

class Webdriver:
    def __init__(self, crypto_array, memory, crypto_data) -> None:
        self.crypto_array = crypto_array
        self.memory: Memory = memory
        self.crypto_data = crypto_data

    def main_function(self, crypto: Crypto) -> None:
        self.memory.array.append(crypto.amount)
        self.memory.check_memory()

        if len(self.memory.array) < 2 or self.memory.array[-1] != self.memory.array[-2]:
            system_clear()

            date = " ".join(datetime.now().strftime("%d-%m-%y %H-%M-%S").split(" "))
            self.crypto_data.append({
                "amount": crypto.amount,
                "base": crypto.base,
                "currency": crypto.currency,
                "date": date
            })

            Console().print("[bold white on red]To exit and save ( in /output ) press [/bold white on red][bold white on yellow]ctrl + C[bold white on yellow]")

            Console().print(Panel(
                f'Amount: [{self.memory.check_price()}]{crypto.get_crypto_amount()}[/{self.memory.check_price()}]\nCurrency: [green]USD[/green]\nUpdated: [yellow]{date}[/yellow]',
                title=str(crypto.base)
            ))

    def get_crypto_data(self) -> None:
        response = requests.get(f"https://api.coinbase.com/v2/prices/{self.crypto_array[0]}-USD/buy")
    
        if response.status_code == 200:
            json_data = response.json()
            
            amount = json_data["data"]["amount"]
            base = json_data["data"]["base"]
            currency = json_data["data"]["currency"]
            
            crypto = Crypto(amount=amount, base=base, currency=currency)
            self.main_function(crypto)

    def create_output_logs(self, crypto_data: list[Crypto]) -> None:
        if len(crypto_data) != 0:
            string = []
            [(lambda crypto: string.append(f'{crypto["amount"]} | {crypto["base"]} | {crypto["currency"]} | {crypto["date"]}'))(crypto) for crypto in self.crypto_data]         

            with open(f'output/log[{" ".join(datetime.now().strftime("%d-%m-%Y %H-%M-%S").split(" "))}{self.crypto_array[0]}].txt', "w", encoding="utf-8") as file:
                file.write("\n".join(string))