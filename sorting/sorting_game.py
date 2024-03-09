import random


def sort_blocks(my_array: list) -> str:
    """
    Sorting blocks (version 1.0) was designed to iterate through the given list and grouping all the blocks using 0
    as a delimiter and packing all this blocks in list inside another result list. If the list has two continuous 0's
    the method will pack an empty list. This method use a simply and direct method that need to pack an sort the blocks
    inside the same and regular loop method.
    :param my_array: list. Is the 'MyArray' list given in the documentation, it will a list of any size with the digits
    from 0 to 9.
    :return: str. The sorted blocks of 'MyArray' and separated with spaces or x depending if the blocks in the list
    was empty or with digits.
    """
    all_blocks = []
    actual_block = []

    for value in my_array:
        if value == 0:
            if actual_block:
                all_blocks.append(''.join(sorted(actual_block)))
                actual_block = []

            else:
                all_blocks.append('x')

        else:
            actual_block.append(str(value))

    if actual_block:
        all_blocks.append(''.join(sorted(actual_block)))

    return ' '.join(all_blocks)


def sort_blocks_v2(my_array: list) -> str:
    """
    Sorting blocks (version 1.0) was designed to (try to) improve the iteration through the given list and grouping
    all the blocks using 0 as a delimiter and packing all this blocks in list inside another result list. If the list
    has two continuous 0's the method will pack an empty list. While the 1.0 method do all in the same loop, this
    new method first do the splitting job in a separated method (called split) and then in this method, the splitted
    block list is operated with a list comprehension. This v2 method will be more efficient than the v1.
    :param my_array: list. Is the 'MyArray' list given in the documentation, it will a list of any size with the digits
    from 0 to 9.
    :return: The sorted blocks of 'MyArray' and separated with spaces or x depending if the blocks in the list
    was empty or with digits.
    """

    sortered_blocks = [''.join(sorted(str(value) for value in block)) or 'x' for block in split(my_array, 0)]

    return ' '.join(sortered_blocks)


def split(my_array: list, delimiter: int) -> list:
    """
    The split method is created to be used inside the v2 sort_blocks function. It's simple, you give a list with
    the digits and you can set a delimiter (in the documentation of this test, it's 0).
    :param my_array: list. Is the 'MyArray' list given in the documentation, it will a list of any size with the digits
    from 0 to 9.
    :param delimiter: The number you want to be the delimiter to split the list in blocks.
    :return: list. A new list with lists within (the blocks of digits needed to proceed with the sorting),
    kinda a matrix.
    """
    all_blocks = []
    actual_block = []

    for value in my_array:
        if value == delimiter:
            all_blocks.append(actual_block)
            actual_block = []

        else:
            actual_block.append(value)

    if actual_block:
        all_blocks.append(actual_block)

    return all_blocks


def print_results(my_array: list, v2: bool = True) -> None:
    """
    This is for print the results of the operation of the 'MyArray' list and the result of sorting a separating the
    blocks of digits in one string.
    :param v2: bool. Is just to define if you wanna use the first method or the v2 method.
    :param my_array: list. Is the 'MyArray' list given in the documentation, it will a list of any size with the digits
    from 0 to 9.
    """
    result = sort_blocks(my_array) if not v2 else sort_blocks_v2(my_array)

    print(f'Input list: {my_array} | Size: {len(my_array)}')
    print(f'Output: {result}\n')


if __name__ == '__main__':

    test_array_1 = [1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1]
    test_array_2 = [2, 1, 0, 0, 3, 4]
    test_custom = [4, 3, 9, 3, 2, 0, 7, 5, 3, 0, 0, 9, 3, 1]

    the_definitive_last_stand_heavy_test_array = [random.randint(0, 9) for _ in range(50)]

    use_version_2 = True

    print_results(test_array_1, v2=use_version_2)
    print_results(test_array_2, v2=use_version_2)
    print_results(test_custom, v2=use_version_2)
    print_results(the_definitive_last_stand_heavy_test_array, v2=use_version_2)
