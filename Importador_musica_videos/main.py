
import re

from PyQt5.QtWidgets import QDialog,QApplication,QMainWindow,QMessageBox,QErrorMessage,QTableWidgetItem,QFileDialog


import sys
import pytube



from codigos.menu import Ui_Menu_opciones
from codigos.v_unoauno import Ui_v_1_a_1
from codigos.v_audio_txt import Ui_Descarga_multiple
from codigos.v_video_txt import Ui_videos_multiple
from codigos.v_unoauno_videos import Ui_v_1_1_videos


class VentanaP1(QMainWindow):
    def __init__(self):
        super(VentanaP1,self).__init__()
        self.ui=Ui_Menu_opciones()
        self.ui.setupUi(self)

        self.ui.btn_opciones.clicked.connect(self.VentanaHija)
        


    def VentanaHija(self):

        seleccion=self.ui.cb_opciones.itemText(self.ui.cb_opciones.currentIndex())

        if seleccion=="1 a 1 audio":
            self.hide()
            otraventana=Ventana_1_por_1(self)
            otraventana.show()

        elif seleccion=="1 a 1 video":
            self.hide()
            otraventana=Ventana_1_por_1_videos(self)
            otraventana.show()

        elif seleccion=="Por archivo .txt audio":
           
            self.hide()
            otraventana=Ventana_muchos_audio(self)
            otraventana.show()

        elif seleccion=="Por archivo .txt video":
            self.hide()
            otraventana=Ventana_muchos_video(self)
            otraventana.show()

        
            

   


class Ventana_1_por_1(QMainWindow):
    def __init__(self,parent=None):
        super(Ventana_1_por_1,self).__init__(parent)
        self.ui=Ui_v_1_a_1()
        self.ui.setupUi(self)

        self.ui.btn_regresar.clicked.connect(self.atras)
        self.ui.btn_descargar.clicked.connect(self.descargar)
        self.ui.lbl_mensaje.clear()

    def descargar(self):
        link=self.ui.txt_link.text()

        if link != "":
            try:
                
                
                youlink=pytube.YouTube(link)

                titulo= youlink.title + ".mp3"
                caracteres = "'!?()/|,[]~ "
                for x in range(len(caracteres)):
                    titulo = titulo.replace(caracteres[x],"")

                
                youlink.streams.filter(abr='160kbps',progressive=False).first().download("Descargas",filename=titulo)
        
                
                mensaje="Cancion: "+ titulo
                QMessageBox.information(self,"Descarga Completada","Descarga Completada \n"+ mensaje,QMessageBox.Ok,QMessageBox.Ok)
                self.ui.txt_link.clear()

                
                
            except:
                mensaje="Ruta mal identificada o el archivo no existe"
                QMessageBox.warning(self,"Descarga Fallida","Descarga Fallida \n"+ mensaje,QMessageBox.Ok,QMessageBox.Ok)
               

        else:
            mensaje="Debe de ingresar un link de Youtube"

            QMessageBox.information(self,"Mensaje","Mensaje \n"+ mensaje,QMessageBox.Ok,QMessageBox.Ok)
            self.ui.txt_link.setText("")

            


    def atras(self):
        self.parent().show()
        self.close()

class Ventana_1_por_1_videos(QMainWindow):
    def __init__(self,parent=None):
        super(Ventana_1_por_1_videos,self).__init__(parent)
        self.ui=Ui_v_1_1_videos()
        self.ui.setupUi(self)

        self.ui.btn_regresar.clicked.connect(self.atras)
        self.ui.btn_descargar.clicked.connect(self.descargar)
        self.ui.lbl_mensaje.clear()

    def descargar(self):
        link=self.ui.txt_link.text()

        if link != "":
        
                
                
            youlink=pytube.YouTube(link)

            titulo= youlink.title + ".mp4"
            caracteres = "'!?()/|,[]~ "
            for x in range(len(caracteres)):
                titulo = titulo.replace(caracteres[x],"")

            
            youlink.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download("Descargas_Videos",filename=titulo)
    
            
            mensaje="Video: "+ titulo
           
            self.ui.txt_link.clear()
            QMessageBox.information(self,"Descarga Completada","Descarga Completada \n"+ mensaje+"\n"+titulo,QMessageBox.Ok,QMessageBox.Ok)
                
       
               

        else:
            mensaje="Debe de ingresar un link de Youtube"

            QMessageBox.information(self,"Mensaje","Mensaje \n"+ mensaje,QMessageBox.Ok,QMessageBox.Ok)
            self.ui.txt_link.setText("")

            


    def atras(self):
        self.parent().show()
        self.close()

