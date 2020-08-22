"""
Provide methods to calculate the extrem value in the data
"""


def richest_hero(data):
    """
    Find the hero with highest average gold each game
    :param data: main data frame we are using
    :return: hero name with highest average gold and amount of gold
    """
    result = data.groupby("hero_id")["gold_spent"].mean().idxmax()
    num = data.groupby("hero_id")["gold_spent"].mean().max()
    return result, round(num)


def poorest_hero(data):
    """
    Find the hero with lowest average gold each game
    :param data: main data frame we are using
    :return: hero name with lowest average gold and amount of gold
    """
    result = data.groupby("hero_id")["gold_spent"].mean().idxmin()
    num = data.groupby("hero_id")["gold_spent"].mean().min()
    return result, round(num)


def killer_hero(data):
    """
    Find the hero with highest average kills each game
    :param data: main data frame we are using
    :return: hero name with highest average kills and number of kills
    """
    result = data.groupby("hero_id")["kills"].mean().idxmax()
    num = data.groupby("hero_id")["kills"].mean().max()
    return result, round(num)


def burden_hero(data):
    """
    Find the hero with highest average deaths each game
    :param data: main data frame we are using
    :return: hero name with highest deaths and number of deaths
    """
    result = data.groupby("hero_id")["deaths"].mean().idxmax()
    num = data.groupby("hero_id")["deaths"].mean().max()
    return result, round(num)


def escape_hero(data):
    """
    Find the hero with lowest average deaths each game
    :param data: main data frame we are using
    :return: hero name with lowest average deaths and number of deaths
    """
    result = data.groupby("hero_id")["deaths"].mean().idxmin()
    num = data.groupby("hero_id")["deaths"].mean().min()
    return result, round(num)


def most_popular_hero(data):
    """
    Find the hero with highest appearances in 20000 games
    :param data: main data frame we are using
    :return: hero name with highest appearances and number of appearances
    """
    result = data.groupby("hero_id")["hero_id"].count().idxmax()
    num = data.groupby("hero_id")["hero_id"].count().max()
    return result, round(num)


def least_popular_hero(data):
    """
    Find the hero with lowest appearances in 20000 games
    :param data: main data frame we are using
    :return: hero name with highest appearances and number of appearances
    """
    result = data.groupby("hero_id")["deaths"].count().idxmin()
    num = data.groupby("hero_id")["deaths"].count().min()
    return result, round(num)


def damage_hero(data):
    """
    Find the hero with highest average damage each game
    :param data: main data frame we are using
    :return: hero name with highest damage and damage dealed
    """
    result = data.groupby("hero_id")["hero_damage"].mean().idxmax()
    num = data.groupby("hero_id")["hero_damage"].mean().max()
    return result, round(num)


def hero_stats(data):
    """
    Print the hero statistics
    :param data: main data frame we are using
    """
    print("Hero_stats")
    print(
        "The most popular hero is %s, with %d games out of 20000"
        % (most_popular_hero(data)[0], most_popular_hero(data)[1])
    )
    print(
        "The least popular hero is %s, with %d games out of 20000"
        % (least_popular_hero(data)[0], least_popular_hero(data)[1])
    )
    print(
        "The richest hero is %s, with average gold of %d each game"
        % (richest_hero(data)[0], richest_hero(data)[1])
    )
    print(
        "The poorest hero is %s, with average gold of %d each game"
        % (poorest_hero(data)[0], poorest_hero(data)[1])
    )
    print(
        "The most violent hero is %s, dealing average of %d damage each game"
        % (damage_hero(data)[0], damage_hero(data)[1])
    )
    print(
        "The slayer hero is %s, killing average of %d heros each game"
        % (killer_hero(data)[0], killer_hero(data)[1])
    )
    print(
        "The burden hero is %s, dying average of %d times each game"
        % (burden_hero(data)[0], burden_hero(data)[1])
    )
