import pytest
import yaml  # type: ignore[import-untyped]
from pathlib import Path
from bank_system.models import BankAccount
from bank_system.value_objects import Money

@pytest.fixture
def sample_money() -> Money:
    return Money(amount=500.0, currency="UAH")

@pytest.fixture
def sample_account() -> BankAccount:
    return BankAccount(
        account_number="ACC-12345",
        client="Максим Войтович",
        balance=1500.0,
        operation="deposit",
        amount=500.0
    )

@pytest.fixture
def account_factory():
    def _create(acc_num: str = "ACC-001", client: str = "Test Client", balance: float = 1000.0):
        return BankAccount(
            account_number=acc_num,
            client=client,
            balance=balance,
            operation="deposit",
            amount=100.0
        )
    return _create