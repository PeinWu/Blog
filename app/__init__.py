from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.markdown import Markdown

app = Flask(__name__)
app.config.from_object('config')


md = Markdown(app,
            extensions=['footnotes'],
            entension_configs={'footnotes':('PLACE_MARKER', '```')},
            safe_mode=True,
            output_format='html4')

db = MongoEngine(app)



from app import views,models
