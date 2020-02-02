import extractData
import classifierBuild


def dataStructures(data_train, data_less50, data_more50):
    dt_struc_less50k = {
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

    dt_struc_more50k = {
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


    for record in data_train:
        if record["class"] == ">50K":
            dt_struc_less50k = incrementCounter(record, dt_struc_less50k)

        else:
            dt_struc_more50k = incrementCounter(record, dt_struc_more50k)

    dt_struc_more50k = averageData(data_more50, dt_struc_more50k)
    dt_struc_less50k = averageData(data_less50, dt_struc_less50k)
    print("ha")

    return dt_struc_less50k, dt_struc_more50k

    # Calcuating the averages
    # for records in dt_struc_more50k:


def incrementCounter(record, data):
    for attribute in record:
        if attribute == "class": break

        try:
            data[attribute] += record[attribute]
        except TypeError:
            if attribute == "workclass" or attribute == "marital" or attribute == "occupation" or \
                    attribute == "relationship" or attribute == "race" or attribute == "sex":
                print(record[attribute])
                print(data[attribute])
                if record[attribute] in data[attribute]:
                    data[attribute][record[attribute]] += 1
    return data


def averageData(data_len, data):
    for records, info in data.items():
        print(records == "age")
        if records == "workclass" or records == "marital" or records == "occupation" or records == "relationship" or records == "race" or records == "sex":
            sum_total = 0
            for attribute in info:
                sum_total += info[attribute]

            for attribute in info:
                data[records][attribute] = info[attribute] / sum_total

        else:
            data[records] = data[records] / len(data_len)
    return data


def main():
    data = extractData.readData("http://research.cs.queensu.ca/home/cords2/annualIncome.txt")
    data_test = extractData.makeTestSet(data)
    data_train = extractData.makeTrainingSet(data)

    dataless_50k, datamore_50k = classifierBuild.processSets(data)

    print(len(data))
    print(len(dataless_50k))
    print(len(datamore_50k))

    print()
    dataStructures(data_train, dataless_50k, datamore_50k)


main()
