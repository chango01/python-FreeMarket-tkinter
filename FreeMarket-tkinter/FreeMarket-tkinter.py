# CREADO POR GITHUB: CHANGO01

# Plataforma para dar de alta Productos y Clientes, y ver su información.
# Se guardan en dos archivos .json, uno para productos y otro para clientes.


import json
from pathlib import Path
from tkinter import *
from tkinter import messagebox

def openFile():                                             # Funciones para abrir los archivos si existen,
    file=Path('productos1.json')                            # y sino los crea. También , estan las funciones
    if file.is_file():                                      # para grabarlos.
        with open('productos1.json', 'r') as file:
            data= json.load(file)
        return data
    else:
        total_productos=[]
        return total_productos
    
def GrabarFile(total_productos):
    with open("productos1.json","w") as file:
        json.dump(total_productos, file) 

def openFile_clientes():
    file=Path('clientes1.json')
    if file.is_file():
        with open('clientes1.json', 'r') as file:
            data= json.load(file)
        return data
    else:
        total_clientes=[]
        return total_clientes
    
def GrabarFile_clientes(total_clientes):
    with open("clientes1.json","w") as file:
        json.dump(total_clientes, file) 

def alta_producto():                                    # Función que busca si existe el código que se ingresa.
    loop=True                                           # Si existe sale el mensaje, sino lo crea y lo guarda.
    while loop==True:
        for k in total_productos:
            if codigo.get()==k["CODIGO"]:
                messagebox.showinfo("ALTA PRODUCTO","CODIGO ya existe. Ingrese uno nuevo")
                loop=False
                break
        else:
            loop=False
            c=codigo.get()
            np=nombre_producto.get()
            p=precio.get()
            s=stock.get()
            total_productos.append({"CODIGO":c,"NOMBRE":np,"PRECIO":p,"STOCK":s})
            GrabarFile(total_productos)
            messagebox.showinfo("ALTA PRODUCTO","El PRODUCTO fue dado de alta correctamente")

def baja_producto():
    loop=True                                           # Busca si existe el código y si lo encuentra lo elimina, 
    while loop==True:                                   # sino avisa que no existe.
        for j in total_productos:
            if codigo1.get()==j["CODIGO"]:
                total_productos.remove(j)
                GrabarFile(total_productos)
                messagebox.showinfo("ALTA PRODUCTO",f"El PRODUCTO {j} fue dado de BAJA correctamente")
                loop=False
                break
        else:
            loop=False
            messagebox.showinfo("ALTA PRODUCTO","El CODIGO del PRODUCTO no existe.")

def mod_alta():
    loop=True                                           # Verifica que el código no exista y modifica los atributos
    while loop==True:                                   # que en los entry es distinto de vacío ó 0.
        for i in total_productos:
            if codigo2.get()==i["CODIGO"]:
                for j in total_productos:
                    if codigo31.get()==j["CODIGO"]:
                        messagebox.showinfo("ALTA PRODUCTO","CODIGO ya existe. Ingrese uno nuevo")
                        loop=False
                        break
                else:
                    ccc=codigo31.get()
                    nomnom=nom_prod3.get()
                    prepre=precio3.get()
                    stosto=stock3.get()
                    if ccc!="":
                        i["CODIGO"]=ccc
                    if nomnom!="":
                        i["NOMBRE"]=nomnom
                    if prepre!=0:
                        i["PRECIO"]=prepre
                    if stosto!=0:
                        i["STOCK"]=stosto
                    loop=False
    GrabarFile(total_productos)
    messagebox.showinfo("ALTA PRODUCTO","El PRODUCTO fue modificado correctamente")

