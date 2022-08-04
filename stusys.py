import os
filename = 'student.txt'
def menu():
    print('===============学生信息管理系统===============')
    print('-------------------功能菜单------------------')
    print('        1.录入学生信息')
    print('        2.查找学生信息')
    print('        3.删除学生信息')
    print('        4.修改学生信息')
    print('        5.排序')
    print('        6.统计学生总人数')
    print('        7.显示所有学生信息')
    print('        0.退出系统')
    print('--------------------------------------------')
def main():
    while True:
        menu()
        answer_choice = int(input('请选择\n'))
        if answer_choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if answer_choice == 0:
                answer_quit = input('您确定要退出系统吗？y/n\n')
                if answer_quit == 'y' or answer_quit == 'Y':
                    print('感谢您的使用！')
                    break
                else:
                    continue
            elif answer_choice == 1:
                insert() #录入学生信息
            elif answer_choice == 2:
                search() #查找学生信息
            elif answer_choice == 3:
                delete() #删除学生信息
            elif answer_choice == 4:
                modify() #修改学生信息
            elif answer_choice == 5:
                sort() #排序
            elif answer_choice == 6:
                total() #统计
            elif answer_choice == 7:
                show()  # 显示
        else:
            print('请输入0-7之间的整数')
def insert():
    student_list=[]
    while True:
        while True:
            try:
                id = int(input('请输入学生的id（如1001）：'))
                break
            except:
                print('请输入整数！')
                continue
        if not id:
            break
        name = input('请输入姓名:\n')
        if not name:
            break
        try:
            grade_Chinese = int(input('请输入语文成绩:\n'))
            grade_English = int(input('请输入英语成绩:\n'))
            grade_Math = int(input('请输入数学成绩:\n'))
            grade_Python = int(input('请输入Python成绩:\n'))
        except:
            print('输入无效，请重新输入')
            continue
        #将信息保存到字典中
        student = {'id': id, 'name': name, 'grade_Chinese': grade_Chinese, 'grade_English': grade_English, 'grade_Math': grade_Math, 'grade_Python': grade_Python}
        #将学生信息添加到列表中
        student_list.append(student)
        answer_continue = input('添加完毕，是否继续添加？y/n\n')
        if answer_continue == 'y' or answer_continue == 'Y':
            continue
        else:
            break
    save(student_list) #保存数据
    print('信息录入完毕！')
def search():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
            student_new = []
            for item in student_old:
                d = dict(eval(item))
                student_new.append(d)
    else:
        print('文件不存在！')
        return
    while True:
        answer_mode = input('请输入查询方式，根据id查询请输入1，根据姓名查新请输入2：\n')
        if answer_mode == '1':
            student_id = input('请输入学生id：\n')
            flag = False
            for item in student_new:
                if item['id'] == student_id:
                    flag = True
                    print(str(item))
            if flag == False:
                print(f'未找到id为{student_id}的学生')
            answer_continue = input('查询完毕，是否继续？y/n\n')
            if answer_continue == 'y' or answer_continue == 'Y':
                continue
            else:
                break
        elif answer_mode == '2':
            student_name = input('请输入学生姓名：\n')
            flag = False
            for item in student_new:
                if item['name'] == student_name:
                    flag = True
                    print(str(item))
            if flag == False:
                print(f'未找到姓名为{student_name}的学生')
            answer_continue = input('查询完毕，是否继续？y/n\n')
            if answer_continue == 'y' or answer_continue == 'Y':
                continue
            else:
                break
        else:
            print('输入有误！')
            continue
def delete():
    while True:
        while True:
            try:
                student_id = int(input('请输入要删除的学生id：\n'))
                break
            except:
                print('请输入一个整数！')
                continue
        if student_id:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False #判断是否进行了删除操作
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  #将字符串转为字典
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            print('目前全部信息为：\n')
            show()
            answer_continue = input('是否继续删除？y/n\n')
            if answer_continue == 'y' or answer_continue == 'Y':
                continue
            else:
                break
        else:
            answer_error = input('输入错误！是否继续？y/n\n')
            if answer_error == 'y' or answer_error == 'Y':
                continue
            else:
                break
