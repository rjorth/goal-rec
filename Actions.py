class Action:
    def __init__(self, name):
        self.name = name
        self.children_actions = []
        self.cost = 1

    def add_child_action(self, action_name):
        child_action = Action(action_name)
        self.children_actions.append(child_action)
        return child_action

    def find_action(self, action_name):
        #print("Analyzing node " + self.name)

        if self.name == action_name:
            #print("Found action " + action_name)
            return self

        for action in self.children_actions:
            a = action.find_action(action_name)
            if a is not None:
                return a

        return None


def create_making_breakfast_tree():
    root = Action("root")

    get_glass_action = root.add_child_action("have_glass")
    juice_oranges_action = get_glass_action.add_child_action("juice_oranges")
    drink_juice_goal = juice_oranges_action.add_child_action("drink_juice")

    get_mug_action = root.add_child_action("get_mug")
    grind_beans_action = get_mug_action.add_child_action("grind_beans")
    drink_coffee_goal = grind_beans_action.add_child_action("drink_coffee")

    get_bagel_action = root.add_child_action("get_bagel")
    spread_cheese_action = get_bagel_action.add_child_action("spread_cheese")
    eat_bagel_goal = spread_cheese_action.add_child_action("eat_bagel")

    return root


breakfast_tree = create_making_breakfast_tree()

breakfast_tree.find_action("eat_bagel")
breakfast_tree.find_action("drink_coffee")
breakfast_tree.find_action("drink_juice")
breakfast_tree.find_action("whatever")
breakfast_tree.find_action("grind_beans")
