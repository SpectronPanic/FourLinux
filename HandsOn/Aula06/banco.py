#!/usr/bin/python


import psycopg2


def conectabanco():
    try:
        con = psycopg2.connect('host=localhost user=python dbname=loja password=4linux')
        return con
    except Exception as e:
        print 'Falhou ao conectar com o banco: ', e
        raise


def cadastrarusuario(login, senha):
    try:
        con = conectabanco()
        cur = con.cursor()
        cur.execute("insert into usuarios(login, senha) \
                    values('%s', '%s')" % (login, senha))
        con.commit()
    except Exception as e:
        print 'Falhou ao cadastrar usuario: ', e
        con = conectabanco()
        con.rollback()
    finally:
        con = conectabanco()
        cur = con.cursor()
        cur.close()
        con.close()


def listarusuarios():
    try:
        con = conectabanco()
        cur = con.cursor()
        cur.execute("select * from usuarios")
        for r in cur.fetchall():
            print r
    except Exception as e:
        print 'Falhou ao listar usuarios: ', e
    finally:
        con = conectabanco()
        cur = con.cursor()
        cur.close()
        con.close()



def buscarusuario(login):
    try:
        con = conectabanco()
        cur = con.cursor()
        cur.execute("select * from usuarios where login = '%s'"%login)
        result = cur.fetchall()
        if result:
            con = conectabanco()
            cur = con.cursor()
            cur.close()
            con.close()
            return result
        else:
            print 'Usuario nao encontrado.'
    except Exception as e:
        print 'Falhou ao buscar usuario: ', e


def deletarusuario(id):
    try:
        con = conectabanco()
        cur = con.cursor()
        cur.execute("select id from usuarios where id = '%s'"%id)
        if not cur.fetchall():
            print 'Voce digitou um ID invalido.'
            return
        cur.execute("delete from usuarios where id = '%s'"%id)
        con.commit()
        print 'Usuario deletado com sucesso.'
    except Exception as e:
        print 'Falha ao deletar usuario: ', e
    finally:
        con = conectabanco()
        cur = con.cursor()
        cur.close()
        con.close()

