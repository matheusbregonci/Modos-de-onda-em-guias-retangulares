from models.TEmn_model import Modo_TEmn
from models.TMmn_model import Modo_TMmn


TEmn = Modo_TEmn(largura = 22.86, 
                 altura = 10.16, 
                 frequencia = 12*10**9, 
                 permissividade = 1, 
                 permeabilidade = 1 , 
                 plano = 'xy')
 
TEmn.calcula_campos()
# TEmn.plota_campo_vetorial('magnetico')
TEmn.plot3DField(campo = 'magnetico', componente = 'z')
# x, y, z = TEmn.coordenadas()

TMmn = Modo_TMmn(largura = 22.86, 
                 altura = 10.16, 
                 frequencia = 12*10**9, 
                 permissividade = 1, 
                 permeabilidade = 1 , 
                 plano = 'xy') 

TMmn.calcula_campos()
# TEmn.plota_campo_vetorial('magnetico')
TMmn.plot3DField(campo = 'eletrico', componente = 'x')