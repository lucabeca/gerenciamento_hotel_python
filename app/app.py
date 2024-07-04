from flask import Flask
from controllers.cliente_controller import cliente_blueprint
from controllers.endereco_controller import endereco_blueprint
from controllers.hotel_controller import hotel_blueprint
from controllers.quarto_controller import quarto_blueprint
from controllers.reserva_controller import reserva_blueprint
from controllers.reserva_detalhe_controller import reserva_detalhe_blueprint
from controllers.tipo_quarto_controller import tipo_quarto_blueprint

app = Flask(__name__)

app.register_blueprint(cliente_blueprint, url_prefix='/clientes')
app.register_blueprint(endereco_blueprint, url_prefix='/enderecos')
app.register_blueprint(hotel_blueprint, url_prefix='/hoteis')
app.register_blueprint(quarto_blueprint, url_prefix='/quartos')
app.register_blueprint(reserva_blueprint, url_prefix='/reservas')
app.register_blueprint(reserva_detalhe_blueprint, url_prefix='/reserva-detalhes')
app.register_blueprint(tipo_quarto_blueprint, url_prefix='/tipo-quartos')

if __name__ == '__main__':
    app.run(debug=True)
