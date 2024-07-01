

import random
import datetime
import tkinter as tk
from tkinter import messagebox

# Global List Declaration
name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []

# Global Variable Declaration
i = 0

# Function Definitions

def Home():
    root = tk.Tk()
    root.title("Hotel Inlet")
    root.geometry("800x600")
    
    # Set background color for the root window
    root.configure(bg='beige')  # Use any color code you prefer
    
    label = tk.Label(root, text="WELCOME TO HOTEL INLET", font=("Arial", 24), bg='#f0f0f0')  # Match background color
    label.pack(pady=20)

    # Define a frame to contain the buttons for better alignment
    button_frame = tk.Frame(root, bg='#f0f0f0')  # Match background color
    button_frame.pack(pady=20)

    # Define button styles with different colors
    button_style = {
        'padx': 20,
        'pady': 10,
        'width': 20
    }

    # Function to generate a random color for each button
    def generate_random_color():
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))  # Generate random color code
        return color

    # Define buttons with random background colors
    booking_btn = tk.Button(button_frame, text="Booking", command=Booking, **button_style, bg=generate_random_color(), fg='white')
    booking_btn.grid(row=0, column=0, padx=10, pady=10)

    rooms_info_btn = tk.Button(button_frame, text="Rooms Info", command=Rooms_Info, **button_style, bg=generate_random_color(), fg='white')
    rooms_info_btn.grid(row=0, column=1, padx=10, pady=10)

    restaurant_btn = tk.Button(button_frame, text="Room Service (Menu Card)", command=restaurant, **button_style, bg=generate_random_color(), fg='white')
    restaurant_btn.grid(row=1, column=0, padx=10, pady=10)

    payment_btn = tk.Button(button_frame, text="Payment", command=Payment, **button_style, bg=generate_random_color(), fg='white')
    payment_btn.grid(row=1, column=1, padx=10, pady=10)

    record_btn = tk.Button(button_frame, text="Record", command=Record, **button_style, bg=generate_random_color(), fg='white')
    record_btn.grid(row=2, column=0, padx=10, pady=10)

    exit_btn = tk.Button(button_frame, text="Exit", command=root.destroy, **button_style, bg=generate_random_color(), fg='white')
    exit_btn.grid(row=2, column=1, padx=10, pady=10)

    root.mainloop()

