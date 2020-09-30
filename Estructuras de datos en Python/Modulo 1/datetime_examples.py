# -*- coding: utf-8 -*-
import datetime

# date objects
# El dia 6 de Abril de 1991.
date = datetime.date(1991,4,6)

# Atributo año de la fecha
date.year
# Atributo mes de la fecha
date.month
# Atributo dia de la fecha
date.day

# Devuelve el dia de la semana. El lunes es el 0 y el Domingo es el 6.
date.weekday()
# Devuelve el dia de la semana. El lunes es el 1 y el Domingo es el 7.
date.isoweekday()
# Devuelve una tupla con 3 elementos: año, numero de semana, dia de la semana
date.isocalendar()
# Devuelve una fecha como un string con el formato 'YYYY-MM-DD'
date.isoformat()

# Fecha minima
date_min = datetime.date.min
# Fecha maxima
date_max = datetime.date.max

# El dia de hoy
today = datetime.date.today()

# EL dia de ayer
yesterday = today - datetime.timedelta(days=1)

# Resta de dos fechas
delta = today - yesterday

# datetime objects
# El dia 15 de Septiempre de 2019 a las 6:04:06
date_and_time = datetime.datetime(2019,9,15,6,4,6)

# Atributo año de la fecha y hora
date_and_time.year
# Atributo mes de la fecha y hora
date_and_time.month
# Atributo dia de la fecha y hora
date_and_time.day
# Atributo hora de la fecha y hora
date_and_time.hour
# Atributo minuto de la fecha y hora
date_and_time.minute
# Atributo segundo de la fecha y hora
date_and_time.second
# Atributo microsegundo de la fecha y hora
date_and_time.microsecond

# Obtengo un objeto date a partir del objeto datetime
date_and_time.date()

# La fecha y hora actual (local)
now = datetime.datetime.now()

# La fecha y la hora actual en UTC (Coordinated Universal Time)
now = datetime.datetime.utcnow()


# time objects
# La hora 10:20:35
time = datetime.time(10, 20, 35)
# Atributo hora de la hora
time.hour
# Atributo minuto de la hora
time.minute
# Atributo segundo de la hora
time.second
# Atributo microsegundo de la hora
time.microsecond

# Hora minima
time_min = datetime.time.min
# Hora maxima
time_max = datetime.time.max