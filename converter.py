"""
USD to BRL converter with IOF tax calculation.

Converts a US dollar amount to Brazilian reais and applies IOF
(Imposto sobre Operacoes Financeiras), the Brazilian financial
operations tax levied on foreign currency transactions.

Author: Daniel Batista
License: MIT
"""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

# IOF rate for international credit card purchases.
# This rate is set by federal decree and has changed several times;
# verify the current value before relying on the output.
DEFAULT_IOF_RATE = Decimal("0.0338")

CENTS = Decimal("0.01")


def convert(amount_usd, exchange_rate, iof_rate=DEFAULT_IOF_RATE):
    """
    Convert a USD amount to BRL and apply IOF.

    Args:
        amount_usd:    Amount in US dollars.
        exchange_rate: USD to BRL rate.
        iof_rate:      IOF rate as a decimal fraction (0.0338 = 3.38%).

    Returns:
        dict with keys: subtotal, iof, total — all Decimal, rounded to cents.

    Raises:
        ValueError: if any input is negative, or the exchange rate is zero.
    """
    amount_usd = Decimal(str(amount_usd))
    exchange_rate = Decimal(str(exchange_rate))
    iof_rate = Decimal(str(iof_rate))

    if amount_usd < 0:
        raise ValueError("Amount cannot be negative.")
    if exchange_rate <= 0:
        raise ValueError("Exchange rate must be greater than zero.")
    if iof_rate < 0:
        raise ValueError("IOF rate cannot be negative.")

    subtotal = amount_usd * exchange_rate
    iof = subtotal * iof_rate
    total = subtotal + iof

    return {
        "subtotal": subtotal.quantize(CENTS, rounding=ROUND_HALF_UP),
        "iof": iof.quantize(CENTS, rounding=ROUND_HALF_UP),
        "total": total.quantize(CENTS, rounding=ROUND_HALF_UP),
    }


def prompt_decimal(message):
    """Prompt until the user provides a valid number."""
    while True:
        try:
            return Decimal(input(message).strip().replace(",", "."))
        except (InvalidOperation, ValueError):
            print("  Please enter a valid number.")
        except (KeyboardInterrupt, EOFError):
            print()
            raise SystemExit(0)


def main():
    print("USD to BRL converter (with IOF)")
    print("-" * 34)

    amount_usd = prompt_decimal("Amount in USD: ")
    exchange_rate = prompt_decimal("USD to BRL exchange rate: ")

    try:
        result = convert(amount_usd, exchange_rate)
    except ValueError as error:
        print("Error: {}".format(error))
        raise SystemExit(1)

    print()
    print("Subtotal (no IOF):  R$ {:>12,.2f}".format(result["subtotal"]))
    print("IOF ({:.2f}%):        R$ {:>12,.2f}".format(
        DEFAULT_IOF_RATE * 100, result["iof"]))
    print("-" * 34)
    print("Total:              R$ {:>12,.2f}".format(result["total"]))


if __name__ == "__main__":
    main()