def mod_producto():
    loop=True                               # Busca el código y si existe crea unos entry para ingresar datos a modificar,
    while loop==True:                       # luego llama a la función mod_alta.
        for i in total_productos:
            if codigo2.get()==i["CODIGO"]:
                alt_pr_cod=Label(ecommerce,text="CODIGO: ",bg=cf,fg=c3).place(x=450,y=140)
                input_cod=Entry(ecommerce,textvariable=codigo31,bg=cf,fg=c1).place(x=510,y=140)
                alt_pr_nom=Label(ecommerce,text="NOMBRE: ",bg=cf,fg=c3).place(x=450,y=170)
                input_nom=Entry(ecommerce,textvariable=nom_prod3,bg=cf,fg=c1).place(x=510,y=170)
                alt_pr_prec=Label(ecommerce,text="PRECIO: ",bg=cf,fg=c3).place(x=450,y=200)
                input_prec=Entry(ecommerce,textvariable=precio3,bg=cf,fg=c1).place(x=510,y=200)
                alt_pr_st=Label(ecommerce,text="STOCK: ",bg=cf,fg=c3).place(x=450,y=230)
                input_st=Entry(ecommerce,textvariable=stock3,bg=cf,fg=c1).place(x=510,y=230)
                bot_alt_guardar=Button(ecommerce,text="Guardar",command=mod_alta,bg=cf,fg=c4).place(x=510,y=260)
                loop=False
                break
        else:
            loop=False
            messagebox.showinfo("ALTA PRODUCTO","El CODIGO del PRODUCTO no existe.")

def buscar_prod():
    loop=True                                           # Busca el producto y lo muestra.
    while loop==True:
        for l in total_productos:
            if codigo3.get()==l["CODIGO"]:
                messagebox.showinfo("ALTA PRODUCTO",f"PRODUCTO: {l}")
                loop=False
                break
        else:
            loop=False
            messagebox.showinfo("ALTA PRODUCTO","El CODIGO del PRODUCTO no existe.")


def imprimir_prod():
    ventana_prod= Tk()                              # Imprime en una nueva ventana todos los valores del archivo.json  .
    ventana_prod.title("PRODUCTOS")
    ventana_prod.geometry("400x600")
    ventana_prod.configure(background=cf)
    eti_prod_list=Label(ventana_prod,text="LISTA PRODUCTOS",bg=cf,fg=c2).place(x=150,y=10)
    yy=50
    for i in total_productos:
        prod_lista=Label(ventana_prod,text=i,bg=cf,fg=c1).place(x=30,y=yy)
        yy=yy+20
    ventana_prod.mainloop()

def alta_cliente():
    loop=True
    while loop==True:
        for k in total_clientes:
            if dni.get()==k["DNI"]:
                messagebox.showinfo("ALTA CLIENTE","El DNI ya existe. Ingrese uno nuevo")
                loop=False
                break
        else:
            loop=False
            d=dni.get()
            if d>=600000 and d<=50000000:
                nc=nombre_cliente.get()
                total_clientes.append({"NOMBRE":nc,"DNI":d,"PRODUCTOS":[]})
                GrabarFile_clientes(total_clientes)
                messagebox.showinfo("ALTA CLIENTE","El CLIENTE fue dado de alta correctamente")
            else:
                messagebox.showinfo("ALTA CLIENTE","Ingreso mal el DNI.")

def baja_cliente():
    loop=True
    while loop==True:
        for j in total_clientes:
            if dni1.get()==j["DNI"]:
                total_clientes.remove(j)
                GrabarFile_clientes(total_clientes)
                messagebox.showinfo("ALTA CLIENTE",f"El CLIENTE {j} fue dado de BAJA correctamente")
                loop=False
                break
        else:
            loop=False
            messagebox.showinfo("ALTA CLIENTE","El DNI del CLIENTE no existe.")

def mod_alta_cli():
    loop=True
    while loop==True:
        for i in total_clientes:
            if dni2.get()==i["DNI"]:
                for j in total_clientes:
                    if dni31.get()==j["DNI"]:
                        messagebox.showinfo("ALTA CLIENTE","DNI ya existe. Ingrese uno nuevo")
                        loop=False
                        break
                else:
                    loop=False
                    ddd=dni31.get()
                    nomon=nom_cli3.get()
                    if nomon!="":
                        i["NOMBRE"]=nomon
                        messagebox.showinfo("ALTA CLIENTE","El CLIENTE fue modificado correctamente")
                        GrabarFile_clientes(total_clientes)
                    if ddd!=0:
                        if ddd>=600000 and ddd<=50000000:
                            i["DNI"]=ddd
                            messagebox.showinfo("ALTA CLIENTE","El CLIENTE fue modificado correctamente")
                            GrabarFile_clientes(total_clientes)
                        else:
                            messagebox.showinfo("ALTA CLIENTE","Ingreso mal el DNI.")
    