class Ventana_muchos_audio(QMainWindow):
    def __init__(self,parent=None):
        super(Ventana_muchos_audio,self).__init__(parent)
        self.ui=Ui_Descarga_multiple()
        self.ui.setupUi(self)

        self.ui.btn_regresar.clicked.connect(self.atras)
        self.ui.btn_ruta.clicked.connect(self.obtener_ruta)
        self.ui.btn_descargar.clicked.connect(self.descargar)
        
    def obtener_ruta(self):
        ruta=QFileDialog.getOpenFileName(self,'Open file')
        for dato in ruta[::-1]:
            txt=dato
        self.ui.txt_ruta.setText(txt)
       

    def descargar(self):
        txt=self.ui.txt_ruta.text()
       
        if txt !="":

            
            canciones=0
            listacanciones=[]
            with open(txt,"r") as archivo:
                for linea in archivo:

                    try:

                        linealimpia = re.sub("\ n","",linea)
                        youlink=pytube.YouTube(linealimpia)
                        titulo= youlink.title + ".mp3"
                        caracteres = "'!?()/|,[]~éíó-¿Éú"
                    
                        
                        for x in range(len(caracteres)):
                            titulo = titulo.replace(caracteres[x],"")
                    
                        
                        youlink.streams.filter(abr='160kbps',progressive=False).first().download("Descargas",filename=titulo)
                        listacanciones.append(titulo)
                        
                        canciones=canciones+1
                    except:
                        pass


            mensaje=""
            for x in listacanciones:
                mensaje=("Cancion: "+ x)+"\n"+mensaje

            cm=("Cantidad de canciones descargadas:"+str(canciones))
        
                
            
            QMessageBox.information(self,"Descarga Completada","Descarga Completada \n"+ mensaje+"\n"+cm,QMessageBox.Ok,QMessageBox.Ok)
            self.ui.txt_ruta.clear()

        else:
            mensaje="Debe de seleccionar el archivo .txt"

            QMessageBox.information(self,"Mensaje","Mensaje \n"+ mensaje,QMessageBox.Ok,QMessageBox.Ok)
              

                
                
      
               

            


    def atras(self):
        self.parent().show()
        self.close()



class Ventana_muchos_video(QMainWindow):
    def __init__(self,parent=None):
        super(Ventana_muchos_video,self).__init__(parent)
        self.ui=Ui_videos_multiple()
        self.ui.setupUi(self)

        self.ui.btn_regresar.clicked.connect(self.atras)
        self.ui.btn_ruta.clicked.connect(self.obtener_ruta)
        self.ui.btn_descargar.clicked.connect(self.descargar)
        
    def obtener_ruta(self):
        ruta=QFileDialog.getOpenFileName(self,'Open file')
        for dato in ruta[::-1]:
            txt=dato
        self.ui.txt_ruta.setText(txt)
       

    def descargar(self):
        txt=self.ui.txt_ruta.text()
      
                
        if txt !="":

            
            canciones=0
            listacanciones=[]
            with open(txt,"r") as archivo:
                for linea in archivo:
                    try:

                        linealimpia = re.sub("\ n","",linea)
                        youlink=pytube.YouTube(linealimpia)
                        titulo= youlink.title + ".mp4"
                        caracteres = "'!?()/|,[]~éíó-¿Éú"
                    
                        
                        for x in range(len(caracteres)):
                            titulo = titulo.replace(caracteres[x],"")
                        try:

                            youlink.streams.filter(progressive=True, file_extension='mp4',res="720p").order_by('resolution')[-1].download("Descargas_Videos",filename=titulo)
                        except:
                            youlink.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download("Descargas_Videos",filename=titulo)
                        listacanciones.append(titulo)
                        
                        canciones=canciones+1
                    except:
                        pass

            mensaje=""
            for x in listacanciones:
                mensaje=("Video: "+ x)+"\n"+mensaje

            cm=("Cantidad de videos descargadas:"+str(canciones))
        
                
            
            QMessageBox.information(self,"Descarga Completada","Descarga Completada \n"+ mensaje+"\n"+cm,QMessageBox.Ok,QMessageBox.Ok)
            self.ui.txt_ruta.clear()

        else:
            mensaje="Debe de seleccionar el archivo .txt"

            QMessageBox.information(self,"Mensaje","Mensaje \n"+ mensaje,QMessageBox.Ok,QMessageBox.Ok)
                

                
                
      
               

            


    def atras(self):
        self.parent().show()
        self.close()




if __name__=="__main__":
    app=QApplication(sys.argv)
    main=VentanaP1()
    main.show()
    sys.exit(app.exec_())