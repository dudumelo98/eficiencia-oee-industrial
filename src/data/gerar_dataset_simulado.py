"""Gerador simulado de producao diaria por maquina, para calculo de OEE."""
import numpy as np
import pandas as pd
from pathlib import Path

RAW_PATH = Path(__file__).parents[2] / 'data' / 'raw'
SEED = 67
MAQUINAS = ['M1', 'M2', 'M3', 'M4']
TEMPO_PLANEJADO_MIN = 480


def gerar_producao(n_dias: int = 120, seed: int = SEED) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    # Cada maquina tem um perfil diferente de gargalo (disponibilidade,
    # performance ou qualidade), pra dar variedade no benchmarking.
    perfil = {
        'M1': {'disp': 0.90, 'perf': 0.85, 'qual': 0.97},
        'M2': {'disp': 0.75, 'perf': 0.88, 'qual': 0.96},
        'M3': {'disp': 0.92, 'perf': 0.65, 'qual': 0.95},
        'M4': {'disp': 0.88, 'perf': 0.90, 'qual': 0.80},
    }
    registros = []
    for maquina in MAQUINAS:
        p = perfil[maquina]
        for dia in range(n_dias):
            disponibilidade = np.clip(rng.normal(p['disp'], 0.05), 0.3, 1.0)
            performance = np.clip(rng.normal(p['perf'], 0.06), 0.3, 1.0)
            qualidade = np.clip(rng.normal(p['qual'], 0.03), 0.5, 1.0)

            tempo_operando = TEMPO_PLANEJADO_MIN * disponibilidade
            tempo_ciclo_ideal = 1.0  # min por unidade
            unidades_produzidas = int((tempo_operando * performance) / tempo_ciclo_ideal)
            unidades_boas = int(unidades_produzidas * qualidade)

            registros.append({
                'maquina': maquina, 'dia': dia,
                'tempo_planejado_min': TEMPO_PLANEJADO_MIN,
                'tempo_operando_min': round(tempo_operando, 1),
                'unidades_produzidas': unidades_produzidas,
                'unidades_boas': unidades_boas,
            })
    return pd.DataFrame(registros)


def salvar_dataset(df: pd.DataFrame) -> None:
    RAW_PATH.mkdir(parents=True, exist_ok=True)
    df.to_csv(RAW_PATH / 'producao_simulado.csv', index=False)
    print(f'{len(df)} registros de producao salvos')


if __name__ == '__main__':
    salvar_dataset(gerar_producao())
