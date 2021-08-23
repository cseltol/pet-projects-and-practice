import time
import heapq
import random
from enum import Enum, auto

"""
Explicit Finite-State Machine(FSM) 
"""


class Operation(Enum):
    WAIT = auto()
    STOP = auto()


class State(Enum):
    WAITING = auto()
    COUNTING = auto()
    LAUNCHING = auto()


class Launch:
    def __init__(self, delay, countdown):
        self._state = State.WAITING
        self._delay = delay
        self._countdown = countdown

    def step(self):
        if self._state is State.WAITING:
            self._state = State.COUNTING
            return Operation.WAIT, self._delay
        if self._state is State.COUNTING:
            if self._countdown == 0:
                self._state = State.LAUNCHING
            else:
                print(f'{self._countdown}...')
                self._countdown -= 1
                return Operation.WAIT, 1
        if self._state is State.LAUNCHING:
            print('Rocket launched!')
            return Operation.STOP, None
        assert False, self._state


def now():
    return time.time()


def random_delay():
    return random.random() * 5


def random_countdown():
    return random.randrange(5)


def launch_rocket(delay, countdown):
    time.sleep(delay)
    for i in reversed(range(countdown)):
        print(f'{i + 1}...')
        time.sleep(1)
    print('Rocket launched!')


def rockets():
    n = 10_000
    return [
        (random_delay(), random_countdown())
        for _ in range(n)
    ]


def run_fsm(r):
    """
    Run rockets using Finite-State Machine(FSM) method
    """
    start = now()
    work = [(start, i, Launch(d, c)) for i, (d, c) in enumerate(r)]

    while work:
        step_at, _id, launch = heapq.heappop(work)
        wait = step_at - now()
        if wait > 0:
            time.sleep(wait)
        op, arg = launch.step()
        if op is Operation.WAIT:
            step_at = now() + arg
            heapq.heappush(work, (step_at, _id, launch))
        else:
            assert op is Operation.STOP


if __name__ == '__main__':
    run_fsm(rockets())
