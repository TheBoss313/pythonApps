import requests
import sys

if "help" in sys.argv or "-help" in sys.argv or "--help" in sys.argv:
    print("Converts money. Parameters: OriginalCurrency, NewCurrency, Amount [Default 1]")
else:
    try:
        base = sys.argv[1].upper()
        new = sys.argv[2].upper()
        amount=sys.argv[3].upper()
        url = f'https://api.exchangerate.host/latest?base={base}&amount={amount}'
        response = requests.get(url)
        data = response.json()
        print(f'{amount} {base} converted to {new} is {data["rates"][new]}')
    except:
        if len(sys.argv) == 3:
            amount = 1
        url = f'https://api.exchangerate.host/latest?base={base}&amount={amount}'
        response = requests.get(url)
        data = response.json()
        print(f'{amount} {base} converted to {new} is {data["rates"][new]}')
