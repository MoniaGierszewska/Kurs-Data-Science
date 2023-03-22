from figures.flat import *

aliases = {
    "ra": rectangle_area,
    "rc": rectangle_circuit
}
aliases.get("XX", print)(10,10)

