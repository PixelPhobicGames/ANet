import dearpygui.dearpygui as dpg
import time

from User import *

# Created By 

# NightWalkers 

    
dpg.create_context()
dpg.create_viewport(title='ANet Client - Ночные ходоки', width=600, height=300)


width, height, channels, data = dpg.load_image("AppData/ProdImages/Svedka.png")
width2, height2, channels2, data2 = dpg.load_image("AppData/ProdImages/Smir75.png")

with dpg.texture_registry(show=False):
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="Svedka")
    dpg.add_static_texture(width=width2, height=height2, default_value=data2, tag="Smir75")


def AddHelp(sender, app_data):
    dpg.delete_item("ShopWindow", children_only=False)
    with dpg.window(tag="Add Help"):
        dpg.set_primary_window("Add Help", True)
        dpg.add_text("")
        dpg.add_text("")
        dpg.add_text(" To Add Balance to Your account Please Contact Your Local NS Connetion , Delieverer ,\n Etc Give Them The Amount in Cash you wish to be Added to Your Account. \n 1$ - USD = 1 ANT")
        dpg.add_text("")
        dpg.add_text("")
        dpg.add_button(label="Go Back", callback=Shop)
def ShipSvedka(sender, app_data):
    dpg.delete_item("PurchaseSvedka", children_only=False)

    if (GetBalance() >= 18):
        print("Shipping")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((NetInfo.Host, NetInfo.Port))
            s.send(bytes(str("ORD:" + UserInfo.Name + ":"  + UserInfo.Address + ":" + UserInfo.Number + ":ID-1:18"), 'utf-8'))

    else:
        print("Declined")


    Shop(0,0)

def PurchaseSvedka(sender, app_data):
    dpg.delete_item("ShopWindow", children_only=False)
    with dpg.window(tag="PurchaseSvedka"):
        dpg.set_primary_window("PurchaseSvedka", True)
        dpg.add_text("")
        dpg.add_text("")
        dpg.add_text("  You are about to Purchase Svedka Vodka 750 ml, \n This Will be Shipped to the Address Provided on Creation of the Account. \n The Bottle will Arrive Within 2-3 Days and will be put in a Cardboard Box.")
        dpg.add_text("")
        dpg.add_text("This Item Costs 18 ANT, This will be taken from Your Account on Order.")
        dpg.add_text("")
        dpg.add_text("")
        dpg.add_text("If You wish to have Custom Order Directions Please Include them Here.")
        Directions = dpg.add_input_text(label="Custom Directions" , tag="Directions")
        dpg.add_text("")
        dpg.add_text("Enter Password Again")
        Pass = dpg.add_input_text(label="Pass" , tag="Pass2")
        dpg.add_text("")
        dpg.add_text("")
        dpg.add_text(str("Shipping Address: " + Encrypt(UserInfo.Address)))
        dpg.add_button(label='Confirm Order' , callback=ShipSvedka)

        dpg.add_button(label="Go Back", callback=Shop)

def WipeAccount(sender, app_data):
    ConfFile = open("AppData/User/User.conf", "w+")
    ConfFile.write(str(""))
    ConfFile.close
    dpg.delete_item("Settings Conf", children_only=False)
    Shop(0,0)

def Create(sender , app_data):
    UserInfo.Name = dpg.get_value("Name")
    UserInfo.Number = dpg.get_value("Number")
    UserInfo.Password = dpg.get_value("Pass")
    UserInfo.Address = dpg.get_value("Address")

    GenerateIDInfo()
    dpg.delete_item("Create Account", children_only=False)
    Shop(0,0)

def CreateAccount(sender , app_data):
    dpg.delete_item("Settings Conf", children_only=False)
    with dpg.window(tag="Create Account"):
        dpg.set_primary_window("Create Account", True)
        dpg.add_text("Enter Name - (Real Name, Will Be Used for Orders)")
        Name = dpg.add_input_text(label="Name" , tag="Name")
        dpg.add_text("Enter Phone Number")
        Number = dpg.add_input_text(label="Number" , tag="Number")
        dpg.add_text("Enter Password")
        Password = dpg.add_input_text(label="Pass" , tag="Pass")
        dpg.add_text("Enter Full Street Adress")
        Address = dpg.add_input_text(label="Address" , tag="Address")
        dpg.add_button(label="Create" , callback=Create)

        dpg.add_text("Note: All Information Is Stored locally in (AppData/User/User.conf) ")
        dpg.add_text("This Data will be encrypted when sent to our Servers. \n Your Identity is Completely Safe")
        dpg.add_text("")



