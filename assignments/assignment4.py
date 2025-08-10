def calculate_btw(price_incl_btw: float, rate: float = 21.0):
    return price_incl_btw * rate / (100 + rate)


def main():
    """
    Assignment also had 50 excl, check if it's included
    """
    price_incl_btw = 99.95
    btw = calculate_btw(price_incl_btw)
    print(f"Prijs inclusief BTW: €{price_incl_btw:.2f}")
    print(f"BTW (21%): €{btw:.2f}")


if __name__ == "__main__":
    main()
