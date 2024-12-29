class Crypto:
    def __init__(self, amount, base, currency) -> None:
        self.amount = amount
        self.base = base
        self.currency = currency

    def get_crypto_amount(self) -> None:
        return self.amount