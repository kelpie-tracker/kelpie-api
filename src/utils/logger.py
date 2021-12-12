# Logs
import logging
from settings import *

# Enviando ao syslog
log = logging.getLogger('kelpie')

logging.basicConfig(level=LEVEL, format='%(levelname)s: %(message)s')
