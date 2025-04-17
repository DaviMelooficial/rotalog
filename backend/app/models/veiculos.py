from ..extensions import db

class Veículo(db.Model):
    __tablename__ = 'veiculos'

    ID_VEICULO = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PLACA = db.Column(db.String(7), unique=True, nullable=False, index=True)
    MARCA = db.Column(db.String(50), nullable=False)
    MODELO = db.Column(db.String(50), nullable=False)
    COR = db.Column(db.String(20), nullable=False)  # Ex: Azul, Branco, Preto, etc.
    ANO_FABRICACAO = db.Column(db.Integer, nullable=False)
    RENAVAM = db.Column(db.String(11), unique=True, nullable=False, index=True)
    CHASSI = db.Colummn(db.String(20), unique=True, nullable=False, index=True)
    TIPO_CARROCERIA = db.Column(db.String(50), nullable=False)  # Ex: refrigerado, alumínio, lonado, 3/4(3Ton), etc.
    CAPACIDADE_CARGA = db.Column(db.Float, nullable=False)  # Capacidade de carga em toneladas
    STATUS = db.Column(db.String(20), nullable=False)  # Ex: Disponível, Em uso, Manutenção, Cancelado
    ID_ROTA = db.Column(db.Integer, db.ForeignKey('rotas.ID_ROTA'), nullable=True)  # FK para a tabela de rotas será atualizado de acordo com o uso.


    def __repr__(self):         
        return (
            f'\n--- Veículo ---\n'
            f'Status: {self.STATUS}'
            f'Placa: {self.PLACA}\n'
            f'Marca: {self.MARCA}\n'
            f'Modelo: {self.MODELO}\n'
            f'Ano: {self.ANO_FABRICACAO}\n'
            #f'Cor: {self.COR}\n'
            #f'Renavam: {self.RENAVAM}\n'
            #f'Chassi: {self.CHASSI}\n'
            f'Tipo de Carroceria: {self.TIPO_CARROCERIA}\n'
            f'Capacidade de Carga: {self.CAPACIDADE_CARGA} toneladas\n'
            f'----------------\n'
        )
