# USD to BRL Converter

Converts a US dollar amount to Brazilian reais and applies IOF
(*Imposto sobre Operações Financeiras*), the Brazilian tax levied on foreign
currency transactions.

## Usage

```bash
python converter.py
```

```
USD to BRL converter (with IOF)
----------------------------------
Amount in USD: 100
USD to BRL exchange rate: 5.42

Subtotal (no IOF):  R$       542.00
IOF (3.38%):        R$        18.32
----------------------------------
Total:              R$       560.32
```

## As a module

```python
from converter import convert

result = convert(amount_usd=100, exchange_rate=5.42)
print(result["total"])   # Decimal('560.32')
```

## Notes

- Monetary values use `Decimal`, not `float`. Binary floating point cannot
  represent most decimal fractions exactly, which produces rounding errors
  that accumulate in financial calculations.
- The IOF rate is set by federal decree and has changed several times.
  `DEFAULT_IOF_RATE` should be verified against the current rate before the
  output is used for anything that matters.
- The exchange rate is supplied by the user. Live rate lookup is on the
  roadmap below.

## Roadmap

This is the first working version. Planned:

- [ ] Live exchange rate via a public API, with a manual fallback
- [ ] Command-line arguments in addition to interactive prompts
- [ ] Support for other IOF rates (wire transfer, cash purchase, savings)
- [ ] Reverse conversion (BRL to USD)
- [ ] Unit tests
- [ ] Optional web interface

## License

MIT: see [LICENSE](LICENSE).
