albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984)
          ]

print(len(albums))

# this was my way of doing it which is clear and keeps album available for other use
# but this is not as efficient as the second method

# for album in albums:
#    name, artist, year = album
#    print("Album: {} Artist: {} Year {}".format(name, artist, year))


for name, artist, year in albums:
    print("Album: {} Artist: {} Year {}".format(name, artist, year))
