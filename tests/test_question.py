import pytest
import pandas as pd
import numpy as np
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tasks.task_manager import *

@pytest.fixture
def sample_df():
    data = {
        'name': ['V', 'Johnny Silverhand', 'Judy Alvarez'],
        'strength': [85, 70, 60],
        'intelligence': [75, 90, 88],
        'agility': [60, 80, 65],
        'health': [100, 95, 85],
        'faction': ['Nomads', 'Rockerboys', 'Moxes']
    }
    return pd.DataFrame(data)

def test_load_character_data(tmp_path):
    df = pd.DataFrame({'name': ['Test'], 'strength': [10]})
    test_file = tmp_path / "test.csv"
    df.to_csv(test_file, index=False)
    result = load_character_data(test_file)
    assert not result.empty

def test_get_top_strength_characters(sample_df):
    top_chars = get_top_strength_characters(sample_df, n=2)
    assert len(top_chars) == 2
    assert top_chars.iloc[0]['name'] == 'V'

def test_calculate_average_stats(sample_df):
    result = calculate_average_stats(sample_df)
    assert isinstance(result, dict)
    assert 'strength' in result

def test_filter_characters_by_faction(sample_df):
    filtered = filter_characters_by_faction(sample_df, 'Moxes')
    assert len(filtered) == 1
    assert filtered.iloc[0]['name'] == 'Judy Alvarez'

def test_normalize_health_points(sample_df):
    df_normalized = normalize_health_points(sample_df)
    assert df_normalized['health'].max() == 1.0

def test_convert_to_numpy_matrix(sample_df):
    mat = convert_to_numpy_matrix(sample_df)
    assert isinstance(mat, np.ndarray)
    assert mat.shape[0] == len(sample_df)

def test_get_character_with_max_intelligence(sample_df):
    char = get_character_with_max_intelligence(sample_df)
    assert char['name'] == 'Johnny Silverhand'

def test_sort_characters_by_agility(sample_df):
    sorted_df = sort_characters_by_agility(sample_df)
    assert sorted_df.iloc[0]['agility'] == 60

def test_create_stat_summary_dataframe(sample_df):
    summary = create_stat_summary_dataframe(sample_df)
    assert isinstance(summary, pd.DataFrame)
    assert 'mean' in summary.index

def test_export_dataframe_to_csv(sample_df, tmp_path):
    output_file = tmp_path / "output.csv"
    export_dataframe_to_csv(sample_df, output_file)
    assert output_file.exists()

def send_post_request(url: str, data: dict, headers: dict = None):
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # hata varsa exception fırlatır
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err} - Status Code: {response.status_code}")
    except Exception as err:
        print(f"Other error occurred: {err}")

class ResultCollector:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1

def run_tests():
    collector = ResultCollector()
    pytest.main(["tests"], plugins=[collector])
    print(f"\nToplam Başarılı: {collector.passed}")
    print(f"Toplam Başarısız: {collector.failed}")
    
    user_score = (collector.passed / (collector.passed + collector.failed)) * 100
    print(round(user_score, 2))
    
    url = "https://edugen-backend-487d2168bc6c.herokuapp.com/projectLog/"
    payload = {
        "user_id": 34,
        "project_id": 232,
        "user_score": round(user_score, 2),
        "is_auto": False
    }
    headers = {
        "Content-Type": "application/json"
    }
    send_post_request(url, payload, headers)

if __name__ == "__main__":
    run_tests()