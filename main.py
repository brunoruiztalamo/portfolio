#Importando "Tkinter". El primer paso es el comando "pip install customtkinter"
#El segundo paso es importarlo desde el codigo
import customtkinter

#Seteando el "modo de apariencia" y "color scheme para Dark Mode"
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Definiendo el elemento raiz (root element)
root = customtkinter.CTk()
root.geometry("500x350")


def login():
    print("Logged In Succesfully!")
    

#Haciendo los botones y declarando el padding con padx y pady
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)


#Agregando labels para que ponga datos, buttons y una checkbox que diga "Remember Me"
label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)    
 
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()

       



