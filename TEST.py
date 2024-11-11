from random import randint
from Bulls_Cows import god_top_rnd, valiadate_secret


for i in range(20000):
    god_secret = valiadate_secret(str(randint(0,god_top_rnd(randint(100000,999999)))), str(god_top_rnd(randint(100000,999999))))
    if god_secret.startswith("000"):
        print(god_secret)