# utils/sheets.py

from google.oauth2.service_account import Credentials
import gspread

def read_google_sheet():
    # Autenticación con las credenciales del servicio
    scope = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = Credentials.from_service_account_file(
        'E:/SANTIAGO/industria 4.0 maxtich/django/python-422510-abce513d6cfc.json', scopes=scope)
    client = gspread.authorize(credentials)
    
    # Abre la hoja de cálculo por su ID
    sheet = client.open_by_key('1rU0MZNV0kf8xEDwiDDl5Go0V1EJtmbcSzY8CXy03N5s')
    
    # Accede a la hoja de trabajo por su índice o nombre
    worksheet = sheet.get_worksheet(0)  # Por ejemplo, la primera hoja
    
    produccion_actual = worksheet.acell('D30').value
    eficiencia = worksheet.acell('D31').value
    cantidad_defectos = worksheet.acell('D32').value
    calidad = worksheet.acell('D33').value
    minutos_indisponibilidad = worksheet.acell('D34').value
    disponibilidad = worksheet.acell('D35').value
    oee = worksheet.acell('E33').value
        
    print(produccion_actual, eficiencia, cantidad_defectos, calidad, minutos_indisponibilidad, disponibilidad, oee)
        
    return {
        'produccion_actual': produccion_actual,
        'eficiencia': eficiencia,
        'cantidad_defectos': cantidad_defectos,
        'calidad': calidad,
        'minutos_indisponibilidad': minutos_indisponibilidad,
        'disponibilidad': disponibilidad,
        'oee': oee
    }