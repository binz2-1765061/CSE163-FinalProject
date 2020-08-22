import os

import pandas as pd

import graph
import question_1 as q1
import question_3 as q3
import tools
from question_2 import randomforest


def run_decision(bool):
    """
    detemine if the user want to run the program
    :param bool: user input of a boolean of either True or False
    : return: return boolean
    """
    return bool


def main():
    # load csv files needed for data processing
    players = pd.read_csv("CSV_files/players.csv")
    hero = pd.read_csv("CSV_files/hero_names.csv")
    match = pd.read_csv("CSV_files/match.csv")
    item = pd.read_csv("CSV_files/item_ids.csv")

    # create variable run_data to determine if user wants to run data
    # modification
    # Warning it takes around an hour to run data modification
    # Warning it takes hour to run the RandomForest for Question 2
    run_data = run_decision(False)
    run_RandomForest = run_decision(False)

    # accessing if the user wants to run the data modification part
    if run_data is True:
        if os.path.exists("user_files/csv_files/final_data.csv"):
            os.remove("user_files/csv_files/final_data.csv")
            tools.data_csv(players, hero, match, item, NUM_OF_GAME=20000)
        else:
            tools.data_csv(players, hero, match, item, NUM_OF_GAME=20000)
        data = pd.read_csv("user_files/csv_files/final_data.csv")
    else:
        data = pd.read_csv("result_csv/final_data.csv")

    # run the answer for first Question
    q1.difference_stats(data)

    # accessing if the user wants to run the RandomForest
    if run_RandomForest is True:
        if os.path.exists("user_files/csv_files/randomforest_trees.csv"):
            os.remove("user_files/csv_files/randomforest_trees.csv")
            randomforest(data)

    # run the answer for third Question
    q3.hero_stats(data)
    graph.kills_damage(data)
    graph.gold_graph(data, match)
    graph.damage_graph(data, match)


if __name__ == "__main__":
    main()
