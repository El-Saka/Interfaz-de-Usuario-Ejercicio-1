import tkinter as tk

class RadioButtonList(tk.Frame):
    def __init__(self, parent, options):
        super().__init__(parent)
        self.options = options
        self.selected_option = tk.StringVar(value="")

        for option in self.options:
            rb = tk.Radiobutton(self, text=option, variable=self.selected_option, value=option, command=self.update_selection)
            rb.pack(anchor="w")

        reset_button = tk.Button(self, text="Reset", command=self.reset_selection)
        reset_button.pack(side="bottom", pady=(10,0))

    def update_selection(self):
        print(f"Selected option: {self.selected_option.get()}")

    def reset_selection(self):
        self.selected_option.set("")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Radio Button List")

    options = ["Option 1", "Option 2", "Option 3"]
    rbl = RadioButtonList(root, options)
    rbl.pack(padx=20, pady=20)

    root.mainloop()
