import data
import random

score = 0
choice_p = ""
cont = True

print("welcome to 'Higher' or 'Lower' game")
gues1 = random.choice(data.data)
gues2 = random.choice(data.data)


def fol_count(gues1, gues2):
    followers1 = gues1['follower_count']
    followers2 = gues2['follower_count']
    return followers1, followers2

def game(followers1, followers2, choice_p, score):
    if choice_p == 'Higher':
        if followers1 > followers2:
            score +=1
            print(f"Right choice, your score is {score}\n{gues1['name']} have {gues1['follower_count']} milion followers and {gues2['name']} have {gues2['follower_count']} milion")
            return score, True
        else:
            print(f"Wrong, your score is {score}\n{gues1['name']} have {gues1['follower_count']} milion followers and {gues2['name']} have {gues2['follower_count']} milion")
            return score, False
    elif choice_p == 'Lower':
        if followers1 < followers2:
            score +=1
            print(f"Right choice, your score is {score}\n{gues1['name']} have {gues1['follower_count']} milion followers and {gues2['name']} have {gues2['follower_count']} milionn")
            return score, True 
        else:
            print(f"Wrong, your score is {score}\n {gues1['name']} have {gues1['follower_count']} milion followers and {gues2['name']} have {gues2['follower_count']} milion")
            return score, False
    else:
        return score, cont

def game_cont(gues1, gues2, choice_p):
    if choice_p == 'Higher':
        gues1 = gues1
        gues2 = random.choice(data.data)
        return gues1, gues2
    elif choice_p == 'Lower':
        gues1 = gues2
        gues2 = random.choice(data.data)
        return gues1, gues2

while cont:
    print(f" First Guess is:{gues1['name']}, {gues1['description']}, From:{gues1['country']} \n VERSUS")
    print(f" Opponent: {gues2['name']}, {gues2['description']}, From:{gues2['country']}")
    choice_p = input("Who have more followers? 'Higher' or 'Lower' ").capitalize()
    followers1, followers2 = fol_count(gues1, gues2)
    score, cont = game(followers1, followers2, choice_p, score)
    if cont:
        gues1, gues2 = game_cont(gues1, gues2, choice_p)