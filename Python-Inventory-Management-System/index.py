

var = "var"





class Window1(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

 

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
   
    def exitProgram(self):
        exit()



