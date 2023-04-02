from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from PIL import Image,ImageTk
import tkinter.messagebox as messagebox
import mysql.connector



root = Tk()
root.geometry('1200x600')
root.configure(bg='white')


def showe():
     
    try:
        conn = mysql.connector.connect(
        user='root', password='', host='localhost', database='python_pos')
        
        if conn.is_connected():
            print("Connection to the database has been established.")
        else:
            print("Connection to the database has failed.")
    
        cur = conn.cursor()


        cur.execute("SELECT NAME FROM  stok_itms")
        rows = cur.fetchall()
        print(len(rows))
        '''
        for index, row in enumerate(rows):
            a = row
            print (a)
        '''
        

        cur.close()
        conn.close()
    except mysql.connector.Error as err:
      print(f"Failed to connect to database: {err}")    
   





'''

mydb = mysql.connector.connect(
                                     host='localhost',
                                     user='root',
                                     password='',
                                     database='python_pos'
)
 
# Printing the connection object
cursor = mydb.cursor()
 
# Show existing tables
cursor.execute("SHOW TABLES")
 
for x in cursor:
  print(x)

'''





#variables

indicator = 1 

password_chk = tk.StringVar(root)
password_chk = "ADMIN"

password = tk.StringVar(root)




#Db VARIABLES


#add to shop variables 

partnoShop = IntVar()
nameShop = StringVar()
modelShop = StringVar()
engineNoShop = StringVar()
brandShop  = StringVar()
priceShop = IntVar()
shopCounter= IntVar()
barcodeShop = IntVar()

#add to stock variables 

partnoStock = IntVar()
nameStock = StringVar()
modelStock = StringVar()
engineNoStock = StringVar()
brandStock  = StringVar()
priceStock = IntVar()
StockCounter= IntVar()
barcodeStock = IntVar()


#ADD TO LEDGER VARIABLES

Account_of        = StringVar()
PAYEMENT_METHOD   = StringVar()
DESCRIPTION       = StringVar()
Contact_NO        = StringVar()
DATE              = StringVar()
DEBIT             = IntVar()
CREDIT            = IntVar()
BALANCE           = IntVar()
EMAIL             = StringVar()


#frontENd Variables 

buttonFont = font.Font(family='Helvetica', size=10, weight='bold')
labelFont  =  font.Font(family='Helvetica', size=14, weight='bold')
heading_font = font.Font(family='Helvetica', size=10, weight='bold')
heading_font_2 = font.Font(family='Helvetica', size=12, weight='bold')
label_Entry_font = font.Font(family='Helvetica', size=14, weight='bold')

image_1 = Image.open("warehouse130.png")
photo_1 = ImageTk.PhotoImage(image_1 )
image_2 = Image.open("shop1330.png")
photo_2= ImageTk.PhotoImage(image_2)
image_3 = Image.open("lense.png")
photo_3= ImageTk.PhotoImage(image_3)
image_4 = Image.open("lense.png")
photo_4= ImageTk.PhotoImage(image_4)
image_5 = Image.open("ledger.png")
photo_5= ImageTk.PhotoImage(image_5)
image_6 = Image.open("diary.png")
photo_6= ImageTk.PhotoImage(image_6)
image_7 = Image.open("counter.png")
photo_7= ImageTk.PhotoImage(image_7)
image_8 = Image.open("settings2.png")
photo_8 = ImageTk.PhotoImage(image_8 )
image_9 = Image.open("ledgerd.png")
photo_9 = ImageTk.PhotoImage(image_9 )
image_10 = Image.open("product.png")
photo_10 = ImageTk.PhotoImage(image_10 )
image_11 = Image.open("add_stock.JFIF")
photo_11 = ImageTk.PhotoImage(image_11 )
image_12 = Image.open("stock.jpg")
photo_12 = ImageTk.PhotoImage(image_12 )
image_13 = Image.open("ledr.jpg")
photo_13 = ImageTk.PhotoImage(image_13 )
image_14 = Image.open("diry.JFIF")
photo_14 = ImageTk.PhotoImage(image_14 )
image_15 = Image.open("conttr.jpg")
photo_15 = ImageTk.PhotoImage(image_15 )
image_16 = Image.open("bilng.jpg")
photo_16 = ImageTk.PhotoImage(image_16 )
image_17 = Image.open("product.png")
photo_17 = ImageTk.PhotoImage(image_17 )
image_18 = Image.open("product.png")
photo_18 = ImageTk.PhotoImage(image_18 )
image_19 = Image.open("product.png")
photo_19 = ImageTk.PhotoImage(image_19 )
image_20 = Image.open("product.png")
photo_20 = ImageTk.PhotoImage(image_20 )









#LOGICAL FUNCTIONS

def enter_admin():

    password_a = password.get()  
    if password_a  == password_chk :
       messagebox.showinfo("ALERT", "ADMIN MODE ACTIVATED")       
       global indicator
       indicator = indicator + 1
       show_Dashboard()

    else :
       messagebox.showinfo("ALERT", "PASSWORD NOT MATCHED")   


def exit_admin():

    global indicator
    indicator = indicator - 1
    messagebox.showinfo("ALERT", "ADMIN MODE DEACTIVATED")


  


#DISPLAYING  functions 

def add_stock():
  if indicator == 2 :
      cf_2.pack_forget()
      cf_3.pack_forget()
      add_shop.pack_forget()
      add_LEDGER.pack_forget()
      transfer_transction.pack_forget()
      check_CUSTOMER.pack_forget()
      check_shop.pack_forget()
      check_stock.pack_forget()
      check_Ledger.pack_forget()
      check_Diary.pack_forget()
      check_counter.pack_forget()
      check_Billing.pack_forget()
      return_products.pack_forget()
      add_stock.pack(side='top' , anchor="n" , pady=40 , padx=30)
      add_stock.pack_propagate(0)
      settings_Mode.pack_forget()
      employe_mode.pack_forget()
      Login_Panel.pack_forget()
      
  else : 
      messagebox.showinfo("ALERT", "ENTER PASWORD TO ENTER")


def add_to_shop():
  if indicator == 2 :
      cf_2.pack_forget()
      cf_3.pack_forget()
      add_stock.pack_forget()  
      add_LEDGER.pack_forget()
      transfer_transction.pack_forget()
      check_CUSTOMER.pack_forget()
      check_shop.pack_forget()
      check_stock.pack_forget()
      check_Ledger.pack_forget()
      check_Diary.pack_forget()
      check_counter.pack_forget()
      check_Billing.pack_forget()
      return_products.pack_forget()
      ad_shop.pack(side='top' , anchor="n" , padx=0)
      ad_shop.pack_propagate(0)
      settings_Mode.pack_forget()
      employe_mode.pack_forget()
      Login_Panel.pack_forget()
  else : 
      messagebox.showinfo("ALERT", "ENTER PASWORD TO ENTER")

def add_to_ledger():
  if indicator == 2 :
      cf_2.pack_forget()
      cf_3.pack_forget()
      add_stock.pack_forget()  
      transfer_transction.pack_forget()
      check_CUSTOMER.pack_forget()
      check_shop.pack_forget()
      check_stock.pack_forget()
      check_Ledger.pack_forget()
      check_Diary.pack_forget()
      check_counter.pack_forget()
      check_Billing.pack_forget()
      return_products.pack_forget()
      ad_shop.pack_forget()
      add_LEDGER.pack(side='top' , anchor="n" , pady=40 , padx=30)
      add_LEDGER.pack_propagate(0) 
      settings_Mode.pack_forget()
      employe_mode.pack_forget()
      Login_Panel.pack_forget()
  
  else : 
      messagebox.showinfo("ALERT", "ENTER PASWORD TO ENTER")


def transfer_transctions():
  if indicator == 2 :
      cf_2.pack_forget()
      cf_3.pack_forget()
      add_stock.pack_forget()  
      check_CUSTOMER.pack_forget()
      check_shop.pack_forget()
      check_stock.pack_forget()
      check_Ledger.pack_forget()
      check_Diary.pack_forget()
      check_counter.pack_forget()
      check_Billing.pack_forget()
      return_products.pack_forget()
      ad_shop.pack_forget()
      add_LEDGER.pack_forget()
      transfer_transction.pack(side='top' , anchor="n" , pady=40 , padx=30)
      transfer_transction .pack_propagate(0)
      settings_Mode.pack_forget()
      employe_mode.pack_forget()
      Login_Panel.pack_forget()
  
  else : 
      messagebox.showinfo("ALERT", "ENTER PASWORD TO ENTER")

def Customer_Details():
  if indicator == 2 :
      cf_2.pack_forget()
      cf_3.pack_forget()
      add_stock.pack_forget()  
      check_shop.pack_forget()
      check_stock.pack_forget()
      check_Ledger.pack_forget()
      check_Diary.pack_forget()
      check_counter.pack_forget()
      check_Billing.pack_forget()
      return_products.pack_forget()
      ad_shop.pack_forget()
      add_LEDGER.pack_forget()
      transfer_transction.pack_forget()
      check_CUSTOMER.pack(side='top' , anchor="n" , padx=0)
      check_CUSTOMER.pack_propagate(0)
      settings_Mode.pack_forget()
      employe_mode.pack_forget()
      Login_Panel.pack_forget()
  else : 
      messagebox.showinfo("ALERT", "ENTER PASWORD TO ENTER")
 

def check_shop():
  if indicator == 2 :
      cf_2.pack_forget()
      cf_3.pack_forget()
      add_stock.pack_forget()  
      check_stock.pack_forget()
      check_Ledger.pack_forget()
      check_Diary.pack_forget()
      check_counter.pack_forget()
      check_Billing.pack_forget()
      return_products.pack_forget()
      ad_shop.pack_forget()
      add_LEDGER.pack_forget()
      transfer_transction.pack_forget()
      check_CUSTOMER.pack_forget()
      check_shop.pack(side='top' , anchor="n" , padx=0)
      check_shop.pack_propagate(0)
      settings_Mode.pack_forget()
      employe_mode.pack_forget()
      Login_Panel.pack_forget()
  else : 
      messagebox.showinfo("ALERT", "ENTER PASWORD TO ENTER")
 
def check_stock():
  if indicator == 2 :
      cf_2.pack_forget()
      cf_3.pack_forget()
      add_stock.pack_forget()  
      check_Ledger.pack_forget()
      check_Diary.pack_forget()
      check_counter.pack_forget()
      check_Billing.pack_forget()
      return_products.pack_forget()
      ad_shop.pack_forget()
      add_LEDGER.pack_forget()
      transfer_transction.pack_forget()
      check_CUSTOMER.pack_forget()
      check_shop.pack_forget()
      check_stock.pack(side='top' , anchor="n" , padx=0)
      check_stock.pack_propagate(0)
      settings_Mode.pack_forget()
      employe_mode.pack_forget()
      Login_Panel.pack_forget()
  else : 
      messagebox.showinfo("ALERT", "ENTER PASWORD TO ENTER")

def show_ledgr():
  if indicator == 2 :
      cf_2.pack_forget()
      cf_3.pack_forget()
      add_stock.pack_forget()  
      check_Diary.pack_forget()
      check_counter.pack_forget()
      check_Billing.pack_forget()
      return_products.pack_forget()
      ad_shop.pack_forget()
      add_LEDGER.pack_forget()
      transfer_transction.pack_forget()
      check_CUSTOMER.pack_forget()
      check_shop.pack_forget()
      check_stock.pack_forget()
      check_Ledger.pack(side='top' , anchor="n" , padx=0)
      check_Ledger.pack_propagate(0)
      settings_Mode.pack_forget()
      employe_mode.pack_forget()
      Login_Panel.pack_forget()
  else : 
      messagebox.showinfo("ALERT", "ENTER PASWORD TO ENTER")

def show_Diary():
  if indicator == 2 :
      cf_2.pack_forget()
      cf_3.pack_forget()
      add_stock.pack_forget()  
      check_CUSTOMER.pack_forget()
      check_shop.pack_forget()
      check_stock.pack_forget()
      check_Ledger.pack_forget()
      check_counter.pack_forget()
      check_Billing.pack_forget()
      return_products.pack_forget()
      ad_shop.pack_forget()
      add_LEDGER.pack_forget()
      transfer_transction.pack_forget()
      check_Diary.pack(side='top' , anchor="n" , padx=0)
      check_Diary.pack_propagate(0)
      settings_Mode.pack_forget()
      employe_mode.pack_forget()
      Login_Panel.pack_forget()
  else : 
      messagebox.showinfo("ALERT", "ENTER PASWORD TO ENTER")

def show_counter():

  cf_2.pack_forget()
  cf_3.pack_forget()
  add_stock.pack_forget()  
  check_CUSTOMER.pack_forget()
  check_shop.pack_forget()
  check_stock.pack_forget()
  check_Ledger.pack_forget()
  check_Diary.pack_forget()
  check_Billing.pack_forget()
  return_products.pack_forget()
  ad_shop.pack_forget()
  add_LEDGER.pack_forget()
  transfer_transction.pack_forget()
  check_counter.pack(side='top' , anchor="n" , padx=0)
  check_counter.pack_propagate(0)
  settings_Mode.pack_forget()
  employe_mode.pack_forget()
  Login_Panel.pack_forget()


def show_Billing():
  cf_2.pack_forget()
  cf_3.pack_forget()
  add_stock.pack_forget()  
  check_CUSTOMER.pack_forget()
  check_shop.pack_forget()
  check_stock.pack_forget()
  check_Ledger.pack_forget()
  check_Diary.pack_forget()
  check_counter.pack_forget()
  return_products.pack_forget()
  ad_shop.pack_forget()
  add_LEDGER.pack_forget()
  transfer_transction.pack_forget()
  check_Billing.pack(side='top' , anchor="n" , padx=0)
  check_Billing.pack_propagate(0)
  employe_mode.pack_forget()
  settings_Mode.pack_forget()
  Login_Panel.pack_forget()



def return_products():

  cf_2.pack_forget()
  cf_3.pack_forget()
  add_stock.pack_forget()  
  check_CUSTOMER.pack_forget()
  check_shop.pack_forget()
  check_stock.pack_forget()
  check_Ledger.pack_forget()
  check_Diary.pack_forget()
  check_counter.pack_forget()
  return_products.pack_forget()
  ad_shop.pack_forget()
  add_LEDGER.pack_forget()
  transfer_transction.pack_forget()
  check_Billing.pack_forget()
  return_products.pack(side='top' , anchor="n" , padx=0)
  return_products.pack_propagate(0)
  settings_Mode.pack_forget()
  employe_mode.pack_forget()
  Login_Panel.pack_forget()


