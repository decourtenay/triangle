with open("zadanie_4_triangle_big.txt") as file:

    triangle = file.readlines()
    triangle_list = []
    for line in triangle:
        line_list = []
        for elem in line.split():
            elem = int(elem)
            line_list.append(elem)
        triangle_list.append(line_list)
    triangle_list.reverse()
    for line in triangle_list[1:]:
        line_index = triangle_list.index(line)
        line_above = triangle_list[line_index-1]
        for elem in line:
            elem_index = line.index(elem)
            elem_above = line_above[elem_index]
            elem_right = line_above[elem_index+1]
            if elem_right > elem_above and elem_right:
                line[elem_index] = elem + elem_right
            else:
                line[elem_index] = elem + elem_above
    max_path_sum = line[0]
    print(f"Suma liczb w maksymalnej ścieżce to {max_path_sum}")


