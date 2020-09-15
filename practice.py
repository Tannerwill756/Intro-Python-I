import math
# word = "hello"

# def stutter(word):

#     print(f'{word[:2]}... {word[:2]}... {word}')


# stutter(word)


def cone_volume(h, r):
    answer = ((math.pi)*(r**2)*(h/3))
    print(round(answer, 2))


cone_volume(100, 2)
