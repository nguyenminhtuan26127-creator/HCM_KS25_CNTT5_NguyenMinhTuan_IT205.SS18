inventory = [
    {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
    {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
]

# Function

def show_inventory(inventory_list):
    if len(inventory_list) == 0:
        print("Kho hàng hiện tại trống!")
    else: 
        print(list(inventory_list))

def add_item(inventory_list):
    # Nhập vào ID
    id_input = input("Nhập mã hàng hóa (ID): ")
    while True:

        if id_input == "":
            id_input = input("Mã hàng hóa không được để trống! Nhập lại: ")
        else:
            break

    
    name_input = input("Nhập tên hàng hóa: ")
    while True:

        if name_input == "":
            name_input = input("Tên hàng hóa không được để trống! Nhập lại: ")
        else:
            break

    quantity_input = input("Nhập số lượng tồn kho: ")
    while True:
            if not quantity_input.isdigit():
                quantity_input = input("Số lượng hàng hóa phải là chữ số! Nhập lại: ")   

            else: 
                quantity_input = int(quantity_input)
                if id_input < 0:
                    quantity_input = input("Số lượng hàng hóa không hợp lệ! Nhập lại: ")

                else:
                    break 

    inventory_list.append({
            'id': id_input, 
            'name': name_input, 
            'quantity': quantity_input
    })

    print("Thêm hàng hóa thành công!")  

def update_quantity(inventory_list):
    id_input = input("Nhập mã hàng hóa cần sửa: ")

    for i in range(len(inventory_list)):
        if inventory_list[i]['id'] == id_input:
            print(f"Tìm thấy hàng hóa: {inventory_list[i]['name']} (số lượng hiện tại: {inventory_list[i]['quantity']})")
            quantity_input = input("Nhập số lượng mới: ")
            while True:
                    if not quantity_input.isdigit():
                        quantity_input = input("Số lượng hàng hóa phải là chữ số! Nhập lại: ")   

                    else: 
                        quantity_input = int(quantity_input)
                        if id_input < 0:
                            quantity_input = input("Số lượng hàng hóa không hợp lệ! Nhập lại: ")

                        else:
                            inventory_list[i]['quantity'] = quantity_input
                            break 

            print("Cập nhật số lượng thành công!")  
            break
    else: 
        print(f"Không tìm thấy hàng hóa có mã [{id_input}]!")


while True:

    print("\n" + " Quản lý kho hàng - Grocery Store ".center(50,"="))
    print("1. Xem danh sách đơn hàng tồn kho")
    print("2. Nhập thêm ghàng hóa mới")
    print("3. Cập nhật số lượng tồn kho theo ID")
    print("4. Thoát")
    print("=" * 50)

    choice = input("Mời chọn chức năng (1-4): ").strip()

    match choice:

        case "1":
            print("\n" + " Danh sách hàng tồn kho ".center(50,"="))
            show_inventory(inventory)

        case "2":
            print("\n" + " Nhập hàng hóa mới ".center(50,"="))
            add_item(inventory)

        case "3":
            print("\n" + " Cập nhật số lượng tồn kho ".center(50,"="))
            update_quantity(inventory)

        case "4":
            print("Đã thoát chương trình.")
            break
        
        # Lựa chọn không hợp lệ
        case _:
            print("Lựa chọn của bạn không hợp lệ!")