def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    while True:
        student_id = input('请输入要修改的学生id：\n')
        if student_id:
            with open(filename, 'w', encoding='utf-8') as wfile:
                flag = False
                for item in student_old:
                    d = dict(eval(item))
                    if str(d['id']) == student_id:
                        print('找到学生信息，可以进行修改')
                        flag = True
                        while True:
                            try:
                                d['name'] = input('请输入姓名:\n')
                                d['grade_Chinese'] = int(input('请输入语文成绩:\n'))
                                d['grade_English'] = int(input('请输入英语成绩:\n'))
                                d['grade_Math'] = int(input('请输入数学成绩:\n'))
                                d['grade_Python'] = int(input('请输入Python成绩:\n'))
                                print('修改成功！')
                            except:
                                print('输入数据有误，请重新输入！')
                            else:
                                break
                    wfile.write(str(d)+'\n')
            if not flag:
                print('未找到学生id，没有进行更改！')
            answer_continue = input('是否继续修改？y/n\n')
            if answer_continue == 'y' or answer_continue == 'Y':
                continue
            else:
                return
        else:
            print('请输入正确的id！')
def sort():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_lst = rfile.readlines()
            student_lst_new = []
            for item in student_lst:
                student_lst_new.append(dict(eval(item)))
        if len(student_lst) == 0:
            print('没有数据！')
        else:
            while True:
                try:
                    sort_order = int(input('请输入排序顺序：升序：0；降序：1\n'))
                except:
                    print('输入排序顺序错误!')
                    continue
                else:
                    if sort_order == 0:
                        sort_order_bool = False
                    else:
                        sort_order_bool = True
                    break
            while True:
                try:
                    sort_method = int(input('请输入排序依据。0:id；1:语文成绩；2:英语成绩；3:数学成绩；4:Python成绩；5:总成绩\n'))
                except:
                    print('输入排序依据错误!')
                    continue
                else:
                    if sort_method < 0 or sort_method > 5:
                        print('输入排序依据错误!')
                        continue
                    break
            method_lst = ['id', 'grade_Chinese', 'grade_English', 'grade_Math', 'grade_Python', 'grade_Total']
            for item in student_lst_new:
                total = item['grade_Chinese'] + item['grade_English'] + item['grade_Math'] + item['grade_Python']
                item['grade_Total'] = total
            student_lst_new.sort(key=lambda x: int(x[method_lst[sort_method]]), reverse=sort_order_bool)
            for item in student_lst_new:
                del item['grade_Total']
            with open(filename, 'w', encoding='utf-8') as wfile:
                for item in student_lst_new:
                    wfile.write(str(item)+'\n')
            print('当前数据为：')
            show()
    else:
        print('文件不存在！')
def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
            print(f'一共有{len(student_old)}位学生')
    else:
        print('未找到文件！')
def show():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_lst = rfile.readlines()
            student_lst_new = []
            for item in student_lst:
                student_lst_new.append(dict(eval(item)))
            if len(student_lst) == 0:
                print('还没有录入学生信息！')
            else:
                print('id\t\t姓名\t\t语文成绩\t\t英语成绩\t\t数学成绩\t\tPython成绩')
                print('----------------------------------------------------------------------------')
                for item in student_lst_new:
                    print(str(item['id'])+'\t\t'+str(item['name'])+'\t\t'+str(item['grade_Chinese'])+'\t\t'+str(item['grade_English'])+'\t\t'+str(item['grade_Math'])+'\t\t'+str(item['grade_Python']))
    else:
        print('未找到文件！')
def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
if __name__ == '__main__': #主程序执行点
    main()