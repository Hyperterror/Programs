import mysql.connector as con
import time
mydb=con.connect(host="localhost",user="root",password="Hyper")
mycursor=mydb.cursor()


set1="Drop database IF EXISTS Bakery;"
mycursor.execute(set1)
set2="Create database IF NOT EXISTS Bakery;"
set3="Use Bakery;"
mycursor.execute(set2)
mycursor.execute(set3)
mycursor.execute("Drop table If Exists Product1;")
set4="Create table IF NOT EXISTS Cust1(Cust_mail char(40) primary key,Cust_name char(30),Cust_mobile char(15),Cust_password char(20));"
mycursor.execute(set4)
set5="Create Table IF NOT EXISTS Product1(Product_Code int primary key,Product_Name char(100) not null,Product_type char(20),Product_price int)"
mycursor.execute(set5)
set6="create table IF NOT EXISTS employee(E_id char(10) primary key , E_name char(30), E_email char(30), E_ph int(10), E_add char(30), J_date date, E_desgn char(15), E_pwd varchar(10));"
mycursor.execute(set6)
set7="insert into product1 values(%s,%s,%s,%s);"

lis1=[(101,'margherita','pizza',399),
(102,'farm fresh','pizza',439),
(103,'pesto','pizza',449),
(104,'little italy','pizza',459),
(105,'pepperoni','pizza',479),
(106,'barbeque','pizza',479),
(107,'arrabbiata','pizza',549),
(108,'chicago style deep dish','pizza',549),
(109,'grilled cheese','sandwich',50),
(313,'paneer','sandwich',60),
(110,'punjabi tikka','sandwich',70),
(111,'tandoori','sandwich',65),
(112,'mexican BLT','sandwich',75),
(113,'club sandwich','sandwich',55),
(114,'blueberry grilled cheese','sandwich',85),
(115,'ham and cheese panini','sandwich',100),
(116,'chicken and cheese panini','sandwich',100),
(117,'pesto alberto','sandwich',95),
(118,'prosscuto','sandwich',100),
(119,'paneer grilled','sandwich',65),
(120,'veg hot dog','sandwich',65),
(121,'non-veg hot dog','sandwich',85),
(122,'baguette','bread',250),
(123,'banana bread','bread',175),
(124,'multigrain','bread',200),
(125,'brioche','bread',250),
(126,'sourdough','bread',250),
(127,'wheat','bread',100),
(128,'sandwich bread','bread',125),
(129,'aloo patties','patties',10),
(130,'paneer patties','patties',15),
(131,'cheese patties','patties',20),
(132,'cheese corn patties','patties',25),
(133,'tandoori patties','patties',30),
(134,'pesto','pasta',135),
(135,'alfredo','pasta',135),
(136,'fettucini','pasta',135),
(137,'carbonara','pasta',155),
(138,'spaghetti','pasta',115),
(139,'arrabbiata','pasta',155),
(140,'tortellini','pasta',135),
(141,'marinara','pasta',135),
(142,'bolognese','pasta',150),
(143,'ricotta','pasta',150),
(144,'lamb rago','pasta',175),
(145,'chicken cheese','pasta',155),
(146,'cheese','pasta',115),
(147,'Plain','donut',35),
(148,'glased','donut',40),
(149,'chocolate','donut',40),
(150,'cinnamon sugar','donut',45),
(151,'smore (filled)','donut',70),
(152,'blueberry crunch (filled)','donut',70),
(153,'beer batter maple bacon','donut',85),
(154,'PB&J (filled)','donut',70),
(155,'Caramel sea salt','donut',85),
(156,'bear claw','donut',55),
(157,'cinnabon','donut',55),
(158,'red velvet','donut',40),
(159,'irish coffee','donut',55),
(160,'honey dipped','donut',50),
(161,'apple cinnamon (filled)','donut',85),
(162,'boston creme (filled)','donut',70),
(163,'jelly (filled)','donut',45),
(164,'waffle batter maple','donut',85),
(165,'bavarian (filled)','donut',70),
(166,'pain au chocolat','french pâtisserie',190),
(167,'croissant','french pâtisserie',175),
(168,'creme brulee','french pâtisserie',250),
(169,'eclair','french pâtisserie',150),
(170,'macarons /doz','french pâtisserie',360),
(171,'Profiterole /doz','french pâtisserie',360),
(172,'religieuse /doz','french pâtisserie',360),
(173,'Mille Feuille /doz','french pâtisserie',480),
(174,'Madeline /doz','french pâtisserie',200),
(175,'Cannele /doz','french pâtisserie',360),
(176,'Chouquette /doz','french pâtisserie',200),
(177,'chocolate','shake',40),
(178,'vanilla','shake',40),
(179,'strawberry','shake',40),
(180,'mango','shake',40),
(181,'oreo','shake',50),
(182,'snickers','shake',50),
(183,'plain','tea',10),
(184,'masala','tea',25),
(185,'cardomom','tea',20),
(186,'ginger','tea',20),
(187,'khulad','tea',25),
(188,'vanilla','cookies',25),
(189,'chocolate','cookies',25),
(190,'almond','cookies',25),
(191,'chocolate chip','cookies',25),
(192,'peanut butter','cookies',25),
(193,'oatmeal raisin','cookies',25),
(194,'apple /slice','pie',35),
(195,'blueberry /slice','pie',35),
(196,'cherry /slice','pie',35),
(197,'chestnut /slice','pie',35),
(198,'walnut /slice','pie',35),
(199,'pumpkin /slice','pie',35),
(200,'pecan /slice','pie',35),
(201,'plain','coffee',20),
(202,'cappucino','coffee',30),
(203,'espresso','coffee',35),
(204,'latte','coffee',49),
(205,'cold brew','coffee',35),
(206,'black','coffee',25),
(207,'iced coffee','coffee',30),
(208,'cold coffee','coffee',35),
(209,'boba','tea',55),
(210,'cold coffee float','coffee',60),
(211,'americano','coffee',35),
(212,'mocha','coffee',40),
(213,'machhiato','coffee',45),
(214,'irish blend','coffee',60),
(215,'frappe','coffee',35),
(216,'frappecino','coffee',40),
(217,'turkish blend','coffee',60),
(218,'hot chocolate','coffee',55),
(219,'vanilla','muffin',25),
(220,'chocolate','muffin',25),
(221,'fruit','muffin',25),
(222,'pb&j','muffin',30),
(223,'butterscotch','muffin',25),
(224,'oatmeal','muffin',25),
(225,'dates','muffin',30),
(226,'cranberries','muffin',30),
(227,'pecan','muffin',30),
(228,'choco chip','muffin',25),
(229,'banana','muffin',25),
(230,'honey','muffin',25),
(231,'apple(cinnamon sugar top)','muffin',35),
(232,'blueberry','muffin',30),
(233,' raisin bran','muffin',25),
(234,'cinnamon','pretzels',25),
(235,'apple','pretzels',25),
(236,'berries','pretzels',25),
(237,'chocolate','pretzels',25),
(238,'pb&j','pretzels',30),
(239,'plain','bagels',25),
(240,'breakfast Sandwich','sandwich',45),
(241,'rainbow','bagels',35),
(242,'pumpernickel','bagels',30),
(243,'frenchtoast','bagels',35),
(244,'whole wheat','bagels',25),
(245,'poppy seeds','bagels',25),
(246,'lemon drizzle','scones',35),
(247,'vanilla cream & strawberry & rhubarb jam','scones',30),
(248,'date','scones',30),
(249,'pumpkin lemonade','scones',35),
(250,'lemonade','scones',30),
(251,'blueberry','scones',30),
(252,'buttermilk','scones',30),
(253,'strawberry','tarts',30),
(254,'chocolate','tarts',30),
(255,'vanilla','tarts',30),
(256,'meringue','tarts',30),
(257,'blueberry','tarts',30),
(258,'rasberry','tarts',30),
(259,'lemon','tarts',30),
(260,'peach','tarts',30),
(261,'apple','tarts',30),
(262,'rasberry chocolate','tarts',40),
(263,'custard','tarts',30),
(264,'vanilla','cake',550),
(265,'banana','cake',550),
(266,'mongo','cake',550),
(267,'orange','cake',550),
(268,'chocolate','cake',550),
(269,'pineapple','cake',550),
(270,'black forest','cake',550),
(271,'red velvet','cake',650),
(272,'butterscotch','cake',650),
(273,'sea salt & caramel','cake',850),
(274,'chocolate & orange','cake',850),
(275,'chocolate & mango','cake',850),
(276,'caramel & almond','cake',850),
(277,'plum','cake',900),
(278,'walnut','cake',550),
(279,'strawberry cheesecake','cake',600),
(280,'chocolate cheesecake','cake',600),
(281,'blueberry cheesecake','cake',600),
(282,'vanilla cheesecake','cake',600),
(283,'mango cheesecake','cake',600),
(284,'orange cheesecake','cake',600),
(285,'almond & caramel','cake',700),
(286,'cookies & cream','cake',700),
(287,'classic american potato','vburger',150),
(288,'mega cheesy onion ring,','vburger',175),
(289,'shroom','vburger',175),
(290,'peri peri paneer','vburger',200),
(291,'barbeque extravaganza','vburger',275),
(292,'cheese melt','vburger',225),
(294,'paneer makhani','vburger',275),
(295,'falafel','vburger',300),
(296,'BURGERMEISTER','vburger',300),
(297,'fresh-from-farm','vburger',300),
(298,'nashville fried chicken','nvburger',350),
(299,'fried chicken','nvburger',300),
(300,'buffalo chicken','nvburger',325),
(302,'grilled','nvburger',275),
(303,'peri peri chicken','nvburger',300),
(304,'german ranch chicken','nvburger',350),
(305,'BURGERMEISTER','nvburger',375),
(306,'Muscular Mutton','nvburger',375),
(307,'Birria mutton','nvburger',395),
(308,'Birria CHicken','nvburger',375),
(309,'Blue cheese lamb','nvburger',395),
(310,'Kung Fu','nvburger',325),
(311,'Orange Chicken','nvburger',325),
(312,'Grilled Peanut Chicken','nvburger',375)]
mycursor.executemany(set7,lis1)
mydb.commit()


