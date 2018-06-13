from flask import Flask
import os
from config import Config
template_dir = os.path.abspath('/appdata/app/build/template')
static = os.path.abspath('/appdata/app/build/assets')

app = Flask(__name__, template_folder=template_dir, static_folder=static)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
from app import routes