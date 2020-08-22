"""
Provide methods to calculate difference between winning team and losing team
"""
import tools


def gold_difference(data):
    """
    Calcualte the average gold spent between winner teams and loser teams
    :param data: main data frame we are using
    :return: the average gold spent difference between
    winner teams and loser teams
    """
    winner = tools.winner_loser(data)[0]
    loser = tools.winner_loser(data)[1]
    win = winner.groupby("match_id")["gold_spent"].mean()
    lose = loser.groupby("match_id")["gold_spent"].mean()
    difference = (win - lose).mean()
    return round(difference)


def kill_difference(data):
    """
    Calcualte the average kills between winner teams and loser teams
    :param data: main data frame we are using
    :return: the average kills difference between winner teams and loser teams
    """
    winner = tools.winner_loser(data)[0]
    loser = tools.winner_loser(data)[1]
    win = winner.groupby("match_id")["kills"].mean()
    lose = loser.groupby("match_id")["kills"].mean()
    difference = (win - lose).mean()
    return round(difference)


def assist_difference(data):
    """
    Calcualte the average assists between winner teams and loser teams
    :param data: main data frame we are using
    :return: the average assists difference between winner teams
    and loser teams
    """
    winner = tools.winner_loser(data)[0]
    loser = tools.winner_loser(data)[1]
    win = winner.groupby("match_id")["assists"].mean()
    lose = loser.groupby("match_id")["assists"].mean()
    difference = (win - lose).mean()
    return round(difference)


def damage_difference(data):
    """
    Calcualte the average assists between winner teams and loser teams
    :param data: main data frame we are using
    :return: the average assists difference between
    winner teams and loser teams
    """
    winner = tools.winner_loser(data)[0]
    loser = tools.winner_loser(data)[1]
    win = winner.groupby("match_id")["hero_damage"].mean()
    lose = loser.groupby("match_id")["hero_damage"].mean()
    difference = (win - lose).mean()
    return round(difference)


def difference_stats(data):
    """
    Print the hero statistics
    :param data: main data frame we are using
    """
    print("Difference Statistics")
    print(
        "Winner team has %d more gold than loser team on average"
        % gold_difference(data)
    )
    print(
        "Winner team makes %d more kills than loser team on average"
        % kill_difference(data)
    )
    print(
        "Winner team makes %d more assists than loser team on average"
        % assist_difference(data)
    )
    print(
        "Winner team deals %d more hero damage than loser team on average"
        % damage_difference(data)
    )
