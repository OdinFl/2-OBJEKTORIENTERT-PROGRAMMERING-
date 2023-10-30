
class Planet:
    " En klasse for å beskrive en planet"
    def __init__(self,navn:str,solavstand:float,radius:float) -> None:

        self.navn=navn
        self.solavstand=solavstand
        self.radius = radius

jorden = Planet( "Jorden", 152, 6371)
mars = Planet("Mars", 227.9, 3389.5)
jupiter = Planet("Jupiter", 778.5, 69911)
print(jorden.radius)
print(jorden)
print(jorden.navn)
print(jorden.solavstand)
print(jorden.radius)
print(mars)
print(mars.navn)
print(mars.solavstand)
print(mars.radius)
print(jupiter)
print(jupiter.navn)
print(jupiter.solavstand)
print(jupiter.radius)
# Oppgave 1: 
# Lag et objekt for Mars, Jupiter og Jorda, der du lagrer informasjon om navn, solavstand og radius. Lagre disse objektene i egne variabler

# Hva skjer om du skriver print(Jorda)?
# Hva skjer om du skriver print(Jorda.navn)?
# Prøv å skriv ut de andre attributtene til klassen

# OBS: pass på rekkefølgen i argumentene til konstruktøren.

# heltall = 1
# desimaltall = 3.14
# tekst = "Hei"

# print(type(heltall))
# print(type(desimaltall))
# print(type(tekst))