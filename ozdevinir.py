import tkinter as tk
from tkinter import ttk
import re

class PDA:
    def __init__(self):
        self.stack = []

    def is_operator(self, char):
        return char in '+-*/'

    def is_digit(self, char):
        return char.isdigit()

    def is_balanced_expression(self, expression):
        state = 0  # Durum 0: Başlangıç, Durum 1: Rakamdan sonra, Durum 2: Operatörden sonra, Durum 3: '(' sonrası

        for char in expression:
            if state == 0:
                if self.is_digit(char):
                    state = 1
                elif char == '(':
                    self.stack.append(char)
                    state = 3
                else:
                    return False

            elif state == 1:
                if self.is_operator(char):
                    state = 2
                elif char == ')':
                    if not self.stack or self.stack[-1] != '(':
                        return False
                    self.stack.pop()
                    state = 1
                else:
                    return False

            elif state == 2:
                if self.is_digit(char):
                    state = 1
                elif char == '(':
                    self.stack.append(char)
                    state = 3
                else:
                    return False

            elif state == 3:
                if self.is_digit(char):
                    state = 1
                elif char == '(':
                    self.stack.append(char)
                else:
                    return False

        return state == 1 and not self.stack

    def evaluate_expression(self, expression):
        # Operatör önceliği sorununu çözmek için ifadeyi değerlendir
        try:
            # eval fonksiyonunu güvenli bir şekilde kullanmak için sadece belirli karakterlere izin ver
            allowed_chars = re.compile(r'^[0-9+\-*/() ]+$')
            if not allowed_chars.match(expression):
                return "Hata: İfade içinde geçersiz karakterler var."
            result = eval(expression)
            return result
        except Exception as e:
            return f"Hata: {str(e)}"

class PDAGUI:
    def __init__(self, root):
        self.pda = PDA()

        self.root = root
        self.root.title("PDA Matematiksel İfade Kontrolü")
        self.root.geometry("500x400")
        self.root.configure(bg='#2C3E50')

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#2C3E50')
        self.style.configure('TLabel', background='#2C3E50', foreground='white', font=('Arial', 14))
        self.style.configure('TEntry', font=('Arial', 14))

        self.frame = ttk.Frame(root, padding="20 20 20 20")
        self.frame.pack(expand=True)

        self.label = ttk.Label(self.frame, text="Bir matematiksel ifade girin:")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.pack(pady=10)

        self.validate_button = tk.Button(self.frame, text="Kontrol Et", font=("Arial", 12), bg='#1ABC9C', fg='white',
                                         activebackground='#16A085', command=self.validate_expression)
        self.validate_button.pack(pady=10)

        self.result_label = ttk.Label(self.frame, text="", font=("Arial", 14), background='#2C3E50', foreground='white')
        self.result_label.pack(pady=10)
        
        self.examples_label = tk.Label(root, text="Geçerli Örnekler Şu Şekildedir:\n5-1*(5+3)\n(6+9)*3\n(7-2*(3-4))/(1+2)")
        self.examples_label.pack(pady=10)

    def validate_expression(self):
        expression = self.entry.get().strip()
        if self.pda.is_balanced_expression(expression):
            result = self.pda.evaluate_expression(expression)
            self.result_label.config(text=f"Girdiğiniz ifade geçerlidir. Sonuç: {result}", foreground='#1ABC9C')
        else:
            self.result_label.config(text="Girdiğiniz ifade geçersizdir. Lütfen kontrol ediniz.", foreground='#E74C3C')

if __name__ == "__main__":
    root = tk.Tk()
    gui = PDAGUI(root)
    root.mainloop()
