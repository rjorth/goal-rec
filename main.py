import run_acts

# a domain theory T = {F, A} where F is the fluents and A is a set of actions
if __name__ == '__main__':
    # define fluents (true/false states)
    f = {"haveGlass": 0,
         "oranges": 0,
         "glass": 0}

    run_acts.get_glass()
    run_acts.juice_oranges()
