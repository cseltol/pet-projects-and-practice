import time
import heapq
import random
import types
from enum import Enum, auto


"""
    Not Explicit Finite-State Machine(FSM)
"""


class Op(Enum):
    WAIT = auto()
    STOP = auto()


def now():
    return time.time()


def random_delay():
    return random.random() * 5


def random_countdown():
    return random.randrange(5)


@types.coroutine # for async
def sleep(delay):
    yield Op.WAIT, delay


async def launch_rocket(delay, countdown):
    # block WAITING
    await sleep(delay)
    # block COUNTING
    for i in reversed(range(countdown)):
        print(f'{i + 1}...')
        await sleep(1)
    # block LAUNCHING
    print('Rocket launched!')


# def launch_rocket(delay, countdown):
#     # block WAITING
#     yield from sleep(delay)
#     # block COUNTING
#     for i in reversed(range(countdown)):
#         print(f'{i + 1}...')
#         yield from sleep(1)
#     # block LAUNCHING
#     print('Rocket launched!')


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
    work = [(start, i, launch_rocket(d, c))
            for i, (d, c) in enumerate(r)]

    while work:
        step_at, id, launch = heapq.heappop(work)
        wait = step_at - now()
        if wait > 0:
            time.sleep(wait)
        try:
            op, arg = launch.send(None)
        except StopIteration:
            continue

        if op is Op.WAIT:
            step_at = now() + arg
            heapq.heappush(work, (step_at, id, launch))
        else:
            assert False, op


if __name__ == '__main__':
    run_fsm(rockets())