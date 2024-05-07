from easysnmp import Session
import CreacionDato


SApduRxSession = [] # Array de elementos de las diferentes sesiones de los PDU en los Rx del sector A. 
SBpduF1Session = [] # Array de elementos de las diferentes sesiones de los PDU de la fila 1 del sector B. 
SBpduF2Session = [] # Array de elementos de las diferentes sesiones de los PDU de la fila 2 del sector B. 

SaKeyValueTemp = {}     # Contiene los elementos que almacenan datos "llave-valor" respecto a la temperatura de los diferentes dispositivos según área.
SbF1KeyValueTemp = {}
SbF2KeyValueTemp = {}
SaKeyValueHumi = {}     # Contiene los elementos que almacenan datos "llave-valor" respecto a la humedad de los diferentes dispositivos segun área.
SbF1KeyValueHumi = {}
SbF2KeyValueHumi = {}

saRxNameTemp = []        # Los siguientes elementos contienen los nombres de cada dispositivo según área para su temperatura y humedad.
sbF1RxpduNameTemp = []  
sbF2RxpduNameTemp = []

saRxNameHumi = []
sbF1RxpduNameHumi = []
sbF2RxpduNameHumi = []

saRxPduDatoTemp = []    # Los siguientes elementos contienen los datos de temperatura y humedad correspondiente a cada dispositivo según área. 
sbF1RxPduDatoTemp = []
sbF2RxPduDatoTemp = []

saRxPduDatoHumi = []
sbF1RXPduDatoHumi = []
sbF2RXPduDatoHumi = []

# Funcion que carga las sesiones de cada pdu segun rack, fila y sector del DC en distintas variables con nombre asociado  
# y luego en un array que los une por area y fila.  
def pduDefinitions():
    
    global SApduRxSession, SBpduF1Session, SBpduF2Session   # Esto indica que se hace referencia a la misma variable global antes declarada. 

    #-----------------------------------------------SECTOR A-------------------------------------------------------------#

    # En el sector A luego de debuggear ha salido para la sesion del R6 el siguiente error:
        # easysnmp.exceptions.EasySNMPTimeoutError: timed out while connecting to remote host
    

    saR1pduSession = Session(hostname='Sa R1 pDu DNS name', community='publiceaton', version=1) 
    # saR2pduSession = Session(hostname='Sa R2 pDu DNS name', community='publiceaton', version=1) ---> r2 y r3 ESTAN DESCONECTADOS
    # saR3pduSession = Session(hostname='Sa R3 pDu DNS name', community='publiceaton', version=1)
    saR4pduSession = Session(hostname='Sa R4 pDu DNS name', community='publiceaton', version=1) 
    saR5pduSession = Session(hostname='Sa R5 pDu DNS name', community='publiceaton', version=1) 
    saR6pduSession = Session(hostname='Sa R6 pDu DNS name', community='publiceaton', version=1)
  
    SApduRxSession = [saR1pDu Session, saR4pDu Session, saR5pDu Session, saR6pDu Session] #[saR2pDu Session, saR3pDu Session, ]
    # Una vez reparado todos los erroes, descomentar las lineas y hacer el mismo procedimiento para probarlos. Debuggear.     

    #-----------------------------------------------SECTOR B-------------------------------------------------------------#
    sbF1R1pduSession = Session(hostname='Sb F1 R1 pDu DNS name', community='publiceaton', version=1)
    sbF1R2pduSession = Session(hostname='Sb F1 R2 pDu DNS name', community='publiceaton', version=1)
    sbF1R3pduSession = Session(hostname='Sb F1 R3 pDu DNS name', community='publiceaton', version=1)
    sbF1R4pduSession = Session(hostname='Sb F1 R4 pDu DNS name', community='publiceaton', version=1)
    sbF1R5pduSession = Session(hostname='Sb F1 R5 pDu DNS name', community='publiceaton', version=1)

    sbF2R1pduSession = Session(hostname='Sb F2 R1 pDu DNS name', community='publiceaton', version=1)
    sbF2R2pduSession = Session(hostname='Sb F2 R2 pDu DNS name', community='publiceaton', version=1)
    sbF2R3pduSession = Session(hostname='Sb F2 R3 pDu DNS name', community='publiceaton', version=1)
    sbF2R4pduSession = Session(hostname='Sb F2 R4 pDu DNS name', community='publiceaton', version=1)
    sbF2R5pduSession = Session(hostname='Sb F2 R5 pDu DNS name', community='publiceaton', version=1)

    SBpduF1Session = [Sb F1 r1 pDuSession, sbF1R2pDuSession, sbF1R3pDuSession, sbF1R4pDuSession, sbF1R5pDuSession]    
    SBpduF2Session = [sbF2R1pDuSession, sbF2R2pDuSession, sbF2R3pDuSession, sbF2R4pDuSession, sbF2R5pDuSession]

    #-----------------------------------------------SECTOR C (en construccion)--------------------------------------------#
    #######################################################################################################################


