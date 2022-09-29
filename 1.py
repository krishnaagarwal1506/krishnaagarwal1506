class Client:
    def __init__(self, client_id, client_name):
        self.__client_id = client_id
        self.__client_name = client_name

    def get_client_name(self):
        return self.__client_name


class AdAgency:
    available_list = ["Product", "Service", "Marketing"]
    counter = 1000

    def __init__(self, client, ad_requirement):
        self.__client = client
        self.booking_id = None
        self.bill_amount = 0
        self.ad_requirement = ad_requirement

    def gen_id(self):
        AdAgency.counter += 2
        self.booking_id = self.__client.get_client_name(
        )[0].upper() + str(AdAgency.counter)

    def get_client(self):
        return self.__client

    def validate_ad_requirement(self):
        flag = 1
        for req in self.available_list:
            if self.ad_requirement == req:
                flag = 0
                break
        if flag == 1:
            return False
        return True


class OutdoorAdAgency (AdAgency):
    def __init__(self, client, outdoor_type, quantity, ad_requirement):
        super().__init__(client, ad_requirement)
        self.__outdoor_type = outdoor_type
        self. __quantity = quantity

    def calculate_bill(self):
        if self.validate_ad_requirement():
            if self.__outdoor_type == "Banner":
                self.bill_amount = 150*self.__quantity
                self.gen_id()
            elif self.__outdoor_type == "Transit":
                self.bill_amount = 170*self.__quantity
                self.gen_id()


c_obj1 = Client(100, "baveST")
out_agen_obj1 = OutdoorAdAgency(c_obj1, "Banner", 300, "Marketing")
out_agen_obj1.calculate_bill()
print(out_agen_obj1.booking_id, out_agen_obj1.bill_amount)
