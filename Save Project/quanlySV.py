student = []


def add_student():
    print("")
    msv = input("Nhập Mã SV: ")
    name = input("Nhập Họ Tên: ")
    age = input("Nhập Tuổi SV: ")
    gpa = float(input("Nhập Điểm Trung Bình Kì = "))
    student.append({"msv": msv, "name": name, "age": age, "GPA": gpa})


def show_student():
    if not student:
        print("Danh Sách SV Trống !!!")
        return
    print("|---------------------------------------------------|")
    print("{:<1} {:<12} {:<20} {:<10} {:<4} {:<1}".format(
        "|", "MSSV", "Ho Ten", "Tuoi", "GPA", "|"))
    print("|---------------------------------------------------|")

    for sv in student:
        print("{:<1} {:<12} {:<20} {:<10} {:<4} {:<1}".format(
            "|", sv["msv"], sv["name"], sv["age"], sv["GPA"], "|"))
        print("|---------------------------------------------------|")


def find_student():
    print("")
    mssv = input("Nhap MSV của SV Cần Tìm: ")
    print("")
    for sv in student:
        if sv["msv"] == mssv:
            print(sv["name"], "là SV cần tìm")
            print("")
            print("|---------------------------------------------------|")
            print("{:<1} {:<12} {:<20} {:<10} {:<4} {:<1}".format(
                "|", "MSSV", "Ho Ten", "Tuoi", "GPA", "|"))
            print("{:<1} {:<12} {:<20} {:<10} {:<4} {:<1}".format(
                "|", sv["msv"], sv["name"], sv["age"], sv["GPA"], "|"))
            print("|---------------------------------------------------|")
            return
        else:
            print("Không tìm thấy SV có MSV:", mssv, "trong DS")


def delete_student():
    print("")
    mssv = input("Nhập MSV cần Xoá: ")
    print("")
    for sv in student:
        if sv["msv"] == mssv:
            print(sv["name"], "là SV cần Xoá")
            student.remove(sv)
            print("Đã Xoá SV có MSV:", mssv, "khỏi danh sách !!!")
            print("")
            show_student()
            return
        else:
            print("Không tìm thấy SV có MSV: ", mssv)


def soft_student():
    print("")
    n = len(student)
    for i in range(n):
        for j in range(0, n - i - 1):
            if student[j]["GPA"] < student[j+1]["GPA"]:
                # đổi chỗ kiểu bubble soft
                student[j], student[j+1] = student[j+1], student[j]

    print("")
    print("DS SV sau khi sắp xếp giảm dần theo GPA")
    show_student()


# Menu
while True:
    print("")
    print("---Menu---")
    print("1. Nhập Thông Tin SV")
    print("2. In Danh Sách SV")
    print("3. Tìm Kiếm SV Trong DS")
    print("4. Xoá SV Trong DS")
    print("5. Sắp Xếp SV Theo GPA")
    print("0. thoát(end)")
    print("")

    select = input("Lựa chọn Chức Năng: ")
    if select == "1":
        add_student()
    elif select == "2":
        show_student()
    elif select == "3":
        find_student()
    elif select == "4":
        delete_student()
    elif select == "5":
        soft_student()
    elif select == "0":
        print("")
        print("Thoát Chương Trình !!!")
        break
    else:
        print("Lựa chọn không hợp lệ")
