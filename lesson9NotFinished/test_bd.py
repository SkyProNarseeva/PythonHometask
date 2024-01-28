from sqlalchemy import text
from sqlalchemy import inspect, create_engine

db_connection_string = "postgresql://x_clients_user:axcmq7V3QLCQwgL39GymqgasJhUlDbH4@dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com/x_clients"

# https://www.sqlalchemy.org/blog/2023/01/26/sqlalchemy-2.0.0-released/

def test_db_connection():
    db = create_engine(db_connection_string)
    # deprecated from version 1.4 
    # names = db.table_names()
    # https://docs.sqlalchemy.org/en/14/core/connections.html#sqlalchemy.engine.Engine.table_names

    inspection = inspect(db)
    names = inspection.get_table_names()
    assert names[1] == 'company'

def test_select():
    db = create_engine(db_connection_string)

    # execute only with the connection https://docs.sqlalchemy.org/en/14/changelog/migration_20.html#migration-20-implicit-execution

    with db.connect() as conn:
        query = text("select * from company")
        result = conn.execute(query).fetchall()
        row1 = result[0] 
        
        assert row1[0] == 3692
        assert row1[4] == "New company"   
      

def test_select():
    db = create_engine(db_connection_string)
    sql_statement = text("select * from company where id > :id")
   
    my_params = {
        'id': 3700
       # 'is_active': True
    }

    with db.connect() as conn:
        
        result = conn.execute(sql_statement, my_params).fetchall()
        assert len(result) == 25
        # row1 = result[0] 
        
        # assert row1[0] == 3692
        # assert row1[4] == "New company"  


# не работает 
def test_insert():
    db = create_engine(db_connection_string)
    sql_statement = text("insert into company(\"name\") values (:new_name)")

    my_params = {
        'new_name': 'Skypro'
    }
    with db.connect() as conn:
        result = conn.execute(sql_statement, my_params).fetchall()

 #insert into company("name") values ('My cool name')