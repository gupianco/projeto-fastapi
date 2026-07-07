from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils.types import ChoiceType

# Cria a conexão do seu banco de dados
db = create_engine('sqlite:///banco.db')

# cria a base do seu banco de dados
Base = declarative_base()

# criar as classes/tabelas do banco


# Usuário
class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    nome = Column('nome', String, nullable=True)
    email = Column('email', String, nullable=False)
    senha = Column('senha', String, nullable=False)
    ativo = Column('ativo', Boolean)
    admin = Column('admin', Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


# Pedido
class Pedido(Base):
    __tablename__ = 'pedidos'

    #STATUS_PEDIDOS = [
    #    ('PENDENTE', 'PENDENTE'),
    #    ('CANCELADO', 'CANCELADO'),
    #    ('FINALIZADO', 'FINALIZADO')
    #]

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    status = Column('status', String) # pendente, cancelado, finalizado
    usuario = Column('usuario', ForeignKey('usuarios.id'))
    preco = Column('preco', Float)
    itens = relationship('ItemPedido', cascade='all, delete')

    def __init__(self, usuario, status='PENDENTE', preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status

    def calcular_preco(self):
        # percorrer todos os itens do pedido
        # somar todos os preços de todos os itens dos pedidos
        # editar o campo "preco" com o valor final do preço do pedido
        self.preco = sum(item.preco_unitario * item.quantidade for item in self.itens)

#ItensPedido
class ItemPedido(Base):
    __tablename__ = 'itens_pedido'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    quantidade = Column('quantidade', Integer)
    sabor = Column('sabor', String)
    tamanho = Column('tamanho', String)
    preco_unitario = Column('preco_unitario', Float)
    pedido = Column('pedido', ForeignKey('pedidos.id'))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.pedido = pedido
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario


# executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)

# migrar o banco de dados

# criar a migração: alembic revision --autogenerate -m "mensagem da migração"
# executar a migração: alembic upgrade head