from random import choice, randint, randrange
from string import ascii_lowercase
from turtle import Turtle, Screen, bye, speed

def gen_hex_color():
    hex_data = [str(num) for num in range(0, 10)]
    hex_data.extend(list(ascii_lowercase[:6]))

    def p():
        return choice(hex_data)
    
    hex_code = f"#{p()}{p()}{p()}{p()}{p()}{p()}"
    return hex_code

def main():
    tim = Turtle()
    tim.pensize(5)
    tim.speed(10)
    while True:
        tim.color(gen_hex_color())
        tim.forward(randint(5, 50))
        tim.right(randrange(30, 361, 60))
        

if __name__ == "__main__":
    main()