import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parents[1]))
import pandas as pd
from src.models.oee import calcular_oee


def test_oee_entre_zero_e_um():
    df = pd.DataFrame({'tempo_operando_min': [400], 'unidades_produzidas': [350], 'unidades_boas': [340]})
    resultado = calcular_oee(df, tempo_planejado_min=480)
    assert 0 < resultado.loc[0, 'oee'] < 1
