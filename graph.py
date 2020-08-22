import matplotlib.pyplot as plt
import seaborn as sns
import tools
import pandas as pd
import numpy as np

sns.set()


def kills_damage(data):
    """
    Take a data csv file
    Make plot for relationship between kills and hero damage
    """
    # res = g.apply(lambda x: x.order(ascending=False).head(20))
    sns.lmplot(x="kills", y="hero_damage", data=data)
    plt.title("Kills and Hero Damage plot")
    plt.xlabel("Kills")
    plt.ylabel("Hero Damage")
    plt.savefig("user_files/image_files/plot1.png", bbox_inches="tight")


def gold_graph(data, match):
    """
    Take data and match csv files
    Make gold difference plot for winning and losing team
    """
    x = np.array(match.loc[:9999, "match_id"])
    winner = tools.winner_loser(data)[0]
    loser = tools.winner_loser(data)[1]
    win = winner.groupby("match_id")["gold_spent"].mean()
    lose = loser.groupby("match_id")["gold_spent"].mean()
    y = (win - lose).to_list()
    y = np.array(y[:10000])
    data_new = pd.DataFrame(data={"x": x, "y": y})
    sns.relplot(x="x", y="y", data=data_new)
    plt.title("Gold difference in 10000 games")
    plt.xlabel("Matches ID")
    plt.ylabel("Gold difference")
    plt.savefig("user_files/image_files/plot2.png", bbox_inches="tight")


def damage_graph(data, match):
    """
    Take data and match csv files
    Make damage difference plot for winning and losing team
    """
    x = np.array(match.loc[:9999, "match_id"])
    winner = tools.winner_loser(data)[0]
    loser = tools.winner_loser(data)[1]
    win = winner.groupby("match_id")["hero_damage"].mean()
    lose = loser.groupby("match_id")["hero_damage"].mean()
    y = (win - lose).to_list()
    y = np.array(y[:10000])
    data_new = pd.DataFrame(data={"x": x, "y": y})
    sns.relplot(x="x", y="y", data=data_new)
    plt.title("Damage difference in 10000 games")
    plt.xlabel("Matches ID")
    plt.ylabel("Damage difference")
    plt.savefig("user_files/image_files/plot3.png", bbox_inches="tight")
