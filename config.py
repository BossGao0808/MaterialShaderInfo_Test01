# 数据库的配置信息

HOSTNAME = '1.15.179.226'
PORT     = '3306'
DATABASE = 'astro_shader'  # 对应数据库的名称
USERNAME = 'Astro_Shader'
PASSWORD = 'CcDY6AMEDK8W5Lft'
DB_URI   = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI=DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY='secret_key'


# 邮箱配置
# 暂时使用的是QQ邮箱
MAIL_SERVER='smtp.qq.com'
MAIL_PORT= 465
MAIL_USE_LTS= False
MAIL_USE_SSL=True
MAIL_DEBUG=True
MAIL_USERNAME='1076993716@qq.com'
MAIL_PASSWORD='dylpgyszywizibaa'
MAIL_DEFAULT_SENDER= '1076993716@qq.com'