def show_Dashboard():
  if indicator == 2 :
      add_stock.pack_forget()  
      check_shop.pack_forget()
      check_stock.pack_forget()
      check_Ledger.pack_forget()
      check_Diary.pack_forget()
      check_counter.pack_forget()
      check_Billing.pack_forget()
      return_products.pack_forget()
      ad_shop.pack_forget()
      add_LEDGER.pack_forget()
      transfer_transction.pack_forget()
      check_CUSTOMER.pack_forget()
      cf_2.pack(side='top' , anchor="n" , pady=20)
      centerframe_2.pack_propagate(0)
      cf_3.pack(side='top' , anchor="n" , padx=0)
      centerframe_3.pack_propagate(0)
      Login_Panel.pack_forget()
      settings_Mode.pack_forget()
      employe_mode.pack_forget()
      Login_Panel.pack_forget()
  else : 
      messagebox.showinfo("ALERT", "ENTER PASWORD TO ENTER")

def shows_settings():

  add_stock.pack_forget()  
  check_shop.pack_forget()
  check_stock.pack_forget()
  check_Ledger.pack_forget()
  check_Diary.pack_forget()
  check_counter.pack_forget()
  check_Billing.pack_forget()
  return_products.pack_forget()
  ad_shop.pack_forget()
  add_LEDGER.pack_forget()
  transfer_transction.pack_forget()
  check_CUSTOMER.pack_forget()
  cf_2.pack_forget()
  cf_3.pack_forget()
  Login_Panel.pack_forget()
  employe_mode.pack_forget()
  settings_Mode.pack(side='top' , anchor="n" , padx=0 , pady=35)
  settings_Mode.pack_propagate(0)


def show_loginPanel():

  add_stock.pack_forget()  
  check_shop.pack_forget()
  check_stock.pack_forget()
  check_Ledger.pack_forget()
  check_Diary.pack_forget()
  check_counter.pack_forget()
  check_Billing.pack_forget()
  return_products.pack_forget()
  ad_shop.pack_forget()
  add_LEDGER.pack_forget()
  transfer_transction.pack_forget()
  check_CUSTOMER.pack_forget()
  cf_2.pack_forget()
  cf_3.pack_forget()
  settings_Mode.pack_forget()
  employe_mode.pack_forget()
  Login_Panel.pack(side='top' , anchor="n" , padx=0 , pady=35)
  Login_Panel.pack_propagate(0)

def employe_panel():

  add_stock.pack_forget()  
  check_shop.pack_forget()
  check_stock.pack_forget()
  check_Ledger.pack_forget()
  check_Diary.pack_forget()
  check_counter.pack_forget()
  check_Billing.pack_forget()
  return_products.pack_forget()
  ad_shop.pack_forget()
  add_LEDGER.pack_forget()
  transfer_transction.pack_forget()
  check_CUSTOMER.pack_forget()
  cf_2.pack_forget()
  cf_3.pack_forget()
  settings_Mode.pack_forget()
  Login_Panel.pack_forget()
  employe_mode.pack(side='top' , anchor="n" , padx=0 , pady = 150)
  employe_mode.pack_propagate(0) 
  


#secondary displaying functions 

def show_Table(): 
   
  retrn_table_Area.pack(side='right' , anchor="n" , padx=10 , pady= 10)
  

def remove_entry():
  
  entry1.delete(0, END)
  entry2.delete(0, END)
  entry3.delete(0, END)
  entry4.delete(0, END)
  entry5.delete(0, END)
  entry6.delete(0, END)
  entry7.delete(0, END)




#Db functions 

def adToShock():
    prtnostk = partnoStock.get()
    nmestk = nameStock .get()
    mdlnostk = modelStock.get() 
    engnnostk = engineNoStock.get()
    brndstk = brandStock.get() 
    prstk = priceStock.get()
    
    bcodestk = barcodeStock.get()
   
    
    try:
        #establishing the connection
        conn = mysql.connector.connect(
        user='root', password='', host='localhost', database='python_pos')

        cur = conn.cursor()

        # Define the data to be inserted


        # Execute the INSERT statement using the data as variables
        cur.execute("INSERT INTO shopitems(Part_NO , NAME , MODEL , ENGINE , BRAND , PRICE, BACODE_NO ) VALUES (%d, '%s' , '%s', '%s' , '%s' , %d , %d  )" % (prtnostk , nmestk  , mdlnostk ,engnnostk  ,  brndstk ,  prstk , bcodestk ))

        # Commit the transaction and close the cursor and connection
        conn.commit()
        cur.close()
        conn.close()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))


def adToShop():
    prtnosh = partnoShop.get()
    nmesh = nameShop.get()
    mdlnosh = modelShop.get() 
    engnnosh = engineNoShop.get()
    brndsh = brandShop.get() 
    prsh = priceShop.get()
    shopCounter.get()
    bcodesh = barcodeShop.get()
   

    entry_8_ad_shop.delete(0, END)
    
    try:
        #establishing the connection
        conn = mysql.connector.connect(
        user='root', password='', host='localhost', database='python_pos')

        cur = conn.cursor()

        # Define the data to be inserted


        # Execute the INSERT statement using the data as variables
        cur.execute("INSERT INTO stok_itms(Part_NO , NAME , MODEL , ENGINE , BRAND , PRICE, BACODE_NO ) VALUES (%d, '%s' , '%s', '%s' , '%s' , %d , %d  )" % (prtnosh , nmesh , mdlnosh , engnnosh ,  brndsh  ,  prsh, bcodesh  ))

        # Commit the transaction and close the cursor and connection
        conn.commit()
        cur.close()
        conn.close()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))




def CREATE_LEDGER():
    AccountOf = Account_of.get()
    Paymntmthd = PAYEMENT_METHOD.get()
    dscrption = DESCRIPTION.get() 
    contactno = Contact_NO.get()
    date = DATE.get()
    debit =  DEBIT.get()
    credit = CREDIT.get()
    baalnce = BALANCE.get()
    email = EMAIL.get()
   

    
    try:
        #establishing the connection
        conn = mysql.connector.connect(
        user='root', password='', host='localhost', database='python_pos')

        cur = conn.cursor()
        
  
        # Execute the INSERT statement using the data as variables
        cur.execute(f"CREATE TABLE {AccountOf} ( Account_of VARCHAR(255) , PAYEMENT_METHOD VARCHAR(255) , DESCRIPTION VARCHAR(255) , Contact_NO VARCHAR(255) , DATE  VARCHAR(255)  , DEBIT INT ,  CREDIT INT , BALANCE INT , EMAIL  VARCHAR(255)     )")
        cur.execute(f"INSERT INTO {AccountOf} (Account_of , PAYEMENT_METHOD, DESCRIPTION , Contact_NO ,  DATE ,DEBIT , CREDIT ,  BALANCE  , EMAIL  ) VALUES ('%s', '%s' , '%s', '%s' , '%s' , %d , %d , %d , '%s'  )" % (AccountOf , Paymntmthd  ,dscrption , contactno ,  date ,  debit, credit  , baalnce , email  ))
        # Commit the transaction and close the cursor and connection
        conn.commit()
        cur.close()
        conn.close()
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))



# left frame
lframe = Frame(root,width=200, height= 800, bg="black", highlightthickness=0 , highlightbackground="white")
lframe.pack(side='left' , anchor="n")
lframe.pack_propagate(0)

f_1 = Frame(lframe, highlightbackground="#525050", bg="black" , highlightthickness=1 , width=200, height= 50)
f_1.pack(  anchor="nw")
f_1.pack_propagate(0)
btnf_1 =Button(f_1, bd=0 ,text='ADD TO STOCK'  , bg='black', fg='white'  , font=buttonFont,  width=190, height= 4 , command = add_stock )
btnf_1.pack( pady= 0,anchor="n")

f_2 = Frame(lframe, highlightbackground="#525050", bg="black" , highlightthickness=1, width=200, height= 50)
f_2.pack(  anchor="nw")
f_2.pack_propagate(0)
btnf_2 =Button(f_2, bd=0 ,text='ADD TO SHOP'  , bg='black', fg='white'  , font=buttonFont,  width=190, height= 4  , command = add_to_shop)
btnf_2.pack( pady= 0,anchor="n")


f_3 = Frame(lframe, highlightbackground="#525050", bg="black" , highlightthickness=1, width=200, height= 50)
f_3.pack(  anchor="nw")
f_3.pack_propagate(0)
btnf_3 =Button(f_3, bd=0 ,text='ADD TO LEDGER'  , bg='black', fg='white'  , font=buttonFont,  width=190, height= 4  , command = add_to_ledger)
btnf_3.pack( pady= 0,anchor="n")


f_4 = Frame(lframe, highlightbackground="#525050", bg="black" , highlightthickness=1 , width=200, height= 50)
f_4 .pack(  anchor="nw")
f_4 .pack_propagate(0)
btnf_4 =Button(f_4, bd=0 ,text='TRANSFER TRANSCITIONS'  , bg='black', fg='white'  , font=buttonFont,  width=190, height= 4  , command = transfer_transctions )
btnf_4.pack( pady= 0,anchor="n")


f_5  = Frame(lframe, highlightbackground="#525050", bg="black" , highlightthickness=1 , width=200, height= 50)
f_5 .pack(  anchor="nw")
f_5 .pack_propagate(0)
btnf_5 =Button(f_5, bd=0 ,text='CUSTOMER DETAILS'  , bg='black', fg='white'  , font=buttonFont,  width=190, height= 4 , command = Customer_Details)
btnf_5.pack( pady= 0,anchor="n")

f_6 = Frame(lframe, highlightbackground="#525050", bg="black" , highlightthickness=1, width=200, height= 50)
f_6 .pack(  anchor="nw")
f_6 .pack_propagate(0)
btnf_6 =Button(f_6, bd=0 ,text='CHECK SHOP'  , bg='black', fg='white'  , font=buttonFont,  width=190, height= 4  , command = check_shop)
btnf_6.pack( pady= 0,anchor="n")


f_7  = Frame(lframe, highlightbackground="#525050", bg="black" , highlightthickness=1 , width=200, height= 50)
f_7.pack(  anchor="nw")
f_7.pack_propagate(0)
btnf_7 =Button(f_7, bd=0 ,text='CHECK STOCK'  , bg='black', fg='white'  , font=buttonFont,  width=190, height= 4 , command = check_stock)
btnf_7.pack( pady= 0,anchor="n")

f_8 = Frame(lframe, highlightbackground="#525050", bg="black" , highlightthickness=1 , width=200, height= 50)
f_8 .pack(  anchor="nw")
f_8 .pack_propagate(0)
btnf_8 =Button(f_8, bd=0 ,text='CHECK LEDGER'  , bg='black', fg='white'  , font=buttonFont,  width=190, height= 4 , highlightbackground="#00bfff", highlightthickness=1 , command = show_ledgr)
btnf_8.pack( pady= 0,anchor="n")

f_9 = Frame(lframe, highlightbackground="#525050", bg="black" , highlightthickness=1 , width=200, height= 50)
f_9.pack(  anchor="nw")
f_9.pack_propagate(0)
btnf_9 =Button(f_9, bd=0 ,text='CHECK DIARY'  , bg='black', fg='white'  , font=buttonFont,  width=190, height= 4 , highlightbackground="#00bfff", highlightthickness=1 , command = show_Diary )
btnf_9.pack( pady= 0,anchor="n")

f_10 = Frame(lframe, highlightbackground="#525050", bg="black" , highlightthickness=1 , width=200, height= 50)
f_10.pack(  anchor="nw")
f_10.pack_propagate(0)
btnf_10 =Button(f_10, bd=0 ,text='COUNTER'  , bg='black', fg='white'  , font=buttonFont,  width=190, height= 4 , highlightbackground="#00bfff", highlightthickness=1 , command = show_counter)
btnf_10.pack( pady= 0,anchor="n")

f_11 = Frame(lframe, highlightbackground="#525050", bg="black" , highlightthickness=1 , width=200, height= 50)
f_11.pack(  anchor="nw")
f_11.pack_propagate(0)
btnf_11 =Button(f_11, bd=0 ,text='BILLING'  , bg='black', fg='white'  , font=buttonFont,  width=190, height= 4 , highlightbackground="#00bfff", highlightthickness=1  , command = show_Billing)
btnf_11.pack( pady= 0,anchor="n")

f_12 = Frame(lframe, highlightbackground="#525050", bg="black" , highlightthickness=1 , width=200, height= 50)
f_12.pack(  anchor="nw")
f_12 .pack_propagate(0)
btnf_12 =Button(f_12, bd=0 ,text='Return Items'  , bg='black', fg='white'  , font=buttonFont,  width=190, height= 4 , highlightbackground="#00bfff", highlightthickness=1 , command = return_products)
btnf_12.pack( pady= 0,anchor="n")

f_last = Frame(lframe, highlightbackground="#525050", bg="black" , highlightthickness=1 , width=200, height= 50)
f_last.pack(  pady= 10, anchor="nw")
f_last.pack_propagate(0)
btnf_last =Button(f_last, bd=0 ,text='DASHBOARD'  , bg='green', fg='white'  , font=buttonFont,  width=190, height= 4 , highlightbackground="#00bfff", highlightthickness=1 , command = show_Dashboard)
btnf_last.pack( pady= 0,anchor="n")




# Center  frames 

centerframe_1  = Frame(root,width=1200, height= 70, bg="black" , highlightthickness=1 , highlightbackground="#89CFF0")
centerframe_1.pack(side='top' , anchor="n" , pady=0)
centerframe_1.pack_propagate(0)

label = Label( centerframe_1, text = "ENTER AS AN ADMIN", relief=RAISED , bg= 'black' , bd=0 , font=heading_font , fg='white' )
label.grid(row = 1 , column = 1 ,  pady= 20,  padx= 240 )

buton_centerframe_1  = Button(centerframe_1 ,bd=0.5,text='LOGIN PANEL' , bg='green', fg='white'  , font=buttonFont,  width=12 , command = show_loginPanel )
buton_centerframe_1.grid(row = 1 , column = 3 ,  pady=20,  padx= 240)





#centerframe 2

cf_2 = centerframe_2  = Frame(root,width=1200, height= 240, bg="white")
centerframe_2.pack(side='top' , anchor="n" , pady=20)
centerframe_2.pack_propagate(0)


cf2_f1 = Frame(centerframe_2,width=250, height=  300, bg="black")
cf2_f1.pack(side='left' , anchor="n" , padx=18)
cf2_f1.pack_propagate(0)

label = Label( cf2_f1, text = "ADD TO STOCK", relief=RAISED , bg= 'black' , bd=0 , font=labelFont , fg='white' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )

label = Label( cf2_f1,  image= photo_1 , bg= 'black' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )

cf2_buton = Button(cf2_f1,bd=0.5,text='ADD TO STOCK' , bg='green', fg='white'  , font=buttonFont,  width=12 ,  height= 1 , command = add_stock)
cf2_buton.pack( pady= 0,anchor="n")

cf2_f2 = Frame(centerframe_2,width=250, height=  300, bg="black")
cf2_f2.pack(side='left' , anchor="n" , padx=18)
cf2_f2.pack_propagate(0)



label = Label( cf2_f2, text = "ADD TO SHOP", relief=RAISED , bg= 'black' , bd=0 , font=labelFont , fg='white' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )

