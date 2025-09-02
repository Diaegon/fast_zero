from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()

"""
 o status_code é opcional, por padrão o FastAPI retorna 200,
 mas é interessante deixar explícito e o response_model é para definir
 o modelo de resposta que a gente espera (pydantic)"""


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'hello world'}


@app.get('/ola', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def ola_html():
    return """
    <html>
        <head>
            <title>FastAPI HTML</title>
        </head>
        <body>
            <h1>Olá, Mundo!</h1>
            <p>Esta é uma resposta HTML simples.</p>
        </body>
    </html>
    """
