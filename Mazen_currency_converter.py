import json, urllib.request
try:
    Amount = float(input("Please Enter the Amount? "))
except ValueError:
    print("Please enter float number")

org_currency=input("Please Enter the three letters of the oreginal currency code ").upper()
if len(org_currency)!=3:
    print("please enter three letters as code of currency")
else:
    print("Your origenal currency is: "+org_currency)
    tar_currency=input("Please Enter the three letters of the target currency code,\n and if you want all available  currency write *: ").upper()
      
       #Load the table of exchange rates         
    try:
            with urllib.request.urlopen("http://api.fixer.io/latest?base="+org_currency) as url:
                data = json.loads(url.read().decode())

            with urllib.request.urlopen("https://openexchangerates.org/api/currencies.json")as c_url:
                countries= json.loads(c_url.read().decode())
            if tar_currency == "*": 
                print("Your order to know the exchange rate in all available  currency ")
                for i in data['rates']:
                  print ("exchange amount: " +str(Amount) +" from "+
                        countries[org_currency]+" to the target currency "+countries[i]+" is : "+ str(Amount*float(data['rates'][i]))+" ,")
            else:
                print("Your target currency is: "+tar_currency)
                result = float(data['rates'][tar_currency])*Amount
                print("exchange amount: " +str(Amount) +" from "+
                       countries[org_currency]+"\n to the target currency "+countries[tar_currency]+" is : "+ str(result))
    except ValueError:
            print("You could have wrong code or the currency is not available,\n or service is not available right now try again later")
