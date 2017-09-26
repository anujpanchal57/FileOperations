# cities = ["Mumbai", "Chennai", "Pune", "Thane", "Delhi"]
#
# # Switch the mode to W which means we want to write a file and specify the file after AS
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         # We've to specify the file in which content has to be written
#         print(city, file=city_file)

# cities = []
#
# # Reads the file CITIES.TXT
# with open("cities.txt", 'r') as city_file:
#     # For each separate city in cities.txt, we're appending it to cities
#     for city in city_file:
#
#         # cities.append(city)
#         # We can also write the above line as
#         # This line helps to remove the next lines which were previously added in the result after reading from the file
#         cities.append(city.strip('\n'))
# print(cities)
#
# # Printing each city separately
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish House Waltz"))
#
# # This will print contents into the file IMELDA
# with open("imelda", 'w') as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda", 'r') as imelda_file:
    contents = imelda_file.readline()

# Not a good idea to use EVAL here, but i gave it a try and nothing great
# It displays just the normal output
imelda = eval(contents)

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)




















