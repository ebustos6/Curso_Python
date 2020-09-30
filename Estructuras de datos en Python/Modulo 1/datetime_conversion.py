# -*- coding: utf-8 -*-
import datetime

date_and_time = datetime.datetime(1991,4,6,12,5,32)

# La funcion strftime crea un string a partir de un objeto datetime
date_and_time.strftime('%Y-%m-%d')
date_and_time.strftime('%Y-%m-%d %H:%M:%S')
date_and_time.strftime('%Y/%m/%d')
date_and_time.strftime('%Y-%m-%d T%H:%M:%S')

# La funcion strptime crea un objeto datetime a partir de un string
datetime.datetime.strptime('1992-09-15', '%Y-%m-%d')
datetime.datetime.strptime('1992-09-15 11:30:25', '%Y-%m-%d %H:%M:%S')
datetime.datetime.strptime('1992-09-15 T11:30:25', '%Y-%m-%d T%H:%M:%S')


