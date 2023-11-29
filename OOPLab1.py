# class Donut():

#     def __init__(self , flavor, toppings, filling, size):

#         self.flavor = flavor

#         self.toppings = toppings

#         self.filling = filling

#         self.size = size

# class Customer():

#       def __init__ (self, name, age, address, favorite_dessert):

#         self.name = name

#         self.age = age

#         self.address = address

#         self.favorite_dessert = favorite_dessert


# class Cake():

#     def __init__(self, flavor, price, quality):

#         self.flavor = flavor

#         self.price = price

#         self.quality = quality


# ------------------------------------------------------------------------------------------
"""class BeefShop ():
    def __init__(self, Id_Member, Name_Member):
        self.Id_Member = Id_Member
        self.Name_Member = Name_Member
        
    def chuck (self, Chuck ):
        self.Chuck = Chuck
        self.Chuck_Price = 280
    def rib (self, Rib ):
        self.Rib = Rib
        self.Rib_Price = 800
    def loin (self, Loin ):
        self.Loin = Loin
        self.Loin_Price = 200
    def brisket (self, Brisket ):
        self.Brisket = Brisket
        self.Brisket_Price = 180
    def plate (self, Plate ):
        self.Plate = Plate
        self.Plate_Price = 300
    def flank (self, Flank ):
        self.Flank = Flank
        self.Flank_Price = 350
    def __str__ (self):
        return "Chuck\t: ({})\nTomahawk: ({})\nLoin\t: ({})\nBrisket\t: ({})\nPlate\t: ({})\nFlank\t: ({})".format(self.Chuck, self.Rib, self.Loin, self.Brisket, self.Plate, self.Flank)

    def Total (self):
        return self.Chuck*self.Chuck_Price + self.Rib*self.Rib_Price + self.Loin*self.Loin_Price + self.Brisket*self.Brisket_Price + self.Plate*self.Plate_Price + self.Flank*self.Flank_Price

    # def paid (self, Paid):
    #     self.Paid = Paid

    # def change (self):
    #     return self.Paid - self.Total() 

Member1 = BeefShop("64015130", "Wanburhan")
Member2 = BeefShop("64015031", "Chidsanupong")
Member3 = BeefShop("64015094", "Pongpipat")
Member4 = BeefShop("64015068", "Narunart")

AllMemberlist = [Member1, Member2, Member3, Member4]
while True:
    Login_Member = str(input ("Please Enter You ID : "))
    Login_Member = [BeefShop for BeefShop in AllMemberlist if BeefShop.Id_Member == Login_Member]
    for BeefShop in Login_Member:
        print ("สวัสดีคุณ : "+BeefShop.Name_Member)
        BeefShop.chuck(0)
        BeefShop.rib(0)
        BeefShop.loin(0)
        BeefShop.brisket(0)
        BeefShop.plate(0)
        BeefShop.flank(0)
        if BeefShop in Login_Member:
            State =  True
            State1 = True
            while State:
                Need = input("สนใจซื้อเนื้อใช่ไหมครับ Y/N : ").upper()
                if Need == "Y" :
                    State1 = True
                    while State1:
                        NeedBeef = input("เลือกประเภทเนื้อที่ต้องการ \n1).Chuck(สันคอ)280บ.\n2).Tomahawk(โทมาฮอว์ค)800บ.\n3).Loin(เนื้อสัน)200บ.\n4).Brisket(เสือร้องไห้)180บ.\n5).Plate(ส่วนท้อง)300บ.\n6).Flank(พื้ันท้อง)350บ.\nถ้าต้องการออกพิม N \n")
                        if NeedBeef == "1" :
                            BeefShop.Chuck = int(input("คุณต้องการเนื้อสันคอกี่ชิ้น? : "))
                        elif NeedBeef == "2" : 
                            BeefShop.Rib = int(input("คุณต้องการซี่โครงกี่ชิ้น? : "))
                        elif NeedBeef == "3" :
                            BeefShop.Loin = int(input("คุณต้องการเนื้อสันกี่ชิ้น? : "))
                        elif NeedBeef == "4" :
                            BeefShop.Brisket = int(input("คุณต้องการเสือร้องไห้กี่ชิ้น? : "))
                        elif NeedBeef == "5" :
                            BeefShop.Plate = int(input("คุณต้องการเนื้อส่วนท้องกี่ชิ้น? : "))
                        elif NeedBeef == "6" :
                            BeefShop.Flank = int(input("คุณต้องการเนื้อพื้นท้องกี่ชิ้น? : "))
                        elif NeedBeef == "N" or NeedBeef == "n" : 
                            State1 = False  
                    print (BeefShop.__str__())
                    print (BeefShop.Total())
                    print ("ขอบคุณที่ใช้บริการครับ '_' ")
                    break
                else :
                    print ("แวะมาใหม่โอกาสหน้านะครับ")
                    break
    if BeefShop not in Login_Member :
        print("รหัสสมาชิกไม่ถูกต้องกรุณากรอกใหม่")"""