def mod_cliente():
    loop=True
    while loop==True:
        for i in total_clientes:
            if dni2.get()==i["DNI"]:
                alta_cli_dni=Label(ecommerce,text="NOMBRE: ",bg=cf,fg=c3).place(x=450,y=440)
                inp_dni=Entry(ecommerce,textvariable=nom_cli3,bg=cf,fg=c1).place(x=510,y=440)
                alta_cli_nom=Label(ecommerce,text="DNI: ",bg=cf,fg=c3).place(x=450,y=470)
                inp_nom=Entry(ecommerce,textvariable=dni31,bg=cf,fg=c1).place(x=510,y=470)
                bt_modalt_guardar=Button(ecommerce,text="Guardar",command=mod_alta_cli,bg=cf,fg=c4).place(x=510,y=500)
                loop=False
                break
        else:
            loop=False
            messagebox.showinfo("ALTA CLIENTE","El DNI no existe.")

def buscar_cli():
    loop=True
    while loop==True:
        for l in total_clientes:
            if dni3.get()==l["DNI"]:
                messagebox.showinfo("ALTA CLIENTE",f"CLIENTE: {l}")
                loop=False
                break
        else:
            loop=False
            messagebox.showinfo("ALTA CLIENTE","El DNI del CLIENTE no existe.")

def imprimir_cli():
    ventana_cli= Tk()
    ventana_cli.title("CLIENTES")
    ventana_cli.geometry("800x600")
    ventana_cli.configure(background=cf)
    eti_cli_list=Label(ventana_cli,text="LISTA CLIENTES",bg=cf,fg=c2).place(x=150,y=10)
    ss=50
    for i in total_clientes:
        cli_lista=Label(ventana_cli,text=i,bg=cf,fg=c1).place(x=30,y=ss)
        ss=ss+20
    ventana_cli.mainloop()

def cliente_prod():
    loop=True                                                  # Busca al cliente que va a sumar los productos al carrito.
    while loop==True:
        for i in total_clientes:
            if dni4.get()==i["DNI"]:
                for l in total_productos:
                    if codigo41.get()==l["CODIGO"]:
                        prod={}
                        prod["NOMBRE"]=l["NOMBRE"]
                        prod["CANTIDAD"]=cantidad.get()
                        i["PRODUCTOS"].append(prod)
                        l["STOCK"]=l["STOCK"]-cantidad.get()
                        GrabarFile_clientes(total_clientes)
                        GrabarFile(total_productos)
                        messagebox.showinfo("ALTA CLIENTE","Se agregó al carrito el producto.")
                        loop=False
                        break
                else:
                    loop=False
                    messagebox.showinfo("ALTA CLIENTE","El CODIGO del PRODUCTO no existe.")

def agreg_prod():
    loop=True                                       # Agrega al archivo clientes.json el código y la cantidad del producto que agrega al carrito.   
    while loop==True:
        for i in total_clientes:    
            if dni4.get()==i["DNI"]:
                pro_cod=Label(ecommerce,text="CODIGO: ",bg=cf,fg=c3).place(x=200,y=530)
                inp_procod=Entry(ecommerce,textvariable=codigo41,bg=cf,fg=c1).place(x=270,y=530)
                cant_cliprod=Label(ecommerce,text="CANTIDAD: ",bg=cf,fg=c3).place(x=200,y=560)
                inp_cliprod=Entry(ecommerce,textvariable=cantidad,bg=cf,fg=c1).place(x=270,y=560)
                bt_cliprod_grdr=Button(ecommerce,text="Guardar",command=cliente_prod,bg=cf,fg=c4).place(x=270,y=590)
                loop=False
                break
        else:
            loop=False
            messagebox.showinfo("ALTA CLIENTE","El DNI no existe.")
