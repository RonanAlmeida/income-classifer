"""
This module is used for building the classifier, in particular creating
the two models of data (>50k,<=50k), incrementing their total values and averaging them

Author: Ronan Almeida
Date: 2019-04-09
"""

# The outside_data_less50 and outside_data_more50 are the two dictionaries
# and models of data (>50k,<=50k) which will store corresponding model averages

outside_data_less50 = {
    "age": 0,
    "workclass": {
        "Private": 0, "Self-emp-not-inc": 0, "Self-emp-inc": 0, "Federal-gov": 0, "Local-gov": 0,
        "State-gov": 0, "Without-pay": 0, "Never-worked": 0
    },
    "educationnum": 0,
    "marital": {
        "Married-civ-spouse": 0, "Divorced": 0, "Never-married": 0, "Separated": 0, "Widowed": 0,
        "Married-spouse-absent": 0, "Married-AF-spouse": 0
    },
    "occupation": {
        "Tech-support": 0, "Craft-repair": 0, "Other-service": 0, "Sales": 0, "Exec-managerial": 0,
        "Prof-specialty": 0, "Handlers-cleaners": 0, "Machine-op-inspct": 0, "Adm-clerical": 0,
        "Farming-fishing": 0, "Transport-moving": 0, "Priv-house-serv": 0, "Protective-serv": 0,
        "Armed-Forces": 0
    },
    "relationship": {
        "Wife": 0, "Own-child": 0, "Husband": 0, "Not-in-family": 0, "Other-relative": 0, "Unmarried": 0
    },
    "race": {
        "White": 0, "Asian-Pac-Islander": 0, "Amer-Indian-Eskimo": 0, "Other": 0, "Black": 0
    },
    "sex": {
        "Female": 0, "Male": 0
    },
    "capitalgain": 0,
    "capitalloss": 0,
    "hours": 0
}

outside_data_more50 = {
    "age": 0,
    "workclass": {
        "Private": 0, "Self-emp-not-inc": 0, "Self-emp-inc": 0, "Federal-gov": 0, "Local-gov": 0,
        "State-gov": 0, "Without-pay": 0, "Never-worked": 0
    },
    "educationnum": 0,
    "marital": {
        "Married-civ-spouse": 0, "Divorced": 0, "Never-married": 0, "Separated": 0, "Widowed": 0,
        "Married-spouse-absent": 0, "Married-AF-spouse": 0
    },
    "occupation": {
        "Tech-support": 0, "Craft-repair": 0, "Other-service": 0, "Sales": 0, "Exec-managerial": 0,
        "Prof-specialty": 0, "Handlers-cleaners": 0, "Machine-op-inspct": 0, "Adm-clerical": 0,
        "Farming-fishing": 0, "Transport-moving": 0, "Priv-house-serv": 0, "Protective-serv": 0,
        "Armed-Forces": 0
    },
    "relationship": {
        "Wife": 0, "Own-child": 0, "Husband": 0, "Not-in-family": 0, "Other-relative": 0, "Unmarried": 0
    },
    "race": {
        "White": 0, "Asian-Pac-Islander": 0, "Amer-Indian-Eskimo": 0, "Other": 0, "Black": 0
    },
    "sex": {
        "Female": 0, "Male": 0
    },
    "capitalgain": 0,
    "capitalloss": 0,
    "hours": 0
}


def dataStructures(data_train):
    """
    Classifies values from the training set into  two average data
    models of >50k and <=50k. It increments and calculates averages
    by calling other functions and returns the final averaged data-sets
    for both models

    Parameters:
        data_train - a list of dictionaries (1/2 of original data)
    Returns:
        dt_struc_less50k, dt_struc_more50k: - dictionaries containing the averaged values
    """

    # Making new dictionaries variables and setting them equal
    # to the outer ones. (For inner scope purposes)
    dt_struc_less50k = outside_data_less50
    dt_struc_more50k = outside_data_more50

    sum_less = 0  # Sum of the count for the >50K model
    sum_more = 0  # Both variables useful for determining averages

    for record in data_train:  # accessing each record (line)
        if record["class"] == ">50K":
            sum_less += 1
            # Calling the incrementCounter function to add up each values (Explained Further Below)
            dt_struc_less50k = incrementCounter(record, dt_struc_less50k)

        else:  # For the <=50k Model
            sum_more += 1
            dt_struc_more50k = incrementCounter(record, dt_struc_more50k)

    # Calling the averageData function to average out the data into their own models
    # (averageData Function is explained further down below)
    dt_struc_more50k = averageData(sum_more, dt_struc_more50k)
    dt_struc_less50k = averageData(sum_less, dt_struc_less50k)

    return dt_struc_less50k, dt_struc_more50k  # return the averaged models


def incrementCounter(record, data):
    """
    Calculates the sum of values based on the current record: for continuous
    and non continuous types of data.

    Parameters:
        record - Contains the dictionary key and values for one person
        data -  a dict: the model data in which values from the record will be tallied
    Returns:
        data - dictionary with the added values from the record
    """

    for attribute in record:  # attribute is the key
        if attribute == "class": break  # skip the class value since it is not used here

        try:  # Try block is for continuous values
            data[attribute] += record[attribute]  # add that value from record to data model

        except TypeError:  # if the attribute is non continuous: Nested dictionary values
            if attribute == "workclass" or attribute == "marital" or attribute == "occupation" or \
                    attribute == "relationship" or attribute == "race" or attribute == "sex":
                if record[attribute] in data[attribute]:  # if the Value is in the nested dictionary
                    data[attribute][record[attribute]] += 1  # increment that value inside the nested dict
    return data  # Return the incremented data


def averageData(data_len, data):
    """
    Get's the data averaged based on the current model, for continuous
    values the data_len (# of increments) is needed

    Parameters:
        data_len - an int value of the number of records in data
        data -  a dict: the model data in which values will be averaged
    Returns:
        data - dictionary with the averaged values from the record
    """

    for records, info in data.items():  # records is the key, info is the value

        # for non continuous values
        if records == "workclass" or records == "marital" or records == "occupation" or records == "relationship" or records == "race" or records == "sex":
            sum_total = 0  # counter for non cont values
            for attribute in info:
                sum_total += info[attribute]

            for attribute in info:  # for nested dicts: Info is a key, attribute is a value
                data[records][attribute] = info[attribute] / sum_total  # Calculate and record average into data dict
        else:  # for continuous values
            data[records] = data[records] / data_len  # Calculate and record average
    return data


# Testing for each function
if __name__ == "__main__":
    import extractData  # imported for testing purposes

    data = extractData.readData("http://research.cs.queensu.ca/home/cords2/annualIncome.txt")

    # dataStructures Module
    data_test = extractData.makeTestSet(data)
    print("Raw Data ", data_test[:2])
    data_model_less, data_model_more = dataStructures(data_test[:2])
    print("\n New Data ", data_model_less)

    # averageData Module
    dataAvg = averageData(2, data_model_less)
    print("\n Averaged Data: ", dataAvg)

    # increment module
    print("\nValues before Increment : ", data[0].values())
    data = incrementCounter(data[0], outside_data_more50)
    print("\nValues after Increment : ", data.values())

