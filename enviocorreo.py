import  tkinter as Tk 
import smtplib
from tkinter import messagebox

#ventana principal
ventana=Tk.Tk()
ventana.title("Ciber Bullis")
ventana.geometry("1200x720")
#Nombre de empresa
Nempresa=Tk.Label(ventana,text="Ciber Bullis", font=("arial",25) )
Nempresa.pack()

#Numero del cliente
NCliente=Tk.Label(ventana,text="Numero de Telefono:")
NCliente.place(x="633",y="100")

#Entrada Numero cliente
ENumeroCliente=Tk.Entry(ventana,width=30,bg="#C5FDFC")
ENumeroCliente.place(x="750",y="100")

#texto nombre cliente
preguntaNom=Tk.Label(ventana,text="Nombre del cliente: ")
preguntaNom.place(x="320",y="100")

#entrada de Nombre de cliente
ENombre=Tk.Entry(ventana,width=30,bg="#C5FDFC")
ENombre.place(x="430",y="100")

#texto Pregunta Marca
PMarcEquipo=Tk.Label(ventana,text="Marca del equipo:  ")
PMarcEquipo.place(x="650",y="150")

#entrada de marca equipo
EMarca=Tk.Entry(ventana,width=30,bg="#C5FDFC")
EMarca.place(x="750",y="150")

#texto Problema Equipo

txtProblema=Tk.Label(ventana,text="Describe el Problema del equipo detalladamente")
txtProblema.place(x="500",y="190")


#Descripcion Probelma del equipo
Problema=Tk.Text(ventana,height="20", bg="#C5FDFC")
Problema.place(x="313",y="220")

#Texto Pregunta si es Lap Top o Celular u otro

pregunta=Tk.Label(ventana,text="¿Que equipo es?\n lapTop,celular,CPU,ALL IN ONE :")
pregunta.place(x=310,y=130)

Equipo=Tk.Entry(ventana,bg="#C5FDFC")
Equipo.place(y=144,x=490)

def destinatario_entry():
    miCorreo = destinatario_entry
    miCorreo= "sagcookies@gmail.com"


#Funcion mandar correo

# Función para enviar el correo electrónico
def enviar_correo():
    # Configura la conexión SMTP
    smtp_server = 'smtp.office365.com'  # Reemplaza con el servidor SMTP adecuado
    smtp_port = 587  # Reemplaza con el puerto SMTP adecuado
    smtp_username = 'cookiesone1@hotmail.com'  # Reemplaza con tu dirección de correo electrónico
    smtp_password = 'GiioGalleta25Y1'  # Reemplaza con tu contraseña de correo electrónico

    # Crea una conexión SMTP
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Obtiene los datos del formulario
        destinatario = "sagcookies@gmail.com"
        NumeroCliente = ENumeroCliente.get()
        NombreCliente = ENombre.get()
        MarcaEquipo = EMarca.get()
        equipo= Equipo.get()
        mensaje = Problema.get("1.0",Tk.END )

      
        # Crea el correo electrónico
        correo = f"Subject: {NombreCliente}\nTo: {destinatario}\n\n{mensaje}\n\n{NumeroCliente}\n\n{equipo }\n\n{MarcaEquipo }"

        # Envía el correo electrónico
        server.sendmail(smtp_username, destinatario, correo)
        server.quit()

        messagebox.showinfo("Éxito", "Correo electrónico enviado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"Error al enviar el correo electrónico: {str(e)}")
        
        
    

enviar_button = Tk.Button(ventana, text="Enviar", command=enviar_correo, height=5,width=10,border=5,bg="#C5FDFC")
enviar_button.place(x=870,y=590)



        








ventana.resizable(False, False)

ventana.mainloop()