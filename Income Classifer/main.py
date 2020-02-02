"""
This is the main module used for calling other modules
and functions, overall seeing how the program runs and
is interconnected

Author: Ronan Almeida
Student Number: 20178025
Date: 2019-04-09
"""

import extractData
import classifierBuild
import classifierTest


def main():
    # extractData functions
    print("Reading in data")
    data = extractData.readData("http://research.cs.queensu.ca/home/cords2/annualIncome.txt")
    print("Making training and test files")
    data_test = extractData.makeTestSet(data)
    data_train = extractData.makeTrainingSet(data)

    # classifierBuild function
    print("Building classifier")
    data_model_less, data_model_more = classifierBuild.dataStructures(data_train)

    # classifierTest functions
    print("Classifying test data")
    prediction_points, incorrectly_classified, percent_accuracy = classifierTest.predictData(data_test, data_model_less, data_model_more)

    print("Classified Correctly: ", +prediction_points)
    print("Classified Incorrectly: ", + incorrectly_classified)
    print("Accuracy: ", str(percent_accuracy) + "%")


main()
