import pandas as pd
import numpy as np

# 1. CSV dosyasından karakter verilerini okur.
# Örnek input: "cyberpunk_characters.csv"
# Örnek output: DataFrame (shape: [3, 6])
def load_character_data(filepath):
    pass

# 2. En yüksek strength değerine sahip ilk n karakteri döndürür.
# Örnek input: df, n=2
# Örnek output: DataFrame -> ["V", "Johnny Silverhand"]
def get_top_strength_characters(df, n=5):
    pass

# 3. Tüm karakterlerin sayısal ortalama değerlerini (strength, intelligence, agility, health) hesaplar.
# Örnek input: df
# Örnek output: {'strength': 71.66, 'intelligence': 84.33, ...}
def calculate_average_stats(df):
    pass

# 4. Belirli bir fraksiyona (faction) ait karakterleri filtreler.
# Örnek input: df, "Moxes"
# Örnek output: DataFrame (1 satırlık) -> "Judy Alvarez"
def filter_characters_by_faction(df, faction_name):
    pass

# 5. Health değerlerini 0-1 aralığına normalize eder.
# Örnek input: df
# Örnek output: df['health']: [1.0, 0.95, 0.85]
def normalize_health_points(df):
    pass

# 6. Sayısal sütunları NumPy matrisine dönüştürür.
# Örnek input: df
# Örnek output: NumPy array -> shape (3, 4)
def convert_to_numpy_matrix(df):
    pass

# 7. Intelligence değeri en yüksek karakteri döndürür.
# Örnek input: df
# Örnek output: Series -> "Johnny Silverhand"
def get_character_with_max_intelligence(df):
    pass

# 8. Agility değerine göre karakterleri küçükten büyüğe sıralar.
# Örnek input: df
# Örnek output: DataFrame (sorted by agility)
def sort_characters_by_agility(df):
    pass

# 9. Sayısal istatistikleri (mean, std, min, max...) içeren yeni bir özet DataFrame oluşturur.
# Örnek input: df
# Örnek output: df.describe() benzeri bir tablo
def create_stat_summary_dataframe(df):
    pass


# 10. DataFrame’i belirtilen bir dosya yoluna CSV olarak kaydeder.
# Örnek input: df, "output.csv"
# Örnek output: output.csv dosyası oluşur (geri döndürmeye gerek yok)
def export_dataframe_to_csv(df, output_path):
    pass