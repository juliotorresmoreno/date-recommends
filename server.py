import sys
sys.path.append(".")
from boot.started import configure
from routes import index
from app import *

configure()

index.configure()