#   Creo ventana.
ecommerce= Tk()
#   Variables de Productos.
codigo=StringVar()
nombre_producto=StringVar()
precio=DoubleVar()
stock=IntVar()
codigo1=StringVar()
codigo2=StringVar()
codigo3=StringVar()
codigo31=StringVar()
nom_prod3=StringVar()
precio3=DoubleVar()
stock3=IntVar()
#   Variables de Cliente.
nombre_cliente=StringVar()
dni=IntVar()
dni1=IntVar()
dni2=IntVar()
dni3=IntVar()
dni4=IntVar()
dni31=IntVar()
nom_cli3=StringVar()
codigo41=StringVar()
cantidad=IntVar()
#   Colores.
cf="#ecedad"
c1="#574423"
c2="#b35715"
c3="#eba823"
c4="#3b89a8"
#   Abro archivos.
total_productos=openFile()
total_clientes=openFile_clientes()
#   Configuto ventana y añado etiqueta de producto y cliente.
ecommerce.title("FreeMarket - Bienvenido")
ecommerce.geometry("1024x680")
ecommerce.configure(background=cf)
ecommerce_eti_prod=Label(ecommerce,text="PRODUCTO",bg=cf,fg=c1).place(x=450,y=10)
ecommerce_eti_cli=Label(ecommerce,text="CLIENTE",bg=cf,fg=c1).place(x=450,y=320)
#   ALTA PRODUCTO.
ecommerce_et_alta=Label(ecommerce,text="ALTA",bg=cf,fg=c2).place(x=80,y=40)
alt_pro_cod=Label(ecommerce,text="CODIGO: ",bg=cf,fg=c3).place(x=10,y=70)
input_cod=Entry(ecommerce,textvariable=codigo,bg=cf,fg=c1).place(x=70,y=70)
alt_pro_nom=Label(ecommerce,text="NOMBRE: ",bg=cf,fg=c3).place(x=10,y=100)
input_nom=Entry(ecommerce,textvariable=nombre_producto,bg=cf,fg=c1).place(x=70,y=100)
alt_pro_prec=Label(ecommerce,text="PRECIO: ",bg=cf,fg=c3).place(x=10,y=130)
input_prec=Entry(ecommerce,textvariable=precio,bg=cf,fg=c1).place(x=70,y=130)
alt_pro_st=Label(ecommerce,text="STOCK: ",bg=cf,fg=c3).place(x=10,y=160)
input_st=Entry(ecommerce,textvariable=stock,bg=cf,fg=c1).place(x=70,y=160)
bot_alta_guardar=Button(ecommerce,text="Guardar",command=alta_producto,bg=cf,fg=c4).place(x=70,y=190)
#   BAJA PRODUCTO.
ecommerce_et_baja=Label(ecommerce,text="BAJA",bg=cf,fg=c2).place(x=320,y=40)
baj_pro_cod=Label(ecommerce,text="CODIGO: ",bg=cf,fg=c3).place(x=230,y=70)
input_bajcod=Entry(ecommerce,textvariable=codigo1,bg=cf,fg=c1).place(x=290,y=70)
bot_baj_bus=Button(ecommerce,text="Buscar",command=baja_producto,bg=cf,fg=c4).place(x=290,y=100)
#   MODIFICACION PRODUCTO.
ecommerce_et_mod=Label(ecommerce,text="MODIFICACIÓN",bg=cf,fg=c2).place(x=490,y=40)
mod_pro_cod=Label(ecommerce,text="CODIGO: ",bg=cf,fg=c3).place(x=450,y=70)
input_modcod=Entry(ecommerce,textvariable=codigo2,bg=cf,fg=c1).place(x=510,y=70)
bot_mod_bus=Button(ecommerce,text="Buscar",command=mod_producto,bg=cf,fg=c4).place(x=510,y=100)
#   BUSCAR PRODUCTO.
ecommerce_et_bus=Label(ecommerce,text="BUSCAR",bg=cf,fg=c2).place(x=720,y=40)
bus_pro_cod=Label(ecommerce,text="CODIGO: ",bg=cf,fg=c3).place(x=660,y=70)
input_buscod=Entry(ecommerce,textvariable=codigo3,bg=cf,fg=c1).place(x=720,y=70)
bot_bus=Button(ecommerce,text="Buscar",command=buscar_prod,bg=cf,fg=c4).place(x=720,y=100)
#   IMPRIMIR LISTA PRODUCTO.
ecommerce_et_lista=Label(ecommerce,text="PRODUCTOS",bg=cf,fg=c2).place(x=890,y=40)
bot_imp=Button(ecommerce,text="Ver",command=imprimir_prod,bg=cf,fg=c4).place(x=910,y=70)
#   ALTA CLIENTE.
cli_et_alta=Label(ecommerce,text="ALTA",bg=cf,fg=c2).place(x=80,y=350)
alt_cli_nom=Label(ecommerce,text="NOMBRE: ",bg=cf,fg=c3).place(x=10,y=380)
input_nom_cli=Entry(ecommerce,textvariable=nombre_cliente,bg=cf,fg=c1).place(x=70,y=380)
alt_cli_dni=Label(ecommerce,text="DNI: ",bg=cf,fg=c3).place(x=10,y=410)
input_dni=Entry(ecommerce,textvariable=dni,bg=cf,fg=c1).place(x=70,y=410)
bt_alt_cli_grdr=Button(ecommerce,text="Guardar",command=alta_cliente,bg=cf,fg=c4).place(x=70,y=440)
#   BAJA CLIENTE.
ecom_et_cli_baja=Label(ecommerce,text="BAJA",bg=cf,fg=c2).place(x=320,y=350)
baj_clidni=Label(ecommerce,text="DNI: ",bg=cf,fg=c3).place(x=250,y=380)
input_bajcli=Entry(ecommerce,textvariable=dni1,bg=cf,fg=c1).place(x=290,y=380)
bt_baj_cli_bus=Button(ecommerce,text="Buscar",command=baja_cliente,bg=cf,fg=c4).place(x=290,y=410)
#   MODIFICACION CLIENTE.
ecommerce_et_mod=Label(ecommerce,text="MODIFICACIÓN",bg=cf,fg=c2).place(x=490,y=350)
mod_cli_dni=Label(ecommerce,text="DNI: ",bg=cf,fg=c3).place(x=470,y=380)
input_moddni=Entry(ecommerce,textvariable=dni2,bg=cf,fg=c1).place(x=510,y=380)
bt_mod_cli_bus=Button(ecommerce,text="Buscar",command=mod_cliente,bg=cf,fg=c4).place(x=510,y=410)
#   BUSCAR CLIENTE.
ecom_et_cli_bus=Label(ecommerce,text="BUSCAR",bg=cf,fg=c2).place(x=720,y=350)
bus_clidni=Label(ecommerce,text="DNI: ",bg=cf,fg=c3).place(x=680,y=380)
input_busdni=Entry(ecommerce,textvariable=dni3,bg=cf,fg=c1).place(x=720,y=380)
bt_dni_bus=Button(ecommerce,text="Buscar",command=buscar_cli,bg=cf,fg=c4).place(x=720,y=410)
#   IMPRIMIR LISTA CLIENTE.
ecom_et_cli_lista=Label(ecommerce,text="CLIENTES",bg=cf,fg=c2).place(x=890,y=350)
bt_cli_imp=Button(ecommerce,text="Ver",command=imprimir_cli,bg=cf,fg=c4).place(x=910,y=380)
#   AGREGAR PRODUCTOS A CLIENTE.
ecom_et_prodacli=Label(ecommerce,text="CARRITO",bg=cf,fg=c2).place(x=70,y=500)
bus_cliprod=Label(ecommerce,text="DNI: ",bg=cf,fg=c3).place(x=10,y=530)
inp_cliprod=Entry(ecommerce,textvariable=dni4,bg=cf,fg=c1).place(x=70,y=530)
bt_cliprod=Button(ecommerce,text="Buscar",command=agreg_prod,bg=cf,fg=c4).place(x=70,y=560)

ecommerce.mainloop()

