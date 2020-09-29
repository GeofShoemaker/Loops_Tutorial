songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0])
print(songs[len(songs)-1])
print(songs[1:2])
songs[len(songs)-1] = "Carousel"
songs.append("Your Love (Deja Vu)")
songs.append("Tokyo Drifting")
songs.append("Youuu")
del songs[2]
animals = ["Brown Bear", "Panda Bear", "Polar Bear"]
animals.append("Raccoon")
print(animals[2])
del animals[0]
for animal in animals:
    print(animal)