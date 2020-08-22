"""
implements a machine learning technique called Ramdomforest
to predict the # of kills per player in Dota2 game. Visualization of
the resulting feature importance and prediction result is also part
of this file.
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

sns.set()


def randomforest(data):
    """
    implememt RandomForest and report graphical representation of useful
    result
    :param data: modified and clean dataset for implementing RandomForest
    :param run: determine if the user is going to run this program
    If run is true, this method runs and produce the desired output.
    """
    # create dummy variables for categorical variables
    data = pd.get_dummies(data)
    # convert and get the label in Numpy array as required to implement
    # randomforest
    labels = np.array(data["kills"])

    # get features except for labels and unrelated ones
    features = data.drop(["kills", "player_slot", "match_id"], axis=1)

    # store the column names of features
    feature_list = list(features.columns)
    # convert features in Numpy array as required to implement randomforest
    features = np.array(features)

    # split the data into testing and training groups for once
    train_features, test_features, train_labels, test_labels = \
        train_test_split(features, labels, test_size=0.2)

    # The baseline predictions are the historical averages
    baseline_preds = data["kills"].mean()

    # get absolute mean of baseline error
    baseline_errors = round(np.mean(abs(baseline_preds - test_labels)), 2)

    # create list to store values and are used to have an output dataframe
    # in CSV
    num_tree = [1, 2, 3, 5, 10, 30, 60, 100]
    mse_list = []
    train_accuracy = []
    test_accuracy = []
    mean_absolute_error_list = []

    # create RandomForest with different number of estimators
    for tree in num_tree:
        # build 100 decision trees for this random forest model
        rf_model = RandomForestRegressor(n_estimators=tree)

        # train the model using randomforest
        rf_model.fit(train_features, train_labels)

        # get predictions of kills from the model created
        predictions = rf_model.predict(test_features)

        # store MSE, train accuracy, test_accuracy to the lists
        mse_list.append(mean_squared_error(test_labels, predictions))
        train_accuracy.append(rf_model.score(train_features, train_labels))
        test_accuracy.append(rf_model.score(test_features, test_labels))

        # get the absolute errors of the prediction and store to list
        errors = abs(predictions - test_labels)
        mean_absolute_errors = round(np.mean(errors), 3)
        mean_absolute_error_list.append(mean_absolute_errors)

    # store the relevant values from RandomForests into dataframe
    tree_estimator_data = pd.DataFrame(
        data={"n_estimator": num_tree, "MSE": mse_list,
              "train_accuracy": train_accuracy,
              "test_accuracy": test_accuracy,
              "mean_absolute_error": mean_absolute_error_list}
    )

    # add baseline error into dataframe to compare with the mean
    # absolute errors
    tree_estimator_data["Baseline Error"] = baseline_errors

    # output data collected from RandomForests into dataframe for
    # easy access
    tree_estimator_data.to_csv(
            "user_files/csv_files/randomforest_trees.csv",
            index=False
        )

    # store the feature importance in series with indexes indicating the
    # name of features
    feature_imp = pd.Series(
        rf_model.feature_importances_, index=feature_list
    ).sort_values(ascending=False)
    # sort out top 10 feature importance
    top_feature_imp = feature_imp.iloc[0:11]

    # plot importance feature graph using horizonal bar chart
    num_feature = np.arange(len(top_feature_imp.index))
    performance = np.array(list(top_feature_imp))

    fig, ax = plt.subplots()
    ax.barh(num_feature, performance, align="center")
    ax.set_yticks(num_feature)
    ax.set_yticklabels(top_feature_imp.index)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel("Feature Importance")
    ax.set_title(
        "Important Features in Predicting Number of Kills in Dota2"
    )
    fig.savefig(
        "user_files/image_files/Important_Features.png",
        bbox_inches="tight"
    )

    # plot prediction vs actual kill graph
    # create a dataframe with predictions of and actual data of # of kills
    predictions_vs_actual = pd.DataFrame(
        data={"prediction": predictions, "label": test_labels}
    )

    sns.relplot(x="label", y="prediction", data=predictions_vs_actual)
    x = np.linspace(data["kills"].min(), data["kills"].max(), 100)
    y = x
    plt.plot(x, y, "-r", label="45-degree line")
    plt.xlabel("Actual Number of Kills")
    plt.ylabel("Predicted Number of Kills")
    plt.title("Actual data vs. Prediction on Number of Kills")
    plt.savefig(
        "user_files/image_files/prediction_actual_kills.png",
        bbox_inches="tight"
    )

    # plot tree number vs test accuracy graph
    sns.relplot(
        x="n_estimator",
        y="test_accuracy",
        kind="line",
        data=tree_estimator_data
    )
    plt.xlabel("Number of Trees in RandomForest")
    plt.ylabel("Test Accuracy")
    plt.title(
        "Test Accuracy vs. Number of Estimators in RandomForest"
    )
    plt.savefig(
        "user_files/image_files/tree_test_accuracy.png",
        bbox_inches="tight"
    )

    # plot tree number vs MSE graph
    sns.relplot(
        x="n_estimator",
        y="MSE",
        kind="line",
        data=tree_estimator_data
    )
    plt.xlabel("Number of Trees in RandomForest")
    plt.ylabel("Mean Squared Error")
    plt.title(
        "MSE vs. Number of Estimators in RandomForest"
    )
    plt.savefig(
        "user_files/image_files/MSE.png",
        bbox_inches="tight"
    )

    # plot error difference vs number of estimators graph
    tree_estimator_data["dif_errors"] = (
        tree_estimator_data["Baseline Error"] -
        tree_estimator_data["mean_absolute_error"]
    )
    sns.relplot(
            x="n_estimator",
            y="dif_errors",
            kind="line",
            data=tree_estimator_data
        )
    plt.xlabel("Number of Trees in RandomForest")
    plt.ylabel("Error Difference")
    plt.title(
        " Error Difference vs. Number of Estimators in RandomForest"
    )
    plt.savefig(
        "user_files/image_files/error_diff.png",
        bbox_inches="tight"
    )
