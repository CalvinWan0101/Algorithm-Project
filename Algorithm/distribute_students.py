def isEmpty(students):
    return students == []

def distribute_students(schools, students):

    result = []

    while(not isEmpty(students)):
        # 遊歷student
        for student in students:
            
            # searrch for the match school and department
            for school in schools:
                if school[2] == student[2]:
                    # if the school is full, remove it from the list
                    if school[3] <= 0:
                        del student[2]
                        del student[3]
                        break
                    else:
                        # 正取
                        if student[3] == 0:
                            temp = student[0]
                            temp.append(student[1])
                            temp.append(school[0])
                            temp.append(school[1])
                            temp.append(school[2])
                            result.append(temp)
                            school[3] -= 1
                            students.remove(student)
                            break
                        # 備取
                        else:
                            
                            break









