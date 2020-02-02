"""
This module is for testing the classifier against unknown values
and determining the percent accuracy of my model

Author: Ronan Almeida
Date: 2019-04-09
"""


def predictData(data_test, less_model, more_model):
    """
    Predict's whether a person's income is >50k or <=50k based on
    the less_model, more_model averaged models compared with records
    in the data_test.


    Parameters:
        data_test - a list of dictionaries of records (1/2 of orginial)
        less_model - Dict: the average model for someone who makes less than 50k
        more_model - Dict: the average model for someone who makes <=50k

    Returns:
        prediction_points - int, The amount of records predicted correctly
        incorrectly_classified - int, The amount of records predicted incorrectly
        percent_accuracy - float, the percent accuracy  of my predictions
    """
    counter_less50 = 0  # Counters to compare records
    counter_greater50 = 0

    predicted_outcome = "unknown"  # the predicted outcome (>50k or <=50k)
    real_outcome = "unknown"  # the actual class value

    prediction_points = 0  # the number of records predicted correct
    total_sum = len(data_test)  # the length of the trainingSet

    for record in data_test:  # For each record (line)

        for attribute in record:  # Each key
            if attribute == "class":

                real_outcome = record[attribute]  # record the real outcome  (>50k or <=50k)

                # Prediction of class (>50k or <=50k): if greater50>less50 data is going to be <=50k
                if counter_greater50 > counter_less50:
                    predicted_outcome = "<=50K"
                else:
                    predicted_outcome = ">50K"

                # Check if outcome is the predicted one
                if real_outcome == predicted_outcome:
                    prediction_points += 1  # add up the correctly predicted
                    counter_less50 = 0  # reset these values for next use
                    counter_greater50 = 0

                else:  # if it was incorrectly predicted
                    counter_less50 = 0  # reset values for next use
                    counter_greater50 = 0
                break  # break out of loop for next record

            # If the value is non-continuous
            if attribute == "workclass" or attribute == "marital" or attribute == "occupation" or \
                    attribute == "relationship" or attribute == "race" or attribute == "sex":

                # Comparing nested dict, values in seeing which is greater than one another
                # e.g if 'Private' is 0.7  in >50k vs 0.8 in <=50k
                if less_model[attribute][record[attribute]] > more_model[attribute][record[attribute]]:
                    counter_less50 += 1

                # If they are equal, do nothing
                elif less_model[attribute][record[attribute]] == more_model[attribute][record[attribute]]:
                    pass
                else:
                    counter_greater50 += 1

            else:  # for continuous values
                # Get the difference from the (record minus the model average)
                # In an absolute value form so that it can be comparable
                less_val = float(abs(record[attribute] - less_model.get(attribute)))
                more_val = float(abs(record[attribute] - more_model.get(attribute)))
                if less_val < more_val:  # The closer the value is to the original the better
                    counter_less50 += 1

                # If they are equal, do nothing
                elif less_val == more_val:
                    pass

                else:
                    counter_greater50 += 1

    # Return the records predicted correctly, records predicted incorrectly and percent accuracy
    return prediction_points, (total_sum - prediction_points), round((prediction_points / total_sum) * 100, 2)


# Testing for each function
if __name__ == "__main__":
    import extractData  # imported for testing purposes
    import classifierBuild

    print("\n TESTING DATA ON A  15 RECORD SAMPLE")
    data = extractData.readData("http://research.cs.queensu.ca/home/cords2/annualIncome.txt")
    data_test = extractData.makeTestSet(data[:30])
    data_train = extractData.makeTrainingSet(data[:30])

    data_model_less, data_model_more = classifierBuild.dataStructures(data_train)

    # classifierTest functions
    prediction_points, incorrectly_classified, percent_accuracy = predictData(data_test, data_model_less,
                                                                              data_model_more)

    print("\nClassified Correctly: ", +prediction_points)
    print("Classified Incorrectly: ", + incorrectly_classified)
    print("Accuracy: ", str(percent_accuracy) + "%")


    # predictData module test
