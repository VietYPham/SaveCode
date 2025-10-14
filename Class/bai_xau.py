# /Nhập họ tên, định dạng cắt các dấu cách thừa ở trước, sau,giữa họ tên
# Chuyển chữ cái đầu các từ là chữ hoa, chữ cái khác là chữ thường/


ho_ten = str(input("Nhập Họ Tên: "))

ho_ten_new = ho_ten.strip()
ho_ten_new_1 = ho_ten.split()
ho_ten_new_2 = " ".join(ho_ten_new_1)
ho_ten_new_3 = ho_ten_new_2.title()
print(ho_ten_new_3)
