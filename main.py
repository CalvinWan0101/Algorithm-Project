# Data Access Layer
from DataAccess.get_school_data import get_school_data
from DataAccess.get_student_data import get_student_data

# Intialize the data
school = get_school_data()
student = get_student_data()

# ['台灣大學', '醫學系', '1001', 2]
# ['台灣大學', '電機系', '1002', 3]
# ['清華大學', '化學系', '2004', 2]
# ['清華大學', '數學系', '2008', 4]
# ['政治大學', '外交系', '3009', 2]

# ['11080002', '楊順亦', 2004, 0, 2008, 0, 1002, 3, 2004, 0, 2008, 0, 1002, 3]
# ['11080003', '劉雅書', 1001, 0, 1002, 0, 2008, 0, 'None', 'None', 'None', 'None', 'None', 'None']
# ['11080004', '郭姵紫', 2004, 1, 3009, 0, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
# ['11080005', '陳怡喬', 2008, 3, 2004, 2, 3009, 1, 'None', 'None', 'None', 'None', 'None', 'None']
# ['11080006', '林宜禾', 2008, 0, 1001, 1, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
# ['11080007', '曹昀志', 3009, 2, 1002, 2, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
# ['11080008', '李偉昀', 3009, 0, 2004, 3, 2008, 2, 'None', 'None', 'None', 'None', 'None', 'None']
# ['11080009', '陳雅玲', 1002, 0, 2004, 0, 2008, 0, 'None', 'None', 'None', 'None', 'None', 'None']
# ['11080010', '陳建緯', 2008, 4, 3009, 3, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
# ['11080011', '毛雲誠', 1001, 2, 1002, 1, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
# ['11080012', '許俊玲', 2008, 1, 1002, 0, 1001, 3, 'None', 'None', 'None', 'None', 'None', 'None']
# ['11080013', '王梅智', 2004, 4, 3009, 4, 1001, 0, 'None', 'None', 'None', 'None', 'None', 'None']
# ['11080014', '林佳蓉', 2004, 5, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']