import psycopg2

class UserConnection():
    conn = None
    def __init__(self):
        try:
            #self.conn = psycopg2.connect("Postresql", type="sql")
            self.conn = psycopg2.connect("dbname=postgres user=postgres.jpszycptvcptyzvvqvau password='SpotsDB_2024%' host=aws-0-us-west-1.pooler.supabase.com port=6543")
        except psycopg2.OperationalError as err:
            print(err)
            self.conn.close()
            
    def read_all(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM "users"
                """)         
            return cur.fetchall()
        
        
    def read_one(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * from users WHERE id = %s         
            """, (id))    
            return cur.fetchone()
        
         
    def write(self, data):
        with self.conn.cursor() as cur:
            
            #insert into users (name, passwd, email) VALUES ('Juan', 'Juan10001', 'juan@gmail.com')
            #print(data)
            
            #a1 ='insert into "users" (name, passwd, email) VALUES ('
            #a2 = 'Juan' + ', '
            #a3 = 'Juan10001' + ', '  
            #a4 = 'juan@gmail.com ' + ')'
            #str_query = a1+a2+a3+a4
            #print (str_query)
            #cur.execute(str_query)


            cur.execute("""
                INSERT INTO "users" (name, passwd, email) VALUES(%(name)s, %(passwd)s, %(email)s)
            """, data)
            self.conn.commit()
            
    
    def delete(self, id):
        with self.conn.cursor() as cur: 
            cur.execute ("""
                DELETE FROM "users" WHERE id = %s
            """, (id,)) 
        self.conn.commit()
        
    
    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute( """
                UPDATE "users" SET name = %(name)s, passwd = %(passwd)s, email = %(email)s WHERE id = %(id)s 
            """, data)
            self.conn.commit()
    
    def __def__(self):
        self.conn.close()