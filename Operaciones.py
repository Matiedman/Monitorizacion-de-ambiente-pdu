# Se hacen operaciones matematicas para obtener los promedios de temperatura 
# y humedad para cada sector. Ademas, se obtienen las temperaturas y humedad 
# de ambos extremos de los mismos. 

# Descomentar y probar una vez que el funcionamiento fisico de cada dispositivo, segun sector, este correcto. 


# Obtencion de los promedios de cada pdu de los valores de temperatura y humedad por sector. Se toma con un decimal.  
def saPromedioTemp(SaKeyValueTemp):
    
    dataAuxTempSa = 0
    dicSizeSa = len(SaKeyValueTemp)
    
    for RxTempValue in SaKeyValueTemp.values():
        dataAuxTempSa += RxTempValue
    
    auxTempPromSa = dataAuxTempSa/dicSizeSa
    saTempProm = round(auxTempPromSa, 1)
    
    return saTempProm

def saPromedioHumi(SaKeyValueHumi):
    
    dataAuxHumiSa = 0
    dicSizeSa = len(SaKeyValueHumi)
    
    for RxHumiValue in SaKeyValueHumi.values():
        dataAuxHumiSa += RxHumiValue
        
    auxHumiPromSa = dataAuxHumiSa/dicSizeSa
    saHumiProm = round(auxHumiPromSa, 1)
    
    return saHumiProm

def sbPromedioTemp(SbF1KeyValueTemp, SbF2KeyValueTemp):

    dataAuxTempF1, dataAuxTempF2 = 0, 0
    dicSizeSbF1 = len(SbF1KeyValueTemp)
    dicSizeSbF2 = len(SbF2KeyValueTemp)

    for F1RxTempValue in SbF1KeyValueTemp.values():
        dataAuxTempF1 += F1RxTempValue

    for F2RxTempValue in SbF2KeyValueTemp.values():
         dataAuxTempF2 += F2RxTempValue

    auxTempPromF1 = dataAuxTempF1/dicSizeSbF1
    auxTempPromF2 = dataAuxTempF2/dicSizeSbF2
    sbTempProm = round((auxTempPromF1 + auxTempPromF2)/2, 1)

    return sbTempProm



def sbPromedioHumi(SbF1KeyValueHumi, SbF2KeyValueHumi):

    dataAuxHumiF1, dataAuxHumiF2 = 0, 0
    dicSizeSbF1 = len(SbF1KeyValueHumi)
    dicSizeSbF2 = len(SbF2KeyValueHumi)

    for F1RxHumiValue in SbF1KeyValueHumi.values():
        dataAuxHumiF1 += F1RxHumiValue

    for F2RxHumiValue in SbF2KeyValueHumi.values():
        dataAuxHumiF2 += F2RxHumiValue

    auxHumiPromF1 = dataAuxHumiF1/dicSizeSbF1
    auxHumiPromF2 = dataAuxHumiF2/dicSizeSbF2

    sbHumiProm = round((auxHumiPromF1 + auxHumiPromF2)/2, 1)

    return sbHumiProm


def scPromedioTemp(ScF1KeyValueTemp, ScF2KeyValueTemp):
    return
def scPromedioHumi(ScF1KeyValueHumi, ScF2KeyValueHumi):
    return

# Obtencion de los valores extremos izquierdo de los pdu por sector de temperatura y humedad.   
def saLeftLimitTemp(saR1pduTemp, saR4pduTemp):
    
    leftAverageTemp = round((saR1pduTemp + saR4pduTemp)/2, 1)
    return leftAverageTemp

def saLeftLimitHumi(saR1pduHumi, saR4pduHumi):
    
    leftAverageHumi = round((saR1pduHumi + saR4pduHumi)/2, 1)
    
    return leftAverageHumi

def sbLeftLimitTemp(sbF1R1pduTemp, sbF2R1pduTemp):

    leftAverageTemp = round((sbF1R1pduTemp + sbF2R1pduTemp)/2, 1)
    return leftAverageTemp

def sbLeftLimitHumi(sbF1R1pduHumi, sbF2R1pduHumi):

    leftAverageHumi = round((sbF1R1pduHumi + sbF2R1pduHumi)/2, 1)
    return leftAverageHumi



def scLeftLimitTemp():
    return

def scLeftLimitHumi():
    return

# Obtencion de los valores extremos derecho de los pdu por sector de temperatura y humedad. 
def saRightLimitTemp():
    return

def saRightLimitHumi():
    return

def sbRightLimitTemp():
    return

def sbRightLimitHumi():
    return

def scRightLimitTemp():
    return

def scRightLimitHumi():
    return