label = Label( cf2_f2,  image= photo_2 , bg= 'black' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )

buton = Button(cf2_f2 ,bd=0.5,text='ADD TO SHOP' , bg='green', fg='white'  , font=buttonFont,  width=12 ,  height= 1  )
buton.pack( pady= 0,anchor="n")

cf2_f3 = Frame(centerframe_2,width=250, height= 300, bg="black")
cf2_f3.pack(side='left' , anchor="n" , padx=18)
cf2_f3.pack_propagate(0)

label = Label( cf2_f3, text = "CHECK SHOP", relief=RAISED , bg= 'black' , bd=0 , font=labelFont , fg='white' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )

label = Label( cf2_f3,  image= photo_3 , bg= 'black' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )

buton = Button(cf2_f3 ,bd=0.5,text='CHECK SHOP' , bg='green', fg='white'  , font=buttonFont,  width=12 ,  height= 1  )
buton.pack( pady= 0,anchor="n")

cf2_f4 = Frame(centerframe_2,width=250, height= 300, bg="black")
cf2_f4.pack(side='left' , anchor="n" ,padx=18)
cf2_f4.pack_propagate(0)

label = Label(cf2_f4, text = "CHECK STOCK", relief=RAISED , bg= 'black' , bd=0 , font=labelFont , fg='white' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )

label = Label( cf2_f4,  image= photo_4 , bg= 'black' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )

buton = Button(cf2_f4 ,bd=0.5,text='CHECK STOCK' , bg='green', fg='white'  , font=buttonFont,  width=12 ,  height= 1)
buton.pack( pady= 0,anchor="n")

cf_2.pack_forget()



#centerframe 3

cf_3  = centerframe_3  = Frame(root,width=1200, height= 240 , bg="white")
centerframe_3.pack(side='top' , anchor="n" , padx=0)
centerframe_3.pack_propagate(0)


cf3_f1 = Frame(centerframe_3,width=250, height= 300, bg="black")
cf3_f1.pack(side='left' , anchor="n" , padx=18)
cf3_f1.pack_propagate(0)
label = Label(cf3_f1, text = "LEGDER", relief=RAISED , bg= 'black' , bd=0 , font=labelFont , fg='white' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )
label = Label(cf3_f1,  image= photo_5 , bg= 'black' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )
buton = Button(cf3_f1  ,bd=0.5,text='LEGDER' , bg='green', fg='white'  , font=buttonFont,  width=12 )
buton.pack( pady= 0,anchor="n")

cf3_f2 = Frame(centerframe_3,width=250, height= 300, bg="black")
cf3_f2.pack(side='left' , anchor="n" , padx=18)
cf3_f2.pack_propagate(0)
label = Label(cf3_f2, text = "DIARY'", relief=RAISED , bg= 'black' , bd=0 , font=labelFont , fg='white' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )
label = Label(cf3_f2,  image= photo_6 , bg= 'black' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )
buton = Button(cf3_f2  ,bd=0.5,text='DIARY' , bg='green', fg='white'  , font=buttonFont,  width=12 ,  height= 1  )
buton.pack( pady= 0,anchor="n")

cf3_f3 = Frame(centerframe_3,width=250, height= 300, bg="black")
cf3_f3.pack(side='left' , anchor="n" , padx=18)
cf3_f3.pack_propagate(0)
label = Label(cf3_f3, text = "COUNTER", relief=RAISED , bg= 'black' , bd=0 , font=labelFont , fg='white' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )
label = Label(cf3_f3,  image= photo_7 , bg= 'black' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )
buton = Button(cf3_f3   ,bd=0.5,text='COUNTER' , bg='green', fg='white'  , font=buttonFont,  width=12 ,  height= 1 )
buton.pack( pady= 0,anchor="n")

cf3_f4 = Frame(centerframe_3,width=250, height= 300, bg="black")
cf3_f4.pack(side='left' , anchor="n" , padx=18)
cf3_f4.pack_propagate(0)
label = Label(cf3_f4, text = "settings", relief=RAISED , bg= 'black' , bd=0 , font=labelFont , fg='white' )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )
label = Label(cf3_f4,  image= photo_8 , bg= 'black' )
label.pack(side='top' , anchor="n" , pady=20, padx=20 )
buton = Button(cf3_f4 ,bd=0.5,text='settings' , bg='green', fg='white'  , font=buttonFont,  width=12 ,  height= 1 ,command = shows_settings )
buton.pack( pady= 0,anchor="n")

cf_3.pack_forget()





#employe_ mode 

employe_mode  = Frame(root,width=1200, height= 240 , bg="white")
employe_mode.pack(side='top' , anchor="n" , padx=0 , pady = 150)
employe_mode.pack_propagate(0)

cf1_em = Frame(employe_mode ,width=250, height= 300, bg="black")
cf1_em.pack(side='left' , anchor="n" , padx=128)
cf1_em.pack_propagate(0)
label1_em = Label(cf1_em , text = "COUNTER", relief=RAISED , bg= 'black' , bd=0 , font=labelFont , fg='white' )
label1_em.pack(side='top' , anchor="n" , pady=10, padx=0 )
label1_em = Label(cf1_em ,  image= photo_7 , bg= 'black' )
label1_em.pack(side='top' , anchor="n" , pady=10, padx=20 )
buton1_em = Button(cf1_em    ,bd=0.5,text='COUNTER' , bg='green', fg='white'  , font=buttonFont,  width=12 ,  height= 1 )
buton1_em.pack( pady= 0,anchor="n")

cf2_em = Frame(employe_mode ,width=250, height= 300, bg="black")
cf2_em.pack(side='left' , anchor="n" , padx=128)
cf2_em.pack_propagate(0)
label2_em = Label(cf2_em , text = "BILLING", relief=RAISED , bg= 'black' , bd=0 , font=labelFont , fg='white' )
label2_em.pack(side='top' , anchor="n" , pady=10, padx=20 )
label2_em = Label(cf2_em ,  image= photo_7 , bg= 'black' )
label2_em.pack(side='top' , anchor="n" , pady=10, padx=20 )
buton2_em = Button(cf2_em ,bd=0.5,text='BILLING' , bg='green', fg='white'  , font=buttonFont,  width=12 ,  height= 1 )
buton2_em.pack( pady= 0,anchor="n")

employe_mode.pack_forget()


# Login PAnel 

Login_Panel = Frame(root,width=400, height= 550,  bg="black" )
Login_Panel.pack(side='top' , anchor="n" , padx=0 , pady=35)
Login_Panel.pack_propagate(0)

label_Login_Panel  = Label(Login_Panel, text=" LOGIN PANEl ", font=("Courier 18 bold") , fg = 'white' , bg = 'black')
label_Login_Panel.grid(row = 1 , column = 2 , padx=10 , pady=60)

label2_Login_Panel  = Label(Login_Panel, text="ENTER THE PASSOWRD FOR ADMIN CONTROLS", font=("Courier 12 bold") , fg = 'white' , bg = 'black')
label2_Login_Panel.grid(row = 2 , column = 2 , padx=55 , pady=5)

entry_Login_Panel  = Entry(Login_Panel, width=22, fg='black',font=('Arial',16,'bold') ,highlightthickness=0.5 , highlightbackground="black"  , textvariable=password  )
entry_Login_Panel.grid(row = 3 , column = 2  , padx=10 , pady=5)

button1_Login_Panel = Button(Login_Panel,bd=0.5,text='ENTER AS ADMIN', bg='green', fg='white'  , font=buttonFont,  width=14 , command = enter_admin )
button1_Login_Panel.grid(row = 4 , column =  2 , padx=10 , pady=10)

button2_Login_Panel = Button(Login_Panel,bd=0.5,text='EXIT AS ADMIN', bg='RED', fg='white'  , font=buttonFont,  width=14 , command = exit_admin )
button2_Login_Panel.grid(row = 5 , column =  2 , padx=10 , pady=10)

button3_Login_Panel= Button(Login_Panel,bd=0.5,text='EMPLOYE LOGIN', bg='blue', fg='white'  , font=buttonFont,  width=14 , command = showe )
button3_Login_Panel.grid(row = 6 , column =  2 , padx=10 , pady=60)

Login_Panel.pack_forget()





#add to stock 

ad_stock = add_stock = Frame(root,width=1300, height= 980, bg="white")
add_stock.pack(side='top' , anchor="n" , pady= 10 , padx=30)
add_stock.pack_propagate(0)

ad_stock_entry_area = Frame(add_stock , width=1000, height= 780, bg = "black")
ad_stock_entry_area.pack(side='top' , anchor="n" , padx=5 , pady = 20)

