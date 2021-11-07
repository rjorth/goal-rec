fake_input = {"glass", "oranges", "haveGlass"}
current_state = {}
action_output = []


def get_glass():
    # check if the precondition is met
    if "glass" in fake_input:
        # if its in the input, then it is true (has been detected)
        # set post conditions. haveGlass is true in the current state
        # the cost is 1
        current_state["haveGlass"] = 1
        action_output.append("get_glass")
        print("Action: ", action_output, "\nCurrent State: ", current_state)

    else:
        print(False)


def juice_oranges():
    if "oranges" in fake_input and "haveGlass" in fake_input:
        current_state["haveJuice"] = 1
        action_output.append("juice_oranges")
        print("Action: ", action_output, "\nCurrent State: ", current_state)
    else:
        print(False)


def drink_juice():
    if "haveJuice" in fake_input:
        current_state.pop("haveJuice")
        current_state["haveJuiceNot"] = 1
        action_output.append("drink_juice")
        print("Action: ", action_output, "\nCurrent State: ", current_state)
    else:
        print(False)
