
import enum


class Direction(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()


def move(direction: Direction):
    if not isinstance(direction, Direction):
        raise ValueError('Invalid direction')

    print(f'Moving {direction.name}({direction.value})')


move(Direction.LEFT)
move(Direction.RIGHT)
