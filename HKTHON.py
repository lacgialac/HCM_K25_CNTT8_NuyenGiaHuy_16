list_xe =[{    "id": "XE001",
        "plate_name_driver": "29-lac",
        "standard": 12,
        "total_km": 500,
        "total_fuel": 65,
        "consumption_dif_index":5.0,
        "status": "Tiêu hao cao"
}]

def   display_all_car_infor(list_xe):
    if not list_xe:
        print("------ Danh sách trống -------")
    else:
        print("\nDanh sách xe: ")
        for item in list_xe:
            print(f'id: {item["id"]}, plate_name_driver: {item["plate_name_driver"]}, standard: {item["standard"]}, total_km: {item["total_km"]}, total_fuel: {item["total_fuel"]}, consumption_dif_index: {item["consumption_dif_index"]}, status: {item["status"]}')

def check_duplicate_id(new_id):
    for item in list_xe:
        if item["id"]==new_id:
            return False
    return True

def  add_new_car(list_xe):
    new_id=input("nhập vào id mới: ").strip().upper()
    if new_id=="":
        print("id không được để trống !")
        return
    found=check_duplicate_id(new_id)
    if found==False:
        print("id đã tồn tại !!")
        return
    new_plate_name_driver=input("nhập vào biễn số xe và tên tài xế cách nhau dấu (-): ").strip()
    if new_plate_name_driver=="":
        print("biển số xe và tên tài xế không được để trống")

    standard=input("nhập vào định mức lý thuyết: ").strip()
 
    
    total_km= input("nhập vàp tổng số km đã đi được: ")
    total_fuel = input("nhập vào tổng số nhiên liệu tiêu thụ thực tế: ")


    consumption_dif_index= int(input("nhập vào chỉ số chênh lệch tiêu hao; "))

    if consumption_dif_index <0 :
        status= "tiết kiệm"
    elif consumption_dif_index<2 and consumption_dif_index >0 :
        status="tiêu chuẩn"
    elif consumption_dif_index> 2 and consumption_dif_index<8:
        status="tiêu hao cao"
    elif consumption_dif_index >8:
        status="quá tải"


    new_car={
        "id": new_id,
        "plate_name_driver": new_plate_name_driver,
        "standard": standard,
        "total_km": total_km,
        "total_fuel": total_fuel,
        "consumption_dif_index":consumption_dif_index,
        "status": status
    }

    list_xe.append(new_car)
    print("đã thêm thành công !")

def update_infor_car(id_to_update):
    for item in list_xe:
        if item["id"] ==id_to_update:
            standard=input("nhập vào định mức lý thuyết: ").strip()
            total_km= input("nhập vàp tổng số km đã đi được: ")
            total_fuel = input("nhập vào tổng số nhiên liệu tiêu thụ thực tế: ")

            item["standard"]=standard
            item[ "total_km"]=total_km
            item[ "total_fuel"]=total_fuel
            print("đã cập nhật thành công !")
            return 
    print("id không tồn tại !!")

def delete_car_by_id(list_xe):
    id_to_remove=input("nhập vào id xe muốn xóa: ")
    for item in list_xe:
        if item["id"]==id_to_remove:
            yn= input("bạn có muốn xóa nó không (Y?N): ")
            if yn=="Y"or yn=="y":
                list_xe=list_xe.remove(item)
                print('đã xóa thành công !')
                return
            elif yn =="N"or yn =="n":
                print("không xóa ...")
                return
            else :
                print("bạn nhập sai lựa chọn rồi !!")
                return
    print("id không tồn tại !!")

def search_car_smart(list_xe):
    while True:
        print("MENU SHEARCH")
        print("1. tìm kiếm chính xác theo mã xe: ")
        print("2. tìm kiếm gần đúng theo biển số xe hoặc tên tài xế:  ")
        print("3. thoát  ")
        
        choice = input("nhập vào lựa chọn của bạn (1-3): ")
        if choice not in ["1","2","3"]:
            print("Vui lồng nhập lại !!")
            continue
        if choice =="1":
            id_to_search=input("nhập vào id xe muốn tìm: ")
            for item in list_xe:
                if item["id"]==id_to_search:
                    print(f'id: {item["id"]}, plate: {item["plate_name_driver"]}, standard: {item["standard"]}, total_km: {item["total_km"]}, total_fuel: {item["total_fuel"]}, consumption_dif_index: {item["consumption_dif_index"]}, status: {item["status"]}')
                    return
            print("id không tồn tại !")

        if choice =="2":
            name_to_search=input("nhập vào tên tài xế hoặc biển số xe để tìm kiếm tương đối !!")
            for item in list_xe:
                if name_to_search in  item["plate_name_driver"]:
                    print(f'id: {item["id"]}, plate: {item["plate_name_driver"]}, standard: {item["standard"]}, total_km: {item["total_km"]}, total_fuel: {item["total_fuel"]}, consumption_dif_index: {item["consumption_dif_index"]}, status: {item["status"]}')
                    return
            print("không tồn tại tên hay biển số xe như vậy !!")

        elif choice =="3":
            print("thoát menu tìm kiếm !!")
            break

while True:
    print('------ menu -------')
    print("1. Hiển thị danh sách đội xe")
    print("2. Bổ sung xe mới vào đội")
    print("3. Cập nhật nhật ký hành trình")
    print("4. xóa xe khỏi đội quản lý")
    print("5. tìm kiếm phương tiện")
    print("6. Thống kê hiệu suất hạm đội")
    print("7. phân loại hiệu suất tự động")
    print("8. Thoát")

    choice = input("nhập vào lựa chọn của bạn (1-8): ")
    if choice not in ["1","2","3","4","5","6","7","8"]:
        print("Vui lồng nhập lại !!")
        continue

    if choice =="1":
        display_all_car_infor(list_xe)

    elif choice == "2":
        add_new_car(list_xe)


    elif choice =="3":
        id_to_update=input("nhập vào mã xe cần cập nhật nhật ký hành trìn: ")
        update_infor_car(id_to_update)

    elif choice =="4":
        delete_car_by_id(list_xe)

    elif choice =="5":
        search_car_smart(list_xe)
        



    elif choice =="8":
        print("Thoát chương trình ...")
        break