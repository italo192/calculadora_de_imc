from tkinter import *
from tkinter.ttk import Progressbar, Style

# Cores
cor1 = "#363434"  # vermelho
cor2 = "#feffff"  # Branco
cor3 = "#37474F"  # azul ciano escuro


# Categorias de IMC e suas cores
categorias = [
    {"categoria": "Muito abaixo do peso", "cor": "#ffffff"},
    {"categoria": "Abaixo do peso", "cor": "#ffff00"},
    {"categoria": "Peso normal", "cor": "#00ff00"},
    {"categoria": "Acima do peso", "cor": "#ffa500"},
    {"categoria": "Obesidade I", "cor": "#ff4500"},
    {"categoria": "Obesidade II", "cor": "#ff0000"},
    {"categoria": "Obesidade III", "cor": "#8b0000"},
]


# Função para calcular o IMC
def calcular():
    try:
        altura = float(entrada1.get())
        # Converter altura de centímetros para metros, se necessário
        if altura > 3:
            altura = altura / 100

        peso = float(entrada2.get())
        imc = peso / (altura**2)
        resultado_label.config(text=f"IMC: {imc:.2f}")

        # Determinar a categoria do IMC e atualizar a barra de progresso e a cor
        if imc < 16:
            categoria = categorias[0]
            progress_bar["value"] = 15
        elif 16 <= imc < 18.5:
            categoria = categorias[1]
            progress_bar["value"] = 25
        elif 18.5 <= imc < 24.9:
            categoria = categorias[2]
            progress_bar["value"] = 50
        elif 25 <= imc < 29.9:
            categoria = categorias[3]
            progress_bar["value"] = 75
        elif 30 <= imc < 34.9:
            categoria = categorias[4]
            progress_bar["value"] = 85
        elif 35 <= imc < 39.9:
            categoria = categorias[5]
            progress_bar["value"] = 95
        else:
            categoria = categorias[6]
            progress_bar["value"] = 100

        categoria_label.config(
            text=categoria["categoria"], bg=categoria["cor"], fg=cor1
        )

        # Atualizar a cor da barra de progresso
        style.configure("TProgressbar", troughcolor=cor1, background=categoria["cor"])

    except ValueError:
        resultado_label.config(text="Por favor, insira valores válidos.")
        progress_bar["value"] = 0
        categoria_label.config(text="", bg=cor1)
        style.configure("TProgressbar", troughcolor=cor1, background=cor1)


# Janela principal
janela = Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x350")
janela.config(bg=cor1)

# Estilo para a barra de progresso
style = Style(janela)
style.theme_use("clam")

# Adicionando Labels e Entradas de Texto
label1 = Label(janela, text="Altura (m ou cm):", bg=cor1, fg=cor2)
label1.grid(row=0, column=0, padx=10, pady=10, sticky=E)

entrada1 = Entry(janela, width=10, font=("Arial", 12))
entrada1.grid(row=0, column=1, padx=10, pady=10)

label2 = Label(janela, text="Peso (kg):", bg=cor1, fg=cor2)
label2.grid(row=1, column=0, padx=10, pady=10, sticky=E)

entrada2 = Entry(janela, width=10, font=("Arial", 12))
entrada2.grid(row=1, column=1, padx=10, pady=10)

# Adicionando o botão centralizado
botao = Button(
    janela, text="Calcular", command=calcular, bg=cor3, fg=cor2, font=("Arial", 12)
)
botao.grid(row=2, column=0, columnspan=2, pady=20)

# Label para mostrar o resultado do IMC
resultado_label = Label(janela, text="", bg=cor1, fg=cor2, font=("Arial", 12))
resultado_label.grid(row=3, column=0, columnspan=2, pady=10)

# Adicionando a barra de progresso centralizada
progress_bar = Progressbar(
    janela, orient=HORIZONTAL, length=200, mode="determinate", style="TProgressbar"
)
progress_bar.grid(row=4, column=0, columnspan=2, pady=10, padx=50)

# Label para mostrar a categoria do IMC
categoria_label = Label(janela, text="", bg=cor1, fg=cor1, font=("Arial", 12))
categoria_label.grid(row=5, column=0, columnspan=2, pady=10)

janela.mainloop()
