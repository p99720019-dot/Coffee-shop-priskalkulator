   #Kilde: The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
#Her har jeg laget en dictionary over de ulike kaffene man kan velge mellom og prisene kaffene koster.
coffees = {
   "espresso" : {
      "name": "Espresso",
      "price": 2.50
   },
   "americano" : {
         "name": "Americano",
         "price": 3
      },
      "latte" : {
         "name": "Latte",
         "price": 2.50
      },
      "cappuccino" : {
         "name": "cappuccino", 
         "price":3 
      },
      "macchiato": {
         "name": "Macchiato",
         "price": 2.50
      },
      "mocha": {
         "name": "Mocha",
         "price": 3.50
      },
      "flat white": {
         "name": "Flat White",
         "price": 2.50
       }
}
#Dette skriver ut i terminalen alle valgene man kan velge mellom
#Skriver ut navn og pris fra ordlisten og legger til kolon etter navnet og £ bak prisen
for coffee in coffees:
   print(coffees[coffee]["name"] + ": " + str(coffees[coffee]["price"])+ "£")

print("----------------------------")
#Her oppretter vi variabelen price som er totalprisen til bestillingen. Denne opptateres ved hvert valg
#Den leser inn brukeren sitt valg og lagrer dette i variabel coffee
#Forsøker å hente riktig kaffe fra ordlisten og prisen for den kaffen og legger det til på price variabelen 
#Hvis dette ikke går så skrives det ut en feilmelding og så får brukeren prøve på nytt
#Måten brukeren får prøve på nytt er en løkke som er evig. Hvis vi klarer å hente prisen til kaffen hopper vi ut av løkken med break.
price = 0
while True:
   coffee = input("What type of coffee would you like?").lower()
   try:
      price = price + coffees[coffee]["price"]
      break
   except:
      print("You typed wrong, try agen.")

#Her lagde jeg en dictionary for de ulike sizene som brukes og prisene til størelsen ved siden av.
sizes = {
   "m" : {
      "name": "M",
      "price": 0
   },
   "l" : {
      "name": "L",
      "price": 1
   },
   "xl" : {
      "name": "Xl",
      "price": 1.50
   }
}
#Dette skriver ut i terminalen alle størelsene som man kan velge mellom
#Skriver ut navn og pris fra ordlisten og legger til kolon etter navnet og £ bak prisen
for size in sizes:
   print(sizes[size]["name"] + ": " + str(sizes[size]["price"]) + "£")

#Forsøker å hente riktig størrelse fra ordlisten og prisen for den størrelsen du velger også legger det til på price variabelen 
#Hvis dette ikke går så skrives det ut en feilmelding så får brukeren prøve på nytt
#Måten brukeren får prøve på nytt er en løkke som er evig. Hvis vi klarer å hente prisen til størrelsen hopper vi ut av løkken med break.
while True:
   size = input("What size would you like?").lower()
   try:
      price = price + sizes[size]["price"]
      break
   except:
      print("You typed wrong, try agen.")

#Her bruker jeg if, elif for og spørre brukeren om de vil ha take away eller ikke med yes, no spørsmål
#Hvis brukeren svarer yes eller no så hopper løkken ut med break
#hvis brukeren svarer noe annet så begynner løkken på nytt og brukeren blir spurt på nytt.
while True:
   take_away = input("Would you like take away, yes or no?").lower()
   if take_away == "no":
      price = price + 0
      break
   elif take_away == "yes":
      price = price + 1
      break

print("----------------------------")
print("Total Cost: £" + str(price))