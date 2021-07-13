import copy
import random


class Hat:

    def __init__(self, **kwargs):
        contents = []
        for key in kwargs:
            for n in range(kwargs[key]):
                contents.append(key)
        self.contents = contents

    # method to remove balls at random
    def draw(self, number_to_draw):
        balls_drawn = []
        if number_to_draw >= len(self.contents):
            return self.contents
        else:
            for n in range(number_to_draw):
                i = random.randrange(len(self.contents))
                balls_drawn.append(self.contents.pop(i))
            self.contents = self.contents
            return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    bad = 0

    for n in range(num_experiments):
        # hat object containing balls
        hat_copy = copy.deepcopy(hat)
        # the colours drawn out of the copied hat object
        colours = hat_copy.draw(num_balls_drawn)
        # if each ball drawn matches an expected ball, add it to a count
        for key in expected_balls.keys():
            count = 0
            for x in range(len(colours)):
                if colours[x] == key:
                    count += 1
            if count < expected_balls[key]:
                bad += 1
                break

    return 1 - (bad / num_experiments)
