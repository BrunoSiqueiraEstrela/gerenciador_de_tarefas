from sqlalchemy.types import Uuid, String, DateTime, Boolean, Enum
from sqlalchemy.schema import Column, Table
from sqlalchemy.sql import func
from uuid import uuid4
from contexto.usuario.dominio.entidades.usuario import Usuario
from libs.database.config import registro_dos_orms
from contexto.usuario.dominio.objeto_de_valor.usuario import NivelDeAcesso

tabela_usuario = Table(
    "Usuario",
    registro_dos_orms.metadata,
    Column("id", Uuid(as_uuid=True), default=uuid4, primary_key=True, index=True),
    Column("nome", String(100), nullable=False, index=True, unique=True),
    Column("email", String(100), nullable=False, index=True, unique=True),
    Column("senha", String(100), nullable=False),
    Column("nivel_de_acesso", Enum(NivelDeAcesso), nullable=False),
    Column("ativo", Boolean, nullable=False, server_default="true"),
    Column("criado_em", DateTime, nullable=False, server_default=func.now()),
    Column(
        "atualizado_em",
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    ),
    Column("deletado_em", DateTime, nullable=True),
)

usuario_orm_mapper = registro_dos_orms.map_imperatively(
    Usuario, tabela_usuario, properties={"id": tabela_usuario.c.id}
)
