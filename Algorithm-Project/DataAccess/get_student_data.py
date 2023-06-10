import pandas as pd

def get_student_data():
    name = ["准考證號碼", "學生姓名", "第一志願", "正備取01", "第二志願", "正備取02", "第三志願", "正備取03", "第四志願", "正備取04", "第五志願", "正備取05", "第六志願", "正備取06"]

    input_data = pd.read_excel('TestCase/input.xlsx', sheet_name="工作表1", usecols=name)
    input_data = input_data.fillna("None")
    input_data = input_data.values.tolist()


    # Convert '正' to 0, '備n' to n
    for i in range(len(input_data)):
        for j in range(len(input_data[i])):
            # if input_data[i][j] is a string
            if isinstance(input_data[i][j], str):
                temp = input_data[i][j]
                if temp[0] == '正':
                    input_data[i][j] = 0
                elif temp[0] == '備':
                    input_data[i][j] = int(temp[1])
    
    # Convert the student ID to string
    for i in range(len(input_data)):
        input_data[i][0] = str(input_data[i][0])
    
    # convert the department code to string
    for i in range(len(input_data)):
        for j in range(2, len(input_data[i]), 2):
            if input_data[i][j] != "None":
                input_data[i][j] = int(input_data[i][j])
                input_data[i][j] = str(input_data[i][j])
    return input_data