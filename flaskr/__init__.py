from flask import Flask
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin




app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tpbzcowclxwsha:66b6d192b4265eb218cbcb032927db0b7683f57982601e5f42a2b3f17a0095ef@ec2-18-235-114-62.compute-1.amazonaws.com:5432/d53h490dvsraic'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER']='smtp.googlemail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
app.config['MAIL_USERNAME']="adedamolabasit09@gmail.com"
app.config['MAIL_PASSWORD']="Nautilus6he!"

bcrypt=Bcrypt(app)
app.config['SECRET_KEY']='d8827d6ff69e5fc8d4792ba5'

mail=Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


login_manager = LoginManager(app)
login_manager.init_app(app)



from flaskr import  app