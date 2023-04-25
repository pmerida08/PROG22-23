"""
Clase Abstracta Movement. Representa una transacción bancaria.
Los movimientos estarán en clases especializadas.

"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Optional
from typeguard import typechecked

class MovementType(Enum):
    InitialBalance: 'IB'
    Deposit: 'DP'
    Withdraw: 'WD'
    TransferIssued: 'TI'
    TransferReceived: 'TR'

@typechecked
@dataclass(frozen=True)
class Movement(ABC):
    type: MovementType
    amount: float
    account: Optional[int] = None

    @abstractmethod
    def __str__(self):
        pass


class InitialBalance(Movement):

    def __init__(self, amount: float):
        super().__init__(MovementType.InitialBalance, amount)

    def __str__(self):
        return f"Creación de la cuenta con ingreso de: {self.amount:.2f} €"


class Deposit(Movement):

    def __init__(self, amount: float):
        super().__init__(MovementType.Deposit, amount)

    def __str__(self):
        return f"Ingreso de {self.amount:.2f} €"


class Withdraw(Movement):

    def __init__(self, amount: float):
        super().__init__(MovementType.Withdraw, -amount)

    def __str__(self):
        return f"Cargo de {-self.amount:.2f} €"


class TransferIssued(Movement):

    def __init__(self, amount: float, account: int):
        super().__init__(MovementType.TransferIssued, -amount, account)

    def __str__(self):
        return f"Transferencia emitida de {-self.amount:.2f} € a la cuenta {self.account:010d}"


class TransferReceived(Movement):

    def __init__(self, amount: float, account: int):
        super().__init__(MovementType.TransferReceived, amount, account)

    def __str__(self):
        return f"Transferencia recibida de {self.amount:.2f} € de la cuenta {self.account:010d}"