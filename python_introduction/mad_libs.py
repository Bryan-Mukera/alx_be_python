adjective_1 = input ("Enter the first adjective:")
adjective_2 = input ("Enter the second adjective:")
adjective_3 = input ("Enter the third adjective:")
noun = input ("Enter a noun:")
verb = input ("Enter a verb:")

first_story = (f"On a beautiful {adjective_1} day I went to the {noun}. I saw a funny monkey {verb} from the trees. Then, I spotted a majestic {adjective_2} lion lounging in the sun.  What a wild and {adjective_3} experience!")

print (first_story)

name = input("Enter your name:")
profession = input("Enter your profession:")
place = input ("Enter place:")
time = input ("Enter a time (e,g midnight, lunchtime):")
noun = input ("Enter a noun:")
verb = input ("Enter  verb")
adjective = input ("Enter an adjective")

if time == 'midnight':
  twist = "Moonlight revealed secret markings on the floor."
elif adjective == 'messy':
  twist = "Security footage showed something shocking"

second_story = (f"Detective {name}, a world-renowned {profession}, was summoned to investigate a baffling incident at the {place}. It was {time}, and the atmosphere was thick with tension. A valuable {noun} had vanished, and witnesses reported someone {verb} near the exhibit just moments before. The scene was unusually {adjective}, raising suspicions of foul play. {twist} Everyone knew Detective {name} was the only one who could crack the case.")

print (second_story)
