import turtle
import pandas as pd

states = pd.read_csv("50_states.csv")
states_names = states['state'].tolist()

# print(states.state[1])

"""l = ['tiny' ,'apple', 'slices']
print(l.index('apple'))"""



# Screen and Turtle
tim = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
tim.hideturtle()
# tim.penup() # enable it if you want, i just like the animation.. i.e. the pendown :P
######


correct_guesses = []
game_on = True
while game_on:
    if len(correct_guesses) == 50:
        game_on = False
    else:
        title_box = f"{len(correct_guesses)}/50"
        answer_state = screen.textinput(title=title_box, prompt="What's another state's name?").title()
        if answer_state == 'Quit':
            # game_on = False
            break
        while answer_state not in states_names:
            print('Incorrect')
            answer_state = screen.textinput(title=title_box, prompt="What's another state's name?").title()
        if answer_state in states_names:
            if answer_state in correct_guesses:
                pass
            else:
                xy = states[states['state'] == answer_state]
                # y = states[states['state'] == answer_state]
                correct_guesses.append(answer_state)
                tim.goto(xy.x[states_names.index(answer_state)], xy.y[states_names.index(answer_state)])
                tim.write(answer_state)








# print(answer_state)


## This function gets the x and y coors of a click on screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
