"""
prepares a modified, clean output data file using all relevant datasets.
"""
import numpy as np
import pandas as pd


def player(data, NUM_OF_GAME):
    """
    select important features from the dataframe for further analysis
    :param data: main dataframe file
    :param NUM_OF_GAME: total number of matches in the analysis
    :return: modified dataframe
    """
    result = data.loc[
        : NUM_OF_GAME * 10 - 1,
        (
            "match_id",
            "hero_id",
            "player_slot",
            "gold_spent",
            "gold_per_min",
            "kills",
            "deaths",
            "assists",
            "denies",
            "last_hits",
            "hero_damage",
            "item_0",
            "item_1",
            "item_2",
            "item_3",
            "item_4",
            "item_5",
            "xp_per_min",
            "hero_healing",
            "tower_damage",
            "level",
            "gold_death",
            "unit_order_move_to_position",
            "unit_order_purchase_item",
        ),
    ]
    return result


def hero_match(data, hero):
    """
    Replace column of hero_id in data with actual hero name
    :param data: main data frame we are using
    :param hero: data frame containing hero English name
    :return: main data frame with hero_id replaced with actual name
    """
    hero_wanting = hero.loc[:, ("hero_id", "localized_name")]
    result = data.merge(hero_wanting, left_on="hero_id", right_on="hero_id",
                        how="left")
    result["hero_id"] = result["localized_name"]
    result = result.drop(columns="localized_name")
    return result


def match_result(data, match, NUM_OF_GAME):
    """
    change numpy boolean values in radiant win column to int
    add a column to measure the win and lose in int
    merge the match result to main data frame
    :param data: main data frame we are using
    :param hero: data frame containing game result
    :param NUM_OF_GAME: number of game using in this data processing work
    :return: main data frame with game result
    """
    match_res = match.loc[: NUM_OF_GAME * 10 - 1, ("match_id",
                          "radiant_win")]
    result = data.merge(match_res, left_on="match_id",
                        right_on="match_id", how="left")

    # fix flake8 problem as the statement is True results in error
    radiant_win_np_bool = np.array(result['radiant_win'], dtype=bool)
    radiant_win_np_bool = radiant_win_np_bool.astype(int)
    result = result.drop("radiant_win", axis=1)
    result = pd.concat(
        [result, pd.DataFrame({"radiant_win": radiant_win_np_bool})],
        axis=1
    )

    win = ((result["player_slot"] < 5) & (result["radiant_win"] == 1)) | (
        (result["player_slot"] > 127) & (result["radiant_win"] == 0)
    )
    result["win"] = win

    # fix flake8 problem as the statement is True results in error
    win_np_bool = np.array(result["win"], dtype=bool)
    win_np_bool = win_np_bool.astype(int)
    result = result.drop("win", axis=1)
    result = pd.concat(
        [result, pd.DataFrame({"win": win_np_bool})],
        axis=1)
    return result


def item_match(data, item):
    """
    modify and merge the item data to main data frame
    modifications:
        change item id to actual item name
        drop the existing item columns
        add new columns of all unique items
        the new columns are created with values of dummy variables
    If the item column has no value, change to No Item in string
    :param data: main data frame we are using
    :param hero: data frame containing item name
    :return: modified main dataframe
    """
    unique_item = item["item_name"].unique()
    result = data.copy()
    for i in range(0, 6):
        result = result.merge(
            item, left_on="item_" + str(i), right_on="item_id", how="left"
        )
        result["item_" + str(i)] = result["item_name"]
        result = result.drop(columns="item_name")
        result = result.drop(columns="item_id")

    for i in range(len(unique_item)):
        result[unique_item[i]] = 0
    result["No Item"] = 0
    values = {
        "item_0": "No Item",
        "item_1": "No Item",
        "item_2": "No Item",
        "item_3": "No Item",
        "item_4": "No Item",
        "item_5": "No Item",
    }
    result = result.fillna(value=values)
    rows = len(result)
    step = int(rows / 10)
    for partition in range(0, rows, step):
        step_range = partition
        for i in range(step_range, (step_range + step)):
            result.loc[i, result.loc[i, "item_0"]] = 1
            result.loc[i, result.loc[i, "item_1"]] = 1
            result.loc[i, result.loc[i, "item_2"]] = 1
            result.loc[i, result.loc[i, "item_3"]] = 1
            result.loc[i, result.loc[i, "item_4"]] = 1
            result.loc[i, result.loc[i, "item_5"]] = 1
    result = result.drop(
        columns=["item_0", "item_1", "item_2", "item_3", "item_4", "item_5"]
    )
    return result


def winner_loser(data):
    """
    Return the winner team and loser team in turple
    :param data: main data frame we are using
    :return: data frame with winner team and loser team
    """
    win = data["win"] == 1
    win_team = data[win]
    lose_team = data[~win]
    return (win_team, lose_team)


def data_csv(players, hero, match, item, NUM_OF_GAME):
    """
    Return a clean and modified CSV file
    :param data: all the data frames
    :return: a CSV file containing all necessary information of matches for
            data processing
    """
    data = player(players, NUM_OF_GAME)
    data = hero_match(data, hero)
    data = match_result(data, match, NUM_OF_GAME)
    data = item_match(data, item)
    data = data.dropna()
    return data.to_csv("user_files/csv_files/final_data.csv", index=False)
