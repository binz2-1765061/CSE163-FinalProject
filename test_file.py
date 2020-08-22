from cse163_utils import assert_equals
import pandas as pd
import question_3 as q3
import question_1 as q1

"""
Provide test methods for question_1 and question_3
"""


def test_question_1(data):
    """
    provide different cases to test methods in question_1
    program crashes if don't meet the expection result
    """
    assert_equals(6706, q1.gold_difference(data))
    assert_equals(5, q1.kill_difference(data))
    assert_equals(9, q1.assist_difference(data))
    assert_equals(7280, q1.damage_difference(data))


def test_question_3(data):
    """
    provide different cases to test methods in question_3
    program crashes if don't meet the expection result
    """
    assert_equals(("Spectre", 23995), q3.richest_hero(data))
    assert_equals(("Earthshaker", 8598), q3.poorest_hero(data))
    assert_equals(("Spectre", 18), q3.killer_hero(data))
    assert_equals(("Queen of Pain", 15), q3.burden_hero(data))
    assert_equals(("Clockwerk", 3), q3.escape_hero(data))
    assert_equals(("Alchemist", 2), q3.most_popular_hero(data))
    assert_equals(("Abaddon", 1), q3.least_popular_hero(data))
    assert_equals(("Spectre", 31122), q3.damage_hero(data))


def main():
    """
    Run the test functions
    """
    data = pd.read_csv("CSV_files/test.csv")
    print(data.loc[:, ("kills", "win")])
    test_question_1(data)
    test_question_3(data)


if __name__ == "__main__":
    main()
