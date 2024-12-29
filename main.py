from src.webdriver import Webdriver
from src.hoc.memory import Memory
from src.hoc.welcome import Welcome
from rich.console import Console
from src.hoc.system import system_clear

if __name__ == "__main__":
    try:
        memory = Memory()
        crypto_data = []
        crypto_array= []

        Welcome().send_welcome("CRYPTO")

        Console().input("[bold white on green]Press enter to choose crypto: [/bold white on green]")
        crypto_array.append(Welcome().start())
        while True:
            Webdriver(crypto_array, memory, crypto_data).get_crypto_data()
    except KeyboardInterrupt:
        Webdriver(crypto_array, memory, crypto_data).create_output_logs(crypto_data)
    finally:
        system_clear()