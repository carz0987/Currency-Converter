import requests

API_key = "fca_live_5Dd54CjhNWpecV53oZBz8reLrFeihEAsrxO46mZ9"
base_url = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_key}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY", "BGN", "BRL", "CHF", "CZK", "DKK", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "ISK", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PLN", "RON", "RUB", "SEK", "SGD", "THB", "TRY", "ZAR"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{base_url}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    
    except Exception as e:
        return None
    
def convert_value(base, target):
    if target not in CURRENCIES:
        print("Invalid target currency, please try again.")
        return None
    
    currencies = target
    url = f"{base_url}&base_currency={base}&currencies={currencies}"

    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    
    except Exception as e:
        print("Invalid currency, please try again. ")
        return None

    

while True:

    choice = input("Welcome to the currency converter! Please press 1 to convert to all currency, or 2 to convert to a specific currency. Press 0 to quit: ")

    if choice == '0':
        print("Thank you, have a great day!")
        break

    elif choice == '1':
        curr = input("Please input a currency type (ex. USD). Press 0 to quit: ").upper()

        if curr == '0':
            print("Thank you, have a nice day!")
            break
        
        data = convert_currency(curr)

        if not data:
            print("Sorry, invalid input. Please enter a valid form of currency. ")
            continue

        try: 
            val = float(input("Please enter a value (ex. 100.00). Press 0 to quit: "))

            if val == 0:
                print("Thank you, have a nice day!")
                break
            
            newval = "{:.2f}".format(val)
            print(f"Here are the rates for {newval} {curr}: ")

            del data[curr]

            for ticker, value in data.items():
                formatted_value = "{:.2f}".format(value * val)
                print(f"{formatted_value} {ticker}")

        except ValueError:
            print("Sorry, please enter a correct value. ")
            continue

    elif choice == '2':
        curr = input("Please input a currency type (ex. USD). Press 0 to quit: ").upper()

        if curr == '0':
            print("Thank you, have a nice day!")
            break
        
        check = convert_currency(curr)

        if not check:
            print("Sorry, invalid input. Please enter a valid form of currency. ")
            continue

        try: 
            val = float(input("Please enter a value (ex. 100.00). Press 0 to quit: "))

            if val == 0:
                print("Thank you, have a nice day!")
                break

        except ValueError:
            print("Sorry, please enter a correct value. ")
            continue

        target = input("Input the currency type you want to convert to. Press 0 to quit: ").upper()

        if target == '0':
            print("Thank you, have a nice day!")
            break

        newdata = convert_value(curr, target)

        newval = "{:.2f}".format(val)
        print(f"Here is the rate for {newval} {curr} to {target}: ")

        for ticker, value in newdata.items():
            formatted_value = "{:.2f}".format(value * val)
            print(f"{formatted_value} {ticker}")



    
