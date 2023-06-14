from DataAccess.get_output_data import get_output_data
def validation(results):
    outputs = get_output_data()
    if outputs == results:
        print("All Correct!")
    else:
        print("Wrong Answer!")
    return


