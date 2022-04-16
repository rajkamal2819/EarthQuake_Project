from tkinter import *

root = Tk()
root.maxsize(800, 600)
root.minsize(800, 600)
root.title("Realtime EarthQuakes Data")

l1 = Label(root, text="Start Date: ", pady=10, padx=10)
l2 = Label(root, text="End Date: ", pady=10, padx=10)
l3 = Label(root, text="Format (YYYY-MM-DD)", pady=10, padx=10)
l4 = Label(root, text="Location (Optional): ", pady=10, padx=10)
l5 = Label(root, text="Min Magnitude (Optional): ", pady=10, padx=10)
l6 = Label(root, text="Limit (Optional): ", pady=10, padx=10)
startDate = Entry()
startDate.grid(row=0, column=1, pady=10, padx=10)
endDate = Entry()
endDate.grid(row=0, column=3, pady=10, padx=10)
location = Entry()
location.grid(row=1, column=1, pady=10, padx=10)
minMag = Entry()
minMag.grid(row=1, column=3, pady=10, padx=10)
limit = Entry()
limit.grid(row=2, column=1, pady=10, padx=10)
l1.grid(row=0, column=0)
l2.grid(row=0, column=2)
l3.grid(row=0, column=4)
l4.grid(row=1, column=0)
l5.grid(row=1, column=2)
l6.grid(row=2, column=0)




root.mainloop()
