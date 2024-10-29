# H3 - Opgave: Mini ELT Data Pipeline

Dette projekt bruger energidataservice.dk API til at hente energidata og afprøve ELT.

## Brug

For at installere nødvendige pakker, kør følgende kommando:

```sh
pip install -r requirements.txt
```

Kør `main.py` script:

```sh
python main.py
```

For at skifte årstal, angives et årstal i `year` i `main.py`

## Oversigt

- **extract.py**: Henter energidata fra et givent årstal.
- **load.py**: Loader dataen ind i CSV-format.
- **transform.py**: Bruger kun `ExchangeGermany` og beregner:
  - Net Export DK1 (MW)
  - Net Export DK2 (MW)
  - Total Net Export (MW)
  - Export Percentage (%)
- **save_results.py**: Gemmer det transformerede data i en TXT-fil.

## Filstruktur

- `main.py`: Hovedscript.
- `config.py`: API URL, mapper.
- `extract.py`: Henter data fra API.
- `load.py`: Gemmer data i CSV-format.
- `transform.py`: Beregner data.
- `save_results.py`: Gemmer resultater til en TXT-fil.
- `ensure_directories.py`: Sikrer, at mapperne eksisterer.

