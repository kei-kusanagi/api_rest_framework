from fastapi import FastAPI

from database import database as connection


app = FastAPI(
    title='prueva de FastAPI',
    description='Provando ando esto de FastAPI que segun muy muy rapida',
    version='1.0.1'
)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

@app.get('/')
async def index():
    return('Hola mundo soy una FastAPI')

@app.get('/about')
async def about():
    return ('bla bla bla bla')