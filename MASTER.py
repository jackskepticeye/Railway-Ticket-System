from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import random
import datetime
import time
import sys

sys.path.insert(0,"/Users/siddhesh/opt/anaconda3/lib/python3.9/site-packages")

from pymysql import *




def main() :

    main_win = Tk()
    app = Login(main_win)
    main_win.mainloop()




class Login() :

    
    def __init__(self,win) :

        self.win = win

        self.win.title("UTS LOGIN")
        self.win.geometry("340x450")
        self.win.configure (background = "maroon")
        
        ##################################### MAIN FRAME ###################################################################
        main_frame = Frame (self.win, bd = 10, width = 340, height = 450, bg = "beige", relief = RIDGE)
        main_frame.grid(row = 1, column = 1)
        ########################################################################################################

        ########################################## VARIABLES ##############################################################
        self.user_ent = StringVar()

        self.pass_ent = StringVar()
        ########################################################################################################

        ############################################# BUTTON FUNCTIONS ###########################################################
        def reg_window () :
            
            self.new_win = Toplevel(self.win)
            
            self.app = Register(self.new_win)



        def login () :

            if self.user_ent.get() == "" or self.pass_ent.get() == "" :

                tkinter.messagebox.showerror ("ERROR","PLEASE ENTER YOUR USERNAME & PASSWORD")

            else :

                conn = connect (host = 'localhost',
                 user = 'root',
                 passwd = 'sid29#ashok',
                 db = 'Registration_Details')

                cr = conn.cursor()

                cr.execute ("select * from Reg_Details where EMAIL = %s and PASSWORD_1 = %s", (self.user_ent.get(), self.pass_ent.get()))

                row = cr.fetchone()

                if row == None :

                    tkinter.messagebox.showerror("ERROR","INVALID USERNAME OR PASSWORD")

                else :

                    open_main = tkinter.messagebox.askyesno("Select Option","ACCESS ONLY TO EMPLOYEES")                

                    if open_main > 0 :

                        self.new_win_1 = Toplevel(self.win)

                        self.app = Train(self.new_win_1)

                    else :

                        if not open_main :

                            return


                conn.commit()

                conn.close()


        def reset_pass_btn () :

            if self.new_pass_ent.get() != self.con_new_pass.get() :

                tkinter.messagebox.showerror ("ERROR","NEW PASSWORD & CONFIRM NEW PASSWORD SHOULD BE SAME",parent = self.win_2 )


            elif self.var_sec_ques.get() == "" or self.var_sec_ans_ent.get() == "" :

                tkinter.messagebox.showerror ("ERROR","ALL FIELDS ARE MANDATORY",parent = self.win_2)


            elif self.new_pass_ent.get() == "" or self.con_new_pass.get() == "" :

                tkinter.messagebox.showerror ("ERROR","ALL FIELDS ARE MANDATORYALL FIELDS ARE MANDATORY",parent = self.win_2)

            else :

                conn = connect (host = 'localhost',
                 user = 'root',
                 passwd = 'sid29#ashok',
                 db = 'Registration_Details')

                cr = conn.cursor()

                query = ("select * from Reg_Details where EMAIL = %s and Security_Q = %s and Security_A = %s")

                value = (self.user_ent.get(),self.var_sec_ques.get(),self.var_sec_ans_ent.get())

                cr.execute (query,value)

                row = cr.fetchone()

                if row == None :

                    tkinter.messagebox.showerror ("ERROR","PLEASE ENTER THE CORRECT ANSWER",parent = self.win_2)

                else :

                    query = ("update Reg_Details set PASSWORD_1 = %s where EMAIL = %s")

                    value = (self.new_pass_ent.get(),self.user_ent.get())

                    cr.execute (query,value)


            conn.commit()

            conn.close()

            tkinter.messagebox.showinfo ("SUCESSFULL","YOUR PASSWORD HAS BEEN RESET SUCCESSFULLY",parent = self.win_2)

            self.win_2.destroy()



                             

                         

                


            
            


        def forgot_pass ():


            if self.user_ent.get() == "" :

                tkinter.messagebox.showerror("ERROR","PLEASE ENTER YOUR EMAIL ADDRESS TO RESET PASSWORD")


            else :

                conn = connect (host = 'localhost',
                 user = 'root',
                 passwd = 'sid29#ashok',
                 db = 'Registration_Details')

                cr = conn.cursor()

                query = ('select * from Reg_Details where EMAIL = %s')

                value = (self.user_ent.get(),)

                cr.execute(query,value)

                row = cr.fetchone()

                if row == None :

                    tkinter.messagebox.showerror("ERROR","PLEASE ENTER A VALID EMAIL ADDRESS")

                else :

                    conn.close()

                    self.win_2 = Toplevel()

                    self.win_2.title("FORGOT PASSWORD")

                    self.win_2.geometry("340x450")

                    self.win_2.configure (background = "beige")

                    self.new_pass_ent = StringVar()

                    self.con_new_pass = StringVar()

                    self.var_sec_ques = StringVar()

                    self.var_sec_ans_ent = StringVar()

                    

                    fp_lbl = Label (self.win_2, text = "RESET PASSWORD", bd = 5, relief = RAISED, justify = CENTER, font = ('Helvetica',22,'bold'), fg = 'maroon', bg = 'beige')
                    fp_lbl.place(x = 40, y =10)


                    sec_ques_lbl = Label (self.win_2, font = ('Helvetica',20,'bold'), text = "Selct Security Question  *", bg = 'beige', fg = 'maroon', bd = 2, relief = SUNKEN, justify = CENTER)
                    sec_ques_lbl.place( x= 30, y = 70)

                    self.combo_sec_ques = ttk.Combobox (self.win_2, font = ('Helvetica',12,'bold'), state = 'readonly', textvariable = self.var_sec_ques, width = 25)             
                    self.combo_sec_ques['values'] = ['SELECT', 'Your Birth Year?','Your Favorite Place?',"Your Pet's Name?","Your Bestfriend's Name?","Your Mom's Middle Name?","Your Father's Birth Year?"]
                    self.combo_sec_ques.place( x = 40, y = 100)
                    self.combo_sec_ques.current(0)


                    sec_ans_lbl = Label (self.win_2, font = ('Helvetica',20,'bold'), text = "Security Answer  *", bg = 'beige', fg = 'maroon', bd = 2, relief = SUNKEN, justify = CENTER)
                    sec_ans_lbl.place( x= 40, y = 160)

                    self.txt_sec_ans_ent = Entry (self.win_2, font = ('Helvetica',12,'bold'), textvariable = self.var_sec_ans_ent, width = 25)                ##
                    self.txt_sec_ans_ent.place( x= 40, y = 190)



                    reset_pass_lbl = Label (self.win_2, font = ('Helvetica',20,'bold'), text = "Enter New Password  *", bg = 'beige', fg = 'maroon', bd = 2, relief = SUNKEN, justify = CENTER)
                    reset_pass_lbl.place( x= 40, y = 250)

                    self.txt_new_pass_ent = Entry (self.win_2, font = ('Helvetica',12,'bold'), width = 25, textvariable = self.new_pass_ent)
                    self.txt_new_pass_ent.place( x= 40, y = 280)


                    reset_con_pass_lbl = Label (self.win_2, font = ('Helvetica',20,'bold'), text = "Confirm New Password  *", bg = 'beige', fg = 'maroon', bd = 2, relief = SUNKEN, justify = CENTER)
                    reset_con_pass_lbl.place( x= 40, y = 330)

                    self.txt_con_new_pass_ent = Entry (self.win_2, font = ('Helvetica',12,'bold'), width = 25, textvariable = self.con_new_pass)
                    self.txt_con_new_pass_ent.place( x= 40, y = 360)


                    reset_btn = Button (self.win_2, font = ('Helvetica',20,'bold'), text = "RESET", bg = 'beige', fg = 'maroon', bd = 2, command = reset_pass_btn )
                    reset_btn.place( x= 100, y = 400)
        ########################################################################################################

        ############################################ TITLE LABEL ############################################################
        wel_lbl = Label (main_frame, text = "WELCOME TO UTS", bd = 5, relief = RAISED, justify = CENTER, font = ('Helvetica',22,'bold'), fg = 'maroon', bg = 'beige')
        wel_lbl.place(x = 40, y =10)
        ########################################################################################################

        ################################################# DATA LABEL & ENTRY FIELD #######################################################
        usr_lbl = Label (main_frame, text = "EMAIL ID  *", bd = 1, relief = SUNKEN, justify = CENTER, font = ('Helvetica',15,'bold'), fg = 'maroon', bg = 'beige')
        usr_lbl.place(x = 40, y = 120)

        self.usr_entry = Entry (main_frame, font = ('Helvetica',12,'bold'), width = 20, textvariable = self.user_ent) 
        self.usr_entry.place(x = 40, y = 150)
        ########################################################################################################

        ################################################## DATA LABELS & ENTRY FIELD ######################################################
        pass_lbl = Label (main_frame, text = "PASSWORD  *", bd = 1, relief = SUNKEN, justify = CENTER, font = ('Helvetica',15,'bold'), fg = 'maroon', bg = 'beige')
        pass_lbl.place(x = 40, y = 200)

        self.password_ent = Entry (main_frame, font = ('Helvetica',12,'bold'), width = 20, textvariable = self.pass_ent ) 
        self.password_ent.place(x = 40, y = 230)
        ########################################################################################################

        ################################################# BUTTONS #######################################################
        login_btn = Button (main_frame, text = "LOGIN", bd = 2, relief = RAISED, font = ('Helvetica',15,'bold'), fg = 'maroon', bg = 'beige', width = 8, command = login)
        login_btn.place(x = 25, y = 300)

        reg_btn = Button (main_frame, text = "REGISTER", bd = 2, relief = RAISED, font = ('Helvetica',15,'bold'), fg = 'maroon', bg = 'beige', width = 8, command = reg_window)
        reg_btn.place(x = 180, y = 300)

        fg_pass_btn = Button (main_frame, text = "FORGOT PASSWORD ?", borderwidth = 0, font = ('Helvetica',15,'bold'), fg = 'maroon', bg = 'beige', command = forgot_pass)
        fg_pass_btn.place(x = 25, y = 380)
        ########################################################################################################






