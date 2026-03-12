import customtkinter as ctk

# Configuração da Janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Dashboard 7ª B")
app.geometry("1000x700")

# Título Principal
label = ctk.CTkLabel(app, text="DASHBOARD ULTRA 7ª B", font=("Outfit", 30, "bold"), text_color="#ff3e3e")
label.pack(pady=40)

# Card de Exemplo (Simulando o seu HTML)
card = ctk.CTkFrame(app, width=800, height=400, corner_radius=20, border_width=2, border_color="#ff3e3e")
card.pack(pady=20, padx=20)

sub_label = ctk.CTkLabel(card, text="Aula em andamento: Matemática", font=("Outfit", 20))
sub_label.place(relx=0.5, rely=0.4, anchor="center")

app.mainloop()
