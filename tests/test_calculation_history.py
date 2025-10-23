import os
import pandas as pd
import pytest
from faker import Faker
from calculator.calculation_history import CalculationHistory

fake = Faker()

@pytest.fixture
def setup_calculation_history(tmpdir):
    temp_file = tmpdir.join("temp_history.csv")
    history = CalculationHistory(filename=str(temp_file))
    return history, str(temp_file)

def test_add_entry(setup_calculation_history):
    history, _ = setup_calculation_history
    operation = fake.word()
    operands = (fake.random_int(), fake.random_int())
    result = sum(operands)
    history.add_entry(operation, operands, result)
    assert len(history.history) == 1
    assert history.history.iloc[0]['operation'] == operation
    assert history.history.iloc[0]['operands'] == str(operands)
    assert history.history.iloc[0]['result'] == result

def test_save_history(setup_calculation_history):
    history, temp_file = setup_calculation_history
    operation = fake.word()
    operands = (fake.random_int(), fake.random_int())
    result = sum(operands)
    history.add_entry(operation, operands, result)
    history.save_history()
    loaded_history = pd.read_csv(temp_file)
    assert len(loaded_history) == 1
    assert loaded_history.iloc[0]['operation'] == operation
    assert loaded_history.iloc[0]['operands'] == str(operands)
    assert loaded_history.iloc[0]['result'] == result

def test_clear_history(setup_calculation_history):
    history, _ = setup_calculation_history
    operation = fake.word()
    operands = (fake.random_int(), fake.random_int())
    result = sum(operands)
    history.add_entry(operation, operands, result)
    history.clear_history()
    assert len(history.history) == 0

def test_load_existing_history(setup_calculation_history):
    history, temp_file = setup_calculation_history
    sample_data = pd.DataFrame({
        'operation': [fake.word() for _ in range(2)],
        'operands': [str((fake.random_int(), fake.random_int())) for _ in range(2)],
        'result': [sum((fake.random_int(), fake.random_int())) for _ in range(2)]
    })
    sample_data.to_csv(temp_file, index=False)
    new_history = CalculationHistory(filename=str(temp_file))
    assert len(new_history.history) == 2
    assert new_history.history.iloc[0]['operation'] == sample_data.iloc[0]['operation']
    assert new_history.history.iloc[1]['operation'] == sample_data.iloc[1]['operation']