label_1_ad_stock = Label(ad_stock_entry_area , text = "PART NO", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_1_ad_stock.grid(row = 1 , column = 1 , pady=19 , padx=14)
entry_1_ad_stock = Entry(ad_stock_entry_area , width=24, fg='black',font=('Arial',16,'bold')  ,highlightthickness=0.5 , highlightbackground="black" , textvariable= partnoStock)
entry_1_ad_stock.grid(row= 1, column=2  , padx=19 )

label_2_ad_stock = Label(ad_stock_entry_area , text = "NAME", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_2_ad_stock.grid(row = 2 , column = 1 , pady=19 , padx=14)
entry_2_ad_stock = Entry(ad_stock_entry_area  , width=24, fg='black',font=('Arial',16,'bold')  ,highlightthickness=0.5 , highlightbackground="black" , textvariable = nameStock)
entry_2_ad_stock.grid(row= 2, column=2 ,padx=19 )

label_3_ad_stock = Label(ad_stock_entry_area , text = "MODEL", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_3_ad_stock.grid(row = 3 , column = 1 , pady=19 , padx=14 )
entry_3_ad_stock = Entry(ad_stock_entry_area , width=24, fg='black',font=('Arial',16,'bold') ,highlightthickness=0.5 , highlightbackground="black" ,textvariable = modelStock)
entry_3_ad_stock.grid(row= 3, column=2 ,padx=19)

label_4_ad_stock = Label(ad_stock_entry_area , text = "ENGINE", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_4_ad_stock.grid(row = 4 , column = 1 ,pady=19 , padx=14 )
entry_4_ad_stock = Entry(ad_stock_entry_area ,width=24, fg='black',font=('Arial',16,'bold') ,highlightthickness=0.5 , highlightbackground="black" ,textvariable = engineNoStock)
entry_4_ad_stock.grid(row= 4, column=2 , padx=19)

label_5_ad_stock = Label(ad_stock_entry_area , text = "BRAND", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_5_ad_stock.grid(row = 5, column = 1 , pady=19 , padx=14)
entry_5_ad_stock = Entry(ad_stock_entry_area , width=24, fg='black',font=('Arial',16,'bold'),highlightthickness=0.5 , highlightbackground="black"  ,textvariable = brandStock )
entry_5_ad_stock.grid(row= 5, column=2 , padx=19, pady=14)

label_6_ad_stock= Label(ad_stock_entry_area , text = "Price", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_6_ad_stock.grid(row = 6, column = 1 , pady=19 , padx=14)
entry_6_ad_stock= Entry(ad_stock_entry_area  , width=24, fg='black',font=('Arial',16,'bold') ,highlightthickness=0.5 , highlightbackground="black"  ,textvariable = priceStock )
entry_6_ad_stock.grid(row= 6, column= 2  , padx=19  , pady=14  )


label_7_ad_stock= Label(ad_stock_entry_area , text = "PRODUCTS ADDED", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_7_ad_stock.grid(row = 4, column = 5 , pady=19 , padx=14)
entry_7_ad_stock = Entry(ad_stock_entry_area  , width=10, fg='black',font=('Arial',16,'bold') ,highlightthickness=0.5 , highlightbackground="black"  ,textvariable = StockCounter)
entry_7_ad_stock.grid(row= 4, column= 7  , padx=19  , pady=14  )
entry_7_ad_stock.insert(END  , "1")

label_8_ad_stock = Label(ad_stock_entry_area , text = "BAR CODE NO .", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_8_ad_stock.grid(row = 7 , column = 1 , pady=8 , padx=14)
entry_8_ad_stock =Entry(ad_stock_entry_area , width=24, fg='black',font=('Arial',16,'bold') ,highlightthickness=0.5 , highlightbackground="black" ,textvariable = barcodeStock  )
entry_8_ad_stock.grid(row= 7, column= 2  , padx=19  , pady= 5  )

button_ad_stock= Button(ad_stock_entry_area , bd=0.5 ,text='ADD WITH SHOP' , bg='green', fg='white'  , font=buttonFont,  width=18 )
button_ad_stock.grid( row= 7 , column= 5 , pady = 2 )

button2_ad_stock= Button(ad_stock_entry_area , bd=0.5 ,text='ADD TO STOCK' , bg='green', fg='white'  , font=buttonFont,  width=18 , command = adToShock )
button2_ad_stock.grid( row= 7 , column= 7 , pady = 2 )

ad_stock.pack_forget()

#add to shop

ad_shop = add_shop = Frame(root,width=1300, height= 880, bg="white" )
add_shop.pack(side='top' , anchor="n" , padx=0)
add_shop.pack_propagate(0)
 
ad_shop_entry_area =Frame(ad_shop,width=1000, height= 780, bg = "black")
ad_shop_entry_area.pack(side='top' , anchor="n" , padx=5 , pady = 70)

label_1_ad_shop = Label(ad_shop_entry_area, text = "PART NO", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_1_ad_shop.grid(row = 1 , column = 1 , pady=19 , padx=14)
entry_1_ad_shop = Entry(ad_shop_entry_area, width=24, fg='black',font=('Arial',16,'bold')  ,highlightthickness=0.5 , highlightbackground="black" ,  textvariable= partnoShop)
entry_1_ad_shop.grid(row= 1, column=2  , padx=19 )

label_2_ad_shop = Label(ad_shop_entry_area, text = "NAME", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_2_ad_shop.grid(row = 2 , column = 1 , pady=19 , padx=14)
entry_2_ad_shop  = Entry(ad_shop_entry_area , width=24, fg='black',font=('Arial',16,'bold')  ,highlightthickness=0.5 , highlightbackground="black" , textvariable = nameShop)
entry_2_ad_shop.grid(row= 2, column=2 ,padx=19 )

label_3_ad_shop = Label(ad_shop_entry_area, text = "MODEL", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_3_ad_shop.grid(row = 3 , column = 1 , pady=19 , padx=14 )
entry_3_ad_shop  = Entry(ad_shop_entry_area , width=24, fg='black',font=('Arial',16,'bold') ,highlightthickness=0.5 , highlightbackground="black" , textvariable = modelShop)
entry_3_ad_shop.grid(row= 3, column=2 ,padx=19)

label_4_ad_shop = Label(ad_shop_entry_area, text = "ENGINE", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_4_ad_shop.grid(row = 4 , column = 1 ,pady=19 , padx=14 )
entry_4_ad_shop  = Entry(ad_shop_entry_area,width=24, fg='black',font=('Arial',16,'bold') ,highlightthickness=0.5 , highlightbackground="black" , textvariable = engineNoShop )
entry_4_ad_shop.grid(row= 4, column=2 , padx=19)

label_5_ad_shop = Label(ad_shop_entry_area, text = "BRAND", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_5_ad_shop.grid(row = 5, column = 1 , pady=19 , padx=14)
entry_5_ad_shop  = Entry(ad_shop_entry_area , width=24, fg='black',font=('Arial',16,'bold'),highlightthickness=0.5 , highlightbackground="black"  , textvariable = brandShop)
entry_5_ad_shop.grid(row= 5, column=2 , padx=19, pady=14)

label_6_ad_shop = Label(ad_shop_entry_area, text = "Price", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_6_ad_shop.grid(row = 6, column = 1 , pady=19 , padx=14)
entry_6_ad_shop = Entry(ad_shop_entry_area , width=24, fg='black',font=('Arial',16,'bold') ,highlightthickness=0.5 , highlightbackground="black" ,   textvariable = priceShop )
entry_6_ad_shop.grid(row= 6, column= 2  , padx=19  , pady=14  )


label_7_ad_shop = Label(ad_shop_entry_area, text = "PRODUCTS ADDED", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_7_ad_shop.grid(row = 4, column = 5 , pady=19 , padx=14)
entry_7_ad_shop = Entry(ad_shop_entry_area , width=10, fg='black',font=('Arial',16,'bold') ,highlightthickness=0.5 , highlightbackground="black"  ,  textvariable = shopCounter)
entry_7_ad_shop .grid(row= 4, column= 7  , padx=19  , pady=14  )


label_8_ad_shop = Label(ad_shop_entry_area, text = "BAR CODE NO .", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=label_Entry_font )
label_8_ad_shop.grid(row = 7 , column = 1 , pady=14 , padx=14)
entry_8_ad_shop =Entry(ad_shop_entry_area , width=24, fg='black',font=('Arial',16,'bold') ,highlightthickness=0.5 , highlightbackground="black"  ,  textvariable = barcodeShop)
entry_8_ad_shop.grid(row= 7, column= 2  , padx=19  , pady=10  )

button_ad_shop = Button(ad_shop_entry_area , bd=0.5 ,text='ADD PRODUCT' , bg='green', fg='white'  , font=buttonFont,  width=18 , command =  adToShop )
button_ad_shop.grid( row= 7 , column= 5 , pady = 8 )

ad_shop.pack_forget()




#ADD TO LEDGER 

ad_LEDGER = add_LEDGER = Frame(root,width=1300, height= 580, bg="black" )
add_LEDGER.pack(side='top' , anchor="n" , pady=40 , padx=5)
add_LEDGER.pack_propagate(0)

labelad_LEDGER = Label(ad_LEDGER, text = "GENERAL LEDGER", relief=RAISED , bg= 'black'  , fg = 'white', bd=0  , font=('Arial',18,'bold') )
labelad_LEDGER.pack(side='top' , anchor="n" , pady=55 , padx=15)

table_area_ad_LEDGER = Frame(ad_LEDGER,width=1200, height= 480, bg="black" )
table_area_ad_LEDGER.pack(side='bottom' , anchor="n" , padx=0)

tblHed_ad_LEDGER = Frame(ad_LEDGER,width=1200, height= 18, bg="blue" )
tblHed_ad_LEDGER.pack(side='bottom' , anchor="n" , padx=0)


entry1_ad_LEDGER= Entry(table_area_ad_LEDGER , width=20, fg='white' , bg= 'black',font=('Arial',12,'bold') )
entry1_ad_LEDGER.grid(row= 2, column=1  , padx=0 )
entry1_ad_LEDGER.insert(END ,  "Account of") 

entry2_ad_LEDGER= Entry(table_area_ad_LEDGER , width=40, fg='black' , bg= 'white',font=('Arial',12,'bold') ,  textvariable= Account_of )
entry2_ad_LEDGER.grid(row= 2, column=2 , padx=0 )


entry3_ad_LEDGER= Entry(table_area_ad_LEDGER , width=20, fg='white', bg= 'black',font=('Arial',12,'bold')  )
entry3_ad_LEDGER.grid(row= 3, column=1  , padx=0 )
entry3_ad_LEDGER.insert(END ,  "PAYEMENT METHOD") 

entry4_ad_LEDGER= Entry(table_area_ad_LEDGER , width=40, fg='black' , bg= 'white',font=('Arial',12,'bold') ,  textvariable=PAYEMENT_METHOD)
entry4_ad_LEDGER.grid(row= 3, column=2 , padx=0 )

entry5_ad_LEDGER= Entry(table_area_ad_LEDGER , width=20, fg='white', bg= 'black',font=('Arial',12,'bold') )
entry5_ad_LEDGER.grid(row= 5, column=1  , padx=0 )
entry5_ad_LEDGER.insert(END ,  "DESCRIPTION") 

entry6_ad_LEDGER= Entry(table_area_ad_LEDGER , width=40, fg='black' , bg= 'white',font=('Arial',12,'bold') ,  textvariable= DESCRIPTION )
entry6_ad_LEDGER.grid(row= 5, column=2 , padx=0 )

entry7_ad_LEDGER= Entry(table_area_ad_LEDGER , width=20, fg='white', bg= 'black' ,font=('Arial',12,'bold') )
entry7_ad_LEDGER.grid(row= 4, column=1  , padx=0 )
entry7_ad_LEDGER.insert(END ,  "Contact NO.") 

entry8_ad_LEDGER= Entry(table_area_ad_LEDGER , width=40, fg='black' , bg= 'white',font=('Arial',12,'bold')  ,  textvariable= Contact_NO)
entry8_ad_LEDGER.grid(row= 4, column=2 , padx=0 )

entry9_ad_LEDGER= Entry(table_area_ad_LEDGER , width=20, fg='white', bg= 'blue',font=('Arial',12,'bold') )
entry9_ad_LEDGER.grid(row= 6, column=1  , padx=0 )
entry9_ad_LEDGER.insert(END ,  "DATE.") 

entry10_ad_LEDGER= Entry(table_area_ad_LEDGER , width=40, fg='black' , bg= 'white',font=('Arial',12,'bold') ,  textvariable= DATE  )
entry10_ad_LEDGER.grid(row= 6, column=2 , padx=0 )

entry11_ad_LEDGER= Entry(table_area_ad_LEDGER , width=21, fg='white' , bg= 'green',font=('Arial',12,'bold')   )
entry11_ad_LEDGER.grid(row= 2, column=3  , padx= 0 )
entry11_ad_LEDGER.insert(END ,  "DEBIT")

entry12_ad_LEDGER= Entry(table_area_ad_LEDGER , width=21, fg='black' , bg= 'white',font=('Arial',12,'bold')  ,  textvariable= DEBIT )
entry12_ad_LEDGER.grid(row= 3, column=3 , padx=0 )

entry13_ad_LEDGER= Entry(table_area_ad_LEDGER , width=21, fg='white', bg= 'red',font=('Arial',12,'bold')   )
entry13_ad_LEDGER.grid(row= 2, column=4  , padx=0 )
entry13_ad_LEDGER.insert(END ,  "CREDIT")

entry14_ad_LEDGER= Entry(table_area_ad_LEDGER , width=21, fg='black' , bg= 'white',font=('Arial',12,'bold') ,  textvariable= CREDIT )
entry14_ad_LEDGER.grid(row= 3 , column=4 , padx=0 )


entry15_ad_LEDGER= Entry(table_area_ad_LEDGER , width=21, fg='white' , bg= 'blue',font=('Arial',12,'bold') )
entry15_ad_LEDGER.grid(row= 2, column= 5  , padx=0 )
entry15_ad_LEDGER.insert(END ,  "BALANCE")

entry16_ad_LEDGER= Entry(table_area_ad_LEDGER , width=21, fg='black' , bg= 'white',font=('Arial',12,'bold')  ,  textvariable= BALANCE)
entry16_ad_LEDGER.grid(row= 3, column=5 , padx=0 )

entry17_ad_LEDGER= Entry(table_area_ad_LEDGER , width=21, fg='white' , bg= 'blue',font=('Arial',12,'bold') )
entry17_ad_LEDGER.grid(row= 4, column= 3  , padx=0 )
entry17_ad_LEDGER.insert(END ,  "EMAIL")

entry18_ad_LEDGER= Entry(table_area_ad_LEDGER , width=21, fg='black' , bg= 'white',font=('Arial',12,'bold')  ,  textvariable= EMAIL )
entry18_ad_LEDGER.grid(row= 5, column=3 , padx=0 )


button_ad_LEDGER= Button(table_area_ad_LEDGER,bd=0.5,text='ADD LEDGER' , bg='green', fg='white'  , font=buttonFont,  width=22  , command = CREATE_LEDGER)
button_ad_LEDGER.grid( row= 8 , column=1 , pady = 40 )

button2_ad_LEDGER= Button(table_area_ad_LEDGER,bd=0.5,text='PRINT' , bg='blue', fg='white'  , font=buttonFont,  width=22 )
button2_ad_LEDGER.grid( row= 9 , column=1 , pady = 5 )

plchldr_ad_LEDGER = Label(table_area_ad_LEDGER , text = "", relief=RAISED, bg= 'black' , bd=0  , font=label_Entry_font )
plchldr_ad_LEDGER.grid(row = 20 , column = 10 , pady=90 , padx=14)

plchldr2_ad_LEDGER = Label(table_area_ad_LEDGER , text = "", relief=RAISED , bg= 'black' , bd=0  , font=label_Entry_font )
plchldr2_ad_LEDGER.grid(row = 21 , column = 10  , pady=0  , padx=90)

ad_LEDGER.pack_forget()

#NOT NEEDED ADD TO DIARY 
'''
ad_DIARY = add_DIARY = Frame(root,width=1300, height= 580, bg="#00bfff" ,highlightthickness=0.5 , highlightbackground="#00bfff")
add_DIARY.pack(side='top' , anchor="n" , pady=40 , padx=30)
add_DIARY.pack_propagate(0)

entry_area =Frame(add_DIARY,width=1000, height= 580, bg="brown" ,highlightthickness=0.5 , highlightbackground="#00bfff")
entry_area.pack(side='left' , anchor="n" , padx=20)
label_1_ad_DIARY = Label(entry_area, text = "PART NO", relief=RAISED , bg= '#89CFF0' , bd=0  , font=label_Entry_font )
label_1_ad_DIARY.grid(row = 1 , column = 1 , pady=14 , padx=14)
entry_1_ad_DIARY = Entry(entry_area , width=12, fg='black',font=('Arial',16,'bold') )
entry_1_ad_DIARY.grid(row= 2, column=1  , padx=14 )
label_2_ad_DIARY = Label(entry_area, text = "NAME", relief=RAISED , bg= '#89CFF0' , bd=0  , font=label_Entry_font )
label_2_ad_DIARY.grid(row = 1 , column = 2 , pady=14 , padx=14)
entry_2_ad_DIARY  = Entry(entry_area , width=12, fg='black',font=('Arial',16,'bold') )
entry_2_ad_DIARY.grid(row= 2, column=2 , padx=14  )
label_3_ad_DIARY = Label(entry_area, text = "MODEL", relief=RAISED , bg= '#89CFF0' , bd=0  , font=label_Entry_font )
label_3_ad_DIARY.grid(row = 1 , column = 3 , pady=14 , padx=14 )
entry_3_ad_DIARY = Entry(entry_area , width=12, fg='black',font=('Arial',16,'bold') )
entry_3_ad_DIARY .grid(row= 2, column=3 , padx=14)
label_4_ad_DIARY = Label(entry_area, text = "ENGINE", relief=RAISED , bg= '#89CFF0' , bd=0  , font=label_Entry_font )
label_4_ad_DIARY.grid(row = 1 , column = 4 , pady=14  , padx=14 )
entry_4_ad_DIARY  = Entry(entry_area , width=12, fg='black',font=('Arial',16,'bold') )
entry_4_ad_DIARY.grid(row= 2, column=4 , padx=14 )
label_5_ad_DIARY= Label(entry_area, text = "BRAND", relief=RAISED , bg= '#89CFF0' , bd=0  , font=label_Entry_font )
label_5_ad_DIARY.grid(row = 1, column = 5 , pady=14 , padx=14)
entry_5_ad_DIARY  = Entry(entry_area , width=12, fg='black',font=('Arial',16,'bold') )
entry_5_ad_DIARY.grid(row= 2, column=5 , padx=14 , pady=14)
label_6_ad_DIARY = Label(entry_area, text = "Price", relief=RAISED , bg= '#89CFF0' , bd=0  , font=label_Entry_font )
label_6_ad_DIARY.grid(row = 1, column = 6 , pady=14 , padx=14)
entry_6_ad_DIARY = Entry(entry_area , width=12, fg='black',font=('Arial',16,'bold') )
entry_6_ad_DIARY.grid(row= 2, column= 6  , padx=14  , pady=14  )
button_ad_DIARY= Button(entry_area ,bd=0.5,text='LEGDER' , bg='#00bfff', fg='white'  , font=buttonFont,  width=12 )
button_ad_DIARY.grid( row= 7 , column=2 )
'''



#transfer_transction 

transfer_transction  = Frame(root,width=1300, height= 880, bg="white" )
transfer_transction .pack(side='top' , anchor="n" , pady=0 , padx=0)
transfer_transction .pack_propagate(0)

button_area_tt = Frame(transfer_transction,width=800, height= 380, bg="black" )
button_area_tt.pack(side='top' , anchor="n" , padx=0 , pady = 40)


label_btnar_tt = Label(button_area_tt, text = "SEACH BY NAME ", relief=RAISED , bg= 'black' , fg = 'white', bd=0 ,font=('Arial',11,'bold')  )
label_btnar_tt.grid(row = 1 , column = 1  , padx = 20 , pady = 20 )

entry_btnar_tt  = Entry(button_area_tt, width=26, fg='black',font=('Arial',9,'bold') )
entry_btnar_tt.grid(row = 1 , column=2  , padx = 20  , pady = 20 )

buton1_tt = Button(button_area_tt,bd= 0.5,text='SEARCH' , bg='green', fg='white'  , font=buttonFont,  width=12 )
buton1_tt.grid(row = 1 , column  = 3 , padx = 20  , pady = 20 )

label2_btnar_tt = Label(button_area_tt, text = "SEARCH BY NO ", relief=RAISED , bg= 'black' , fg = 'white' , bd=0  ,font=('Arial',11,'bold') )
label2_btnar_tt.grid(row = 2 , column = 1   , padx = 20  , pady = 20 )

entry2_btna_tt  = Entry(button_area_tt, width=26, fg='black',font=('Arial',9,'bold') )
entry2_btna_tt.grid(row = 2 , column=2   , padx = 20  , pady = 20 )

buton2_tt = Button(button_area_tt ,bd=0.5,text='LEGDER' , bg='blue', fg='white'  , font=buttonFont,  width=12 )
buton2_tt.grid(row = 2 , column  = 3  , padx = 20  , pady = 20 )


buton3_tt= Button(button_area_tt ,bd= 0.5,text='print' , bg='blue', fg='white'  , font=buttonFont,  width=12 )
buton3_tt.grid(row = 2 , column  = 5 , padx = 20  , pady = 20 )

plcehldr_btnar_tt=  Label(button_area_tt, text = "SEA", relief=RAISED , bg= 'black' , fg = 'white', bd=0 ,font=('Arial',11,'bold')  )
plcehldr_btnar_tt.grid(row = 1  , column = 0  , padx = 100 , pady = 0 )

plcehldr2_btnar_tt =  Label(button_area_tt, text = "SE ", relief=RAISED , bg= 'black' ,  fg = 'white', bd=0 ,font=('Arial',11,'bold')  )
plcehldr2_btnar_tt.grid(row = 1  , column = 7  , padx = 100 , pady = 0 )



entry_area =Frame(transfer_transction ,width=1300, height= 780, bg="black" )
entry_area.pack(side='top' , anchor="n" , padx=0  , pady = 5)

plchldr_tt  = Label(entry_area, text = " ", relief=RAISED , bg= 'black' , fg = "white" , bd=0  ,font=('Arial',18,'bold')  )
plchldr_tt.grid(row = 0 , column = 1 , pady=30 , padx=0)


label_2_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
label_2_tt.grid(row = 1 , column = 2 , pady=0 , padx=0)
label_2_tt.insert(END, "Account Of")

entry_2_tt = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_2_tt.grid(row = 2, column=2  , padx = 0 )

entry_22_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_22_tt.grid(row = 3, column=2  , padx = 0 )

entry_23_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_23_tt.grid(row = 4, column=2  , padx = 0 )

entry_24_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_24_tt.grid(row = 5, column=2  , padx = 0 )

entry_25_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_25_tt.grid(row = 6, column=2  , padx = 0 )

entry_26_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_26_tt.grid(row = 7, column=2  , padx = 0 )

entry_27_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_27_tt.grid(row = 8, column=2  , padx = 0 )

entry_28_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_28_tt.grid(row = 9, column=2  , padx = 0 )


label_3_tt = Entry(entry_area , width=18, fg='white' , bg = "blue",font=('Arial',9,'bold') )
label_3_tt.grid(row = 1, column = 3 , pady=0 , padx=0)
label_3_tt.insert(END, "DATE")

entry_3_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_3_tt.grid(row = 2, column=3  , padx = 0 )

entry_31_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_31_tt.grid(row = 3, column=3  , padx = 0 )

entry_32_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_32_tt.grid(row = 4, column=3  , padx = 0 )

entry_33_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_33_tt.grid(row = 5, column=3  , padx = 0 )

entry_34_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_34_tt.grid(row = 6, column=3  , padx = 0 )

entry_35_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_35_tt.grid(row = 7, column=3  , padx = 0 )

entry_36_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_36_tt.grid(row = 8, column=3  , padx = 0 )

entry_37_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_37_tt.grid(row = 9, column=3  , padx = 0 )



label_5_tt = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
label_5_tt.grid(row = 1 , column = 5 , pady=0 , padx=0)
label_5_tt.insert(END, "PAYEMENT METHOD")

entry_5_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_5_tt.grid(row = 2, column= 5  , padx = 0 )

entry_52_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_52_tt.grid(row = 3, column= 5  , padx = 0 )

entry_53_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_53_tt.grid(row = 4, column= 5  , padx = 0 )

entry_54_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_54_tt.grid(row = 5, column= 5  , padx = 0 )

entry_55_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_55_tt.grid(row = 6, column= 5  , padx = 0 )

entry_56_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_56_tt.grid(row = 7, column= 5  , padx = 0 )

entry_57_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_57_tt.grid(row = 8, column= 5  , padx = 0 )

entry_58_tt  = Entry(entry_area , width=21, fg='black',font=('Arial',9,'bold') )
entry_58_tt.grid(row = 9, column= 5  , padx = 0 )





label_6_tt= Entry(entry_area , width=32, fg='black',font=('Arial',9,'bold') )
label_6_tt.grid(row = 1 , column = 6 , pady=0 , padx=0)
label_6_tt.insert(END, "DESCRIPTION")

entry_6_tt = Entry(entry_area , width=32, fg='black',font=('Arial',9,'bold') )
entry_6_tt.grid(row = 2, column=6  , padx = 0 )

entry_62_tt = Entry(entry_area , width=32, fg='black',font=('Arial',9,'bold') )
entry_62_tt.grid(row = 3, column=6  , padx = 0 )

entry_63_tt = Entry(entry_area , width=32, fg='black',font=('Arial',9,'bold') )
entry_63_tt.grid(row = 4, column=6  , padx = 0 )

entry_64_tt = Entry(entry_area , width=32, fg='black',font=('Arial',9,'bold') )
entry_64_tt.grid(row = 5, column=6  , padx = 0 )

entry_65_tt = Entry(entry_area , width=32, fg='black',font=('Arial',9,'bold') )
entry_65_tt.grid(row = 6, column=6  , padx = 0 )

entry_66_tt = Entry(entry_area , width=32, fg='black',font=('Arial',9,'bold') )
entry_66_tt.grid(row = 7, column=6  , padx = 0 )

entry_67_tt = Entry(entry_area , width=32, fg='black',font=('Arial',9,'bold') )
entry_67_tt.grid(row = 8, column=6  , padx = 0 )

entry_68_tt = Entry(entry_area , width=32, fg='black',font=('Arial',9,'bold') )
entry_68_tt.grid(row = 9, column=6  , padx = 0 )





label_7_tt = Entry(entry_area , width=18, fg='white'  , bg = "green",font=('Arial',9,'bold') )
label_7_tt.grid(row = 1 , column = 7 , pady=0 , padx=0)
label_7_tt.insert(END, "DEBIT")

entry_7_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_7_tt.grid(row = 2, column=7  , padx = 0 )

entry_72_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_72_tt.grid(row = 3, column=7  , padx = 0 )

entry_73_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_73_tt.grid(row = 4, column=7  , padx = 0 )

entry_74_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_74_tt.grid(row = 5, column=7  , padx = 0 )

entry_75_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_75_tt.grid(row = 6, column=7  , padx = 0 )

entry_76_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_76_tt.grid(row = 7, column=7  , padx = 0 )

entry_77_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_77_tt.grid(row = 8, column=7  , padx = 0 )

entry_78_tt = Entry(entry_area , width=18, fg='black',font=('Arial',9,'bold') )
entry_78_tt.grid(row = 9, column=7  , padx = 0 )




label_8_tt = Entry(entry_area , width=18, fg='white' , bg = "red",font=('Arial',9,'bold') )
label_8_tt .grid(row = 1 , column = 8 , pady=0 , padx=0)
label_8_tt.insert(END, "CREDIT")

entry_8_tt  = Entry(entry_area , width= 18 , fg='black',font=('Arial',9,'bold') )
entry_8_tt.grid(row = 2, column=8  , padx = 0 )

entry_82_tt  = Entry(entry_area , width= 18 , fg='black',font=('Arial',9,'bold') )
entry_82_tt.grid(row = 3, column=8  , padx = 0 )

entry_83_tt  = Entry(entry_area , width= 18 , fg='black',font=('Arial',9,'bold') )
entry_83_tt.grid(row = 4, column=8  , padx = 0 )

entry_84_tt  = Entry(entry_area , width= 18 , fg='black',font=('Arial',9,'bold') )
entry_84_tt.grid(row = 5, column=8  , padx = 0 )

entry_85_tt  = Entry(entry_area , width= 18 , fg='black',font=('Arial',9,'bold') )
entry_85_tt.grid(row = 6, column=8  , padx = 0 )

entry_86_tt  = Entry(entry_area , width= 18 , fg='black',font=('Arial',9,'bold') )
entry_86_tt.grid(row = 7, column=8  , padx = 0 )

entry_87_tt  = Entry(entry_area , width= 18 , fg='black',font=('Arial',9,'bold') )
entry_87_tt.grid(row = 8, column=8  , padx = 0 )

entry_88_tt  = Entry(entry_area , width= 18 , fg='black',font=('Arial',9,'bold') )
entry_88_tt.grid(row = 9, column=8  , padx = 0 )





label_9_tt = Entry(entry_area , width=18  , fg='white'  , bg = "blue",font=('Arial',9,'bold') )
label_9_tt.grid(row = 1 , column = 9 , pady=0 , padx=0)
label_9_tt.insert(END, "Balance")

entry_9_tt = Entry(entry_area , width=18 , fg='black',font=('Arial',9,'bold') )
entry_9_tt.grid(row = 2, column=9  , padx = 0 )

entry_92_tt = Entry(entry_area , width=18 , fg='black',font=('Arial',9,'bold') )
entry_92_tt.grid(row = 3, column=9  , padx = 0 )

entry_93_tt = Entry(entry_area , width=18 , fg='black',font=('Arial',9,'bold') )
entry_93_tt.grid(row = 4, column=9  , padx = 0 )

entry_94_tt = Entry(entry_area , width=18 , fg='black',font=('Arial',9,'bold') )
entry_94_tt.grid(row = 5, column=9  , padx = 0 )

entry_95_tt = Entry(entry_area , width=18 , fg='black',font=('Arial',9,'bold') )
entry_95_tt.grid(row = 6, column=9  , padx = 0 )

entry_96_tt = Entry(entry_area , width=18 , fg='black',font=('Arial',9,'bold') )
entry_96_tt.grid(row = 7, column=9  , padx = 0 )

entry_97_tt = Entry(entry_area , width=18 , fg='black',font=('Arial',9,'bold') )
entry_97_tt.grid(row = 8, column=9  , padx = 0 )

entry_98_tt = Entry(entry_area , width=18 , fg='black',font=('Arial',9,'bold') )
entry_98_tt.grid(row = 9, column=9  , padx = 0 )

buton_tt = Button(entry_area ,bd=0.5,text='SAVE CHANGES' , bg='red', fg='white'  , font=buttonFont,  width=16 )
buton_tt.grid(row = 13, column= 2  , pady = 20  )

buton_tt = Button(entry_area ,bd=0.5,text='PRINT' , bg='blue', fg='white'  , font=buttonFont,  width=16 )
buton_tt.grid(row = 13, column= 3  , pady = 20  )

transfer_transction.pack_forget()




#CUSTOMER_DETAILS

chk_CUSTOMER = check_CUSTOMER = Frame(root,width=1420, height= 680, bg="white" )
check_CUSTOMER.pack(side='top' , anchor="n" , padx=0)
check_CUSTOMER.pack_propagate(0)

CUSTOMER_label_Area = Frame(check_CUSTOMER,width=600, height= 70, bg="white" )
CUSTOMER_label_Area.pack(side='top' , anchor="ne" , padx=0 , pady= 10)
 
label = Label(CUSTOMER_label_Area , text = "CUSTOMER HISTORY", relief=RAISED , bg= 'white'  ,fg =  "black" , bd=0, font=("Arial", 14 , "bold")  )
label.pack(side='left' , anchor="w" , pady=5, padx=255 )

CUSTOMER_table_Area = Frame(check_CUSTOMER,width=1000, height= 590, bg="black" )
CUSTOMER_table_Area.pack(side='right' , anchor="n" , padx=10 , pady= 10   , fill="y", expand=True)



CUSTOMER_button_area = Frame(check_CUSTOMER,width=350, height= 580, bg="black" )
CUSTOMER_button_area.pack(side='left' , anchor="n" , padx=20 , pady= 0)



label = Label(CUSTOMER_button_area, text = "SEARCH BY ID ", relief=RAISED , bg= 'black' , fg = "white" , bd=0, font=("Arial", 10 , "bold")  )
label.pack(side='top' , anchor="n" , pady=5, padx=5 )
entry = Entry(CUSTOMER_button_area, width=22 ,  fg='black'  ,highlightthickness=0.5 , highlightbackground="black" ,font=('Arial',13,'bold') )
entry.pack(pady= 0,anchor="n")
buton = Button(CUSTOMER_button_area  ,bd=0.5,text='SEARCH' , bg='blue', fg='white'  , font=buttonFont,  width=12 )
buton.pack( pady= 15,anchor="n")

label = Label(CUSTOMER_button_area, text = "SEARCH BY NAME", relief=RAISED , bg= 'black' , fg = "white"  , bd=0, font=("Arial", 10 , "bold")  )
label.pack(side='top' , anchor="n" , pady=10, padx=5 )
entry = Entry(CUSTOMER_button_area, width=11, fg='black',highlightthickness=0.5 , highlightbackground="black" ,font=('Arial',16,'bold') )
entry.pack(pady= 0,anchor="n")
buton = Button(CUSTOMER_button_area  ,bd=0.5,text='SEARCH' , bg='green', fg='white'  , font=buttonFont,  width=12 )
buton.pack( pady= 10,anchor="n")

plchlder_cba = Label(CUSTOMER_button_area, text = " ", relief=RAISED , bg= 'black' , fg = "white" , bd=0, font=("Arial", 10 , "bold")  )
plchlder_cba.pack(side='top' , anchor="n" , pady=125, padx=5 )



CUSTOMER_items = [("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22"),
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ),
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ),
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22"),
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22"),
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22"), 
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ), 
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ), 
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ), 
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ), 
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ), 
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ), 
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ), 
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22"),
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ), 
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ), 
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ), 
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ), 
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ), 
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ),
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ),
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ),
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ),
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ),
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ),
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" ),
               ("ARSHAD" , "03000-938272" , "SPARE" , "5"  ,"30_12_22" )]
                                                                 
