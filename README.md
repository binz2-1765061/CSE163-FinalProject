This is the instruction to run our Projet:

First, you have to unzip everything the "CSE163Project" under the SAME DIRECTORY

Second, after unzipping, you should open main.py and install following packages:
    pandas
    matplotlib
    seaborn
    sklearn
    os
    numpy

Thrid, the result of our research question1 and question3 is shown in terminal by running main.py The graphs are save in user_files/Image_files 
(Our original graph is saved in result_image)

Fourth, here is the key part. Since reseach question2 involves with machine learning. Our merged data file and the machine learnhing code
Merging data file takes about 1 hour. Machine learning code takes about 30 mins. So, for your convenience, we don't run the codes for those
parts by default, UNLESS:
    If you change the parameter (False) of run_data = run_decision(False) => run_data = run_decision(True) to run DATA MERGING code,
    and you can re-run main.py,
        the result of merged data file should in user_files/csv_files

    If you change the parameter (False) of run_RandomForest = run_decision(False) => run_decision(True) to run MACHINE LEARNING code
    and you can re-run main.py,
        two results should be produced in user_files/csv_files/randomforest_trees.csv and relevant images in user_files/image_files/
        with name of Important_Features.png; prediction_actual_kills.png; tree_test_accuracy.png; MSE.png; error_diff.png.


Last, you are all set! Have a wonderful summer
