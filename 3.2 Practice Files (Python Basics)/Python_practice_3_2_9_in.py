west_counties=("Arapahoe",'Denver','Jefferson')
east_counties=("El Paso","Boulder",'Aspen')

county=input("What county would you like to confirm?")

if county in west_counties or east_counties:
    print("That county is part of the database")
else:
    print("That county is not part of the database")