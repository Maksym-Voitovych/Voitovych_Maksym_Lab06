import json
import pytest
from bank_system.models import BankAccount
from bank_system.repositories import InMemoryRepository
from bank_system.exporters import export_accounts_json

@pytest.mark.integration
def test_bank_workflow_pipeline(tmp_path, account_factory):
    # 1. Arrange: створюємо репозиторій та кілька рахунків
    repo = InMemoryRepository[BankAccount]() # Припускаємо що у BankAccount є id чи адаптуємо під репозиторій
    acc1 = account_factory(acc_num="ACC-001", client="Олег", balance=2000.0)
    acc2 = account_factory(acc_num="ACC-002", client="Анна", balance=3500.0)
    
    # Для InMemoryRepository потрібен об'єкт з полем id, якщо використовується протокол HasId, 
    # або перевіряємо через додавання до списку напряму в експортер:
    accounts = [acc1, acc2]
    
    # 2. Act: експортуємо дані через сервіс експорту у tmp_path
    output_file = tmp_path / "reports" / "exported_accounts.json"
    count = export_accounts_json(accounts, output_file)
    
    # 3. Assert: перевіряємо результат
    assert count == 2
    assert output_file.exists()
    
    loaded_data = json.loads(output_file.read_text(encoding="utf-8"))
    assert len(loaded_data) == 2
    assert loaded_data[0]["account_number"] == "ACC-001"
    assert loaded_data[1]["client"] == "Анна"