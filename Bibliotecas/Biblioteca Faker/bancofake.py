import psycopg2
from faker import Faker

con = psycopg2.connect(
    host='localhost',
    database = 'spock',
    user='postgres',
    password='postgres'
)
cur=con.cursor()

fake = Faker(locale='pt-br')

base_sql='''
    INSERT INTO Seguidores
        (nome,email,usuario)
    VALUES
        ('{}','{}','{}')
'''

for i in range(1000):
    nome=fake.name()
    email=fake.email()
    usuario=fake.user_name()
    sql=base_sql.format(nome,email,usuario)
    cur.execute(sql)

con.commit()
con.close()