for data in mycursor:
    print()
def main():
    inloop = 1
    while inloop:
        print()
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("       WELCOME TO MELOSO BAKERY       ")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

        print("Login As:")
        print("Choice 1:ADMIN")
        print("Choice 2:CUSTOMER")
        print("Choice 3:EXIT")

        choice=input("Enter your choice:")

        if choice=='1':
            password=input("Enter the password:")
            if password=="Sweet":
                admin_login(mydb,mycursor)
            else:
                print("!!Incorrect Password!!")
                time.sleep(1)

        elif choice=='2':
            customer_login(mydb,mycursor)
        elif choice=='3':
            exit()
        else:
            print("!Invalid Choice!")

def admin_login(mydb,mycursor):
    print()
    print("      WELCOME! YOU ARE LOGGED IN AS ADMIN       ")
    print()
    print("----SETTINGS----")
    print("Choice 1:Add an item")
    print("Choice 2:Remove an item")
    print("Choice 3:Update item price")
    print("Choice 4:See all the items")
    print("Choice 5:Exit")

    Choice=int(input("Enter your choice:"))
    print()
    time.sleep(0.5)

    if Choice==1:
        print("What whould you like to add?")
        product_code=int(input("Enter product Code"))
        product_name=input("Enter product name:")
        product_type=input("Enter Product type")
        product_price=int(input("Enter product price:"))
        list1=[product_code,product_name,product_type,product_price]
        
        try:
            query="INSERT INTO Product1(product_code,product_name,product_price) Values (%s,%s,%s,%s)"
            mycursor.execute(query,list1)
            mydb.commit()
            print("!The item has been added to the list!")

        except Exception as e:
              print("!!ERROR OCCURED!!")

              time.sleep(1)
              admin_login(mydb,mycursor)

    elif Choice==2:
        display_items(mycursor)
        print("Which item you would like to remove?")
        id1 = int(input("Enter product id:"))
        list2=[id1]
        try:
            query1="DELETE FROM Product1 WHERE product_code=%s;"
            mycursor.execute(query1,list2)
            mydb.commit()
            print("The item has been removed from the shop!")
        except Exception as e:
            print("!INVALID ITEM!")
            time.sleep(1)
            admin_login(mydb,mycursor)
       
    elif Choice==3:
        display_items(mycursor)
        print("Which item price you would like to update?")
        id2 = int(input("Enter product ID:"))
        name1=input('Enter the updated product name:')
        type1=input('Enter the updated Product type:')
        price=int(input("Enter the updated price:"))
        list3=[price, id2]
        list4=[name1, id2]
        lis5=[type1,id2]
        try:
            query3="UPDATE Product1 SET product_price=%s WHERE product_code=%s;"
            
            query4="UPDATE Product1 SET product_name=%s WHERE product_code=%s;"
            quer5="Update Prosuct1 SET product_type=%s WHERE product_code=%s;"
            mycursor.execute(query3,list3)
            mydb.commit()
            mycursor.execute(query4,list4)
            mydb.commit()
            mycursor.execute(quer5,lis5)
            print("!The item price has been updated!")
            print("!The item type has been updated!")
            print("!The item name has been updated!")
        except Exception as e:
            print("!Invalid Product ID!")
        
            time.sleep(1)
            admin_login(mydb,mycursor)

    elif Choice==4:
        display_items(mycursor)
        time.sleep(1.5)
        admin_login(mydb,mycursor)
    elif Choice==5:
        main()
    else:
        print("Invalid Choice!")
        time.sleep(1)
        admin_login(mydb,mycursor)

