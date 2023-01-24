from asyncio.windows_events import NULL
from flask import Flask
from ViewClasses import *
import psycopg2
class model:
    # constructor
    def __init__(self, host, user, password, database,port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
        # self.cursor = None
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port = self.port
                # cursor = None
            )
        except Exception as e:
            print("There is error in connection", str(e))
    # Destructor
    def __del__(self):
        if self.connection != None:
            self.connection.close()

    def getRoadMapList(self):
        
        if self.connection != None:
            cursor = self.connection.cursor()
            try:
                cursor.execute('select * from public."roadmap"')
                roadMapList = cursor.fetchall()
                # print(roadMapList)
                return roadMapList
            except Exception as e:
                print("Exception in checkUserExist", str(e))
                return NULL
            finally:
                if cursor != None:
                    cursor.close()
        else:
            return NULL
    def getcourse(self, id):
        
        if self.connection != None:
            cursor = self.connection.cursor()
            try:
                cursor.execute("select * from public.roadmap where rd_id =  %s;",[id["id"]])
                course = cursor.fetchone()
                return course
            except Exception as e:
                print("Exception in Fetching Course", str(e))
                return NULL
            finally:
                if cursor != None:
                    cursor.close()
        else:
            return NULL
# Open a cursor to perform database operations
    def insertRoadmap(self, roadmap):
        if self.connection != None:
                cursor = self.connection.cursor()
                try:
                    query = 'INSERT INTO public."roadmap" (rd_dept,rd_semester,rd_year,rd_crs_code,rd_crs_name,rd_prac_status,rd_crs_hr,rd_crs_book,rd_crs_outline) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    args = ('usma', '12345', '32202-3561801-6', 'xyz.png', 'lahore', 'usma@gmail.com', 'true', 'xyzz', 'male')
                    cursor.execute(query, args)
                    self.connection.commit()
                    return True
                except Exception as e:
                    print("Exception in insertRoadmap", str(e))
                    return False
                finally:
                    if cursor != None:
                        cursor.close()
        else:
                return False
    def updateRoadmap(self, dept, course_name, course_code, ID=240):
        if self.connection != None:
            cursor = self.connection.cursor()
            try:
                query = f'''update public."roadmap" set rd_dept = {dept}, rd_crs_name = {course_name}, rd_crs_code = '{course_code}' where  rd_id = {ID};'''
                cursor.execute(query)
                self.connection.commit()
                return True
                
            except Exception as e:
                print("Exception in updateRoadmap", str(e))
                return False
            finally:
                if cursor:
                    cursor.close()
        else:
            return False
    # delete course from Roadmap
    def deleteCourse(self, ID=240):
        if self.connection != None:
            cursor = self.connection.cursor()
            try:
                query = f'delete from public."roadmap" where rd_id = {ID};'
                cursor.execute(query)
                self.connection.commit()
                return True
            except Exception as e:
                print("Exception in deleteRoadmap", str(e))
                return False
            finally:
                if cursor:
                    cursor.close()
        else:
            return False

    # delete item into inventory
# cur = conn.cursor()
# cur.execute('INSERT INTO public."user" (usr_name, usr_password, usr_cnic, usr_profile_pic, usr_address, usr_email, usr_active_status, usr_bio, usr_gender)' 
# 'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
# ('usma', '12345', '32202-3561801-6', 'xyz.png', 'lahore', 'usma@gmail.com', 'true', 'xyzz', 'male'))
# cur.execute('INSERT INTO public."admin" (admin_id,usr_id, admin_role)'
#             'VALUES (%s,%s, %s)',
#             (1,1,1)
#             )
# conn.commit()
# cur.close()
# conn.close()
# m = model('localhost', 'postgres','12345', 'ACMS','5432')
# m.getRoadMap()