# ----------------------------------------------------------------------------------------------


class BeefShop ():
    def __init__(self, Id_Member, Name_Member):
        self.Id_Member = Id_Member
        self.Name_Member = Name_Member

    def chuck(self, Chuck):
        self.Chuck = Chuck
        self.Chuck_Price = 280

    def rib(self, Rib):
        self.Rib = Rib
        self.Rib_Price = 800

    def loin(self, Loin):
        self.Loin = Loin
        self.Loin_Price = 200

    def brisket(self, Brisket):
        self.Brisket = Brisket
        self.Brisket_Price = 180

    def plate(self, Plate):
        self.Plate = Plate
        self.Plate_Price = 300

    def flank(self, Flank):
        self.Flank = Flank
        self.Flank_Price = 350

    def __str__(self):
        return "Chuck\t: ({})\nTomahawk: ({})\nLoin\t: ({})\nBrisket\t: ({})\nPlate\t: ({})\nFlank\t: ({})".format(self.Chuck, self.Rib, self.Loin, self.Brisket, self.Plate, self.Flank)

    def Total(self):
        return self.Chuck*self.Chuck_Price + self.Rib*self.Rib_Price + self.Loin*self.Loin_Price + self.Brisket*self.Brisket_Price + self.Plate*self.Plate_Price + self.Flank*self.Flank_Price

    def paid(self, Paid):
        self.Paid = Paid

    def change(self):
        return self.Paid - self.Total()


Member1 = BeefShop("64015130", "Wanburhan")
Member2 = BeefShop("64015031", "Chidsanupong")
Member3 = BeefShop("64015094", "Pongpipat")
Member4 = BeefShop("64015068", "Narunart")

AllMemberlist = [Member1, Member2, Member3, Member4]
while True:
    Login_Member = str(input("Please Enter You : "))
    Login_Member = [
        BeefShop for BeefShop in AllMemberlist if BeefShop.Id_Member == Login_Member]
    for BeefShop in Login_Member:
        print("สวัสดีคุณ : "+BeefShop.Name_Member)
        BeefShop.chuck(0)
        BeefShop.rib(0)
        BeefShop.loin(0)
        BeefShop.brisket(0)
        BeefShop.plate(0)
        BeefShop.flank(0)
        if BeefShop in Login_Member:
            State = True
            State1 = True
            while State:
                Need = input("สนใจซื้อเนื้อใช่ไหมครับ Y/N : ").upper()
                if Need == "Y":
                    State1 = True
                    while State1:
                        NeedBeef = input(
                            "เลือกประเภทเนื้อที่ต้องการ \n1).Chuck(สันคอ)280บ.\n2).Tomahawk(โทมาฮอว์ค)800บ.\n3).Loin(เนื้อสัน)200บ.\n4).Brisket(เสือร้องไห้)180บ.\n5).Plate(ส่วนท้อง)300บ.\n6).Flank(พื้ันท้อง)350บ.\nถ้าต้องการออกพิม N \n")
                        if NeedBeef == "1":
                            BeefShop.Chuck = int(
                                input("คุณต้องการเนื้อสันคอกี่ชิ้น? : "))
                        elif NeedBeef == "2":
                            BeefShop.Rib = int(
                                input("คุณต้องการซี่โครงกี่ชิ้น? : "))
                        elif NeedBeef == "3":
                            BeefShop.Loin = int(
                                input("คุณต้องการเนื้อสันกี่ชิ้น? : "))
                        elif NeedBeef == "4":
                            BeefShop.Brisket = int(
                                input("คุณต้องการเสือร้องไห้กี่ชิ้น? : "))
                        elif NeedBeef == "5":
                            BeefShop.Plate = int(
                                input("คุณต้องการเนื้อส่วนท้องกี่ชิ้น? : "))
                        elif NeedBeef == "6":
                            BeefShop.Flank = int(
                                input("คุณต้องการเนื้อพื้นท้องกี่ชิ้น? : "))
                        elif NeedBeef == "N" or NeedBeef == "n":
                            State1 = False
                    print(BeefShop.__str__())
                    print(BeefShop.Total())
                    if BeefShop.Total() > 0:
                        BeefShop.Paid = int(input("จ่ายเงินเป็นจำนวน : "))
                        if BeefShop.change() > 0:
                            print("เงินทอน = "+str(BeefShop.change()))
                        else:
                            print("เงินจ่ายมาพอดี")
                        print("ขอบคุณที่ใช้บริการครับ '_' ")
                        break
                else:
                    print("แวะมาใหม่โอกาสหน้านะครับ")
                    break
    if BeefShop not in Login_Member:
        print("รหัสสมาชิกไม่ถูกต้องกรุณากรอกใหม่")
