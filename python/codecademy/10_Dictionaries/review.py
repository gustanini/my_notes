songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

#create a dictionary called plays

plays = {key:value for key, value in zip(songs, playcounts)}

print(plays)

#add song and update respect

plays["Purple Haze"] = 1

plays["Respect"] = 94

#create dictionary

library = {"The Best Songs": plays, "Sunday Feelings": {}}

print(library)