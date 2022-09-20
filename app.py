from flask import Flask,render_template
import config
from exts import db,mail
from blueprints import user_bp,shaderinfo_bp
from flask_migrate import Migrate

# testtest2

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)



migrate = Migrate(app,db)

app.register_blueprint(user_bp)
app.register_blueprint(shaderinfo_bp)



if __name__ == '__main__':
    app.run()