class Register() :

    def __init__(self,node) :

        self.node = node

        self.node.title("UTS REGISTER")
        self.node.geometry("800x550")
        self.node.configure (background = "maroon")

        ####################################### VARAIBELS #################################################################
        self.var_fname_ent = StringVar()
        self.var_lname_ent = StringVar()
        self.var_contact_ent = StringVar()
        self.var_email_ent = StringVar()
        self.var_sec_ques = StringVar()
        self.var_sec_ans_ent = StringVar()
        self.var_pass_ent = StringVar()
        self.var_con_pass_ent = StringVar()
        ########################################################################################################

        ############################################# BUTTON FUNCTIONS ###########################################################
        def return_login () :

            self.node.destroy()

            

        def Reg ():

            if self.var_fname_ent.get() == "" or self.var_lname_ent.get() == "" or self.var_sec_ques.get() == 'SELECT' :

                tkinter.messagebox.showerror ("ERROR","ALL FIELDS ARE MANDATORY")

            elif self.var_pass_ent.get() != self.var_con_pass_ent.get() :

                tkinter.messagebox.showerror ("ERROR","PASSWORD & CONFIRM PASSWORD SHOULD BE SAME")

            else :

               conn = connect (host = 'localhost',
                   user = 'root',
                   passwd = 'sid29#ashok',
                   db = 'Registration_Details')

               cr = conn.cursor()

               query = ('select * from Reg_Details where EMAIL = %s')

               value  = (self.var_email_ent.get())

               cr.execute (query,value)

               row = cr.fetchone()

               if row != None :

                   tkinter.messagebox.showerror ("ERROR","User Already Exists")

               else :

                   cr.execute(""" insert into Reg_Details values
                                  ('{}','{}','{}','{}','{}','{}','{}');""".format(self.var_fname_ent.get(),
                                                                                  self.var_lname_ent.get(),
                                                                                  self.var_contact_ent.get(),
                                                                                  self.var_email_ent.get(),
                                                                                  self.var_sec_ques.get(),
                                                                                  self.var_sec_ans_ent.get(),
                                                                                  self.var_pass_ent.get()))
                               

               conn.commit()

               conn.close()

               tkinter.messagebox.showinfo("SUCCESSFULL", "REGISTARTION SUCCESSFULL")

               print ('F_Name : ', self.var_fname_ent.get(), 'L_Name : ',self.var_lname_ent.get(), 'Contact : ',self.var_contact_ent.get(), 'Email : ',self.var_email_ent.get(), 'Sec_Ques : ',self.var_sec_ques.get(), 'Sec_Ans : ',self.var_sec_ans_ent.get(), 'Password : ',self.var_pass_ent.get())
        ########################################################################################################

        ########################################## MAIN FRAME ##############################################################
        main_frame = Frame (self.node, bd = 10, width = 800, height = 550, bg = "beige", relief = RIDGE)
        main_frame.grid(row = 1, column = 1)
        ########################################################################################################


        ############################################# TITLE LABEL ###########################################################
        reg_lbl = Label (main_frame, font = ('Helvetica',30,'bold'), text = "REGISTER HERE", bg = 'beige', fg = 'maroon', bd = 5, relief = RAISED, justify = CENTER)
        reg_lbl.place( x= 250, y = 20)
        ########################################################################################################


        ################################################# DATA LABELS & ENTRY FIELDS #######################################################
        fname_lbl = Label (main_frame, font = ('Helvetica',20,'bold'), text = "First Name  *", bg = 'beige', fg = 'maroon', bd = 2, relief = SUNKEN, justify = CENTER)
        fname_lbl.place( x= 50, y = 120)

        self.txt_fname_ent = Entry (main_frame, font = ('Helvetica',12,'bold'), width = 25, textvariable = self.var_fname_ent)
        self.txt_fname_ent.place( x= 50, y = 160)

        

        contact_lbl = Label (main_frame, font = ('Helvetica',20,'bold'), text = "Contact  *", bg = 'beige', fg = 'maroon', bd = 2, relief = SUNKEN, justify = CENTER)
        contact_lbl.place( x= 50, y = 200)

        self.txt_contact_ent = Entry (main_frame, font = ('Helvetica',12,'bold'), width = 25, textvariable = self.var_contact_ent)
        self.txt_contact_ent.place( x= 50, y = 240)



        sec_ques_lbl = Label (main_frame, font = ('Helvetica',20,'bold'), text = "Select Security Question  *", bg = 'beige', fg = 'maroon', bd = 2, relief = SUNKEN, justify = CENTER)
        sec_ques_lbl.place( x= 50, y = 280)

        self.combo_sec_ques = ttk.Combobox (main_frame, font = ('Helvetica',12,'bold'), state = 'readonly', width = 25, textvariable = self.var_sec_ques)
        self.combo_sec_ques['values'] = ['SELECT', 'Your Birth Year?','Your Favorite Place?',"Your Pet's Name?","Your Favorite Color?","Your Favorite Food?","Your Favorite Movie?"]
        self.combo_sec_ques.place( x = 50, y = 320)
        self.combo_sec_ques.current(0)



        
        pass_lbl = Label (main_frame, font = ('Helvetica',20,'bold'), text = "Password  *", bg = 'beige', fg = 'maroon', bd = 2, relief = SUNKEN, justify = CENTER)
        pass_lbl.place( x= 50, y = 360)

        self.txt_pass_ent = Entry (main_frame, font = ('Helvetica',12,'bold'), width = 25, textvariable = self.var_pass_ent)
        self.txt_pass_ent.place( x= 50, y = 400)
        ########################################################################################################


        ############################################### DATA LABELS & ENTRY FIELDS #########################################################
        lname_lbl = Label (main_frame, font = ('Helvetica',20,'bold'), text = "Last Name  *", bg = 'beige', fg = 'maroon', bd = 2, relief = SUNKEN, justify = CENTER)
        lname_lbl.place( x= 550, y = 120)

        self.txt_lname_ent = Entry (main_frame, font = ('Helvetica',12,'bold'), width = 25, textvariable = self.var_lname_ent)
        self.txt_lname_ent.place( x= 550, y = 160)


        

        email_lbl = Label (main_frame, font = ('Helvetica',20,'bold'), text = "Email  *", bg = 'beige', fg = 'maroon', bd = 2, relief = SUNKEN, justify = CENTER)
        email_lbl.place( x= 550, y = 200)
        
        self.txt_email_ent = Entry (main_frame, font = ('Helvetica',12,'bold'), width = 25, textvariable = self.var_email_ent)
        self.txt_email_ent.place( x= 550, y = 240)



        sec_ans_lbl = Label (main_frame, font = ('Helvetica',20,'bold'), text = "Security Answer  *", bg = 'beige', fg = 'maroon', bd = 2, relief = SUNKEN, justify = CENTER)
        sec_ans_lbl.place( x= 550, y = 280)

        self.txt_sec_ans_ent = Entry (main_frame, font = ('Helvetica',12,'bold'), width = 25, textvariable = self.var_sec_ans_ent)
        self.txt_sec_ans_ent.place( x= 550, y = 320)



        con_pass_lbl = Label (main_frame, font = ('Helvetica',20,'bold'), text = "Confirm Password  *", bg = 'beige', fg = 'maroon', bd = 2, relief = SUNKEN, justify = CENTER)
        con_pass_lbl.place( x= 550, y = 360)

        self.txt_con_pass_ent = Entry (main_frame, font = ('Helvetica',12,'bold'), width = 25, textvariable = self.var_con_pass_ent)
        self.txt_con_pass_ent.place( x= 550, y = 400)
        ########################################################################################################


        ################################################## BUTTONS ######################################################
        reg_btn = Button (main_frame, text = "REGISTER", bd = 2, relief = RAISED, font = ('Helvetica',15,'bold'), fg = 'maroon', bg = 'beige', width = 10, height = 2, command = Reg )
        reg_btn.place( x = 250, y = 460)

        login_now_btn = Button (main_frame, text = "LOGIN", bd = 2, relief = RAISED, font = ('Helvetica',15,'bold'), fg = 'maroon', bg = 'beige', width = 10, height = 2, command = return_login)
        login_now_btn.place( x = 410, y = 460)
        ########################################################################################################





