class DeliveryOrder:

    def __init__(self, id, customer_name, delivery_address, distance_km, cos_per_km, package_weight, extra_fee):
        self.id = id
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.distance_km = distance_km
        self.cos_per_km = cos_per_km
        self.package_weight = package_weight
        self.extra_fee = extra_fee
        self.total_delivery_fee = 0
        self.delivery_type = 0

    def calculate_delivery_fee(self):
        # dùng để tính và cập nhật total_delivery_fee
        fee = self.distance_km * self.cos_per_km + self.extra_fee
        if self.package_weight > 10:
            fee += (self.package_weight - 10) * 5000
        self.total_delivery_fee = fee
        return self.total_delivery_fee

    def classify_delivery(self):
        # dùng để phân loại và cập nhật delivery_type
        if self.distance_km <= 5:
            self.delivery_type = "Nội thành"
        elif self.distance_km <= 20:
            self.delivery_type = "Ngoại thành"
        else:
            self.delivery_type = "Liên tỉnh"
        return self.delivery_type

    def __repr__(self):
        return (f"[{self.id}] {self.customer_name} - {self.delivery_address} "
                f"| {self.distance_km}km, {self.package_weight}kg "
                f"| Phí: {self.total_delivery_fee} | Loại: {self.delivery_type}")


class DeliveryOrderManager:

    def __init__(self):
        self.orders = []

    def display_delivery_orders(self):
        if not self.orders:
            print("Chưa có đơn giao hàng nào.")
            return
        for item in self.orders:
            print(item)

    def add_delivery_order(self, new_order):
        self.orders.append(new_order)

    def search_order_delivery(self, id_search):
        for i in self.orders:
            if i.id == id_search:
                print("Thông tin đơn hàng:")
                print(i)
                return i
        return None

    def check_id_exists(self, id_to_check):
        for i in self.orders:
            if i.id == id_to_check:
                return True
        return False

    def remove_order_by_id(self, id_to_delete):
        for item in self.orders:
            if item.id == id_to_delete:
                self.orders.remove(item)
                return True
        return False

    def update_order(self, id_to_update):
        order = None
        for i in self.orders:
            if i.id == id_to_update:
                order = i
                break
        if order is None:
            print("id không tồn tại !")
            return

        print("Để trống (Enter) nếu không muốn thay đổi giá trị đó.")

        name = input(f"Tên khách hàng [{order.customer_name}]: ").strip()
        if name:
            order.customer_name = name

        address = input(f"Địa chỉ giao hàng [{order.delivery_address}]: ").strip()
        if address:
            order.delivery_address = address

        dis = input(f"Khoảng cách (km) [{order.distance_km}]: ").strip()
        if dis:
            order.distance_km = float(dis)

        cos_km = input(f"Đơn giá/km [{order.cos_per_km}]: ").strip()
        if cos_km:
            order.cos_per_km = float(cos_km)

        pac_we = input(f"Khối lượng kiện hàng (kg) [{order.package_weight}]: ").strip()
        if pac_we:
            order.package_weight = float(pac_we)

        ex_fee = input(f"Phụ phí [{order.extra_fee}]: ").strip()
        if ex_fee:
            order.extra_fee = float(ex_fee)

        order.calculate_delivery_fee()
        order.classify_delivery()
        print("Cập nhật thành công!")
        print(order)


manager = DeliveryOrderManager()

while True:
    print("=============MENU===========")
    print('1. Hiển thị danh sách đơn giao hàng')
    print("2. Thêm đơn hàng mới")
    print("3. Cập nhật đơn giao hàng")
    print("4. Xóa đơn giao hàng")
    print("5. Tìm kiếm đơn giao hàng")
    print('6. Thoát')
    print("============================")
    input_choice = input("Nhập vào lựa chọn của bạn: ").strip()

    if input_choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Vui lòng nhập lại !")
        continue

    match input_choice:
        case "1":
            manager.display_delivery_orders()

        case "2":
            new_id = input("Nhập vào id mới: ").strip()
            if new_id == "":
                print("id không được bỏ trống !")
                continue
            if manager.check_id_exists(new_id):
                print("id đã tồn tại: ")
                continue

            name = input("Nhập vào tên mới: ").strip()
            if name == "":
                print("name không được bỏ trống !")
                continue

            address = input("Nhập vào địa chỉ giao hàng: ").strip()
            if address == "":
                print("address không được bỏ trống !")
                continue

            try:
                dis = float(input("Nhập vào khoảng cách: "))
                cos_km = float(input("Nhập vào đơn giá: "))
                pac_we = float(input("Nhập vào khối lượng kiện hàng: "))
                ex_fee = float(input("Nhập vào phụ phí: "))
            except ValueError:
                print("Giá trị nhập không hợp lệ, vui lòng nhập lại số !")
                continue

            new_delivery_order = DeliveryOrder(new_id, name, address, dis, cos_km, pac_we, ex_fee)
            new_delivery_order.calculate_delivery_fee()
            new_delivery_order.classify_delivery()

            manager.add_delivery_order(new_delivery_order)
            print("Đã thêm đơn hàng thành công!")
            print(new_delivery_order)

        case "3":
            id_to_update = input("Nhập vào mã đơn hàng cần cập nhật: ").strip()
            if not manager.check_id_exists(id_to_update):
                print("id không tồn tại !")
                continue
            else:
                manager.update_order(id_to_update)

        case "4":
            id_to_delete = input("Nhập vào mã đơn hàng cần xóa: ").strip()
            if not manager.check_id_exists(id_to_delete):
                print("id không tồn tại !")
            else:
                yn = input("Nhập vào Y để xóa, N để quay lại: ").strip().upper()
                if yn == "Y":
                    manager.remove_order_by_id(id_to_delete)
                    print("Đã xóa thành công!")
                else:
                    continue

        case "5":
            id_to_search = input("Nhập vào mã đơn hàng cần tìm kiếm: ").strip()
            if not manager.check_id_exists(id_to_search):
                print("id không tồn tại !")
            else:
                manager.search_order_delivery(id_to_search)

        case "6":
            print("Thoát")
            break