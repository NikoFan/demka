# import tkinter as tk
# from tkinter import ttk
#
#
# class HistoryFrame(tk.Frame):
#     def __init__(self, parent, sales_data=None):
#         super().__init__(parent)
#
#         title_label = tk.Label(self, text="История реализации продукции", font=("Arial", 16, "bold"))
#         title_label.pack(pady=10)
#
#         table_frame = ttk.Frame(self)
#         table_frame.pack(fill="both", expand=True, padx=20, pady=10)
#
#         columns = ("product_name", "quantity", "sale_date")
#         self.sales_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
#
#         self.sales_table.heading("product_name", text="Наименование продукции")
#         self.sales_table.column("product_name", width=200, anchor="center")
#
#         self.sales_table.heading("quantity", text="Количество")
#         self.sales_table.column("quantity", width=100, anchor="center")
#
#         self.sales_table.heading("sale_date", text="Дата продажи")
#         self.sales_table.column("sale_date", width=150, anchor="center")
#
#         self.sales_table.pack(fill="both", expand=True)
#
#         if sales_data:
#             self.load_sales_data(sales_data)
#
#     def load_sales_data(self, sales_data):
#         for row in self.sales_table.get_children():
#             self.sales_table.delete(row)
#         for sale in sales_data:
#             self.sales_table.insert("", "end", values=(sale["product_name"], sale["quantity"], sale["sale_date"]))


import tkinter as tk
from tkinter import ttk
from db.db import Database

from .current_partner import Partner
class HistoryFrame(tk.Frame):
    def __init__(self, parent, controller, partner_name=None):
        tk.Frame.__init__(self, parent)

        title_label = tk.Label(self, text="История реализации продукции", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0)
        self.partner_name = partner_name
        back_btn = ((ttk.Button(self, text="Обратно",
                                command=lambda: (
                                    controller.open_partner_form())))
                    .grid(row=0, column=1, padx=5, pady=5))
        self.database = Database()

        table_frame = ttk.Frame(self)
        table_frame.grid(row=1, column=0, ipadx=5, ipady=6, padx=5, pady=5, columnspan=2)


        columns = ("product_name", "partner_name", "quantity", "sale_date")
        self.sales_table = ttk.Treeview(table_frame, columns=columns, show="headings", height=20)

        self.sales_table.heading("product_name", text="Продукция")
        self.sales_table.column("product_name", width=150, anchor="center")

        self.sales_table.heading("partner_name", text="Партнер")
        self.sales_table.column("partner_name", width=150, anchor="center")

        self.sales_table.heading("quantity", text="Количество")
        self.sales_table.column("quantity", width=100, anchor="center")

        self.sales_table.heading("sale_date", text="Дата продажи")
        self.sales_table.column("sale_date", width=120, anchor="center")

        self.sales_table.grid(row=2, column=0, ipadx=30, ipady=6, padx=5, pady=5)
        self.grid_columnconfigure(0, weight=2)
        self.rowconfigure(1, weight=2)

        if partner_name:
            self.load_sales_data()

    def load_sales_data(self):
        """Loads sales data into the sales_table for the specified partner."""
        # Clear existing rows in the table
        for row in self.sales_table.get_children():
            self.sales_table.delete(row)

        # Fetch sales data using get_sales_data function
        sales_data = self.database.get_sales_data(Partner.get_name())

        # Insert each entry into the table
        for entry in sales_data:
            self.sales_table.insert(
                "", "end",
                values=(
                    entry["product_name"],
                    entry["partner_name"],
                    entry["quantity"],
                    entry["sale_date"]
                )
            )
