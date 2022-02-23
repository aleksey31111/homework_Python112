from math import pi, pow


def square_figure(figure_type, **kwargs):
    if figure_type == 'rhombus':
        return (kwargs['d1'] * kwargs['d2']) / 2
    elif figure_type == 'square':
        return pow(kwargs['a'], 2)
    elif figure_type == 'trapezoid':
        return ((kwargs['a'] + kwargs['b']) * kwargs['h']) / 2
    elif figure_type == 'circle':
        return pow(kwargs['r'], 2) * pi
    elif figure_type == 'unknown':
        return "invalid data"


print(square_figure(figure_type='rhombus', d1=10, d2=8))
print(square_figure(figure_type='square', a=5))
print(square_figure(figure_type='trapezoid', a=12, b=3, h=6))
print(square_figure(figure_type='circle', r=18))
print(square_figure(figure_type='unknown', a=1, b=2, c=3))
