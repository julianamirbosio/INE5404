from janelalogin import JanelaLogin


if __name__ == "__main__":
    print("Iniciando a aplicação")
    janelalogin = JanelaLogin()
    janelalogin.configure(fg_color="#ffffff")
    janelalogin.mainloop()
    print("Aplicação encerrada")