CUSTOMER_head = ["NAME" , "PHONE" , "PRODUCT BOUGH" , " UNIT" , "DATE" ]

for i in range(5):
    b = Entry(CUSTOMER_table_Area, width=18, fg='black',font=('Arial',12,'bold') )
    b.grid(row=0, column=i , pady=10)
    b.insert(END ,  CUSTOMER_head[i])    

for i in range(22):
    for j in range(5):
        c = Entry(CUSTOMER_table_Area, width=18,  fg='black',font=('Arial',12,'bold') )
        c.grid( row=i+1, column=j , pady=2)
        c.insert(END, CUSTOMER_items[i][j])


plcehldr_cta = Label(CUSTOMER_table_Area, text = " ", relief=RAISED , bg= 'black' , fg = "white" , bd=0, font=("Arial", 10 , "bold")  )
plcehldr_cta.grid( row= 16 , column= 1 , pady=8)

chk_CUSTOMER.pack_forget()

#check shop 

chk_shop= check_shop = Frame(root,width=1120, height= 580, bg="white" )
check_shop.pack(side='top' , anchor="n" , padx=0)
check_shop.pack_propagate(0)

shop_table_Area = Frame(check_shop,width=1000, height= 580, bg="black" )
shop_table_Area.pack(side='left' , anchor="n" , padx=5 , pady = 24 )