class Train () :

    def __init__ (self,root) :

        self.root = root

        self.root.title ("UTS RAILWAY")

        self.root.geometry ("1350x680")

        self.root.configure (background = "maroon")

        
        ########################################## FRAMES ##############################################################
        
        ### MAIN FRAME, TOP FRAME 1, TOP FRAME 2 #####
        main_frame = Frame (self.root, bd = 10, width = 1350, height = 700, bg = "beige", relief = RIDGE)
        main_frame.grid()

        top_frame_1  = Frame (main_frame, bd = 10, width = 1340, height = 100, bg = "beige", relief = RIDGE)
        top_frame_1.grid()

        top_frame_2 = Frame (main_frame, bd = 10, width = 1300, height = 500, bg = "beige", relief = RIDGE)
        top_frame_2.grid()
        ########

        ### TOP FRAME 2 : frame 1 & 2 #####
        top_2_frame_1 = Frame (top_frame_2, bg = 'beige', width = 890, height = 500, bd = 5, relief = RIDGE)
        top_2_frame_1.grid(row = 1 , column = 0)

        top_2_frame_2 = Frame (top_frame_2, bg = 'beige', width = 400, height = 500, pady = 2, bd = 5, relief = RIDGE)
        top_2_frame_2.grid(row = 1 , column = 1)
        ########

        ### TOP RIGHT FRAME, BOTTOM RIGHT FRAME #####
        top_right_frame = Frame (top_2_frame_2, bg = 'beige', width = 404, height = 420, bd = 5, pady = 15 , relief = RIDGE)
        top_right_frame.pack(side = TOP)

        bottom_right_frame = Frame (top_2_frame_2, bg = 'beige', width = 408, height = 100, bd = 5, pady = 15 , relief = RIDGE)
        bottom_right_frame.pack(side = BOTTOM)
        ########

        ### TOP FRAME : 1A, 2A #####
        top_frame_1_a = Frame (top_2_frame_1, bg = 'beige', width = 900, height = 330, bd = 5, relief = RIDGE)
        top_frame_1_a.pack(side = TOP)

        top_frame_2_a = Frame (top_2_frame_1, bg = 'beige', width = 900, height = 320, bd = 5, relief = RIDGE)
        top_frame_2_a.pack(side = BOTTOM)
        ########

        #### TOP LEFT FRAME 1, 2, 3 ####
        top_left_1 = Frame (top_frame_1_a, bg = 'beige', width = 300, height = 200, bd = 5, padx = 20, pady = 1, relief = RIDGE)
        top_left_1.pack(side = LEFT)

        top_left_2 = Frame (top_frame_1_a, bg = 'beige', width = 300, height = 200, bd = 5, relief = RIDGE)
        top_left_2.pack(side = RIGHT)

        top_left_3 = Frame (top_frame_1_a, bg = 'beige', width = 300, height = 200, bd = 5, pady = 5, relief = RIDGE)
        top_left_3.pack(side = RIGHT)
        ########

        #### BOTTOM LEFT FAME 1 ####
        bottom_left_1 = Frame (top_frame_2_a, bg = 'beige', width = 450, height = 300, bd = 5, pady = 12, relief = RIDGE)
        bottom_left_1.pack(side = LEFT)
        ########

        ### BOTTOM LEFT FAME 2 #####
        bottom_left_2 = Frame (top_frame_2_a, bg = 'beige', width = 450, height = 300, bd = 5, relief = RIDGE)
        bottom_left_2.pack(side = RIGHT)
        ########

        ################################################################################################################
        
        ### TITLE LABEL #####
        title_lb = Label (top_frame_1, font = ('Helvetica',40,'bold'), text = "UNRESERVED RAILWAY TICKETING SYSTEM", width = 41, bg = 'beige', fg = 'maroon', relief = 'solid', padx = 4, justify = CENTER)
        title_lb.grid(row = 0 , column = 0)
        ########

        ########################################### VARIABLES #####################################################################
        date_1 = StringVar()
        time_1 = StringVar()
        ticket_class = StringVar()
        ticket_price = StringVar()
        child_ticket = StringVar()
        adult_ticket = StringVar()
        origin = StringVar()
        destination = StringVar()
        route_fee = StringVar()
        route = StringVar()
        receipt_ref = StringVar()

        text_input = StringVar()
        global operator
        operator = ""

        date_1.set("")
        time_1.set("")
        ticket_class.set("")
        ticket_price.set("")
        child_ticket.set("")
        adult_ticket.set("")
        origin.set("")
        destination.set("")
        route_fee.set("")
        route.set("")
        receipt_ref.set("")

        var_1 = IntVar()
        var_2 = IntVar()
        var_3 = IntVar()
        var_4 = IntVar()
        var_5 = IntVar()
        var_6 = StringVar()
        var_7 = IntVar()
        var_8 = StringVar()
        var_9 = StringVar()
        var_10 = IntVar()
        var_11 = IntVar()
        var_12 = IntVar()
        var_13 = IntVar()

        tax = StringVar()
        sub_total = StringVar()
        total = StringVar()

        var_1.set("0")
        var_2.set("0")
        var_3.set("0")
        var_4.set("0")
        var_5.set("0")
        var_6.set("0")
        var_7.set("0")
        var_8.set("0")
        var_9.set("0")
        var_10.set("0")
        var_11.set("0")
        var_12.set("0")
        var_13.set("0")
        
        ################################################################################################################

        ########################################### BUTTON FUNCTIONS #####################################################################

        def print_1() :

            data = open(r'/Users/siddhesh/Desktop/ticket.txt' ,'w')

            data.write('\nCLASS : {} \nGROSS PRICE : {} \nADULT : {} \nCHILD : {} \nSOURCE : {} \nDESTINATION : {} \nNET PRICE : {} \nREF NO. : {} \nTIME : {} \nDATE : {} \nROUTE : {}'.format(ticket_class.get(),ticket_price.get(),adult_ticket.get(),child_ticket.get(),origin.get(),destination.get(),route_fee.get(), receipt_ref.get(),time_1.get(),date_1.get(),route.get()))

            
            data.close()

            print ('\nCLASS : ',ticket_class.get(), '\nGROSS PRICE : ',ticket_price.get(), '\nADULT : ', adult_ticket.get(), '\nCHILD : ',child_ticket.get(), '\nSOURCE : ',origin.get(), '\nDESTINATION : ', destination.get(), '\nNET PRICE : ',route_fee.get(), '\nREF NO. : ',  receipt_ref.get(), '\nTIME : ',time_1.get(), '\nDATE : ',date_1.get(), '\nROUTE : ',route.get())



            conn = connect (host = 'localhost',
                user = 'root',
                passwd = 'sid29#ashok',
                db = 'Train')

            cr = conn.cursor()

            cr.execute ("""insert into Ticket values
                           ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');""".format(ticket_class.get(),ticket_price.get(),adult_ticket.get(),child_ticket.get(),origin.get(),destination.get(),route_fee.get(),receipt_ref.get(),time_1.get(),date_1.get(),route.get()))

            conn.commit()

            conn.close()

        
        def a_exit() :

            a_exit = tkinter.messagebox.askyesno ("UTS RAILWAY","Are you sure you want to quit?")           

            if a_exit > 0 :

                root.destroy()

                return


        def clear() :

            var_1.set("0")
            var_2.set("0")
            var_3.set("0")
            var_4.set("0")
            var_5.set("0")
            var_6.set("0")
            var_7.set("0")
            var_8.set("0")
            var_9.set("0")
            var_10.set("0")
            var_11.set("0")
            var_12.set("0")
            var_13.set("0")
            tax.set("0")
            sub_total.set("0")
            total.set("0")
            date_1.set("")
            time_1.set("")
            ticket_class.set("")
            ticket_price.set("")
            child_ticket.set("")
            adult_ticket.set("")
            origin.set("")
            destination.set("")
            route_fee.set("")
            route.set("")
            receipt_ref.set("")

            return

        

        def btnclick(numbers) :

            global operator

            operator = operator + str(numbers)

            text_input.set(operator)

            return

        

        def clear_display() :

            global operator

            operator = " "

            text_input.set(" ")

            return

        

        def equals_btn() :

            global operator

            sumup = str(eval(operator))

            text_input.set(sumup)

            operator = " "

            return

        def total_btn () :

            if  (7 <= var_7.get() <= 15) :

                if  (var_1.get() == 1) and (var_11.get() == 1) and (var_3.get() == 1) : # Gen,Adult,Single


                    tcost = int(15)
                    single = int(var_12.get())
                    adult_tax = str('%.2f' % ((tcost * single) * 0.05))
                    adult_fees =  str('%.2f' % (tcost * single))
                    total_cost =  str('%.2f' %  ((tcost * single) + (tcost * single) * 0.05))
                    tax.set(adult_tax)
                    sub_total.set(adult_fees)
                    total.set(total_cost)
                    ticket_class.set("GENERAL")
                    ticket_price.set(adult_fees)
                    child_ticket.set(0)
                    adult_ticket.set(var_10.get())
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                elif (var_1.get() == 1) and (var_11.get() == 1) and (var_4.get() == 1) : # Gen,Child,Single


                    tcost = float(7.5)
                    single = int(var_12.get())
                    child_tax = str('%.2f' % ((tcost * single) * 0.05))
                    child_fees =  str('%.2f' % (tcost * single))
                    total_cost =  str('%.2f' %  ((tcost * single) + (tcost * single) * 0.05))
                    tax.set(child_tax)
                    sub_total.set(child_fees)
                    total.set(total_cost)
                    ticket_class.set("GENERAL")
                    ticket_price.set(child_fees)
                    child_ticket.set(var_13.get())
                    adult_ticket.set(0)
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                elif  (var_2.get() == 1) and (var_11.get() == 1) and (var_3.get() == 1) and (var_4.get() == 0) : # First,Adult,Single

                    tcost = int(65)
                    single = int(var_12.get())
                    adult_tax = str('%.2f' % ((tcost * single) * 0.05))
                    adult_fees =  str('%.2f' % (tcost * single))
                    total_cost =  str('%.2f' %  ((tcost * single) + (tcost * single) * 0.05))
                    tax.set(adult_tax)
                    sub_total.set(adult_fees)
                    total.set(total_cost)
                    ticket_class.set("FIRST")
                    ticket_price.set(adult_fees)
                    child_ticket.set(0)
                    adult_ticket.set(var_10.get())
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                elif  (var_2.get() == 1) and (var_11.get() == 1) and (var_3.get() == 0) and (var_4.get() == 1) : # First,Child,Single

                    tcost = float(32.5)
                    single = int(var_12.get())
                    child_tax = str('%.2f' % ((tcost * single) * 0.05))
                    child_fees =  str('%.2f' % (tcost * single))
                    total_cost =  "₹", str('%.2f' %  ((tcost * single) + (tcost * single) * 0.05))
                    tax.set(child_tax)
                    sub_total.set(child_fees)
                    total.set(total_cost)
                    ticket_class.set("FIRST")
                    ticket_price.set(child_fees)
                    child_ticket.set(var_13.get())
                    adult_ticket.set(0)
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                elif  (var_1.get() == 1) and (var_5.get() == 1) and (var_3.get() == 1) : # Gen,Adult,Return

                    tcost = int(30)
                    return_1 = int(var_6.get())
                    adult_tax = str('%.2f' % ((tcost * return_1) * 0.05))
                    adult_fees =  str('%.2f' % (tcost * return_1))
                    total_cost =  str('%.2f' %  ((tcost * return_1) + (tcost * return_1) * 0.05))
                    tax.set(adult_tax)
                    sub_total.set(adult_fees)
                    total.set(total_cost)
                    ticket_class.set("GENERAL")
                    ticket_price.set(adult_fees)
                    child_ticket.set(0)
                    adult_ticket.set(var_10.get())
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                elif  (var_1.get() == 1) and (var_5.get() == 1) and (var_4.get() == 1) : # Gen,Child,Return

                    tcost = int(15)
                    return_1 = int(var_6.get())
                    child_tax = str('%.2f' % ((tcost * return_1) * 0.05))
                    child_fees =  str('%.2f' % (tcost * return_1))
                    total_cost =  str('%.2f' %  ((tcost * return_1) + (tcost * return_1) * 0.05))
                    tax.set(child_tax)
                    sub_total.set(child_fees)
                    total.set(total_cost)
                    ticket_class.set("GENERAL")
                    ticket_price.set(child_fees)
                    child_ticket.set(var_13.get())
                    adult_ticket.set(0)
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                elif  (var_2.get() == 1) and (var_5.get() == 1) and (var_3.get() == 1) : # Fist,Adult,Return

                    tcost = int(130)
                    return_1 = int(var_6.get())
                    adult_tax = str('%.2f' % ((tcost * return_1) * 0.05))
                    adult_fees =  str('%.2f' % (tcost * return_1))
                    total_cost =  str('%.2f' %  ((tcost * return_1) + (tcost * return_1) * 0.05))
                    tax.set(adult_tax)
                    sub_total.set(adult_fees)
                    total.set(total_cost)
                    ticket_class.set("FIRST")
                    ticket_price.set(adult_fees)
                    child_ticket.set(0)
                    adult_ticket.set(var_10.get())
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                elif  (var_2.get() == 1) and (var_5.get() == 1) and (var_4.get() == 1) : # First,Child,Return

                    
                    tcost = int(65)
                    return_1 = int(var_6.get())
                    child_tax = str('%.2f' % ((tcost * return_1) * 0.05))
                    child_fees =  str('%.2f' % (tcost * return_1))
                    total_cost =  str('%.2f' %  ((tcost * return_1) + (tcost * return_1) * 0.05))
                    tax.set(child_tax)
                    sub_total.set(child_fees)
                    total.set(total_cost)
                    ticket_class.set("FIRST")
                    ticket_price.set(child_fees)
                    child_ticket.set(var_13.get())
                    adult_ticket.set(0)
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


            if  (4 <= var_7.get() <= 6) : 

                if  (var_1.get() == 1) and (var_11.get() == 1) and (var_3.get() == 1) : # Gen,Adult,Single
                        tcost = int(10)
                        single = int(var_12.get())
                        adult_tax = str('%.2f' % ((tcost * single) * 0.05))
                        adult_fees =  str('%.2f' % (tcost * single))
                        total_cost =  str('%.2f' %  ((tcost * single) + (tcost * single) * 0.05))
                        tax.set(adult_tax)
                        sub_total.set(adult_fees)
                        total.set(total_cost)
                        ticket_class.set("GENERAL")
                        ticket_price.set(adult_fees)
                        child_ticket.set(0)
                        adult_ticket.set(var_10.get())
                        origin.set(var_8.get())
                        destination.set(var_9.get())
                        route_fee.set(total_cost)
                        route.set("DIRECT")

                        x = random.randint(109,5876)
                        random_ref = str(x)
                        receipt_ref.set(random_ref)


                elif (var_1.get() == 1) and (var_11.get() == 1) and (var_4.get() == 1) : # Gen,Child,Single
                        tcost = int(5)
                        single = int(var_12.get())
                        child_tax = str('%.2f' % ((tcost * single) * 0.05))
                        child_fees =  str('%.2f' % (tcost * single))
                        total_cost =  str('%.2f' %  ((tcost * single) + (tcost * single) * 0.05))
                        tax.set(child_tax)
                        sub_total.set(child_fees)
                        total.set(total_cost)
                        ticket_class.set("GENERAL")
                        ticket_price.set(child_fees)
                        child_ticket.set(var_13.get())
                        adult_ticket.set(0)
                        origin.set(var_8.get())
                        destination.set(var_9.get())
                        route_fee.set(total_cost)
                        route.set("DIRECT")

                        x = random.randint(109,5876)
                        random_ref = str(x)
                        receipt_ref.set(random_ref)


                elif  (var_2.get() == 1) and (var_11.get() == 1) and (var_3.get() == 1) and (var_4.get() == 0) : # First,Adult,Single

                        tcost = int(50)
                        single = int(var_12.get())
                        adult_tax = str('%.2f' % ((tcost * single) * 0.05))
                        adult_fees =  str('%.2f' % (tcost * single))
                        total_cost =  str('%.2f' %  ((tcost * single) + (tcost * single) * 0.05))
                        tax.set(adult_tax)
                        sub_total.set(adult_fees)
                        total.set(total_cost)
                        ticket_class.set("FIRST")
                        ticket_price.set(adult_fees)
                        child_ticket.set(0)
                        adult_ticket.set(var_10.get())
                        origin.set(var_8.get())
                        destination.set(var_9.get())
                        route_fee.set(total_cost)
                        route.set("DIRECT")

                        x = random.randint(109,5876)
                        random_ref = str(x)
                        receipt_ref.set(random_ref)


                elif  (var_2.get() == 1) and (var_11.get() == 1) and (var_3.get() == 0) and (var_4.get() == 1) : # First,Child,Single

                        tcost = int(25)
                        single = int(var_12.get())
                        child_tax = str('%.2f' % ((tcost * single) * 0.05))
                        child_fees =  str('%.2f' % (tcost * single))
                        total_cost =  str('%.2f' %  ((tcost * single) + (tcost * single) * 0.05))
                        tax.set(child_tax)
                        sub_total.set(child_fees)
                        total.set(total_cost)
                        ticket_class.set("FIRST")
                        ticket_price.set(child_fees)
                        child_ticket.set(var_13.get())
                        adult_ticket.set(0)
                        origin.set(var_8.get())
                        destination.set(var_9.get())
                        route_fee.set(total_cost)
                        route.set("DIRECT")

                        x = random.randint(109,5876)
                        random_ref = str(x)
                        receipt_ref.set(random_ref)


                elif  (var_1.get() == 1) and (var_5.get() == 1) and (var_3.get() == 1) : # Gen,Adult,Return

                        tcost = int(20)
                        return_1 = int(var_6.get())
                        adult_tax = str('%.2f' % ((tcost * return_1) * 0.05))
                        adult_fees =  str('%.2f' % (tcost * return_1))
                        total_cost =  str('%.2f' %  ((tcost * return_1) + (tcost * return_1) * 0.05))
                        tax.set(adult_tax)
                        sub_total.set(adult_fees)
                        total.set(total_cost)
                        ticket_class.set("GENERAL")
                        ticket_price.set(adult_fees)
                        child_ticket.set(0)
                        adult_ticket.set(var_10.get())
                        origin.set(var_8.get())
                        destination.set(var_9.get())
                        route_fee.set(total_cost)
                        route.set("DIRECT")

                        x = random.randint(109,5876)
                        random_ref = str(x)
                        receipt_ref.set(random_ref)


                elif  (var_1.get() == 1) and (var_5.get() == 1) and (var_4.get() == 1) : # Gen,Child,Return

                        tcost = int(10)
                        return_1 = int(var_6.get())
                        child_tax = str('%.2f' % ((tcost * return_1) * 0.05))
                        child_fees =  str('%.2f' % (tcost * return_1))
                        total_cost =  str('%.2f' %  ((tcost * return_1) + (tcost * return_1) * 0.05))
                        tax.set(child_tax)
                        sub_total.set(child_fees)
                        total.set(total_cost)
                        ticket_class.set("GENERAL")
                        ticket_price.set(child_fees)
                        child_ticket.set(var_13.get())
                        adult_ticket.set(0)
                        origin.set(var_8.get())
                        destination.set(var_9.get())
                        route_fee.set(total_cost)
                        route.set("DIRECT")

                        x = random.randint(109,5876)
                        random_ref = str(x)
                        receipt_ref.set(random_ref)


                elif  (var_2.get() == 1) and (var_5.get() == 1) and (var_3.get() == 1) : # Fist,Adult,Return

                        tcost = int(100)
                        return_1 = int(var_6.get())
                        adult_tax = str('%.2f' % ((tcost * return_1) * 0.05))
                        adult_fees =  str('%.2f' % (tcost * return_1))
                        total_cost =  str('%.2f' %  ((tcost * return_1) + (tcost * return_1) * 0.05))
                        tax.set(adult_tax)
                        sub_total.set(adult_fees)
                        total.set(total_cost)
                        ticket_class.set("FIRST")
                        ticket_price.set(adult_fees)
                        child_ticket.set(0)
                        adult_ticket.set(var_10.get())
                        origin.set(var_8.get())
                        destination.set(var_9.get())
                        route_fee.set(total_cost)
                        route.set("DIRECT")

                        x = random.randint(109,5876)
                        random_ref = str(x)
                        receipt_ref.set(random_ref)


                elif  (var_2.get() == 1) and (var_5.get() == 1) and (var_4.get() == 1) : # First,Child,Return

                        
                        tcost = int(50)
                        return_1 = int(var_6.get())
                        child_tax = str('%.2f' % ((tcost * return_1) * 0.05))
                        child_fees =  str('%.2f' % (tcost * return_1))
                        total_cost =  str('%.2f' %  ((tcost * return_1) + (tcost * return_1) * 0.05))
                        tax.set(child_tax)
                        sub_total.set(child_fees)
                        total.set(total_cost)
                        ticket_class.set("FIRST")
                        ticket_price.set(child_fees)
                        child_ticket.set(var_13.get())
                        adult_ticket.set(0)
                        origin.set(var_8.get())
                        destination.set(var_9.get())
                        route_fee.set(total_cost)
                        route.set("DIRECT")

                        x = random.randint(109,5876)
                        random_ref = str(x)
                        receipt_ref.set(random_ref)




            if 0  < var_7.get() <= 3 :
 
                if  (var_1.get() == 1) and (var_11.get() == 1) and (var_3.get() == 1) : # Gen,Adult,Single
                    tcost = int(5)
                    single = int(var_12.get())
                    adult_tax = str('%.2f' % ((tcost * single) * 0.05))
                    adult_fees =  str('%.2f' % (tcost * single))
                    total_cost =  str('%.2f' %  ((tcost * single) + (tcost * single) * 0.05))
                    tax.set(adult_tax)
                    sub_total.set(adult_fees)
                    total.set(total_cost)
                    ticket_class.set("GENERAL")
                    ticket_price.set(adult_fees)
                    child_ticket.set(0)
                    adult_ticket.set(var_10.get())
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                elif (var_1.get() == 1) and (var_11.get() == 1) and (var_4.get() == 1) : # Gen,Child,Single
                    tcost = float(2.5)
                    single = int(var_12.get())
                    child_tax = str('%.2f' % ((tcost * single) * 0.05))
                    child_fees =  str('%.2f' % (tcost * single))
                    total_cost =  str('%.2f' %  ((tcost * single) + (tcost * single) * 0.05))
                    tax.set(child_tax)
                    sub_total.set(child_fees)
                    total.set(total_cost)
                    ticket_class.set("GENERAL")
                    ticket_price.set(child_fees)
                    child_ticket.set(var_13.get())
                    adult_ticket.set(0)
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                

                elif  (var_2.get() == 1) and (var_11.get() == 1) and (var_3.get() == 1) and (var_4.get() == 0) : # First,Adult,Single

                    tcost = int(25)
                    single = int(var_12.get())
                    adult_tax = str('%.2f' % ((tcost * single) * 0.05))
                    adult_fees =  str('%.2f' % (tcost * single))
                    total_cost =  str('%.2f' %  ((tcost * single) + (tcost * single) * 0.05))
                    tax.set(adult_tax)
                    sub_total.set(adult_fees)
                    total.set(total_cost)
                    ticket_class.set("FIRST")
                    ticket_price.set(adult_fees)
                    child_ticket.set(0)
                    adult_ticket.set(var_10.get())
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                elif  (var_2.get() == 1) and (var_11.get() == 1) and (var_3.get() == 0) and (var_4.get() == 1) : # First,Child,Single

                    tcost = float(12.5)
                    single = int(var_12.get())
                    child_tax = str('%.2f' % ((tcost * single) * 0.05))
                    child_fees =  str('%.2f' % (tcost * single))
                    total_cost =  str('%.2f' %  ((tcost * single) + (tcost * single) * 0.05))
                    tax.set(child_tax)
                    sub_total.set(child_fees)
                    total.set(total_cost)
                    ticket_class.set("FIRST")
                    ticket_price.set(child_fees)
                    child_ticket.set(var_13.get())
                    adult_ticket.set(0)
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                   
                elif  (var_1.get() == 1) and (var_5.get() == 1) and (var_3.get() == 1) : # Gen,Adult,Return

                    tcost = int(10)
                    return_1 = int(var_6.get())
                    adult_tax = str('%.2f' % ((tcost * return_1) * 0.05))
                    adult_fees =  str('%.2f' % (tcost * return_1))
                    total_cost =  str('%.2f' %  ((tcost * return_1) + (tcost * return_1) * 0.05))
                    tax.set(adult_tax)
                    sub_total.set(adult_fees)
                    total.set(total_cost)
                    ticket_class.set("GENERAL")
                    ticket_price.set(adult_fees)
                    child_ticket.set(0)
                    adult_ticket.set(var_10.get())
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                elif  (var_1.get() == 1) and (var_5.get() == 1) and (var_4.get() == 1) : # Gen,Child,Return

                    tcost = int(5)
                    return_1 = int(var_6.get())
                    child_tax = str('%.2f' % ((tcost * return_1) * 0.05))
                    child_fees =  str('%.2f' % (tcost * return_1))
                    total_cost =  str('%.2f' %  ((tcost * return_1) + (tcost * return_1) * 0.05))
                    tax.set(child_tax)
                    sub_total.set(child_fees)
                    total.set(total_cost)
                    ticket_class.set("GENERAL")
                    ticket_price.set(child_fees)
                    child_ticket.set(var_13.get())
                    adult_ticket.set(0)
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                    

                elif  (var_2.get() == 1) and (var_5.get() == 1) and (var_3.get() == 1) : # Fist,Adult,Return

                    tcost = int(50)
                    return_1 = int(var_6.get())
                    adult_tax = str('%.2f' % ((tcost * return_1) * 0.05))
                    adult_fees =  str('%.2f' % (tcost * return_1))
                    total_cost =  str('%.2f' %  ((tcost * return_1) + (tcost * return_1) * 0.05))
                    tax.set(adult_tax)
                    sub_total.set(adult_fees)
                    total.set(total_cost)
                    ticket_class.set("FIRST")
                    ticket_price.set(adult_fees)
                    child_ticket.set(0)
                    adult_ticket.set(var_10.get())
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)


                elif  (var_2.get() == 1) and (var_5.get() == 1) and (var_4.get() == 1) : # First,Child,Return

                    
                    tcost = int(25)
                    return_1 = int(var_6.get())
                    child_tax = str('%.2f' % ((tcost * return_1) * 0.05))
                    child_fees =  str('%.2f' % (tcost * return_1))
                    total_cost =  str('%.2f' %  ((tcost * return_1) + (tcost * return_1) * 0.05))
                    tax.set(child_tax)
                    sub_total.set(child_fees)
                    total.set(total_cost)
                    ticket_class.set("FIRST")
                    ticket_price.set(child_fees)
                    child_ticket.set(var_13.get())
                    adult_ticket.set(0)
                    origin.set(var_8.get())
                    destination.set(var_9.get())
                    route_fee.set(total_cost)
                    route.set("DIRECT")

                    x = random.randint(109,5876)
                    random_ref = str(x)
                    receipt_ref.set(random_ref)
        ################################################################################################################

        #################################### RECEIPT, CLASS, TICKET, ADULT, CHILD LABELS############################################################################
        receipt_title_lb = Label (top_right_frame, font = ('Helvetica',18,'bold'), bg = "beige", fg = 'maroon',  text = "TICKET RECEIPT", width = 40, padx = 4, justify = CENTER)
        receipt_title_lb.grid(row = 0 , column = 0)

        class_1_lb_1 = Label (bottom_right_frame, font = ('Helvetica',14,'bold'), bg = 'beige', fg = 'maroon', text = "CLASS", width = 9, relief = 'sunken', justify = CENTER)
        class_1_lb_1.grid(row = 0 , column = 0)

        class_2_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), textvariable = ticket_class, width = 9, relief = 'sunken', justify = CENTER)
        class_2_lb_1.grid(row = 1 , column = 0)

        ticket_1_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), bg = 'beige', fg = 'maroon', text = "TICKET", width = 9, relief = 'sunken', justify = CENTER)
        ticket_1_lb_1.grid(row = 0 , column = 1)

        ticket_2_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), textvariable = ticket_price, width = 9, relief = 'sunken', justify = CENTER)
        ticket_2_lb_1.grid(row = 1 , column = 1)

        adult_1_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), bg = 'beige', fg = 'maroon', text = "ADULT", width = 9, relief = 'sunken', justify = CENTER)
        adult_1_lb_1.grid(row = 0 , column = 2)

        adult_2_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), textvariable = adult_ticket, width = 9, relief = 'sunken', justify = CENTER)
        adult_2_lb_1.grid(row = 1 , column = 2)

        child_1_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), bg = 'beige', fg = 'maroon', text = "CHILD", width = 9, relief = 'sunken', justify = CENTER)
        child_1_lb_1.grid(row = 0 , column = 3)

        child_2_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), textvariable = child_ticket, width = 9, relief = 'sunken', justify = CENTER)
        child_2_lb_1.grid(row = 1 , column = 3)
        ################################################################################################################

        ################################################## SEPARATION LABEL ##############################################################
        lb_1_sb = Label (bottom_right_frame, font = ('Helvetica',14,'bold'), bg = 'maroon', width = 54, height = 2, relief = 'sunken')
        lb_1_sb.grid(row = 2, column = 0 , columnspan = 4)
        ################################################################################################################

        ############################################### ORIGIN LABEL #################################################################
        origin_1_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), bg = 'beige', fg = 'maroon', text = "FROM", width = 9, relief = 'sunken', justify = CENTER)
        origin_1_lb_1.grid(row = 3, column = 1)

        origin_2_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), textvariable = origin, width = 9, relief = 'sunken', justify = CENTER)
        origin_2_lb_1.grid(row = 3, column = 2)
        ################################################################################################################

        ############################################### DESTINATION, PRICE LABEL #################################################################
        destination_1_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), bg = 'beige', fg = 'maroon', text = "TO", width = 9, relief = 'sunken', justify = CENTER)
        destination_1_lb_1.grid(row = 4, column = 1)

        destination_2_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), textvariable = destination, width = 9, relief = 'sunken', justify = CENTER)
        destination_2_lb_1.grid(row = 4, column = 2)

        price_1_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), bg = 'beige', fg = 'maroon', text = "PRICE", width = 9, relief = 'sunken', justify = CENTER)
        price_1_lb_1.grid(row = 5, column = 1)

        price_2_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), textvariable = route_fee, width = 9, relief = 'sunken', justify = CENTER)
        price_2_lb_1.grid(row = 5, column = 2)
        ################################################################################################################

        ################################################### SEPARATION LABEL #############################################################
        lb_2_sb = Label (bottom_right_frame, font = ('Helvetica',14,'bold'), bg = 'maroon', width = 54, height = 2, relief = 'sunken')
        lb_2_sb.grid(row = 6, column = 0 , columnspan = 4)
        ################################################################################################################

        #############################################REFERENCE, TIME, DATE, ROUTE LABELS###################################################################
        ref_1_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), bg = 'beige', fg = 'maroon', text = "Ref No", width = 9, relief = 'sunken', justify = CENTER)
        ref_1_lb_1.grid(row = 7, column = 0)

        ref_2_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), textvariable = receipt_ref, width = 9, relief = 'sunken', justify = CENTER)
        ref_2_lb_1.grid(row = 8, column = 0)

        time_1_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), bg = 'beige', fg = 'maroon', text = "TIME", width = 9, relief = 'sunken', justify = CENTER)
        time_1_lb_1.grid(row = 7, column = 1)

        time_2_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), textvariable = time_1, width = 9, relief = 'sunken', justify = CENTER)
        time_2_lb_1.grid(row = 8, column = 1)

        date_1_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), bg = 'beige', fg = 'maroon', text = "DATE", width = 9, relief = 'sunken', justify = CENTER)
        date_1_lb_1.grid(row = 7, column = 2)

        date_2_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), textvariable = date_1, width = 9, relief = 'sunken', justify = CENTER)
        date_2_lb_1.grid(row = 8, column = 2)

        route_1_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), bg = 'beige', fg = 'maroon', text = "ROUTE", width = 9, relief = 'sunken', justify = CENTER)
        route_1_lb_1.grid(row = 7, column = 3)

        route_2_lb_1= Label (bottom_right_frame, font = ('Helvetica',14,'bold'), textvariable = route, width = 9, relief = 'sunken', justify = CENTER)
        route_2_lb_1.grid(row = 8, column = 3)
        ################################################################################################################

        ######################################### DATE & TIME FORMAT #######################################################################
        date_1.set(time.strftime("%d-%m-%y"))
        time_1.set(time.strftime("%H:%M:%S"))
        ################################################################################################################
        
        ########################################################## BUTTONS ######################################################
        total_btn = Button (bottom_right_frame, font = ('Helvetica',14,'bold'), fg = 'green', text = "TOTAL", width = 9, height = 1, padx = 2, pady = 20, bd = 2, command = total_btn)
        total_btn.grid(row = 10, column = 0)

        clear_btn = Button (bottom_right_frame, font = ('Helvetica',14,'bold'), fg = 'blue', text = "CLEAR", width = 9, height = 1, padx = 2, pady = 20, bd = 2, command = clear)
        clear_btn.grid(row = 10, column = 1)

        print_btn = Button (bottom_right_frame, font = ('Helvetica',14,'bold'), fg = 'grey', text = "PRINT", width = 9, height = 1, padx = 2, pady = 20, bd = 2,command = print_1)
        print_btn.grid(row = 10, column = 2)

        exit_btn = Button (bottom_right_frame, font = ('Helvetica',14,'bold'), fg = 'red', text = "EXIT", width = 9, height = 1, padx = 2, pady = 20, bd = 2, command = a_exit)
        exit_btn.grid(row = 10, column = 3)
        ################################################################################################################

        ################################################ CLASS LABEL & CHECKBOXES ################################################################
        class_lbl = Label (top_left_1,font = ('Helvetica',22,'bold'), text = "CLASS", bg = "beige", fg = 'maroon', bd = 8, justify = 'center')
        class_lbl.grid(row = 0, column = 0)

        chk_general = Checkbutton (top_left_1, font = ('Helvetica',20,'bold'), text = "GENERAL", height = 3, bg = "beige", fg = 'maroon', variable = var_1, onvalue = 1, offvalue = 0)
        chk_general.grid(row = 1, column = 0, sticky = W)

        chk_first = Checkbutton (top_left_1, font = ('Helvetica',20,'bold'), text = "FIRST", height = 3, bg = "beige", fg = 'maroon', variable = var_2, onvalue = 1, offvalue = 0)
        chk_first.grid(row = 2, column = 0, sticky = W)
        ################################################################################################################

        ############################################## ROUTE LABEL, COMBO & CHECK BOXES ##################################################################
        select_lbl = Label (top_left_3,font = ('Helvetica',22,'bold'), text = "ROUTE DETAILS", bg = "beige", fg = 'maroon', bd = 8, justify = 'center')
        select_lbl.grid(row = 0, column = 0, sticky = W)

        origin_lbl = Label (top_left_3,font = ('Helvetica',16,'bold'), text = "SELECT SOURCE", bg = "beige", fg = 'maroon', bd = 8, justify = 'center')
        origin_lbl.grid(row = 1, column = 0, sticky = W)

        origin_com_box = ttk.Combobox(top_left_3, textvariable = var_8, font = ('Helvetica',13,'bold'), state = 'readonly', width = 8)
        origin_com_box ['value'] = [' ', 'THANE', 'DIGHE', 'AIROLI', 'RABALE', 'GHANSOLI', 'KOPAR KHAIRANE', 'TURBHE', 'SANPADA', 'VASHI', 'JUINAGAR', 'NERUL', 'SEAWOODS', 'CBD BELAPUR', 'KHARGHAR', 'MANSOROVAR', 'KHANDESHWAR', 'PANVEL']
        origin_com_box.current(0)
        origin_com_box.grid(row = 1, column = 1)

        destination_lbl = Label (top_left_3,font = ('Helvetica',16,'bold'), text = "SELECT DESTINATION", bg = "beige", fg = 'maroon', bd = 8, justify = 'center')
        destination_lbl.grid(row = 2, column = 0, sticky = W)

        dest_com_box = ttk.Combobox(top_left_3, textvariable = var_9, font = ('Helvetica',13,'bold'), state = 'readonly', width = 8)
        dest_com_box ['value'] = [' ', 'THANE', 'DIGHE', 'AIROLI', 'RABALE', 'GHANSOLI', 'KOPAR KHAIRANE', 'TURBHE', 'SANPADA', 'VASHI', 'JUINAGAR', 'NERUL', 'SEAWOODS', 'CBD BELAPUR', 'KHARGHAR', 'MANSOROVAR', 'KHANDESHWAR', 'PANVEL']
        dest_com_box.current(0)
        dest_com_box.grid(row = 2, column = 1)
        
        chk_adult = Checkbutton (top_left_3, font = ('Helvetica',16,'bold'), text = "ADULT",  bg = "beige", fg = 'maroon', variable = var_3, onvalue = 1, offvalue = 0)
        chk_adult.grid(row = 3, column = 0, sticky = W)
        adult_ent = Entry (top_left_3, font = ('Helvetica',15,'bold'), textvariable = var_10, width = 10).grid(row = 3, column = 1, sticky = W) 

        chk_child = Checkbutton (top_left_3, font = ('Helvetica',16,'bold'), text = "CHILD",  bg = "beige", fg = 'maroon', variable = var_4, onvalue = 1, offvalue = 0)
        chk_child.grid(row = 4, column = 0, sticky = W)
        child_ent = Entry (top_left_3, font = ('Helvetica',15,'bold'), textvariable = var_13, width = 10).grid(row = 4, column = 1, sticky = W) 
        ################################################################################################################

        ################################################ TICKET LABEL & CHECK BOXES ################################################################
        ticket_type_lbl = Label (top_left_2,font = ('Helvetica',22,'bold'), text = "TICKET TYPE", bg = "beige", fg = 'maroon', bd = 8, justify = 'center')
        ticket_type_lbl.grid(row = 0, column = 0, sticky = W)

        distance_lbl = Label (top_left_2,font = ('Helvetica',22,'bold'), text = "DISTANCE", bg = "beige", fg = 'maroon', bd = 8, justify = 'center')
        distance_lbl.grid(row = 1, column = 0, sticky = W)

        distance_ent = Entry (top_left_2, font = ('Helvetica',15,'bold'), textvariable = var_7, width = 11).grid(row = 1, column = 1, sticky = W) 


        chk_single = Checkbutton (top_left_2, font = ('Helvetica',20,'bold'), text = "SINGLE", height = 2, bg = "beige", fg = 'maroon', variable = var_11, onvalue = 1, offvalue = 0)
        chk_single.grid(row = 2, column = 0, sticky = W)
        single_ent = Entry (top_left_2, font = ('Helvetica',15,'bold'), textvariable = var_12, width = 11).grid(row = 2, column = 1, sticky = W) 

        chk_return = Checkbutton (top_left_2, font = ('Helvetica',20,'bold'), text = "RETURN", height = 2, bg = "beige", fg = 'maroon', variable = var_5, onvalue = 1, offvalue = 0)
        chk_return.grid(row = 3, column = 0, sticky = W)
        return_ent = Entry (top_left_2, font = ('Helvetica',15,'bold'), textvariable = var_6, width = 11).grid(row = 3, column = 1, sticky = W) 
        ################################################################################################################

        ########################################## TAX & TOTAL LABELS ######################################################################
        tax_lbl = Label (bottom_left_1,font = ('Helvetica',22,'bold'), text = "GST", height = 3, bg = "beige", fg = 'maroon', bd = 8, justify = 'center')
        tax_lbl.grid(row = 0, column = 0, sticky = W)
        tax_lbl_ent =  Entry (bottom_left_1, font = ('Helvetica',15,'bold'), textvariable = tax, width = 28).grid(row = 0, column = 1, sticky = W)

        sub_total_lbl = Label (bottom_left_1,font = ('Helvetica',22,'bold'), text = "SUB TOTAL", height = 3, bg = "beige", fg = 'maroon', bd = 8, justify = 'center')
        sub_total_lbl.grid(row = 1, column = 0, sticky = W)
        sub_total_lbl_ent =  Entry (bottom_left_1, font = ('Helvetica',15,'bold'), textvariable = sub_total, width = 28).grid(row = 1, column = 1, sticky = W) 

        total_lbl_1 = Label (bottom_left_1,font = ('Helvetica',22,'bold'), text = "TOTAL", height = 3, bg = "beige", fg = 'maroon', bd = 8, justify = 'center')
        total_lbl_1.grid(row = 2, column = 0, sticky = W)
        total_lbl_1_ent =  Entry (bottom_left_1, font = ('Helvetica',15,'bold'), textvariable = total, width = 28).grid(row = 2, column = 1, sticky = W) 
        ################################################################################################################

        ############################################## CALCULATOR ##################################################################
        self.txt_display_ent =  Entry (bottom_left_2, font = ('Helvetica',15,'bold'), textvariable = text_input, bd = 5, insertwidth = 4, justify = 'right').grid(columnspan = 4)

        self.btn_7 = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '7', command = lambda : btnclick(7)).grid(row = 1 , column = 0)  

        self.btn_8 = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '8', command = lambda : btnclick(8)).grid(row = 1 , column = 1)

        self.btn_9 = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '9', command = lambda : btnclick(9)).grid(row = 1 , column = 2)

        addition = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '+', command = lambda : btnclick("+")).grid(row = 1 , column = 3)


        self.btn_4 = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '4', command = lambda : btnclick(4)).grid(row = 3 , column = 0)

        self.btn_5 = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '5', command = lambda : btnclick(5)).grid(row = 3 , column = 1)

        self.btn_6 = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '6', command = lambda : btnclick(6)).grid(row = 3 , column = 2)

        subtraction = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '-', command = lambda : btnclick("-")).grid(row = 3 , column = 3)


        self.btn_1 = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '1', command = lambda : btnclick(1)).grid(row = 4 , column = 0)

        self.btn_2 = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '2', command = lambda : btnclick(2)).grid(row = 4 , column = 1)

        self.btn_3 = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '3', command = lambda : btnclick(3)).grid(row = 4 , column = 2)

        multiplication = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = 'X', command = lambda : btnclick("*")).grid(row = 4 , column = 3)


        self.btn_0 = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '0', command = lambda : btnclick(0)).grid(row = 5 , column = 0)

        self.btn_clear = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = 'C', command = clear_display).grid(row = 5 , column = 1)

        self.btn_equals = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '=', command = equals_btn).grid(row = 5 , column = 2)

        self.division = Button (bottom_left_2, height = 3, padx = 6, pady = 5, bd = 2, fg = 'black', font = ('Helvetica',15,'bold'), width = 4, text = '/', command = lambda : btnclick("/")).grid(row = 5 , column = 3)
        ################################################################################################################


if __name__ == '__main__' :

    main()

    

    
    