# Creacion de diccionarios para almacenar los valores de temperatura y humedad como "Clave: Valor". 
def deviceConfigName():

    global saRxNameTemp, sbF1RxpduNameTemp, sbF2RxpduNameTemp, saRxNameHumi, sbF1RxpduNameHumi, sbF2RxpduNameHumi

    # Lista de temperatura por area:
    saRxNameTemp = ["saR1pduTemp", "saR4pduTemp", "saR5pduTemp", "saR6pduTemp"] # ["saR2pduTemp", "saR3pduTemp"] Estas faltan conectar.  
    sbF1RxpduNameTemp = ["sbF1R1pduTemp", "sbF1R2pduTemp", "sbF1R3pduTemp", "sbF1R4pduTemp", "sbF1R5pduTemp"] # Falta continuar hasta el R10]  
    sbF2RxpduNameTemp = ["sbF2R1pduTemp", "sbF2R2pduTemp", "sbF2R3pduTemp", "sbF2R4pduTemp", "sbF2R5pduTemp"] # Falta continuar hasta el R10]

    # Lista de humedad por area:
    saRxNameHumi = ["saR1pduHumi", "saR4pduHumi", "saR5pduHumi", "saR6pduHumi"] # ["saR2pduHumi", "saR3pduHumi"]  Estas faltan conectar.
    sbF1RxpduNameHumi = ["sbF1R1pduHumi", "sbF1R2pduHumi", "sbF1R3pduHumi", "sbF1R4pduHumi", "sbF1R5pduHumi"] # Falta continuar hasta el R10]
    sbF2RxpduNameHumi = ["sbF2R1pduHumi", "sbF2R2pduHumi", "sbF2R3pduHumi", "sbF2R4pduHumi", "sbF2R5pduHumi"] # Falta continuar hasta el R10]
    

# Creacion de los datos de temperatura y humedad:
def tempHumiDataCreate():

    # Creacion de los datos de temperatura:
    for SaRx in SApduRxSession:
        saRxPduDatoTemp.append(CreacionDato.getTemperature(SaRx))      # Con el metodo append() se van agregando elementos al final de la lista. 
    
    for SbF1Rx in SBpduF1Session:
        sbF1RxPduDatoTemp.append(CreacionDato.getTemperature(SbF1Rx))      
    
    for SbF2Rx in SBpduF2Session:
        sbF2RxPduDatoTemp.append(CreacionDato.getTemperature(SbF2Rx))     

    # Creacion de los datos de humedad:
    for SaRx in SApduRxSession:
        saRxPduDatoHumi.append(CreacionDato.getHumidity(SaRx))         
    
    for SbF1Rx in SBpduF1Session:
        sbF1RXPduDatoHumi.append(CreacionDato.getHumidity(SbF1Rx))      
    
    for SbF2Rx in SBpduF2Session:
        sbF2RXPduDatoHumi.append(CreacionDato.getHumidity(SbF2Rx))   


# A partir de las listas anteriores creadas, seguidamente se harán diccionarios para manejar los valores segun el dispositivo (clave-valor). 
def sxFxRxKey_value():

    global SaKeyValueTemp, SbF1KeyValueTemp, SbF2KeyValueTemp, SaKeyValueHumi, SbF1KeyValueHumi, SbF2KeyValueHumi

    # Contiene los elementos que almacenan datos "llave-valor" respecto a la temperatura de los diferentes dispositivos según área.
    SaKeyValueTemp = {saRxNameTemp:saRxPduDatoTemp for (saRxNameTemp, saRxPduDatoTemp) in zip(saRxNameTemp, saRxPduDatoTemp)} 
    SbF1KeyValueTemp = {sbF1RxpduNameTemp:sbF1RxPduDatoTemp for (sbF1RxpduNameTemp, sbF1RxPduDatoTemp) in zip(sbF1RxpduNameTemp, sbF1RxPduDatoTemp)}
    SbF2KeyValueTemp = {sbF2RxpduNameTemp:sbF2RxPduDatoTemp for (sbF2RxpduNameTemp, sbF2RxPduDatoTemp) in zip(sbF2RxpduNameTemp, sbF2RxPduDatoTemp)}
    
    # Contiene los elementos que almacenan datos "llave-valor" respecto a la humedad de los diferentes dispositivos segun área.
    SaKeyValueHumi = {saRxNameHumi:saRxPduDatoHumi for (saRxNameHumi,saRxPduDatoHumi) in zip(saRxNameHumi, saRxPduDatoHumi)}    
    SbF1KeyValueHumi = {sbF1RxpduNameHumi:sbF1RXPduDatoHumi for (sbF1RxpduNameHumi, sbF1RXPduDatoHumi) in zip(sbF1RxpduNameHumi, sbF1RXPduDatoHumi)}
    SbF2KeyValueHumi = {sbF2RxpduNameHumi:sbF2RXPduDatoHumi for (sbF2RxpduNameHumi, sbF2RXPduDatoHumi) in zip(sbF2RxpduNameHumi, sbF2RXPduDatoHumi)}