import customtkinter as ctk

root = ctk.CTk()
root.geometry("750x550")
root.title("This is a custom design")

ctk.set_appearance_mode("dark")

title_label = ctk.CTkLabel(root, text="Project Ideas", font=ctk.CTkFont(size=30))
title_label.pack(padx=10, pady=(40, 20))

frame = ctk.CTkFrame(root)
frame.pack(fill="x", padx=100)

language_frame = ctk.CTkFrame(frame)
language_frame.pack(padx=100, pady=(20, 5), fill="both")

language_label = ctk.CTkLabel(language_frame, text="Programming Language", font=ctk.CTkFont(weight="bold"))
language_label.pack()
language_dropdown = ctk.CTkComboBox(language_frame, values=["Python", "Java", "C++", "A.I"])
language_label.pack(pady=10)

difficulty_frame = ctk.CTkFrame(frame)
difficulty_frame.pack(padx=100, pady=5, fill="both")
difficulty_label = ctk.CTkLabel(difficulty_frame, text="Project Difficulty", font=ctk.CTkFont(weight="bold"))
difficulty_label.pack()

difficulty_value = ctk.StringVar(value="Easy")
radiobutton1 = ctk.CTkRadioButton(difficulty_frame, text="Easy", variable=difficulty_value, value="Easy")
radiobutton1.pack(side="left", padx=(10, 20), pady=10)
radiobutton2 = ctk.CTkRadioButton(difficulty_frame, text="Medium", variable=difficulty_value, vaule="Medium")
radiobutton2.pack(side="left", padx=(10, 20), pady=10)
radiobutton3 = ctk.CTkRadioButton(difficulty_frame, text="Hard", variable=difficulty_value, value="Hard")
radiobutton3.pack(side="left", padx=(10, 20), pady=10)

features_frame = ctk.CTkFrame(frame)
features_frame.pack(padx=100, pady=5, fill="both")
features_label = ctk.CTkLabel(features_frame, text="Features", font=ctk.CTkFont(weight="bold"))
features_label.pack()
checkbox1 = ctk.CTkCheckBox(features_frame, text="Database")
checkbox1.pack(side="left", padx=50, pady=10)
checkbox1 = ctk.CTkCheckBox(features_frame, text="API")
checkbox1.pack(side="left", padx=50, pady=10)

button = ctk.CTkButton(frame, text="Generate")
button.pack(pady=10, fill="x", padx=100)

result = ctk.CTkTextbox(root, font=ctk.CTkFont(size=15))
result.pack(pady=10, fill="x", padx=100)
root.mainloop()