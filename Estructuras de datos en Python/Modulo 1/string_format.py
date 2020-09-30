# -*- coding: utf-8 -*-
import string

name = 'Emanuel'
formatter = string.Formatter()
formatter.format('Hola {}', name)

'Hola {}'.format(name)

# Ejemplos de la funcion format
'{} + {} = {}'.format(2, 5, 7)

'{1} + {2} = {0}'.format(7, 5, 2)

'Hola {name}'.format(name = name)

'{0} + {1} = {result}'.format(2, 5, result = 7)

'{0:f} + {1:f} = {result:f}'.format(2, 5, result = 7)
'{0:.3f} + {1:.3f} = {result:.3f}'.format(2, 5, result = 7)
'{:d}'.format(25)
'{:.0f}'.format(25.50)

'Hola {name:16}'.format(name = name)
'Hola {name:<16}'.format(name = name)
'Hola {name:>16}'.format(name = name)
'Hola {name:^16}'.format(name = name)
'Hola {name:*^16s}'.format(name = name)