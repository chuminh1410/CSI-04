import math

def cal_diagonal(edge_length):
    diagonal = math.sqrt(edge_length**2 + edge_length**2)
    return diagonal

print(cal_diagonal(2))