def Booking():
    def validate_date(date_str):
        try:
            datetime.datetime.strptime(date_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def submit_booking():
        nonlocal i
        n = name_entry.get().strip()
        p1 = phone_entry.get().strip()
        a = address_entry.get().strip()
        ci = checkin_entry.get().strip()
        co = checkout_entry.get().strip()

        if not all([n, p1, a, ci, co]):
            messagebox.showwarning("Incomplete Information", "Please fill in all fields.")
            return

        if not validate_date(ci) or not validate_date(co):
            messagebox.showwarning("Invalid Date", "Please enter dates in format DD/MM/YYYY.")
            return

        ci = datetime.datetime.strptime(ci, '%d/%m/%Y')
        co = datetime.datetime.strptime(co, '%d/%m/%Y')

        if co <= ci:
            messagebox.showwarning("Invalid Date", "Check-Out date must be after Check-In date.")
            return

        d = (co - ci).days

        room_types = ["Standard Non-AC", "Standard AC", "3-Bed Non-AC", "3-Bed AC"]
        room_prices = [3500, 4000, 4500, 5000]
        selected_room = room_type_var.get()
        room_type = room_types[selected_room]
        room_price = room_prices[selected_room]

        rn = random.randrange(40) + 300
        cid = random.randrange(40) + 10

        while rn in roomno or cid in custid:
            rn = random.randrange(60) + 300
            cid = random.randrange(60) + 10

        name.append(n)
        phno.append(p1)
        add.append(a)
        checkin.append(ci.strftime('%d/%m/%Y'))
        checkout.append(co.strftime('%d/%m/%Y'))
        room.append(room_type)
        price.append(room_price * d)  # Calculate price based on days stayed
        rc.append(0)
        p.append(0)
        roomno.append(rn)
        custid.append(cid)
        day.append(d)

        messagebox.showinfo("Booking Successful", f"Room Booked Successfully!\nRoom No.: {rn}\nCustomer ID: {cid}")

        booking_window.destroy()
        Home()

    booking_window = tk.Toplevel()
    booking_window.title("Booking")
    booking_window.geometry("600x400")

    name_label = tk.Label(booking_window, text="Name:")
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.Entry(booking_window)
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    phone_label = tk.Label(booking_window, text="Phone No.:")
    phone_label.grid(row=1, column=0, padx=10, pady=10)
    phone_entry = tk.Entry(booking_window)
    phone_entry.grid(row=1, column=1, padx=10, pady=10)

    address_label = tk.Label(booking_window, text="Address:")
    address_label.grid(row=2, column=0, padx=10, pady=10)
    address_entry = tk.Entry(booking_window)
    address_entry.grid(row=2, column=1, padx=10, pady=10)

    checkin_label = tk.Label(booking_window, text="Check-In (DD/MM/YYYY):")
    checkin_label.grid(row=3, column=0, padx=10, pady=10)
    checkin_entry = tk.Entry(booking_window)
    checkin_entry.grid(row=3, column=1, padx=10, pady=10)

    checkout_label = tk.Label(booking_window, text="Check-Out (DD/MM/YYYY):")
    checkout_label.grid(row=4, column=0, padx=10, pady=10)
    checkout_entry = tk.Entry(booking_window)
    checkout_entry.grid(row=4, column=1, padx=10, pady=10)

    room_type_var = tk.IntVar()
    room_type_var.set(0)

    room_type_label = tk.Label(booking_window, text="Room Type:")
    room_type_label.grid(row=5, column=0, padx=10, pady=10)

    room_type_options = ["Standard Non-AC - Rs. 3500", "Standard AC - Rs. 4000", "3-Bed Non-AC - Rs. 4500", "3-Bed AC - Rs. 5000"]
    for i, option in enumerate(room_type_options):
        tk.Radiobutton(booking_window, text=option, variable=room_type_var, value=i).grid(row=5, column=i+1, padx=10, pady=10)

    submit_btn = tk.Button(booking_window, text="Submit", command=submit_booking)
    submit_btn.grid(row=6, column=0, columnspan=2, pady=20)

    booking_window.mainloop()

def Rooms_Info():
    rooms_info_window = tk.Toplevel()
    rooms_info_window.title("Rooms Info")
    rooms_info_window.geometry("800x600")

    info_text = """
    HOTEL ROOMS INFO

    STANDARD NON-AC
    ---------------------------------------------------------------
    Room amenities include: 1 Double Bed, Television, Telephone,
    Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and
    an attached washroom with hot/cold water.

    STANDARD AC
    ---------------------------------------------------------------
    Room amenities include: 1 Double Bed, Television, Telephone,
    Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and
    an attached washroom with hot/cold water + Window/Split AC.

    3-BED NON-AC
    ---------------------------------------------------------------
    Room amenities include: 1 Double Bed + 1 Single Bed, Television,
    Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1
    Side table, Balcony with an Accent table with 2 Chair and an
    attached washroom with hot/cold water.

    3-BED AC
    ---------------------------------------------------------------
    Room amenities include: 1 Double Bed + 1 Single Bed, Television,
    Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 
    1 Side table, Balcony with an Accent table with 2 Chair and an
    attached washroom with hot/cold water + Window/Split AC.
    """

    info_label = tk.Label(rooms_info_window, text=info_text, justify=tk.LEFT, padx=20, pady=20, font=("Arial", 12))
    info_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    rooms_info_window.mainloop()

def restaurant():
    def add_to_cart():
        item = menu_listbox.get(tk.ACTIVE)
        selected_items.append(item)
        update_cart()

    def remove_from_cart():
        index = cart_listbox.curselection()
        if index:
            selected_items.pop(index[0])
            update_cart()

    def update_cart():
        cart_listbox.delete(0, tk.END)
        for item in selected_items:
            cart_listbox.insert(tk.END, item)

    restaurant_window = tk.Toplevel()
    restaurant_window.title("Restaurant Menu")
    restaurant_window.geometry("800x600")

    menu_text = """
    HOTEL INLET
    -----------------------------------------------------------------
                             Menu Card
    -----------------------------------------------------------------
     BEVERAGES                       26 Dal Fry................ 140.00
    --------------------------------      27 Dal Makhani............ 150.00
     1  Regular Tea............. 20.00      28 Dal Tadka.............. 150.00
     2  Masala Tea.............. 25.00
     3  Coffee.................. 25.00      ROTI
     4  Cold Drink.............. 25.00     --------------------------------
     5  Bread Butter............ 30.00      29 Plain Roti.............. 15.00
     6  Bread Jam............... 30.00      30 Butter Roti............. 15.00
     7  Veg. Sandwich........... 50.00      31 Tandoori Roti........... 20.00
     8  Veg. Toast Sandwich....     32 Butter Naan............. 20.00
     9  Cheese Toast Sandwich... 70.00
    10 Grilled Sandwich........ 70.00      RICE
                                          --------------------------------
     SOUPS                                  33 Plain Rice.............. 90.00
    --------------------------------      34 Jeera Rice.............. 100.00
    11 Tomato Soup............ 80.00      35 Veg. Pulao.............. 110.00
    12 Veg. Soup.............. 90.00
    13 Sweet Corn Soup........ 90.00      NON-VEG
                                          --------------------------------
     TANDOOR                                 36 Chicken Curry........... 250.00
    --------------------------------         37 Mutton Curry............ 270.00
    14 Paneer Tikka.......... 150.00         38 Chicken Masala.......... 260.00
    15 Tandoori Roti.......... 20.00         39 Mutton Masala........... 280.00
    16 Paneer Masala......... 180.00
    17 Paneer Butter Masala.. 180.00      SWEETS
    18 Paneer Do Pyaza....... 180.00     --------------------------------
    19 Paneer Pasanda........ 190.00      40 Gulab Jamun............. 70.00
                                          41 Kheer.................. 80.00

     CHINESE
    --------------------------------
    20 Manchurian............ 130.00     OTHERS
    21 Fried Rice............ 130.00     --------------------------------
    22 Noodles............... 140.00      42 Pappad................ 15.00
    23 Hong Kong Chicken..... 250.00      43 Mixed Pickle.......... 25.00
    24 Veg. Spring Roll...... 80.00
    25 Non-Veg. Spring Roll.. 90.00
    """

    menu_label = tk.Label(restaurant_window, text=menu_text, justify=tk.LEFT, padx=20, pady=20, font=("Arial", 12))
    menu_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    selected_items = []

    # Listbox for selecting items
    menu_listbox = tk.Listbox(restaurant_window, selectmode=tk.SINGLE, font=("Arial", 12), height=20, width=50)
    menu_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    add_to_cart_btn = tk.Button(restaurant_window, text="Add to Cart", command=add_to_cart)
    add_to_cart_btn.pack()

    remove_from_cart_btn = tk.Button(restaurant_window, text="Remove from Cart", command=remove_from_cart)
    remove_from_cart_btn.pack()

    # Listbox for displaying selected items (cart)
    cart_listbox = tk.Listbox(restaurant_window, selectmode=tk.SINGLE, font=("Arial", 12), height=20, width=50)
    cart_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    restaurant_window.mainloop()

def Payment():
    def pay():
        c = int(cno.get())
        if cno.get() == '':
            messagebox.showwarning("Pay Status", "Please enter card number")
        else:
            messagebox.showinfo("Pay Status", "Your payment is Successful for")
            checkout_window.destroy()
            root.destroy()

    checkout_window = tk.Toplevel()
    checkout_window.title("Payment")
    checkout_window.geometry("600x400")

    pay_lbl = tk.Label(checkout_window, text="Enter card number: ")
    pay_lbl.pack(pady=50)

    cno = tk.Entry(checkout_window)
    cno.pack(pady=50)

    pay_btn = tk.Button(checkout_window, text="pay", command=pay)
    pay_btn.pack(pady=50)

    checkout_window.mainloop()

def Record():
    record_window = tk.Toplevel()
    record_window.title("Record")
    record_window.geometry("800x600")

    for j in range(len(name)):
        record = f"Customer ID: {custid[j]}\nName: {name[j]}\nPhone No.: {phno[j]}\nAddress: {add[j]}\nRoom Type: {room[j]}\nRoom No.: {roomno[j]}\nPrice: Rs. {price[j]}\nCheck-In: {checkin[j]}\nCheck-Out: {checkout[j]}\nDays Stay: {day[j]}\nRestaurant Charges: Rs. {rc[j]}\nPayment: Rs. {p[j]}\n\n"
        record_label = tk.Label(record_window, text=record, font=("Arial", 12))
        record_label.pack(anchor=tk.W)

    record_window.mainloop()

Home()