shop_button_area = Frame(check_shop,width=200, height= 580, bg="black")
shop_button_area.pack(side='right' , anchor="n" , padx=20 , pady = 24)

label1_chkshop = Label(shop_button_area, text = "SEARCH BY NAME", relief=RAISED , bg= 'black'  , fg = "white", bd=0 ,font=('Arial',10,'bold')   )
label1_chkshop.pack(side='top' , anchor="n" , pady=10 )
entry = Entry(shop_button_area, width=16, fg='black',font=('Arial',14,'bold') ,highlightthickness=0.5 , highlightbackground="black")
entry.pack(anchor="n" , pady= 10)
buton = Button(shop_button_area  ,bd=0.5,text='SEARCH' , bg='green', fg='white'  , font=buttonFont,  width=12 )
buton.pack( anchor="n" , pady=14)

label = Label(shop_button_area, text = "search by id", relief=RAISED , bg= 'black'  , fg = "white" , bd=0  ,font=('Arial',13,'bold') )
label.pack(side='top' , anchor="n" , pady=12 )
entry = Entry(shop_button_area, width=16, fg='black',font=('Arial',14,'bold') ,highlightthickness=0.5 , highlightbackground="black")
entry.pack(pady= 10,anchor="n")
buton = Button(shop_button_area  ,bd=0.5,text='SEARCH' , bg='green', fg='white'  , font=buttonFont,  width=12 )
buton.pack( anchor="n" , pady=10)

plchldr_chkshop = Label(shop_button_area, text = " id", relief=RAISED , bg= 'black'  , fg = "white" , bd=0  ,font=('Arial',13,'bold') )
plchldr_chkshop .pack(side='top' , anchor="n" , pady=120 )




