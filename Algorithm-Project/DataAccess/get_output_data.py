import pandas as pd

def get_output_data():
    input_data = pd.read_excel('TestCase/output.xlsx', sheet_name="工作表1", usecols=["准考證號碼", "學生姓名", "錄取校名", "錄取科系", "錄取科系代碼"])
    input_data = input_data.dropna()
    input_data = input_data.values.tolist()

# Convert all intergers to strings
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            input_data[i][j] = str(input_data[i][j])

    return input_data
