import psycopg2
import bcrypt

conexion1 = psycopg2.connect(database="usuarios", 
                             user="postgres", 
                             password="Vielma")

cursor1=conexion1.cursor()