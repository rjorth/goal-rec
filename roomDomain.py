from py2pddl import Domain, create_type
from py2pddl import predicate, action


# predicates are basically fluents which serve as pre and post conditions
# the action methods continually update the current state
# roomDomain'
class RoomDomain(Domain):
    Person = create_type("Person")
    Mug = create_type("Mug")
    Room = create_type("Room")
    Location = create_type(
        "Location")  # within the room. might can be where the desk is (working/studying) or where the whiteboard is

    # enter room > get mug > move > get marker [goal is teach class]

    @predicate(Person, Location)
    def at_location(self, p, lo):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(Person, Mug)
    def has_mug(self, p, m):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(Person, Room)
    def in_room(self, p, r):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @action(Person, Location, Room)
    def move(self, p, lo, r):
        precondition = [self.in_room(p, r), ~self.atLocation(p, lo)]
        effect = [self.atLocation(p, lo),self.in_room(p, r)]
        return precondition, effect

    @action(Mug, Person, Room)
    def get_mug(self, m, p, r):
        precondition = [~self.has_mug(p, m), self.in_room(p, r)]
        effect = [self.has_mug(p, m), self.in_room(p, r)]
        return precondition, effect

    @action(Mug, Person, Room)
    def leave_mug(self, m, p, r):
        precondition = [self.in_room(p, r), self.has_mug(p, m)]
        effect = [self.in_room(p, r), ~self.has_mug(p, m)]
        return precondition, effect

    @action(Person, Room)
    def enter_room(self, p, r):
        precondition = [~self.in_room(p, r)]
        effect = [self.in_room(p, r)]
        return precondition, effect


from py2pddl import goal, init


class RoomProblem(RoomDomain):

    def __init__(self):
        super().__init__()
        self.mug = RoomDomain.Mug.create_objs([1], prefix="m")
        self.person = RoomDomain.Person.create_objs([1], prefix="p")
        self.room = RoomDomain.Room.create_objs([1], prefix="r")

    @init
    def init(self):
        at = [self.has_mug(self.person[1], self.mug[1]),
              self.in_room(self.person[1], self.room[1])]
        return at

    @goal
    def goal(self):
        return [self.has_mug(self.person[1], self.mug[1]),
                self.in_room(self.person[1], self.room[1])]
