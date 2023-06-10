def gale_shapley(schools, students):
    def test():
        print("school result")
        for i in range(len(school_result)):
            print(schools[i][2], end=': ')
            for j in range(len(school_result[i])):
                print(school_result[i][j][0], school_result[i][j][school_result[i][j][14]+1],end=', ')
            print()         
        print("wait: ", end='')
        for student in students:
            print(student[0], end=', ')
        print()
        print()

    for student in students:
        student.append(2)
    
    school_result = [] # 初始化科系錄取名單
    for i in range(len(schools)):
        school_result.append([])

    student_result = [] # 初始化學生分發結果

    round_count = 1

    waiting_list = students.copy() # 初始化waiting list

    while len(waiting_list) != 0: # 在所有人都分配完之前不斷遊歷students
        print("Round", round_count)
        print("--------------------------------------------------------------------------------")
        round_count += 1

        for student in waiting_list: # 遊歷students
            print("✅ 正在處理:",student[0])

            for i in range(len(schools)): # 尋找第一志願 school
                if schools[i][2] == student[student[14]]:
                    school = schools[i]
                    break

            if len(school_result[i]) == school[3]: # 科系額滿
                print("幹你娘科系額滿")
                if school_result[i][len(school_result[i])-1][school_result[i][len(school_result[i])-1][14]+1] > student[student[14]+1]: # student 比錄取列表的最後一人前面
                    school_result[i][len(school_result[i])-1][14]+=2
                    # ---
                    if school_result[i][len(school_result[i])-1][14] == 14 or school_result[i][len(school_result[i])-1][school_result[i][len(school_result[i])-1][14]] == 'None': # 落榜
                        print("幹你娘落榜")
                        temp = []
                        temp.append(school_result[i][len(school_result[i])-1][0])
                        temp.append(school_result[i][len(school_result[i])-1][1])
                        temp.append("未錄取")
                        temp.append("未錄取")
                        temp.append("未錄取")
                        student_result.append(temp)
                        students.remove(student)
                    else:
                    # ---
                        students.insert(0, school_result[i][len(school_result[i])-1]) # 將最後一個人繼續分發
                    del school_result[i][len(school_result[i])-1]
                    # school_result[i].append(student)
                    # 依照正備取順序插入school_result
                    for j in range(len(school_result[i])):
                        if student[student[14]+1] < school_result[i][j][school_result[i][j][14]+1]:
                            school_result[i].insert(j, student)
                            break
                        elif j == len(school_result[i])-1:
                            school_result[i].append(student)
                            break
                    students.remove(student)
                    test()
                else: # student 比錄取列表的最後一人後面
                    student[14]+=2
                    if student[14] == 14 or student[student[14]] == 'None':
                        print("幹你娘落榜")
                        temp = []
                        temp.append(student[0])
                        temp.append(student[1])
                        temp.append("未錄取")
                        temp.append("未錄取")
                        temp.append("未錄取")
                        student_result.append(temp)
                        students.remove(student)
                    test()
            else: # 科系還有名額
                if student[student[14]] == 0: # 正取
                    print("幹你娘正取")
                    if len(school_result[i]) != 0: # 科系有人
                        print("幹你娘科系有人")
                        if len(school_result[i])+1 <= school[3]: # 加入student後錄取名單沒爆
                            print("幹你娘加入student後錄取名單沒爆")
                            for j in range(len(school_result[i])): # 依照正備取順序插入school_result
                                if student[student[14]+1] < school_result[i][j][school_result[i][j][14]+1]:
                                    school_result[i].insert(j, student)
                                    break
                                elif j == len(school_result[i])-1 and student[student[14]+1] >= school_result[i][j][school_result[i][j][14]+1]:
                                    school_result[i].append(student)
                                    break
                            students.remove(student)
                            test()
                        else: # 加入student後錄取名單爆了
                            print("幹你娘加入student後錄取名單爆了")
                            for j in range(len(school_result[i])): # 依照正備取順序插入school_result
                                if student[student[14]+1] < school_result[i][j][school_result[i][j][14]+1]:
                                    school_result[i].insert(j, student)
                                    break
                                elif j == len(school_result[i])-1 and student[student[14]+1] >= school_result[i][j][school_result[i][j][14]+1]:
                                    school_result[i].append(student)
                                    break
                            school_result[i][len(school_result[i])-1][14]+=2
                            # ---
                            if school_result[i][len(school_result[i])-1][14] == 14 or school_result[i][len(school_result[i])-1][school_result[i][len(school_result[i])-1][14]] == 'None': # 落榜
                                print("幹你娘落榜")
                                temp = []
                                temp.append(school_result[i][len(school_result[i])-1][0])
                                temp.append(school_result[i][len(school_result[i])-1][1])
                                temp.append("未錄取")
                                temp.append("未錄取")
                                temp.append("未錄取")
                                student_result.append(temp)
                                students.remove(student)

                            else:
                            # ---
                                students.insert(0, school_result[i][len(school_result[i])-1]) # 將最後一個人繼續分發
                            del school_result[i][len(school_result[i])-1]
                            test()
                    else: # 科系沒人
                        print("幹你娘科系沒人")
                        school_result[i].append(student) # 直接加入school_result
                        students.remove(student)
                        test()
                else: # 備取
                    print("幹你娘備取")
                    if len(school_result[i]) != 0: # 科系有人
                        print("幹你娘科系有人")
                        if len(school_result[i])+1 <= school[3]: # 加入student後錄取名單沒爆
                            print("幹你娘加入student後錄取名單沒爆")
                            for j in range(len(school_result[i])): # 依照正備取順序插入school_result
                                if student[student[14]+1] < school_result[i][j][school_result[i][j][14]+1]:
                                    school_result[i].insert(j, student)
                                    break
                                elif j == len(school_result[i])-1 and student[student[14]+1] >= school_result[i][j][school_result[i][j][14]+1]:
                                    school_result[i].append(student)
                                    break
                            students.remove(student)
                            test()
                        else: # 加入student後錄取名單爆了
                            print("幹你娘加入student後錄取名單爆了")
                            for j in range(len(school_result[i])): # 依照正備取順序插入school_result
                                if student[student[14]+1] < school_result[i][j][school_result[i][j][14]+1]:
                                    school_result[i].insert(j, student)
                                    break
                                elif j == len(school_result[i])-1 and student[student[14]+1] >= school_result[i][j][school_result[i][j][14]+1]:
                                    school_result[i].append(student)
                                    break
                            school_result[i][len(school_result[i])-1][14]+=2
                            # ---
                            if school_result[i][len(school_result[i])-1][14] == 14 or school_result[i][len(school_result[i])-1][school_result[i][len(school_result[i])-1][14]] == 'None': # 落榜
                                print("幹你娘落榜")
                                temp = []
                                temp.append(school_result[i][len(school_result[i])-1][0])
                                temp.append(school_result[i][len(school_result[i])-1][1])
                                temp.append("未錄取")
                                temp.append("未錄取")
                                temp.append("未錄取")
                                student_result.append(temp)
                                students.remove(student)
                                continue
                            else:
                            # ---
                                students.insert(0, school_result[i][len(school_result[i])-1]) # 將最後一個人繼續分發
                            del school_result[i][len(school_result[i])-1]
                            test()
                    else: # 科系沒人
                        print("幹你娘科系沒人")
                        school_result[i].append(student) # 直接加入school_result
                        students.remove(student)
                        test()
    
        waiting_list = students.copy()

    for i in range(len(school_result)): # 將科系錄取名單轉換成學生分發結果
        for j in range(len(school_result[i])):
            temp = []
            temp.append(school_result[i][j][0])
            temp.append(school_result[i][j][1])
            temp.append(schools[i][0])
            temp.append(schools[i][1])
            temp.append(schools[i][2])
            student_result.append(temp)

    student_result.sort(key=lambda x: x[0])

    return student_result