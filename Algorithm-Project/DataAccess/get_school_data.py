import pandas as pd

def get_school_data():
    input_data = pd.read_excel('TestCase/input.xlsx', sheet_name="工作表1", usecols=["校名", "科系", "科系代碼", "欲錄取人數"])
    input_data = input_data.dropna()
    input_data = input_data.values.tolist()

# Convert the department code to string, and the number of students to int
    for i in range(len(input_data)):
        for j in range(2, len(input_data[i])):
            input_data[i][j] = int(input_data[i][j])

    for i in range(len(input_data)):
        input_data[i][2] = str(input_data[i][2])

    return input_data