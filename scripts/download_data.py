import os
import kagglehub

def baixar_dataset():
    data_path = "data/brazil_total_aeronautical_occurrences_2010_2021.csv"
    if not os.path.exists(data_path):
        print("⏬ Baixando dataset do KaggleHub...")
        path = kagglehub.dataset_download("liamarguedas/brazil-total-aeronautical-occurrences-2010-2021")
        print("✔️ Dataset baixado em:", path)
    else:
        print("📁 Dataset já existe.")

if __name__ == "__main__":
    baixar_dataset()
