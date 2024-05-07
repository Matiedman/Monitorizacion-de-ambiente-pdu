import Configuraciones
from Configuraciones import *
from Operaciones import saPromedioTemp, saPromedioHumi, sbPromedioHumi, sbPromedioTemp, saLeftLimitTemp, saLeftLimitHumi,  sbLeftLimitTemp, sbLeftLimitHumi
from Comunicacion import sendEmailsToAlertForHumi, sendEmailsToAlertForTemp, emailConfig
from CreacionDato import *
# from easysnmp import Session, snmp_get, snmp_walk


promTempSa, promTempSb, promTempSc, promHumiSa, promHumiSb, promHumiSc = 0, 0, 0, 0, 0, 0
leftEndTempSa, rightEndTempSa, leftEndTempSb, rightEndTempSb, leftEndTempSc, rightEndTempSc = 0, 0, 0, 0, 0, 0 
leftEndHumiSa, rightEndHumiSa, leftEndHumiSb, rightEndHumiSb, leftEndHumiSc, rightEndHumiSc = 0, 0, 0, 0, 0, 0

 
def main():

    configCreate()                                   # Se crean las configuraciones de los objetos para obtener los datos de temperatura y humedad. 
    tempHumiDataCreate()
    sxFxRxKey_value() 
    getProm()
    getEdgeData()               

    print("PDUenvironmentSa,name=Temp Temp=" + str(promTempSa) + "\n")
    print("PDUenvironmentSa,name=Humi Humi=" + str(promHumiSa) + "\n") 
    print("PDUenvironmentSa,name=Temp LeftTemp=" + str(leftEndTempSa) + "\n")
    print("PDUenvironmentSa,name=Humi LeftHumi=" + str(leftEndHumiSa) + "\n") 
    print("PDUenvironmentSb,name=Temp Temp=" + str(promTempSb) + "\n")
    print("PDUenvironmentSb,name=Humi Humi=" + str(promHumiSb) + "\n") 
    print("PDUenvironmentSb,name=Temp LeftTemp=" + str(leftEndTempSb) + "\n")
    print("PDUenvironmentSb,name=Humi LeftHumi=" + str(leftEndHumiSb) + "\n") 

def configCreate():

    pduDefinitions()
    deviceConfigName()
    tempHumiDataCreate()
    sxFxRxKey_value()
    emailConfig()

def getProm(): 

    global promTempSa, promTempSb, promTempSc, promHumiSa, promHumiSb, promHumiSc
   
    promTempSa = saPromedioTemp(Configuraciones.SaKeyValueTemp) 
    promHumiSa = saPromedioHumi(Configuraciones.SaKeyValueHumi) 
    saTempHumiCheck(promTempSa, promHumiSa)
    
    promTempSb = sbPromedioTemp(Configuraciones.SbF1KeyValueTemp, Configuraciones.SbF2KeyValueTemp) 
    promHumiSb = sbPromedioHumi(Configuraciones.SbF1KeyValueHumi, Configuraciones.SbF2KeyValueHumi) 
    sbTempHumiCheck(promTempSb, promHumiSb)
   
    # promTempSc = Operaciones.scPromedioTemp(Configuraciones.ScF1KeyValueTemp, Configuraciones.ScF2KeyValueTemp) -> Hay que crear el diccionario. 
    # promHumiSc = Operaciones.scPromedioHumi(Configuraciones.ScF1KeyValueHumi, Configuraciones.ScF2KeyValueHumi)
    
    # Se actualizan los archivos txt de los tres sectores con los datos obtenidos. Se comentan los que llaman a Sector A y C ya que aun no esta implementado.
    # saUpdateFileTXT(promHumiSa, promTempSa)
    sbUpdateFileTXT(promHumiSb, promTempSb)  
    # scUpdateFileTXT(promHumiSc, promTempSc)
    

