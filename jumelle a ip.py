import tkinter as tk 
import socket

# => Application qui va traduire un nom de domaine en ipV4 

def dns_to_ipv4():
    dns = ma_super_saisie.get()
    ipV4 = socket.gethostbyname(dns)
    l_resultat.config(text=f"IP : {ipV4}" ,fg="black")

# Création de la fenêtre principal (Création de l'objet)
root = tk.Tk()

# Dimension de la fenêtre
root.geometry("300x150")

# Titre de la fenêtre
root.title("Jumelle d'ip")

# Création d'un label (titre)
mon_super_titre = tk.Label(root, text="La Jumelle à Ip Site" ,fg="red")
l_resultat = tk.Label(root, text="" ,fg="black")

# Création d'une zone de saisie
ma_super_saisie = tk.Entry(root)

# Création d'un bouton
mon_boutton = tk.Button(root, text="Valider", command=dns_to_ipv4 ,fg="green")
bouton_quitter = tk.Button(root, text="Quitter", command=root.quit ,fg="yellow")

# Placement des widgets
mon_super_titre.pack()
ma_super_saisie.pack()
l_resultat.pack()
mon_boutton.pack()
bouton_quitter.pack()

# Boucle de la fenêtre
root.mainloop() 

