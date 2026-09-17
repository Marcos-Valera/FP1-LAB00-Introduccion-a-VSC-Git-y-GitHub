from datetime import datetime

hora_actual = datetime.now().hour

if hora_actual < 12:
    print("¡Buenos días Marcos!")
elif hora_actual < 20:
    print("¡Buenas tardes Marcos!")
elif hora_actual < 23:
    print("¡Buenas noches Marcos!")