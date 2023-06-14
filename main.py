import pandas as pd
import time

from DataAccess.get_school_data import get_school_data
from DataAccess.get_student_data import get_student_data
from Algorithm.gale_shapley import gale_shapley
from Validation.validation import validation

schools = get_school_data()
students = get_student_data()

t1=time.time()
results = gale_shapley(schools, students)
t2=time.time()

print('准考證號碼 學生姓名 錄取校名 錄取科系 錄取科系代碼')
for result in results:
    print(' '.join(result))

validation(results)
print('Time: ', t2-t1)