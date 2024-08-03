import tkinter as tk

def calculate_billing():
    # Input Data
    unit_amount = float(unit_amount_entry.get())
    boi_amount = float(unit_BOI_entry.get())
    container_40 = float(container_40_entry.get())
    container_20 = float(container_20_entry.get())
    entries = float(entries_entry.get())
    over = float(over_entry.get())
    amend = float(amend_entry.get())

    # Algorithms
    multiplier = 1091.50
    multiplier_boi = 3068

    unit_a = unit_amount * multiplier
    boi_a = boi_amount * multiplier_boi
    sms_a = unit_amount + boi_amount

    result_40 = float(container_40) * 2920.50
    result_20 = float(container_20) * 2655

    enter = 90
    hand = 1750
    handsum = sms_a * hand

    vat = (100 + 18) / 100

    hrate = 1750
    hvat = 18
    hsum = hvat / 100
    hsum1 = hsum * handsum
    
    # Results
    result = unit_a + boi_a
    formatted_result = "{:,.2f}".format(result)
    result_con = result_40 + result_20
    formatted_result_con = "{:,.2f}".format(result_con)
    result_sms = sms_a * 3.54
    formatted_result_sms = "{:,.2f}".format(result_sms)
    formatted_result_over = "{:,.2f}".format(over)    
    result_enter = entries * enter
    formatted_result_enter = "{:,.2f}".format(result_enter)
    result_handling = sms_a * hand
    formatted_result_hand = "{:,.2f}".format(result_handling)
    formatted_result_amend = "{:,.2f}".format(amend)

    trico = (result + result_con) + (result_sms + over)
    trico_rs = "{:,.2f}".format(trico)
    gfm = result_enter + result_handling + amend
    gfm_rs = "{:,.2f}".format(gfm)
    tv = trico / vat
    tv_rs = "{:,.2f}".format(tv)
    vatout = trico - tv
    vatout_rs = "{:,.2f}".format(vatout)

    han1 = handsum + hsum1 + result_enter - hsum1
    han1_rs = "{:,.2f}".format(han1)
    han2 = hsum1
    han2_rs = "{:,.2f}".format(han2)
    han3 = handsum + hsum1 + result_enter
    han3_rs = "{:,.2f}".format(han3)
    
      
    # Output Data
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "\n""                 TRICO INVOICE ""\n\n")
    output_text.insert(tk.END, "  Total Value of units is   : Rs. " + formatted_result + "\n")
    output_text.insert(tk.END, "  Value of total Containers : Rs. " + formatted_result_con + "\n")
    output_text.insert(tk.END, "  Total SMS Value           : Rs. " + formatted_result_sms + "\n")
    output_text.insert(tk.END, "  Total Entrie Value        : Rs. " + formatted_result_enter + "\n")
    output_text.insert(tk.END, "  Total Handling Charge     : Rs. " + formatted_result_hand + "\n")
    output_text.insert(tk.END, "  Total Over Charge         : Rs. " + formatted_result_over + "\n")
    output_text.insert(tk.END, "  Total Amendment Charge    : Rs. " + formatted_result_amend + "\n")
    output_text.insert(tk.END, "\n""                  GFM AMOUNT ""\n")
    output_text.insert(tk.END, "     Handling Amount    = Rs. " + han1_rs + "\n")
    output_text.insert(tk.END, "     H VAT Amount       = Rs. " + han2_rs + "\n")
    output_text.insert(tk.END, "     TOTAL GFM AMOUNT   = Rs. " + han3_rs + "\n")
    output_text.insert(tk.END, "\n""                 TRICO AMOUNT ""\n")
    output_text.insert(tk.END, "     Trico + VGM Amount = Rs. " + tv_rs + "\n")
    output_text.insert(tk.END, "     VAT Amount         = Rs. " + vatout_rs + "\n")
    output_text.insert(tk.END, "     TOTAL TRICO AMOUNT = Rs. " + trico_rs + "\n\n")

           

def reset():
    # Erase all of the input data and output data
    unit_amount_entry.delete(0, tk.END)
    unit_BOI_entry.delete(0, tk.END)  # Updated variable name
    container_40_entry.delete(0, tk.END)
    container_20_entry.delete(0, tk.END)
    entries_entry.delete(0, tk.END)
    over_entry.delete(0, tk.END)
    amend_entry.delete(0, tk.END)

    output_text.delete("1.0", tk.END)

root = tk.Tk()
root.geometry('530x720')
root.title("Invoice Verfication & Costing")
root.config(bg="gray")
lable = tk.Label(root, text="GFM & TRICO - PAYMENTS", width=900, font=('Helvetica', 18, 'bold'))#Heading
lable.pack(padx=15, pady=20)

# Create a grid frame
grid_frame = tk.Frame(root)
grid_frame.pack()

# Add the labels and input boxes to the grid frame
unit_amount_label = tk.Label(grid_frame, text="(1063.75) Number of UNITS :")
unit_amount_label.grid(row=0, column=0)
unit_amount_entry = tk.Entry(grid_frame)
unit_amount_entry.grid(row=0, column=1)

unit_BOI_label = tk.Label(grid_frame, text="(3068) Number of NON BOI UNITS :")
unit_BOI_label.grid(row=1, column=0)
unit_BOI_entry = tk.Entry(grid_frame)
unit_BOI_entry.grid(row=1, column=1)

container_40_label = tk.Label(grid_frame, text="40ft Containers : ")
container_40_label.grid(row=2, column=0)
container_40_entry = tk.Entry(grid_frame)
container_40_entry.grid(row=2, column=1)

container_20_label = tk.Label(grid_frame, text="20ft Containers : ")
container_20_label.grid(row=3, column=0)
container_20_entry = tk.Entry(grid_frame)
container_20_entry.grid(row=3, column=1)

entries_label = tk.Label(grid_frame, text="Enter Number of ENTRIES : ")
entries_label.grid(row=4, column=0)
entries_entry = tk.Entry(grid_frame)
entries_entry.grid(row=4, column=1)

over_label = tk.Label(grid_frame, text="OVER CHARGE amount : ")
over_label.grid(row=5, column=0)
over_entry = tk.Entry(grid_frame)
over_entry.grid(row=5, column=1)

amend_label = tk.Label(grid_frame, text="AMENDMENT CHARGE amount : ")
amend_label.grid(row=6, column=0)
amend_entry = tk.Entry(grid_frame)
amend_entry.grid(row=6, column=1)

# Calculate Button
calculate_button = tk.Button(root, text="CALCULATE", command=calculate_billing, width=30, font=('Helvetica', 12, 'bold'))
calculate_button.config(bg="Green")
calculate_button.pack(padx=10, pady=10)

reset_button = tk.Button(root, text="RESET", command=reset, width=40)
reset_button.pack(padx=10, pady=10)

# Output Text
output_text = tk.Text(root, height=23, width=50)
output_text.config(bg="light Blue")
output_text.pack()

root.mainloop()
