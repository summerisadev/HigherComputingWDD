"""Validates an inputted score, takes in a min, max and score to be checked"""
def validateScore(min,max,score):
    state = False # we default the validation to false, as if something goes wrong, its better to supply a false than true
    code  = ""    # this is also returned if wanting to be logged
    dec   = 0

    dec = str(score).index(".") + 2

    if score < min or score > max:
        state = False
        code  = "OutOfBounds"
    # elif len(score) > 4:
    #     state = False
    #     code  = "TooLong"
    elif str(score)[dec] != "":
        state = False
        code  = "InvalidFormatting"
    else:
        state = True
    

    print(dec)


validateScore(0, 10, 9.85)