# Dados

Produção diária simulada de 4 máquinas, 120 dias cada, com perfil de gargalo diferente por máquina.

## Por que simulado

O UCI AI4I 2020 traz sensor industrial agregado, não histórico de produção diário por máquina com disponibilidade, performance e qualidade separados, que é o que preciso para decompor OEE. Gerei uma base sintética (`src/data/gerar_dataset_simulado.py`).

## Geração

```bash
python -m src.data.gerar_dataset_simulado
```
