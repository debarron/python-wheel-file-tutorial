from my_package.fp_stuff import fp_module

_two_multiplayer = fp_module.multiplyer(2)
_add_five = fp_module.adder(5)

def multiply_by_two(num: int) -> int:
    return _two_multiplayer(num)


def start_by_five(num: int) -> int:
    return _add_five(num)

