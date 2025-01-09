import os

SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
PWD = os.path.abspath(os.curdir)

DEBUG = True # En despliegue esto pasa a FALSE

SQLALCHEMY_DATABASE_URI = 'postgresql://proyecto_tienda_8_2_user:1hkh9kVrSDQZyLVRBUuzEggajC4DoIeG@dpg-ctvp1qrtq21c73ah7i0g-a.frankfurt-postgres.render.com/proyecto_tienda_8_2'
# SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Ejemplo basico de postgresql
# Comparalo con ejemplo de Mysql
#SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://root:password@localhost/base_datos'
#SQLALCHEMY_TRACK_MODIFICATIONS=False

