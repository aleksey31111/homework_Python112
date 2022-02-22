from math import pi, pow


def square_figure(**kwargs):
    temp = list()
    # for key in kwargs:
        # if key == 'rhombus':
        #     for value in kwargs.values():
        #         if type(value) == int:
        #             temp.append(value)
        #     return temp[0] * temp[1] / 2
    if kwargs.keys() == 'square':
        for value in kwargs.values():
            print(value)
            # if type(value) == int:
            #     temp.append(value)
        # return pow(temp[0], 2)
        # elif key == 'trapezoid':
        #     for value in kwargs.values():
        #         if type(value) == int:
        #             temp.append(value)
        #     return ((temp[0] + temp[1]) * temp[3]) / 2
        # elif key == 'circle':
        #     for value in kwargs.values():
        #         if type(value) == int:
        #             return pi * pow(value, 2)
        # else:
        #     print("invalid data")


# print(square_figure(figure_type='rhombus', d1=10, d2=8))
print(square_figure(figure_type='square', a=5))
# print(square_figure(figure_type='trapezoid', a=12, b=3, h=6))
# print(square_figure(figure_type='circle', r=18))
# print(square_figure(figure_type='unknown', a=1, b=2, c=3))
