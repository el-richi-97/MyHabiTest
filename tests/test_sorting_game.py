from sorting.sorting_game import sort_blocks_v2, sort_blocks


def test_sort_blocks_test_array_1():
    """
    Tests that the v1.0 method of sorting the blocks given in the documentation returns the desired string with
    sorted and separated blocks of digits, from the 1st sample list.
    """
    test_array_1 = [1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1]
    result_str_1 = sort_blocks(test_array_1)

    assert result_str_1 == '123 1378 167'


def test_sort_blocks_test_array_2():
    """
    Tests that the v1.0 method of sorting the blocks given in the documentation returns the desired string with
    sorted and separated blocks of digits, from the 2nd sample list.
    """
    test_array_2 = [2, 1, 0, 0, 3, 4]
    result_str_2 = sort_blocks(test_array_2)

    assert result_str_2 == '12 x 34'


def test_sort_blocks_v2_test_array_1():
    """
    Tests that the v2.0 method of sorting the blocks given in the documentation returns the desired string with
    sorted and separated blocks of digits, from the 1st sample list.
    """
    test_array_1 = [1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1]
    result_str_1 = sort_blocks_v2(test_array_1)

    assert result_str_1 == '123 1378 167'


def test_sort_blocks_v2_test_array_2():
    """
    Tests that the v2.0 method of sorting the blocks given in the documentation returns the desired string with
    sorted and separated blocks of digits, from the 2nd sample list.
    """
    test_array_2 = [2, 1, 0, 0, 3, 4]
    result_str_2 = sort_blocks_v2(test_array_2)

    assert result_str_2 == '12 x 34'
