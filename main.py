import pandas as pd

from DataAccess.get_school_data import get_school_data
from DataAccess.get_student_data import get_student_data
# from Algorithm.distribute_students import distribute_students

schools = get_school_data()
students = get_student_data()

# results = distribute_students(schools, students)

# print('准考證號碼 學生姓名 錄取校名 錄取科系 錄取科系代碼')
# for result in results:
#     print(' '.join(result))