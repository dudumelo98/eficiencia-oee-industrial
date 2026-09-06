# Análise de Eficiência Operacional e OEE Industrial

Decomposição de OEE (Disponibilidade x Performance x Qualidade) e identificação de gargalo por máquina, sobre base simulada de 4 máquinas.

## Resultados

| Máquina | OEE | Gargalo |
|---|---|---|
| M3 | 0,556 | Performance |
| M4 | 0,633 | Qualidade |
| M2 | 0,637 | Disponibilidade |
| M1 | 0,734 | Performance |

## Como rodar

```bash
pip install -r requirements.txt
python -m src.data.gerar_dataset_simulado
jupyter notebook notebooks/
pytest tests/
```

Detalhes completos em [reports/relatorio_final.md](reports/relatorio_final.md).
