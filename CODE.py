
class data:
    def __init__(self,id = "",dulieuinput = ""):
        self.id = id 
        self.dulieuinput = dulieuinput     
    def load():
        ff = open("savedata.txt",'r')
        moc = int(ff.readline())
        for i in range(moc):
            listOfLIST[i].id = ff.readline()
            listOfLIST[i].dulieuinput = ff.readline()
    def create(n):
        listOfLIST[n].id = str(n) 
        listOfLIST[n].dulieuinput = input("hay nhap du lieu")
    def update(n):
        listOfLIST[n].dulieuinput = input("hay update du lieu")
    def delete(n):
         
        listOfLIST[n].dulieuinput = ""
    def showall():
        for i in range(len(listOfLIST)):
            if listOfLIST[i].dulieuinput != "":
                print(listOfLIST[i].id,"/n")
                print(listOfLIST[i].dulieuinput,"/n")
    def save(moc):
        ff = open("savedata.txt",'w')
        ff.write(str(moc))
        ff.write("\n")
        for i in range(len(listOfLIST)):
            ff.write(listOfLIST[i].id)
            ff.write("\n")
            ff.write(listOfLIST[i].dulieuinput)
            ff.write("\n")
    def saveload(moc):
        ff = open("savedata.txt",'w')
        ff.write(str(moc))
        ff.write("\n")
        for i in range(len(listOfLIST)):
            ff.write(listOfLIST[i].id)
            ff.write(listOfLIST[i].dulieuinput)
listOfLIST = [data() for i in range(0,1000)]  

turn = "on"
moc = 0
while turn != "off":
    print("1, create")
    print("2,update ")
    print("3, delete ")
    print("4, showall ")
    print("5 load ")
    print("6, save ")
    print("7 off ")
    turn = input()
    if turn == "7":
        turn = "off"
    if turn == "1":
        data.create(moc)
        moc = moc +1
    if turn == "2":
        chonso = int(input("hay chon so can update "))
        data.update(chonso) 
    if turn == "3":
        chonso = int(input("hay chon so can delete "))
        data.delete(chonso)
    if turn == "4":
        data.showall
    if turn == "6":
        data.save(moc)
    if turn == "5":
        data.load()
    if turn == "8":
        data.saveload(moc)

