import sys


def flag(size):
    """Main function. Flag drawing."""
    validation(size)
    size = int(size)
    zero_matrix = [[' ' for _ in range(int(size*1.5+1))] for _ in range(size+1)]
    matrix = draw_flag(zero_matrix, size)
    string = string_output(matrix)
    return string


def validation(size):
    """Validation. The size value must be an integer real even number."""
    if not size.isdecimal() or size == '0' or int(size) % 2 != 0:
        raise Exception(AttributeError)


def draw_flag(matrix, size):
    """
    The implementation of drawing is done through drawing a quarter
    of the flag and its subsequent mirroring.
    """
    matrix = draw_quarter_flag(matrix, size)
    matrix = add_other_parts_flag(matrix)
    return matrix


def draw_quarter_flag(matrix, size):
    """
    Draws a quarter of the flag. Successive borders, crosses and zeros.
    """
    vertical_length = size
    horizontal_length = int(size*3/2)
    matrix = draw_borders(matrix, size)
    matrix = draw_x_marker(vertical_length, horizontal_length, size, matrix)
    matrix = draw_o_marker(vertical_length, horizontal_length, size, matrix)
    return matrix


def add_other_parts_flag(matrix):
    """Mirror reflection."""
    for idx, token in enumerate(matrix):
        matrix[idx] += matrix[idx][::-1]
    matrix += matrix[::-1]
    return matrix


def draw_borders(matrix, size):
    """Borders are drawn. First top then side."""
    for i in range(int(size*1.5+1)):
        matrix[0][i] = '#'
    for i in range(int(size+1)):
        matrix[i][0] = '#'
    return matrix


def draw_x_marker(v, h, size, matrix):
    """Drawing 'x' markers."""
    length = int(size/2)
    count = 0
    offset_y, offset_x = 0, int(size/2)-1
    while count < length:
        matrix[v-offset_y][h-offset_x] = 'x'
        offset_y += 1
        offset_x -= 1
        count += 1
    return matrix


def draw_o_marker(v, h, size, matrix):
    """Drawing 'o' markers."""
    for t in range(1, int(size/2)):
        length = int(size/2)-t
        count = 0
        offset_y, offset_x = 0, int(size/2)-1-t
        while count < length:
            matrix[v-offset_y][h-offset_x] = 'o'
            offset_y += 1
            offset_x -= 1
            count += 1
    return matrix


def string_output(matrix):
    """Single line output."""
    string = ''
    for token in matrix:
        string += ''.join(token) + '\n'
    return string.rstrip('\n')


if __name__ == '__main__':
    arg = sys.argv[1]
    print(flag(arg))
