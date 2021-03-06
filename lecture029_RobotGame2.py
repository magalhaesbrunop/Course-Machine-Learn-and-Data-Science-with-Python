class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '<{}, {}>'.format(self.x, self.y)


class Reward(Point):
    def __init__(self, x, y, name):
        super(Reward, self).__init__(x, y)
        self.name = name

    def __str__(self):
        return '<{}, {}>: {}'.format(self.x, self.y, self.name)

    def __repr__(self):
        return '<Reward> {}'.format(str(self))


"""
reward1 = Reward(1, 1, 'gold coin')
print('',reward1.x, '\n', reward1.name)
"""


class Robot(Point):
    def move_up(self):
        if self.y < 10:
            self.y = self.y + 1
        else:
            print('Forbidden movement')

    def move_down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            print('Forbidden movement')

    def move_left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            print('Forbidden movement')

    def move_right(self):
        if self.x < 10:
            self.x = self.x + 1
        else:
            print('Forbidden movement')


def check_reward(robot, rewards):
    ok = False
    for reward in rewards:
        if reward.x == robot.x and reward.y == robot.y:
            print("The robot found an item: {}".format(reward.name))
            ok = True
    return ok


import random

robot1 = Reward(random.randint(0, 10), random.randint(0, 10), 'coin')
robot2 = Reward(random.randint(0, 10), random.randint(0, 10), 'energy')
robot3 = Reward(random.randint(0, 10), random.randint(0, 10), 'laser arm')
robot4 = Reward(random.randint(0, 10), random.randint(0, 10), 'coin')
robot5 = Reward(random.randint(0, 10), random.randint(0, 10), 'energy')
robot6 = Reward(random.randint(0, 10), random.randint(0, 10), 'laser arm')
robot7 = Reward(random.randint(0, 10), random.randint(0, 10), 'coin')
robot8 = Reward(random.randint(0, 10), random.randint(0, 10), 'energy')
robot9 = Reward(random.randint(0, 10), random.randint(0, 10), 'laser arm')
rewards = [robot1, robot2, robot3]

robot = Robot(random.randint(0, 10), random.randint(0, 10))
for i in range(10):
    movement = input('Write which do you want: up, down, right, left\n')
    if movement == 'up':
        robot.move_up()
    elif movement == 'down':
        robot.move_down()
    elif movement == 'left':
        robot.move_left()
    elif movement == 'right':
        robot.move_right()
    else:
        print('Forbidden movement')
        continue
    print(robot)
    check_reward(robot, rewards)

