import logging
import pandas as pd
from pathlib import Path
from src.data.gerar_dataset_simulado import gerar_producao, salvar_dataset, TEMPO_PLANEJADO_MIN

RAW_PATH = Path(__file__).parents[2] / 'data' / 'raw'
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def pipeline_completo() -> pd.DataFrame:
    caminho = RAW_PATH / 'producao_simulado.csv'
    if not caminho.exists():
        salvar_dataset(gerar_producao())
    return pd.read_csv(caminho)
