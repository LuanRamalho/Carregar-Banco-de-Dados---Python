import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import sqlite3

def read_sql_file():
    file_path = filedialog.askopenfilename(title="Select SQL File", filetypes=[("SQL Files", "*.sql")])
    if file_path:
        with open(file_path, 'r') as file:
            sql_commands = file.read()
            execute_sql_commands(sql_commands)

def execute_sql_commands(commands):
    # Criar ou conectar ao banco de dados SQLite
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    try:
        # Executar os comandos SQL
        cursor.executescript(commands)
        conn.commit()
        messagebox.showinfo("Success", "SQL commands executed successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        cursor.close()
        conn.close()

def create_gui():
    window = tk.Tk()
    window.title("SQL Reader")
    window.geometry("600x400")
    window.configure(bg="#f0f0f0")

    # Título
    title_label = tk.Label(window, text="SQL Reader", font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#4A90E2")
    title_label.pack(pady=20)

    # Botão para carregar arquivo SQL
    load_button = tk.Button(window, text="Load SQL File", command=read_sql_file, font=("Arial", 14), bg="#4A90E2", fg="white")
    load_button.pack(pady=10)

    # Text area para mostrar os resultados
    result_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Arial", 12), bg="#ffffff", fg="#333333")
    result_area.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
