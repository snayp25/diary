import speech_recognition as sr
import random
import time
from speach import audio



levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]

}


def play_game(level):
    w = random.choice(levels[level])
    print(f'Приготовбся сказать это слово: {w}')
    
    try:
        a = audio()
        if a.lower() == w.lower():
            print('верно!')
        else:
            print(':(')
            print(f'я услышал твое слово как {a}')
    except:
        print('я даже не понял что ты сказал')
play_game("easy")