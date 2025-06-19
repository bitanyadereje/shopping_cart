import tkinter as tk
from tkinter import messagebox
from cart import ShoppingCart

# Create cart service instance
cart = ShoppingCart()

# ===== Functions =====

def add_item():
    name = entry_name.get().strip()
    try:
        price = float(entry_price.get())
        quantity = int(entry_quantity.get())
        if price <= 0 or quantity <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Enter a valid positive price and quantity.")
        return

    cart.add_item(name, price, quantity)
    update_cart()
    clear_inputs()

def remove_item():
    name = entry_name.get().strip()
    if name in cart.items:
        cart.remove_item(name)
        update_cart()
        clear_inputs()
    else:
        messagebox.showinfo("Not Found", f"No item named '{name}' in cart.")

def update_item():
    name = entry_name.get().strip()
    try:
        price = float(entry_price.get())
        quantity = int(entry_quantity.get())
        if price <= 0 or quantity <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Enter a valid positive price and quantity.")
        return

    if name in cart.items:
        # Update price and quantity
        cart.items[name] = {'item': cart.items[name]['item'], 'quantity': quantity}
        cart.items[name]['item'].price = price
        update_cart()
        clear_inputs()
    else:
        messagebox.showinfo("Not Found", f"No item named '{name}' in cart.")

def clear_cart():
    cart.items = {}  # Reset cart dictionary
    update_cart()
    messagebox.showinfo("Cart Cleared", "You checked out. Thank you!")

def update_cart():
    cart_list.delete(0, tk.END)
    for name, data in cart.get_cart().items():
        cart_list.insert(tk.END, f"{name} - {data['quantity']} × ${data['price']:.2f}")
    total_label.config(text=f"Total: ${cart.calculate_total():.2f}")

def clear_inputs():
    entry_name.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)

# ===== GUI Layout =====

root = tk.Tk()
root.title("🛒 Shopping Cart Service")
root.geometry("480x420")
root.resizable(False, False)


tk.Label(root, text="Item Name").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

tk.Label(root, text="Price").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_price = tk.Entry(root, width=30)
entry_price.grid(row=1, column=1, padx=10, pady=5, columnspan=2)

tk.Label(root, text="Quantity").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_quantity = tk.Entry(root, width=30)
entry_quantity.grid(row=2, column=1, padx=10, pady=5, columnspan=2)


tk.Button(root, text="Add Item", width=15, command=add_item).grid(row=3, column=0, pady=10)
tk.Button(root, text="Remove Item", width=15, command=remove_item).grid(row=3, column=1, pady=10)
tk.Button(root, text="Update Item", width=15, command=update_item).grid(row=3, column=2, pady=10)


tk.Button(root, text="Checkout / Clear Cart", width=48, bg="lightgray", command=clear_cart).grid(row=4, column=0, columnspan=3, pady=5)

# Cart list display
cart_list = tk.Listbox(root, width=65, height=10)
cart_list.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Total display
total_label = tk.Label(root, text="Total: $0.00", font=("Helvetica", 12, "bold"))
total_label.grid(row=6, column=0, columnspan=3, pady=5)

root.mainloop()
