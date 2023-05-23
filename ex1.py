import search
import random
import math

_debug_ = True

#Please write your IDs here.
ids = ["111111111", "111111111"]


class TaxiProblem(search.Problem):
    """This class implements a medical problem according to problem description file"""

    def __init__(self, initial):

        original_problem = initial.copy()
        new_rep = initial.copy()
        
        # Add gas station map to new_rep
        for row,value in enumerate(original_problem["map"]):
            for col,value2 in enumerate(original_problem["map"][row]):
                if value == 'G':
                    new_rep["gas_stations"] |= (row,col)


        # Insert into map the taxis themself. value in map = index of taxi in map
        for index,taxi in enumerate(original_problem["taxis"]):
            print(taxi)
            taxi_location = taxi["location"]
            # In the taxi location, Put the taxi index.
            new_rep["map"][taxi_location[0]][taxi_location[1]] = str(index)

        # Add Max fuel to taxis in new_rep
        for index,taxi in enumerate(original_problem["taxis"]):
            new_rep["taxis"][index]["max_fuel"] = taxi["fuel"]

        # Add empty passengers list to taxis in new_rep. passengers will be by index
        for index,taxi in enumerate(original_problem["taxis"]):
            new_rep["taxis"][index]["passengers"] = []

        if _debug_:
            print("new_rep: ", new_rep)

        search.Problem.__init__(self, new_rep)
        
    def actions(self, state):
        """Returns all the actions that can be executed in the given
        state. The result should be a tuple (or other iterable) of actions
        as defined in the problem description file"""

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""

    def goal_test(self, state):
        """ Given a state, checks if this is the goal state.
         Returns True if it is, False otherwise."""

    def h(self, node):
        """ This is the heuristic. It gets a node (not a state,
        state can be accessed via node.state)
        and returns a goal distance estimate"""
        return 0

    def h_1(self, node):
        """
        This is a simple heuristic
        """

    def h_2(self, node):
        """
        This is a slightly more sophisticated Manhattan heuristic
        """

    """Feel free to add your own functions
    (-2, -2, None) means there was a timeout"""


def create_taxi_problem(game):
    return TaxiProblem(game)