def Shop(sender , app_data):
    with dpg.window(tag="ShopWindow"):
        dpg.set_primary_window("ShopWindow", True)
        dpg.delete_item("Settings Conf", children_only=False)
        dpg.delete_item("Add Help", children_only=False)
        with dpg.menu_bar():
            with dpg.menu(label="Shop"):
                dpg.add_menu_item(label="Open Shop")
            with dpg.menu(label="Account"):
                dpg.add_menu_item(label="Settings" , callback=Settings)
            with dpg.menu(label="Help"):
                dpg.add_menu_item(label="Adding ANT Balance to Account" , callback=AddHelp)
        if (PullID() == 0):
            dpg.add_text("No User Data Found, Please Create an Account", pos=[100, 50])
        else:
            dpg.add_text(str("Welcome, " + Encrypt(UserInfo.Name)) , pos=[240, 40])

            dpg.add_image("Svedka" , pos=[70, 100])
            dpg.add_text("Swedish Vodka (Svedka)" , pos=[280, 120])
            dpg.add_text("Size: 1 Liter" , pos=[280, 140])
            dpg.add_text("Price: 20 ANT" , pos=[280, 160])
            dpg.add_text("Description: This is a Vodka From Sweden, \nIts Very Cheap. We Always Have This \n on Hand. The Flavor is Decent and Smooth." , pos=[280, 190])
            dpg.add_button(label="Purchase This Item" , pos=[280, 240] , callback=PurchaseSvedka)

            dpg.add_image("Smir75" , pos=[67/2, 100 + 300])
            dpg.add_text("Smirnoff Vodka (Smirnoff)" , pos=[280, 120 + 300])
            dpg.add_text("Size: 750 mL" , pos=[280, 140 + 300])
            dpg.add_text("Price: 18 ANT" , pos=[280, 160 + 300])
            dpg.add_text("Description: This is a Vodka From Russia, \nAlso Cheap." , pos=[280, 190 + 300])
            dpg.add_button(label="Purchase This Item" , pos=[280, 240 + 300] )



           

def Settings(sender , app_data):
    dpg.delete_item("ShopWindow", children_only=False)
    with dpg.window(tag="Settings Conf"):
        dpg.set_primary_window("Settings Conf", True)
        with dpg.menu_bar():
            with dpg.menu(label="Return"):
                dpg.add_menu_item(label="Back to Shop" , callback=Shop)

        if (PullID() == 0):
            dpg.add_text("No User Data Found", pos=[230, 50])
            dpg.add_button(label="Create Account", pos=[230, 70] , callback=CreateAccount)
        else:
            UserInfo.Balance = GetBalance()
            dpg.add_text("Account Details:")
            dpg.add_text(str("Name: " + Encrypt(UserInfo.Name)))
            dpg.add_text(str("Number: " + Encrypt(UserInfo.Number)))
            dpg.add_text(str("Address: " + Encrypt(UserInfo.Address)))
            dpg.add_text(str("Account Balance: " + str(UserInfo.Balance) + " ANT"))
            dpg.add_button(label="Delete Account", callback=WipeAccount)



def Connect(sender, app_data):
    LoadingVal = 0

    while (True):
        dpg.set_value("Loading" , LoadingVal)
        LoadingVal = LoadingVal + 0.1
        time.sleep(0.1)
        if (LoadingVal > 1):
            dpg.delete_item("Main", children_only=False)
            Shop(0,0)
        
            break

with dpg.window(tag="Main"):
    dpg.add_text("ANet Client", pos=[300 - 55, 0])
    dpg.add_text("")
    dpg.add_text("")
    dpg.add_text("")
    dpg.add_text("")
    dpg.add_text("")
    dpg.add_text("")
    dpg.add_text("")

    dpg.add_slider_float(label="Encryption Status" , tag="Loading", default_value=0.0, max_value=1, pos=[40, 150])
    dpg.add_text("")
    dpg.add_button(label="Connect To Server", callback=Connect ,  pos=[40, 200] )

dpg.setup_dearpygui()
dpg.show_viewport()

dpg.set_primary_window("Main", True)

dpg.start_dearpygui()

dpg.destroy_context()