def getEdgeData():

    global leftEndTempSa, rightEndTempSa, leftEndTempSb, rightEndTempSb, leftEndTempSc, rightEndTempSc
    global leftEndHumiSa, rightEndHumiSa, leftEndHumiSb, rightEndHumiSb, leftEndHumiSc, rightEndHumiSc
    
    # Hay que ver sus ubicaciones fisicas. Luego descomentar y probar. 
    leftEndTempSa = saLeftLimitTemp(Configuraciones.SaKeyValueTemp.get('saR1pduTemp', 'Error en conectar'), Configuraciones.SaKeyValueTemp.get('saR4pduTemp', 'Error en conectar'))
    # rightEndTempSa = Operaciones.saRightLimitTemp(Configuraciones.SaKeyValueHumi.get())
    leftEndHumiSa = saLeftLimitHumi(Configuraciones.SaKeyValueHumi.get('saR1pduHumi', 'Error en conectar'), Configuraciones.SaKeyValueHumi.get('saR4pduHumi', 'Error en conectar'))
    # rightEndHumiSa = Operaciones.saRightLimitHumi(Configuraciones.SaKeyValueHumi.get())
    
    leftEndTempSb = sbLeftLimitTemp(Configuraciones.SbF1KeyValueTemp.get('sbF1R1pduTemp', 'Error en conectar'), Configuraciones.SbF2KeyValueTemp.get('sbF2R1pduTemp', 'Error en conectar'))
    # rightEndTempSb = Operaciones.sbRightLimitTemp(Configuraciones.SbF1KeyValueTemp.get('sbF1R10pduTemp', 'Error en conectar'), Configuraciones.SbF2KeyValueTemp.get('sbF2R10pduTemp', 'Error en conectar')) -> Racks no disponibles
    leftEndHumiSb = sbLeftLimitHumi(Configuraciones.SbF1KeyValueHumi.get('sbF1R1pduHumi', 'Error en conectar'), Configuraciones.SbF2KeyValueHumi.get('sbF2R1pduHumi', 'Error en conectar'))
    # rightEndHumiSb = Operaciones.sbRightLimitHumi(Configuraciones.SbF1KeyValueHumi.get('sbF1R10pduHumi', 'Error en conectar'), Configuraciones.SbF2KeyValueHumi.get('sbF2R10pduHumi', 'Error en conectar')) -> Racks no disponibles

    # Hay que crear los diccionarios. Luego descomentar y probar. 
    # leftEndTempSc = Operaciones.scLeftLimitTemp(Configuraciones.ScF1KeyValueTemp, Configuraciones.ScF2KeyValueTemp)
    # rightEndTempSc = Operaciones.scRightLimitTemp(Configuraciones.ScF1KeyValueTemp, Configuraciones.ScF2KeyValueTemp)
    # leftEndHumiSc = Operaciones.scLeftLimitHumi(Configuraciones.ScF1KeyValueTemp, Configuraciones.ScF2KeyValueTemp)
    # rightEndHumiSc = Operaciones.scRightLimitHumi(Configuraciones.ScF1KeyValueHumi, Configuraciones.ScF2KeyValueHumi)
    
    # Se actualizan los archivos txt de los tres sectores con los datos obtenidos de sus extremos.
    # Se comentan los que llaman a Sector A y C ya que aun no esta implementado. 
    
    # saLeftUpdateFileTXT(leftEndHumiSa, leftEndTempSa)
    # saRightUpdateFileTXT(rightEndHumiSa, rightEndTempSa)
    
    sbLeftUpdateFileTXT(leftEndHumiSb, leftEndTempSb)
    # sbRightUpdateFileTXT(rightEndHumiSb, rightEndTempSb)
    
    # scLeftUpdateFileTXT(leftEndHumiSc, leftEndTempSc)
    # scRightUpdateFileTXT(rightEndHumiSc, rightEndTempSc)

# Las siguientes funciones verifican que no se hayan pasado lo limites ambientales establecidos. Si es asi, se enviará un msj por Chat de Google y un email para alertar. 
# Por practicidad se comentaran las funciones que prueban los lados extremos. 
def saTempHumiCheck(promTempSa, promHumiSa): 
    
    if promTempSa < 12 or promTempSa > 20:
        if(promTempSa < 12):
            sendEmailsToAlertForTemp(promTempSa)
        else:
            sendEmailsToAlertForTemp(promTempSa)
    
    if promHumiSa < 25 or promHumiSa > 85:
        if(promHumiSa < 25):
            sendEmailsToAlertForHumi(promHumiSa)
        else:
            sendEmailsToAlertForHumi(promHumiSa)
            
# def saTempHumiLeftCheck(leftEndTempSa, leftEndHumiSa):
    
#     if leftEndTempSa < 12 or leftEndTempSa > 20:
#         if(promTempSa < 12):
#             sendEmailsToAlertForTemp(leftEndTempSa)
#         else:
#             sendEmailsToAlertForTemp(leftEndTempSa)
    
#     if leftEndHumiSa < 25 or leftEndHumiSa > 85:
#         if(leftEndHumiSa < 25):
#             sendEmailsToAlertForHumi(leftEndHumiSa)
#         else:
#             sendEmailsToAlertForHumi(leftEndHumiSa)
               
def sbTempHumiCheck(promTempSb, promHumiSb):  
    
    if promTempSb < 12 or promTempSb > 20:
        if(promTempSb < 12):
            sendEmailsToAlertForTemp(promTempSb)
        else:
            sendEmailsToAlertForTemp(promTempSb)
    
    if promHumiSb < 25 or promHumiSb > 85:
        if(promHumiSb < 25):
            sendEmailsToAlertForHumi(promHumiSb)
        else:
            sendEmailsToAlertForHumi(promHumiSb)

# def sbTempHumiLeftCheck(leftEndTempSb, leftEndHumiSb):
    
#     if leftEndTempSb < 12 or leftEndTempSb > 20:
#         if(promTempSb < 12):
#             sendEmailsToAlertForTemp(leftEndTempSb)
#         else:
#             sendEmailsToAlertForTemp(leftEndTempSb)
    
#     if leftEndHumiSb < 25 or leftEndHumiSb > 85:
#         if(leftEndHumiSb < 25):
#             sendEmailsToAlertForHumi(leftEndHumiSb)
#         else:
#             sendEmailsToAlertForHumi(leftEndHumiSb)
    

if __name__ == '__main__':
    main()