shop_items = [("sto443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200077"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"),]
                                                                 
shop_head = ["part no" , "NAme" , "Engine" , "Brand" , "Made" , "price"]

for i in range(6):
    b = Entry(shop_table_Area, width=8, fg='black',font=('Arial',16,'bold') )
    b.grid(row=0, column=i , pady=10)
    b.insert(END ,  shop_head[i])    

for i in range(15):
    for j in range(6):
        c = Entry(shop_table_Area, width=8,  fg='black',font=('Arial',16,'bold') )
        c.grid( row=i+1, column=j , pady=2)
        c.insert(END,  shop_items[i][j])


chk_shop.pack_forget()





#check stock 

chk_stock= check_stock = Frame(root,width=1120, height= 580, bg="white" )
check_stock.pack(side='top' , anchor="n" , padx=0)
check_stock.pack_propagate(0)

stock_table_Area = Frame(check_stock,width=1000, height= 580, bg="black" )
stock_table_Area.pack(side='left' , anchor="n" , padx=5 , pady = 24 )

stock_button_area = Frame(check_stock,width=200, height= 580, bg="black")
stock_button_area.pack(side='right' , anchor="n" , padx=20 , pady = 24)

label = Label(stock_button_area, text = "SEARCH BY NAME", relief=RAISED , bg= 'black' , fg = 'white' , bd=0 ,font=('Arial',12,'bold')   )
label.pack(side='top' , anchor="n" , pady=10 )
entry = Entry(stock_button_area, width=16, fg='black',font=('Arial',14,'bold') ,highlightthickness=0.5 , highlightbackground="black")
entry.pack(anchor="n" , pady= 10)
buton = Button(stock_button_area  ,bd=0.5,text='SEARCH' , bg='green', fg='white'  , font=buttonFont,  width=12 )
buton.pack( anchor="n" , pady=14)

label = Label(stock_button_area, text = "search by id", relief=RAISED , bg= 'black' , fg = 'white' , bd=0  ,font=('Arial',12,'bold') )
label.pack(side='top' , anchor="n" , pady=12 )
entry = Entry(stock_button_area, width=16, fg='black',font=('Arial',14,'bold') ,highlightthickness=0.5 , highlightbackground="black")
entry.pack(pady= 10,anchor="n")
buton = Button(stock_button_area  ,bd=0.5,text='SEARCH' , bg='green', fg='white'  , font=buttonFont,  width=12 )
buton.pack( anchor="n" , pady=10)

plchldr_chk_stock= Label(stock_button_area, text = " id", relief=RAISED , bg= 'black'  , fg = "white" , bd=0  ,font=('Arial',13,'bold') )
plchldr_chk_stock.pack(side='top' , anchor="n" , pady=120 )

stock_items = [("sto443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200077"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083"),]
                                                                 
stock_head = ["part no" , "NAme" , "Engine" , "Brand" , "Made" , "price"]

for i in range(6):
    b = Entry(stock_table_Area, width=8, fg='black',font=('Arial',16,'bold') )
    b.grid(row=0, column=i , pady=10)
    b.insert(END ,  stock_head[i])    

for i in range(15):
    for j in range(6):
        c = Entry(stock_table_Area, width=8,  fg='black',font=('Arial',16,'bold') )
        c.grid( row=i+1, column=j , pady=2)
        c.insert(END,  stock_items[i][j])


chk_stock.pack_forget()


#CHECK Ledger 

chk_Ledger = check_Ledger = Frame(root,width=1400, height= 880, bg="white" ,highlightthickness=0.5 , highlightbackground="#00bfff")
check_Ledger.pack(side='top' , anchor="n" , padx=0)
check_Ledger.pack_propagate(0)


chkLedger_button_area = Frame(check_Ledger,width=800, height= 380, bg="black" )
chkLedger_button_area.pack(side='top' , anchor="n" , padx=0 , pady = 40)


label_btnar_chklgr = Label(chkLedger_button_area , text = "SEACH BY NAME ", relief=RAISED , bg= 'black' , fg = 'white', bd=0 ,font=('Arial',11,'bold')  )
label_btnar_chklgr.grid(row = 1 , column = 1  , padx = 20 , pady = 20 )

entry_btnar_chklgr  = Entry(chkLedger_button_area, width=26, fg='black',font=('Arial',9,'bold') )
entry_btnar_chklgr.grid(row = 1 , column=2  , padx = 20  , pady = 20 )

buton1_chklgr = Button(chkLedger_button_area ,bd= 0.5,text='SEARCH' , bg='green', fg='white'  , font=buttonFont,  width=12 )
buton1_chklgr.grid(row = 1 , column  = 3 , padx = 20  , pady = 20 )

label2_btnar_chklgr = Label(chkLedger_button_area , text = "SEARCH BY NO ", relief=RAISED , bg= 'black' , fg = 'white' , bd=0  ,font=('Arial',11,'bold') )
label2_btnar_chklgr.grid(row = 2 , column = 1   , padx = 20  , pady = 20 )

entry2_btnar_chklgr  = Entry(chkLedger_button_area, width=26, fg='black',font=('Arial',9,'bold') )
entry2_btnar_chklgr.grid(row = 2 , column=2   , padx = 20  , pady = 20 )

buton2_chklgr = Button(chkLedger_button_area ,bd=0.5,text='LEGDER' , bg='blue', fg='white'  , font=buttonFont,  width=12 )
buton2_chklgr.grid(row = 2 , column  = 3  , padx = 20  , pady = 20 )


buton3_chklgr = Button(chkLedger_button_area ,bd= 0.5,text='print' , bg='blue', fg='white'  , font=buttonFont,  width=12 )
buton3_chklgr.grid(row = 2 , column  = 5 , padx = 20  , pady = 20 )

plcehldr_btnar_chklgr =  Label(chkLedger_button_area , text = "SEA", relief=RAISED , bg= 'black' , fg = 'white', bd=0 ,font=('Arial',11,'bold')  )
plcehldr_btnar_chklgr.grid(row = 1  , column = 0  , padx = 100 , pady = 0 )

plcehldr2_btnar_chklgr =  Label(chkLedger_button_area , text = "SE ", relief=RAISED , bg= 'black' ,  fg = 'white', bd=0 ,font=('Arial',11,'bold')  )
plcehldr2_btnar_chklgr.grid(row = 1  , column = 7  , padx = 100 , pady = 0 )

Ledger_table_Area_chklgr= Frame(check_Ledger,width=1200, height= 380, bg="black")
Ledger_table_Area_chklgr.pack(side='top' , anchor="n" , padx=0 , pady = 30)

plcedr1_btnar_chklgr =  Label(Ledger_table_Area_chklgr, text = " ", relief=RAISED , bg= 'black' , fg = 'white', bd=0 ,font=('Arial',11,'bold')  )
plcedr1_btnar_chklgr.grid(row = 0  , column = 0  , padx = 0 , pady = 20 )

plcedr2_btnar_chklgr =  Label(Ledger_table_Area_chklgr , text = " ", relief=RAISED , bg= 'black' , fg = 'white', bd=0 ,font=('Arial',11,'bold')  )
plcedr2_btnar_chklgr.grid(row = 10  , column = 0  , padx = 0 , pady = 20 )



'''
buton2 = Button(Ledger_button_area ,bd=0.5,text='LEGDER' , bg='#00bfff', fg='white'  , font=buttonFont,  width=12 )
buton2.pack( pady= 0,anchor="n")
entry1 = Entry(Ledger_button_area, width=12, fg='black',font=('Arial',16,'bold') )
entry1.pack(pady= 0,anchor="n")
'''
'''
Ledger_items = [("12313" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200077" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),]
                                                                 
Ledger_head = ["S/n" , "LEDGER NO" , "NAME" , "ADRESS" , "COUNTRY" , "PHONE" , "Class"]

for i in range(7):
    b = Entry(Ledger_table_Area, width=12, fg='black',font=('Arial',16,'bold') )
    b.grid(row=0, column=i , pady=10)
    b.insert(END ,  Ledger_head[i])    

for i in range(17):
    for j in range(7):
        c = Entry(Ledger_table_Area, width=12,  fg='black',font=('Arial',16,'bold') )
        c.grid( row=i+1, column=j , pady=2)
        c.insert(END,  Ledger_items[i][j])
'''

label_2_chkl  = Entry(Ledger_table_Area_chklgr , width=21, fg='black',font=('Arial',9,'bold') )
label_2_chkl.grid(row = 1 , column = 2 , pady=5 , padx= 0 )
label_2_chkl.insert(END, "Account Of")

entry_2_chkl = Entry(Ledger_table_Area_chklgr  , width=21, fg='black',font=('Arial',9,'bold') )
entry_2_chkl.grid(row = 2, column=2  , padx = 0 ,  pady=1 )
entry_2_chkl.insert(END, "BAshir Ahmad")

entry_22_chkl  = Entry(Ledger_table_Area_chklgr, width=21, fg='black',font=('Arial',9,'bold') )
entry_22_chkl.grid(row = 3, column=2  , padx = 0  ,  pady=1)
entry_22_chkl.insert(END, ".")

entry_23_chkl  = Entry(Ledger_table_Area_chklgr, width=21, fg='black',font=('Arial',9,'bold') )
entry_23_chkl.grid(row = 4, column=2  , padx = 0  ,  pady=1)
entry_23_chkl.insert(END, "BAshir Ahhmad")

entry_24_chkl  = Entry(Ledger_table_Area_chklgr, width=21, fg='black',font=('Arial',9,'bold') )
entry_24_chkl.grid(row = 5, column=2  , padx = 0 ,  pady=1 )
entry_24_chkl.insert(END, " .")

entry_25_chkl  = Entry(Ledger_table_Area_chklgr, width=21, fg='black',font=('Arial',9,'bold') )
entry_25_chkl.grid(row = 6, column=2  , padx = 0 ,  pady=1)
entry_25_chkl.insert(END, " .")

entry_26_chkl  = Entry(Ledger_table_Area_chklgr, width=21, fg='black',font=('Arial',9,'bold') )
entry_26_chkl.grid(row = 7, column=2  , padx = 0 ,  pady=1)
entry_26_chkl.insert(END, "BAshir Ahhmad")

entry_27_chkl  = Entry(Ledger_table_Area_chklgr, width=21, fg='black',font=('Arial',9,'bold') )
entry_27_chkl.grid(row = 8, column=2  , padx = 0 ,  pady=1)
entry_27_chkl.insert(END, ". ")

entry_28_chkl  = Entry(Ledger_table_Area_chklgr, width=21, fg='black',font=('Arial',9,'bold') )
entry_28_chkl.grid(row = 9, column=2  , padx = 0 ,  pady=1)
entry_28_chkl.insert(END, " .")



label_3_chkl = Entry(Ledger_table_Area_chklgr , width=18, fg='white' , bg = "blue",font=('Arial',9,'bold') )
label_3_chkl.grid(row = 1, column = 3 , padx=0 ,  pady=1)
label_3_chkl.insert(END, "DATE")

entry_3_chkl = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_3_chkl.grid(row = 2, column=3  , padx = 0 ,  pady=1)
entry_3_chkl.insert(END, "18 - 02 - 07")

entry_31_chkl = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_31_chkl.grid(row = 3, column=3  , padx = 0 ,  pady=1)
entry_31_chkl.insert(END, " ")

entry_32_chkl = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_32_chkl.grid(row = 4, column=3  , padx = 0 ,  pady=1)
entry_32_chkl.insert(END, "  ")


entry_33_chkl = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_33_chkl.grid(row = 5, column=3  , padx = 0 ,  pady=1)
entry_33_chkl .insert(END, "20 - 02 - 07")


entry_34_chkl = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_34_chkl.grid(row = 6, column=3  , padx = 0 ,  pady=1)
entry_34_chkl.insert(END, " ")

entry_35_chkl = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_35_chkl.grid(row = 7, column=3  , padx = 0 ,  pady=1)
entry_35_chkl.insert(END, " ")

entry_36_chkl = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_36_chkl.grid(row = 8, column=3  , padx = 0 ,  pady=1)
entry_36_chkl.insert(END, "24 - 02 - 07")

entry_37_chkl = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_37_chkl.grid(row = 9, column=3  , padx = 0 ,  pady=1)
entry_37_chkl.insert(END, " ")



label_5_chkl = Entry(Ledger_table_Area_chklgr , width=21, fg='black',font=('Arial',9,'bold') )
label_5_chkl.grid(row = 1 , column = 5 ,  pady=1 , padx=0)
label_5_chkl.insert(END, "PAYEMENT METHOD")

entry_5_chkl  = Entry(Ledger_table_Area_chklgr , width=21, fg='black',font=('Arial',9,'bold') )
entry_5_chkl.grid(row = 2, column= 5  , padx = 0 ,  pady=1)
entry_5_chkl.insert(END, "BY BANK")


entry_52_chkl  = Entry(Ledger_table_Area_chklgr , width=21, fg='black',font=('Arial',9,'bold') )
entry_52_chkl.grid(row = 3, column= 5  , padx = 0  ,  pady=1)
entry_52_chkl.insert(END, "ONLINE")


entry_53_chkl  = Entry(Ledger_table_Area_chklgr , width=21, fg='black',font=('Arial',9,'bold') )
entry_53_chkl.grid(row = 4, column= 5  , padx = 0 ,  pady=1)
entry_53_chkl.insert(END, " ")


entry_54_chkl  = Entry(Ledger_table_Area_chklgr , width=21, fg='black',font=('Arial',9,'bold') )
entry_54_chkl.grid(row = 5, column= 5  , padx = 0 ,  pady=1)
entry_54_chkl.insert(END, "BY BANK")


entry_55_chkl  = Entry(Ledger_table_Area_chklgr , width=21, fg='black',font=('Arial',9,'bold') )
entry_55_chkl.grid(row = 6, column= 5  , padx = 0  ,  pady=1)
entry_55_chkl.insert(END, " ")

entry_56_chkl  = Entry(Ledger_table_Area_chklgr , width=21, fg='black',font=('Arial',9,'bold') )
entry_56_chkl.grid(row = 7, column= 5  , padx = 0 ,  pady=1)
entry_56_chkl.insert(END, "Ledger to  ledger")

entry_57_chkl  = Entry(Ledger_table_Area_chklgr , width=21, fg='black',font=('Arial',9,'bold') )
entry_57_chkl.grid(row = 8, column= 5  , padx = 0 ,  pady=1)
entry_57_chkl.insert(END, " ")


entry_58_chkl  = Entry(Ledger_table_Area_chklgr , width=21, fg='black',font=('Arial',9,'bold') )
entry_58_chkl.grid(row = 9, column= 5  , padx = 0 ,  pady=1)
entry_58_chkl.insert(END, "LEDGER TO LEDGER")



label_6_chkl= Entry(Ledger_table_Area_chklgr , width=32, fg='black',font=('Arial',9,'bold') )
label_6_chkl.grid(row = 1 , column = 6  , padx=0 ,  pady=1)
label_6_chkl.insert(END, "DESCRIPTION")

entry_61_chkl= Entry(Ledger_table_Area_chklgr , width=32, fg='black',font=('Arial',9,'bold') )
entry_61_chkl.grid(row = 2, column=6  , padx = 0 ,  pady=1)
entry_61_chkl.insert(END, " SOME RANDOM DISCRIPTION")

entry_62_chkl = Entry(Ledger_table_Area_chklgr, width=32, fg='black',font=('Arial',9,'bold') )
entry_62_chkl.grid(row = 3, column=6  , padx = 0 ,  pady=1)
entry_62_chkl.insert(END, " ")

entry_63_chkl = Entry(Ledger_table_Area_chklgr , width=32, fg='black',font=('Arial',9,'bold') )
entry_63_chkl.grid(row = 4, column=6  , padx = 0 ,  pady=1)
entry_63_chkl.insert(END, " ")

entry_64_chkl = Entry(Ledger_table_Area_chklgr , width=32, fg='black',font=('Arial',9,'bold') )
entry_64_chkl.grid(row = 5, column=6  , padx = 0 ,  pady=1)
entry_64_chkl.insert(END, "SOME RANDOM DISCRIPTION")

entry_65_chkl = Entry(Ledger_table_Area_chklgr , width=32, fg='black',font=('Arial',9,'bold') )
entry_65_chkl.grid(row = 6, column=6  , padx = 0 ,  pady=1)
entry_65_chkl.insert(END, " ")

entry_66_chkl = Entry(Ledger_table_Area_chklgr , width=32, fg='black',font=('Arial',9,'bold') )
entry_66_chkl.grid(row = 7, column=6  , padx = 0 ,  pady=1)
entry_66_chkl.insert(END, " ")

entry_67_chkl = Entry(Ledger_table_Area_chklgr , width=32, fg='black' , bg = 'blue',font=('Arial',9,'bold') )
entry_67_chkl.grid(row = 8, column=6  , padx = 0  ,  pady=1)
entry_67_chkl.insert(END, " DISCRIPTION ")

entry_68_chkl = Entry(Ledger_table_Area_chklgr , width=32, fg='black',font=('Arial',9,'bold') )
entry_68_chkl.grid(row = 9, column=6  , padx = 0 ,  pady=1)
entry_68_chkl.insert(END, "SOME RANDOM DISCRIPTION")




label_7_chkl= Entry(Ledger_table_Area_chklgr , width=18, fg='white'  , bg = "green",font=('Arial',9,'bold') )
label_7_chkl.grid(row = 1 , column = 7 ,  pady=1 , padx=0)
label_7_chkl.insert(END, "DEBIT")

entry_71_chkl = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_71_chkl.grid(row = 2, column=7  , padx = 0 ,  pady=1 )
entry_71_chkl.insert(END, " 2300")


entry_72_chkl  = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_72_chkl .grid(row = 3, column=7  , padx = 0 ,  pady=1)
entry_72_chkl.insert(END, " ")

entry_73_chkl  = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_73_chkl .grid(row = 4, column=7  , padx = 0 ,  pady=1)
entry_73_chkl.insert(END, "3000")

entry_74_chkl  = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_74_chkl .grid(row = 5, column=7  , padx = 0 ,  pady=1)
entry_74_chkl.insert(END, "9000")

entry_75_chkl  = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_75_chkl .grid(row = 6, column=7  , padx = 0 ,  pady=1)
entry_75_chkl.insert(END, " ")

entry_76_chkl  = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_76_chkl .grid(row = 7, column=7  , padx = 0 ,  pady=1)
entry_76_chkl.insert(END, " 3333")

entry_77_chkl  = Entry(Ledger_table_Area_chklgr , width=18, fg='black' , bg  = 'green',font=('Arial',9,'bold') )
entry_77_chkl .grid(row = 8, column=7  , padx = 0 ,  pady=1)
entry_77_chkl.insert(END, "TOTAL DEBIT ")

entry_78_chkl  = Entry(Ledger_table_Area_chklgr , width=18, fg='black',font=('Arial',9,'bold') )
entry_78_chkl .grid(row = 9, column=7  , padx = 0 ,  pady=1)
entry_78_chkl.insert(END, " 6666 ")





label_8_chkl = Entry(Ledger_table_Area_chklgr , width=18, fg='white' , bg = "red",font=('Arial',9,'bold') )
label_8_chkl.grid(row = 1 , column = 8 ,  pady=1 , padx=0)
label_8_chkl.insert(END, "CREDIT")

entry_81_chkl  = Entry(Ledger_table_Area_chklgr , width= 18 , fg='black',font=('Arial',9,'bold') )
entry_81_chkl.grid(row = 2, column=8  , padx = 0 ,  pady=1)
entry_81_chkl.insert(END, " ")

entry_82_chkl  = Entry(Ledger_table_Area_chklgr, width= 18 , fg='black',font=('Arial',9,'bold') )
entry_82_chkl.grid(row = 3, column=8  , padx = 0 ,  pady=1)
entry_82_chkl.insert(END, "2200")

entry_83_chkl  = Entry(Ledger_table_Area_chklgr, width= 18 , fg='black',font=('Arial',9,'bold') )
entry_83_chkl.grid(row = 4, column=8  , padx = 0 ,  pady=1)
entry_83_chkl.insert(END, " ")

entry_84_chkl  = Entry(Ledger_table_Area_chklgr, width= 18 , fg='black',font=('Arial',9,'bold') )
entry_84_chkl.grid(row = 5, column=8  , padx = 0 ,  pady=1)
entry_84_chkl.insert(END, " ")

entry_85_chkl  = Entry(Ledger_table_Area_chklgr, width= 18 , fg='black',font=('Arial',9,'bold') )
entry_85_chkl.grid(row = 6, column=8  , padx = 0 ,  pady=1)
entry_85_chkl .insert(END, "3333")

entry_86_chkl  = Entry(Ledger_table_Area_chklgr, width= 18 , fg='black',font=('Arial',9,'bold') )
entry_86_chkl.grid(row = 7, column=8  , padx = 0 ,  pady=1)
entry_86_chkl.insert(END, " ")

entry_87_chkl  = Entry(Ledger_table_Area_chklgr, width= 18 , fg='black' , bg  = 'red',font=('Arial',9,'bold') )
entry_87_chkl.grid(row = 8, column=8  , padx = 0 ,  pady=1)
entry_87_chkl.insert(END, " CREDIT")

entry_88_chkl  = Entry(Ledger_table_Area_chklgr, width= 18 , fg='black',font=('Arial',9,'bold') )
entry_88_chkl.grid(row = 9, column=8  , padx = 0 ,  pady=1)
entry_88_chkl.insert(END, " 6742")



label_9_chkl = Entry(Ledger_table_Area_chklgr , width=18, fg='white' , bg = "blue",font=('Arial',9,'bold') )
label_9_chkl.grid(row = 1 , column = 9 ,  pady=1, padx=0)
label_9_chkl.insert(END, "balance")

entry_91_chkl  = Entry(Ledger_table_Area_chklgr , width= 18 , fg='black',font=('Arial',9,'bold') )
entry_91_chkl.grid(row = 2, column=9  , padx = 0 ,  pady=1)
entry_91_chkl .insert(END, " 89990")

entry_92_chkl = Entry(Ledger_table_Area_chklgr , width=18 , fg='black',font=('Arial',9,'bold') )
entry_92_chkl.grid(row = 2, column=9  , padx = 0 ,  pady=1)
entry_92_chkl.insert(END, " ")

entry_93_chkl = Entry(Ledger_table_Area_chklgr , width=18 , fg='black',font=('Arial',9,'bold') )
entry_93_chkl.grid(row = 3, column=9  , padx = 0 ,  pady=1)
entry_93_chkl.insert(END, " ")

entry_94_chkl = Entry(Ledger_table_Area_chklgr , width=18 , fg='black',font=('Arial',9,'bold') )
entry_94_chkl.grid(row = 4, column=9  , padx = 0 ,  pady=1)
entry_94_chkl.insert(END, " ")

entry_95_chkl = Entry(Ledger_table_Area_chklgr , width=18 , fg='black',font=('Arial',9,'bold') )
entry_95_chkl.grid(row = 5, column=9  , padx = 0 ,  pady=1)
entry_95_chkl.insert(END, "72902 ")

entry_96_chkl = Entry(Ledger_table_Area_chklgr , width=18 , fg='black',font=('Arial',9,'bold') )
entry_96_chkl.grid(row = 6, column=9  , padx = 0 ,  pady=1)
entry_96_chkl.insert(END, " ")

entry_97_chkl = Entry(Ledger_table_Area_chklgr , width=18 , fg='black',font=('Arial',9,'bold') )
entry_97_chkl.grid(row = 7, column=9  , padx = 0 ,  pady=1)
entry_97_chkl.insert(END, " ")

entry_98_chkl = Entry(Ledger_table_Area_chklgr , width=18 , fg='black' , bg ='blue',font=('Arial',9,'bold') )
entry_98_chkl.grid(row = 8, column=9  , padx = 1)
entry_98_chkl .insert(END, " TOTAL BALANCE ")

entry_99_chkl= Entry(Ledger_table_Area_chklgr , width=18 , fg='black',font=('Arial',9,'bold') )
entry_99_chkl.grid(row = 9, column=9  , padx = 1 )
entry_99_chkl.insert(END, "55000")


chk_Ledger.pack_forget()




#CHECK_Diary

chk_Diary= check_Diary = Frame(root,width=1120, height= 580, bg="white" )
check_Diary.pack(side='top' , anchor="n" , padx=0)
check_Diary.pack_propagate(0)


Diary_table_Area = Frame(check_Diary,width=1000, height= 580, bg="black" )
Diary_table_Area.pack(side='right' , anchor="n" , padx=40 , pady = 30)

Diary_button_area = Frame(check_Diary,width=200, height= 580, bg="black" )
Diary_button_area.pack(side='left' , anchor="n" , padx=20 , pady = 30)
label = Label(Diary_button_area, text = "ADD LEDGER NO TO UPDATE", relief=RAISED , bg= 'black' , fg = 'white' , bd=0  ,font=('Arial',12,'bold') )
label.pack(side='top' , anchor="n" , pady=10, padx=20 )

entry = Entry(Diary_button_area, width=21, fg='black',font=('Arial',16,'bold') )
entry.pack(pady= 10,anchor="n")

buton = Button(Diary_button_area  ,bd=0.5,text='SUBMIT NO' , bg='green', fg='white'  , font=buttonFont,  width=14 )
buton.pack( pady= 20,anchor="n")

label2 = Label(Diary_button_area, text = "ADD  ", relief=RAISED , bg= 'black' , fg = 'white' , bd=0  ,font=('Arial',12,'bold') )
label2.pack(side='top' , anchor="n" , pady=167, padx=20 )

Diary_items = [("12313" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200077" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),]
                                                                 
Diary_head = ["Account of" , "contact no" , "NAME" , "debit " , " credit" , " Balance" , "DIJEKSTRA "]

for i in range(7):
    b = Entry(Diary_table_Area, width=10, fg='black',font=('Arial',12,'bold') )
    b.grid(row=0, column=i , pady=10)
    b.insert(END ,  Diary_head[i])
      

for i in range(17):
    for j in range(7):
        c = Entry(Diary_table_Area, width=10,  fg='black',font=('Arial',12,'bold') )
        c.grid( row=i+1, column=j , pady=2)
        c.insert(END,  Diary_items[i][j])
        
chk_Diary.pack_forget()



#counter

chk_counter = check_counter = Frame(root,width=1420, height= 680, bg="white" )
check_counter.pack(side='top' , anchor="n" , padx=0)
check_counter.pack_propagate(0)

counter_label_Area = Frame(check_counter,width=600, height= 70, bg="white" )
counter_label_Area.pack(side='top' , anchor="ne" , padx=0 , pady= 10)
 
counter_table_Area = Frame(check_counter,width=1000, height= 590, bg="black" )
counter_table_Area.pack(side='right' , anchor="n" , padx=10 , pady= 10)

counter_button_area = Frame(check_counter,width=350, height= 580, bg="black" )
counter_button_area.pack(side='left' , anchor="n" , padx=20 , pady= 0)



label = Label(counter_button_area, text = "SEARCH PRODUCT", relief=RAISED , bg= 'black', fg= 'white' , bd=0, font=("Arial", 10 , "bold")  )
label.pack(side='top' , anchor="n" , pady=5, padx=5 )
entry = Entry(counter_button_area, width=22 ,  fg='black'  ,highlightthickness=0.5 , highlightbackground="black" ,font=('Arial',13,'bold') )
entry.pack(pady= 0,anchor="n")

buton = Button(counter_button_area  ,bd=0.5,text='SEARCH' , bg='blue', fg='white'  , font=buttonFont,  width=16 )
buton.pack( pady= 15,anchor="n")

label = Label(counter_button_area, text = "ADD PRODUCT", relief=RAISED , bg= 'black', fg= 'white' , bd=0, font=("Arial", 10 , "bold")  )
label.pack(side='top' , anchor="n" , pady=10, padx=5 )
entry = Entry(counter_button_area, width=11, fg='black',highlightthickness=0.5 , highlightbackground="black" ,font=('Arial',16,'bold') )
entry.pack(pady= 0,anchor="n")


label = Label(counter_button_area, text = "ADD UNIT", relief=RAISED , bg= 'black', fg= 'white', bd=0, font=("Arial", 10 , "bold")  )
label.pack(side='top' , anchor="n" , pady=10, padx=5 )
entry = Entry(counter_button_area, width=11, fg='black',highlightthickness=0.5 , highlightbackground="black" ,font=('Arial',16,'bold') )
entry.pack(pady= 0,anchor="n")


label = Label(counter_button_area, text = "ADD NAME", relief=RAISED ,  bg= 'black', fg= 'white', bd=0, font=("Arial", 10 , "bold")  )
label.pack(side='top' , anchor="n" , pady=10, padx=5 )
entry = Entry(counter_button_area, width=11, fg='black',highlightthickness=0.5 , highlightbackground="black" ,font=('Arial',16,'bold') )
entry.pack(pady= 0,anchor="n")


label = Label(counter_button_area, text = "ADD PHONE", relief=RAISED , bg= 'black', fg= 'white' , bd=0, font=("Arial", 10 , "bold")  )
label.pack(side='top' , anchor="n" , pady=10, padx=5 )
entry = Entry(counter_button_area, width=11, fg='black',highlightthickness=0.5 , highlightbackground="black" ,font=('Arial',16,'bold') )
entry.pack(pady= 0,anchor="n")
buton = Button(counter_button_area  ,bd=0.5,text='ADD TO BILL' , bg='green', fg='white'  , font=buttonFont,  width=16 )
buton.pack( pady= 20,anchor="n")

label = Label(counter_label_Area , text = "COUNTER", relief=RAISED , bg= 'white' , bd=0, font=("Arial", 14 , "bold")  )
label.pack(side='left' , anchor="w" , pady=5, padx=255 )

label = Label(counter_label_Area , text = "PRODUCTS ADDED", relief=RAISED , bg= 'white' , bd=0, font=("Arial", 10 , "bold")  )
label.pack(side='left' , anchor="n" , pady=5, padx=5 )
entry = Entry(counter_label_Area ,width=8,  highlightthickness=0.5 , highlightbackground="black", fg='black',font=('Arial',16,'bold') )
entry.pack(side='left' , pady= 0, padx=5,anchor="n")
entry.insert(END, "0")

label = Label(counter_label_Area , text = "TOTAL BILL", relief=RAISED , bg= 'white' , bd=0, font=("Arial", 10 , "bold")  )
label.pack(side='left' , anchor="n" , pady=5, padx=5 )
entry = Entry(counter_label_Area , width=8, highlightthickness=0.5 , highlightbackground="black", fg='black',font=('Arial',16,'bold') )
entry.pack(side='left' , pady= 0, padx=15,anchor="n")
entry.insert(END, "200")





counter_items = [("COUNTER" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200077" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),]
                                                                 
counter_head = ["S/n" , "LEDGER NO" , "NAME" , "ADRESS" , "COUNTRY" , "PHONE" , "Class"]

for i in range(7):
    b = Entry(counter_table_Area, width=12, fg='black',font=('Arial',12,'bold') )
    b.grid(row=0, column=i , pady=10)
    b.insert(END ,  counter_head[i])    

for i in range(15):
    for j in range(7):
        c = Entry(counter_table_Area, width=12,  fg='black',font=('Arial',12,'bold') )
        c.grid( row=i+1, column=j , pady=2)
        c.insert(END, counter_items[i][j])

chk_counter.pack_forget()



#Billing'



chk_Billing = check_Billing = Frame(root,width=1350, height= 580, bg="white")
check_Billing.pack(side='top' , anchor="n" , padx=0)
check_Billing.pack_propagate(0)

label1 = Label(chk_Billing, text = "BILLING PANEL ", relief=RAISED , bg= 'white' , fg = 'black' , bd=0, font=("Arial", 18 , "bold")  )
label1.pack(side='top' , anchor="n" , padx=10 , pady= 30)

Billing_label_Area = Frame(check_Billing,width=600, height= 70, bg="white" )
Billing_label_Area.pack(side='top' , anchor="ne" , padx=0 , pady= 10)

Billing_table_Area = Frame(check_Billing ,width=1000, height= 590, bg="black" )
Billing_table_Area.pack(side='top' , anchor="n" , padx=0 , pady= 0)

label = Label(Billing_table_Area, text = "CUSTOMER HISTORY ", relief=RAISED , bg= 'black' , fg = 'white' , bd=0, font=("Arial", 14 , "bold")  )
label.grid(row = 1,  column = 3 , padx = 60)


label = Label(Billing_table_Area, text = "NAME OF CUSTOMER", relief=RAISED , bg= 'black' , fg = 'white', bd=0, font=("Arial", 10 , "bold")  )
label.grid(row = 2,  column = 2, padx = 60)
entry1 = Entry(Billing_table_Area, width=22 ,  fg='black'  ,highlightthickness=0.5 , highlightbackground="white" ,font=('Arial',13,'bold') )
entry1.grid(row = 2 ,  column = 3 , pady = 20 ,padx = 60 )
entry1.insert(END , "alpha")

label = Label(Billing_table_Area, text = "previous", relief=RAISED , bg= 'black' , fg = 'white' , bd=0, font=("Arial", 10 , "bold")  )
label.grid(row = 3,  column = 2 ,padx = 60)
entry2 = Entry(Billing_table_Area, width=22 ,  fg='black'  ,highlightthickness=0.5 , highlightbackground="white" ,font=('Arial',13,'bold') )
entry2.grid(row = 3 ,  column = 3 , pady = 20 , padx = 60)
entry2.insert(END , "YES")

label = Label(Billing_table_Area, text = "uptill bill", relief=RAISED , bg= 'black' , fg = 'white' , bd=0, font=("Arial", 10 , "bold")  )
label.grid(row = 4,  column = 2 , padx = 60)
entry3 = Entry(Billing_table_Area, width=22 ,  fg='black'  ,highlightthickness=0.5 , highlightbackground="white" ,font=('Arial',13,'bold') )
entry3.grid(row = 4 ,  column = 3 , pady = 20  , padx = 60)
entry3.insert(END , "$300")

label = Label(Billing_table_Area, text = "BILL RECIVED", relief=RAISED , bg= 'black' , fg = 'white' , bd=0, font=("Arial", 14 , "bold")  )
label.grid(row = 1, column = 8 , pady = 20)

label = Label(Billing_table_Area, text = "NAME", relief=RAISED , bg= 'black' , fg = 'white' , bd=0, font=("Arial", 10 , "bold")  )
label.grid(row = 2,  column = 7 , padx = 20)
entry4 = Entry(Billing_table_Area, width=22 ,  fg='black'  ,highlightthickness=0.5 , highlightbackground="white" ,font=('Arial',13,'bold') )
entry4.grid(row = 2 ,  column = 8 , pady = 20)
entry4.insert(END , "HABIB")

label = Label(Billing_table_Area, text = "products", relief=RAISED , bg= 'black' , fg = 'white' , bd=0, font=("Arial", 10 , "bold")  )
label.grid(row = 3,  column = 7 , padx = 20)
entry5= Entry(Billing_table_Area, width=22 ,  fg='black'  ,highlightthickness=0.5 , highlightbackground="white" ,font=('Arial',13,'bold') )
entry5.grid(row = 3 ,  column = 8 , pady = 20)
entry5.insert(END , "FRONT MIRROR")

label = Label(Billing_table_Area, text = "TAXES", relief=RAISED , bg= 'black' , fg = 'white', bd=0, font=("Arial", 10 , "bold")  )
label.grid(row = 4,  column = 7 , padx = 20)
entry6 = Entry(Billing_table_Area, width=22 ,  fg='black'  ,highlightthickness=0.5 , highlightbackground="white" ,font=('Arial',13,'bold') )
entry6.grid(row = 4 ,  column = 8 , pady = 20 )
entry6.insert(END , "$200")

label = Label(Billing_table_Area, text = "TOTAL BILL", relief=RAISED , bg= 'black' , fg = 'white' , bd=0, font=("Arial", 10 , "bold")  )
label.grid(row = 5,  column = 7 , padx = 20)
entry7 = Entry(Billing_table_Area, width=22 ,  fg='black'  ,highlightthickness=0.5 , highlightbackground="white" ,font=('Arial',13,'bold') )
entry7.grid(row = 5 ,  column = 8 , pady = 20)
entry7.insert(END , "$500")

buton = Button(Billing_table_Area , bd=0.5,text='CASH RECIEVED' , bg='green', fg='white'  , font=buttonFont,  width=16 , command = remove_entry )
buton.grid(row = 8 ,  column = 8 , pady = 20)



chk_Billing.pack_forget()




# return_products

retrn_products = return_products = Frame(root,width=1350, height= 580, bg="white" )
return_products.pack(side='top' , anchor="n" , padx=0)
return_products.pack_propagate(0)


retrn_label_Area = Frame(return_products,width=600, height= 70, bg="white"  )
retrn_label_Area.pack(side='top' , anchor="ne" , padx=40 , pady= 10)
label = Label(retrn_label_Area, text = "RETURN PRODUCT", relief=RAISED , bg= 'white' , bd=0, font=("Arial", 14 , "bold")  )
label.pack(side='top' , anchor="n" , pady=10, padx=205 )

r = retrn_table_Area = Frame(return_products,width=1000, height= 590, bg="black" )
retrn_table_Area.pack(side='right' , anchor="n" , padx=10 , pady= 10)
retrn_table_Area.pack_forget()

retrn_button_area = Frame(return_products,width=350, height= 580, bg="black" )
retrn_button_area.pack(side='left' , anchor="n" , padx=20 , pady= 0)

label = Label(retrn_button_area, text = "PRODUCT ID", relief=RAISED , bg= 'black' , fg = 'white', bd=0, font=("Arial", 10 , "bold")  )
label.pack(side='top' , anchor="n" , pady=5, padx=5 )
entry = Entry(retrn_button_area, width=21 ,  fg='black'  ,highlightthickness=0.5 , highlightbackground="black" ,font=('Arial',13,'bold') )
entry.pack(pady= 0,anchor="n")


label = Label(retrn_button_area, text = "CUSTOMER NAME", relief=RAISED , bg= 'black' , fg = 'white' , bd=0, font=("Arial", 10 , "bold")  )
label.pack(side='top' , anchor="n" , pady=10, padx=5 )
entry = Entry(retrn_button_area, width=21, fg='black',highlightthickness=0.5 , highlightbackground="black" ,font=('Arial',16,'bold') )
entry.pack(pady= 0,anchor="n")
buton = Button(retrn_button_area  ,bd=0.5,text='Return' , bg='blue', fg='white'  , font=buttonFont,  width=12 )
buton.pack( pady= 10,anchor="n")

buton = Button(retrn_button_area  ,bd=0.5,text='CHECK Returns' , bg='green', fg='white'  , font=buttonFont,  width=12 , command = show_Table )
buton.pack( pady= 50,anchor="n")


retrn_items = [("COUNTER" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200077" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"), 
               ("23443" , "ALPHA" , "BEta" , "Gama"  ,"sigma" ,  "200083" ,  "CUSTOMER"),]
                                                                 
retrn_head = ["S/n" , "LEDGER NO" , "NAME" , "ADRESS" , "COUNTRY" , "PHONE" , "Class"]

for i in range(7):
    b = Entry(retrn_table_Area, width=12, fg='black',font=('Arial',12,'bold') )
    b.grid(row=0, column=i , pady=10)
    b.insert(END ,  retrn_head[i])    

for i in range(17):
    for j in range(7):
        c = Entry(retrn_table_Area, width=12,  fg='black',font=('Arial',12,'bold') )
        c.grid( row=i+1, column=j , pady=2)
        c.insert(END, retrn_items[i][j])

return_products.pack_forget()



# settings Mode 

settings_Mode  = Frame(root,width=900, height= 550,  bg="black" )
settings_Mode.pack(side='top' , anchor="n" , padx=0 , pady=35)
settings_Mode.pack_propagate(0)

label_settings_Mode = Label(settings_Mode , text="TO CHANGE ADMIN PASSWORD", font=("Courier 14 bold") , fg = 'white' , bg = 'black')
label_settings_Mode.grid(row = 1 , column = 1 , padx=40 , pady=60)

label1_sM = Label(settings_Mode , text = "enter the old password", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=('Arial',12,'bold'))
label1_sM.grid(row = 2 , column = 1 , pady=19 , padx=14)

entry1_sM = Entry(settings_Mode , width=24, fg='black',font=('Arial',16,'bold')  ,highlightthickness=0.5 , highlightbackground="black")
entry1_sM.grid(row= 3, column=1  , padx=19 )

label1_sM = Label(settings_Mode, text = "enter the new password", relief=RAISED , bg= 'black' , fg='white' , bd=0 , font=('Arial',12,'bold') )
label1_sM.grid(row = 4 , column = 1 , pady=19 , padx=14)

entry12_sM = Entry(settings_Mode, width=24, fg='black',font=('Arial',16,'bold')  ,highlightthickness=0.5 , highlightbackground="black")
entry12_sM.grid(row= 5, column=1 , padx=19 )

button1_sM= Button(settings_Mode , bd=0.5 ,text='CHANGE THE PASSWORD' , bg='red', fg='white'  , font=buttonFont,  width=21 )
button1_sM.grid( row= 6 , column= 1 , pady = 20 )



label2_sM = Label(settings_Mode , text="TO CHANGE  DATA BASE ROOT", font=("Courier 14 bold") , fg = 'white' , bg = 'black')
label2_sM.grid(row = 1 , column = 2 , padx=40 , pady=60)

label22_sM = Label(settings_Mode , text = "ENTER THE DATABASE NAME", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=('Arial',12,'bold') )
label22_sM.grid(row = 2 , column = 2 , pady=19 , padx=14)

entry22_sM = Entry(settings_Mode , width=24, fg='black',font=('Arial',16,'bold')  ,highlightthickness=0.5 , highlightbackground="black")
entry22_sM.grid(row= 3, column=2  , padx=19 )

label23_sM = Label(settings_Mode , text = "ENTER THE DATABASE PASSWORD", relief=RAISED , bg= 'black' , fg='white' , bd=0  , font=('Arial',12,'bold'))
label23_sM.grid(row = 4 , column = 2 , pady=19 , padx=14)

entry23_sM = Entry(settings_Mode , width=24, fg='black',font=('Arial',16,'bold')  ,highlightthickness=0.5 , highlightbackground="black")
entry23_sM.grid(row= 5, column=2  , padx=19 )

button2_sM= Button(settings_Mode , bd=0.5 ,text='CHANGE THE DATABASE ' , bg='red', fg='white'  , font=buttonFont,  width=21 )
button2_sM.grid( row= 6 , column= 2 , pady = 20 )

settings_Mode.pack_forget()


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

    def exitProgram(self):
        exit()
        



app = Window(root)









root.mainloop()





