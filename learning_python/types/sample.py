from typing import Dict, List, Optional, Set, Tuple, Union, cast

import numpy as np

a: Union[int, None]  # Union[x, None] is same as Optional[x]
a = None

b: Optional[int] = None

c: List[float] = [3]

d: List[list] = [[4]]

e: Tuple[int, float] = 2, 3

f: Set = {2, 3}

g: Dict = {"a": 1, "b": 2}

h: Union[List, np.ndarray] = np.array([1, 2])
h = [2, 3]


def add_one(x: int) -> int:
    return x + 1


if __name__ == "__main__":
    print(a)
    print(b)
    print(c)
    print(f)
    m: Optional[int] = 0
    m = cast(int, m)  # Optional[int] cannot be put directly
    print(add_one(m))
