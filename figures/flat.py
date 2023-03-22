def rectangle_area(edge_a, edge_b):
    return edge_a * edge_b

def rectangle_circuit(edge_a, edge_b):
    return (2 * edge_a) +( 2 * edge_b)

def is_square (edge_a, edge_b):
    return edge_a == edge_b

def circle_area(r):
    return 3.1415 * (r ** 2)

def circle_circuit(r):
    return 2 * 3.1415 *r

print(circle_area(20))

print(circle_circuit(13))