def display_items(mycursor):
    print("Enter Product Type")
    print("1. Sandwitch ")
    print("2. Pizza")
    print("3. Pasta")
    print("4.Bread")
    print("5.Patties")
    print("6.Donut")
    print("7. French Pâtisserie")
    print("8.Shake")
    print("9.Tea")
    print("10.Cookies")
    print("11.Coffee")
    print("12. Pie")
    print("13.Muffin")
    print("14. Pretzels")
    print("15.Bagels")
    print("16. Scones")
    print("17.Tarts")
    print("18.Cake")
    print("19. Veg Burgers")
    print("20. Non-Veg Burgers")
    ask1=int(input("Enter Product Type"))
    if ask1==1:
        set15="Select * from Product1 where product_type=%s;"
        types1=["sandwich"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==2:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Pizza"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==3:
        set15="Select * from Product1 where product_type=%s;"
        types1=["pasta"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif  ask1==4:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Bread"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==5:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Patties"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==6:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Donut"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==7:
        set15="Select * from Product1 where product_type=%s;"
        types1=["French Pâtisserie"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==8:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Shake"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==9:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Tea"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==10:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Cookies"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==11:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Coffee"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==12:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Pie"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==13:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Muffin"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==14:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Pretzels"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==15:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Bagels"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==16:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Scones"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==17:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Tarts"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==18:
        set15="Select * from Product1 where product_type=%s;"
        types1=["Cake"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==19:
        set15="Select * from Product1 where product_type=%s;"
        types1=["vburger"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
    elif ask1==20:
        set15="Select * from Product1 where product_type=%s;"
        types1=["nvburger"]
        mycursor.execute(set15,types1)
        results=mycursor.fetchall()
        print("List of items: ")
        print("ID","Name","Type","Price",sep=" ")
        for each in results:
            print(each[0],each[1],each[2],each[3],sep=" ")
"""
    mycursor.execute(query)
    results=mycursor.fetchall()
    print("List of items: ")
    print("ID","Name","Price",sep=" ")
    for each in results:
        print(each[0],each[1],each[2],sep=" ")
"""


def customer_login(mydb,mycursor):
    print("     WELCOME! YOU ARE LOGGED IN AS CUSTOMER       ")
    print("Here are the list of items")
    print("Choice 1:Billing")
    print("Choice 2:Exit")
    choice1=int(input("ENTER YOUR CHOICE:"))
    if choice1==1:
        name=input("Enter your name: ")
        print("What do you like to buy ",name,"?")
        time.sleep(0.5)
        display_items(mycursor)
        print()
        total=0
        items=[]
        while 1:
            id3=int(input("ENTER PRODUCT ID: "))
            quantity=int(input("ENTER THE QUANTITY: "))
            list6=[id3]

            try:
                query="SELECT * FROM Product1 WHERE product_code=%s"
                mycursor.execute(query,list6)
                result=mycursor.fetchone()
                
                total = result[3]*quantity
                items.append([result[1],quantity])
                i=input("Anything else?Answer Y for Yes and N for No: ")
                if i=='N':
                     if total !=0:
                        print()
                        print("        WELCOME TO MELOSA BAKERY        ")
                        print("-------Billing Details-------")
                        print("Name:",name)
                        print("Items:")
                        items.append([result[1],quantity])
                        for each in items:
                            print(each[0],each[1],sep=":")
                            print("Total:",total)
                            print("Thank you! Have a nectarous day!")
                            print()
                            time.sleep(1)
                            customer_login(mydb,mycursor)
            
            except Exception as e:
                print("Invalid Entry!")
                print(e)
                break
    elif choice1==2:
       main()
    else:
        print("Invalid Choice!")
        time.sleep(1)
        customer_login(mydb,mycursor)            
"""
            if total==0:
                print()
                print("        WELCOME TO MELOSA BAKERY        ")
                print("-------Billing Details-------")
                print("Name:",name)
                print("Items:")
                for each in items:
                    print(each[0],each[1],sep=":")
                    print("Total:",total)
                    print("Thank you! Have a nectarous day!")
                    print()

                time.sleep(1)
                customer_login(mydb,mycursor)

    elif choice==2:
        main()
    else:
        print("Invalid Choice!")
        time.sleep(1)
        customer_login(mydb,mycursor)
"""
