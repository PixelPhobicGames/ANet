import dearpygui.dearpygui as dpg
import time

from User import *

# Created By 

# NightWalkers 

dpg.create_context()
dpg.create_viewport(title='ANet Client - Ночные ходоки', width=600, height=300)


def Create(sender , app_data):
    dpg.delete_item("Create Account", children_only=False)
    Shop(0,0)

def CreateAccount(sender , app_data):
    dpg.delete_item("Settings Conf", children_only=False)
    with dpg.window(tag="Create Account"):
        dpg.set_primary_window("Create Account", True)
        dpg.add_text("Enter Name - (Real Name, Will Be Used for Orders)")
        Name = dpg.add_input_text(label="Name")
        dpg.add_text("Enter Phone Number")
        Number = dpg.add_input_int(label="Number")
        dpg.add_text("Enter Password")
        Password = dpg.add_input_int(label="Pass")
        dpg.add_button(label="Create" , callback=Create)
        if (Name != "" and Password != 0 ):
            GenerateIDInfo(Name , Number , Password)


def Shop(sender , app_data):
    with dpg.window(tag="ShopWindow"):
        dpg.set_primary_window("ShopWindow", True)
        dpg.delete_item("Settings Conf", children_only=False)
        with dpg.menu_bar():
            with dpg.menu(label="Shop"):
                dpg.add_menu_item(label="Open Shop")
            with dpg.menu(label="Account"):
                dpg.add_menu_item(label="Settings" , callback=Settings)

        if (PullID() == 0):
            dpg.add_text("No User Data Found, Please Create an Account", pos=[100, 50])
           

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