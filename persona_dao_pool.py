from cursor_del_pool import CursorDelPool
from pool_conexion import Conexion
from persona import Persona
from logger_base import log


class PersonaDAOPool:
    """
    DAO (Data Access Object)
    """
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []

            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)

            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona insertada: {persona}')

            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')

            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {persona}')

            return cursor.rowcount


if __name__ == '__main__':
    persona1 = Persona(nombre='Pepito', apellido='Grillo', email='p@mail.com')
    personas_insertadas = PersonaDAOPool.insertar(persona1)
    log.debug(f'Personas insertadas: {personas_insertadas}')

    # persona1 = Persona(1, 'Pepito', 'Grillo', 'p@mail.com')
    # registros_actualizados = PersonaDAOPool.actualizar(persona1)
    # log.debug(f'Personas actualizadas: {registros_actualizados}')

    # persona1 = Persona(id_persona=7)
    # personas_eliminadas = PersonaDAOPool.eliminar(persona1)
    # log.debug(f'Personas eliminadas: {personas_eliminadas}')

    personas_lista = PersonaDAOPool.seleccionar()
    for persona_lista in personas_lista:
        log.debug(persona_lista)