class BankAccount:
    
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
        self._transactions = [] #_ = convencion "privado"
    
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("El monto debe ser positivo")
        self.balance += amount
        self._transactions.append(("deposit", amount))
        
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("El monto debe ser positivo")
        if amount > self.balance:
            raise ValueError("Saldo insuficiente")
        self.balance -= amount
        self._transactions.append(("withdraw", amount))
    
    def get_history(self) -> list:
        return self._transactions.copy()
    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"
    
    def transfer(self, amount: float, target_account: 'BankAccount') -> None:
        """Transfiere dinero a otra cuenta.

    Args:
        amount: Monto a transferir, debe ser positivo.
        target_account: Cuenta destino.

    Raises:
        ValueError: Si amount <= 0 o saldo insuficiente.
    """
        if amount <= 0:
            raise ValueError("El monto debe ser positivo")
        if amount > self.balance:
            raise ValueError("Saldo insuficiente para la transferencia")
        self.balance -= amount
        target_account.balance += amount
        self._transactions.append(("transfer_out", amount, target_account.owner)) 
        target_account._transactions.append(("transfer_in", amount, self.owner)) 

cuenta = BankAccount("Juan", 1000)
cuenta.deposit(500)
cuenta.withdraw(200)
cuenta.transfer(300, BankAccount("Maria"))
print(cuenta.get_history())
print(cuenta)