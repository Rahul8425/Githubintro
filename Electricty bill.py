def calEB():
    #input Product name as P
    P =input("Enter Product name : ")
    #input Quantity as Q
    Q =int(input("Enter Quantity : "))
    #input price per unit as PP
    PP =int(input("Enter price per unit : "))
     #calculate Basic Bill as BB = Q*PP
    BB = Q*PP

    #calculate Total Bill as TB = Q*PP + (Q*PP)*0.18
    TB = Q*PP + (Q*PP)*0.18

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #print Product name
    print("Produuct name : ",P)
    #print Quantity
    print("Quantity : ",Q)
    #print price per unit
    print("price per unit : ",PP)
    #print  Basic Bill
    print("Basic Bill : ",BB)
    #print Total Bill
    print("Total Bill : ",TB)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

calEB()
