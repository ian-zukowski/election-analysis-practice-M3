counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict.keys():
#     print (county)

# for county, voters in counties_dict.items():
#     print(county, voters)

for county, voters in counties_dict.items():
    print(county+" has "+str(voters)+" registered voters.")