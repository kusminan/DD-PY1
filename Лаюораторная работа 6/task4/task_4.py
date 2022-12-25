import json

INPUT_FILE = "input_1.csv"

def csv_to_list_dict(filename) -> list[dict]:
    with open(filename) as file:
        keys = list(file.readline().rstrip().split(","))
        values = list(file.readlines())
        list_of_values = []
        for line in values:
            list_of_values.append(line.rstrip().split(","))
        dict_of_values = {}
        csv_list_of_data = []
        for element in range(len(list_of_values)):
            count = 0
            for column in keys:
                dict_of_values.update({column: list_of_values[element][count]})
                if count == 8:
                    full_dict = dict_of_values.copy()
                    csv_list_of_data.append(full_dict)
                count += 1
    return csv_list_of_data

csv_to_list_dict(INPUT_FILE)
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
