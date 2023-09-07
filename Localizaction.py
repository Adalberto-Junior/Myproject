import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
#formato de phonenumbers pricisa
telefone = "+351966989818"
telefone_ajus = phonenumbers.parse(telefone)
print(telefone_ajus)

#descubrir a localização 
local = geocoder.description_for_number(telefone_ajus, 'pt')
#print('\n')
print(local)

hora = timezone.time_zones_for_number(telefone_ajus) 
print(hora)
