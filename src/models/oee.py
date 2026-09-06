"""Decomposicao de OEE (Disponibilidade x Performance x Qualidade) e analise de gargalo."""
import pandas as pd

TEMPO_CICLO_IDEAL = 1.0


def calcular_oee(df: pd.DataFrame, tempo_planejado_min: float) -> pd.DataFrame:
    df = df.copy()
    df['disponibilidade'] = df['tempo_operando_min'] / tempo_planejado_min
    df['performance'] = (df['unidades_produzidas'] * TEMPO_CICLO_IDEAL) / df['tempo_operando_min']
    df['qualidade'] = df['unidades_boas'] / df['unidades_produzidas']
    df['oee'] = df['disponibilidade'] * df['performance'] * df['qualidade']
    return df


def identificar_gargalo(df_oee: pd.DataFrame) -> pd.DataFrame:
    """Pra cada maquina, aponta qual dos 3 componentes do OEE e o mais fraco (o gargalo)."""
    resumo = df_oee.groupby('maquina')[['disponibilidade', 'performance', 'qualidade', 'oee']].mean()
    resumo['gargalo'] = resumo[['disponibilidade', 'performance', 'qualidade']].idxmin(axis=1)
    return resumo.sort_values('oee')
