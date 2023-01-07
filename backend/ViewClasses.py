class admin:
    def __init__(self,usr_id, admin_role):
        self.usr_id = usr_id
        self.admin_role = admin_role
class user:
    def __init__(self,usr_name, usr_password,usr_cnic,usr_profile_pic,usr_address,usr_email,usr_active_status,usr_gender,usr_bio):
        self.usr_name = usr_name
        self.usr_password = usr_password
        self.usr_cnic=usr_cnic
        self.usr_profile_pic=usr_profile_pic
        self.usr_address=usr_address
        self.usr_email=usr_email
        self.usr_active_status=usr_active_status
        self.usr_gender=usr_gender
        self.usr_bio=usr_bio
class roadmap:
    def __init__(self,rd_dept,rd_semester,rd_year,rd_crs_code,rd_crs_name,rd_prac_status,rd_crs_hr,rd_crs_book,rd_crs_outline):
        self.rd_dept = rd_dept
        self.rd_semester=rd_semester
        self.rd_year = rd_year
        self.rd_crs_code = rd_crs_code
        self.rd_crs_name=rd_crs_name
        self.rd_prac_status=rd_prac_status
        self.rd_crs_hr=rd_crs_hr
        self.rd_crs_book = rd_crs_book
        self.rd_crs_outline = rd_crs_outline
class affiliated_colleges:
    def __init__(self,ac_year, ac_name,ac_student_count,ac_incharge,ac_address):
        self.ac_year = ac_year
        self.ac_name = ac_name
        self.ac_student_count = ac_student_count
        self.ac_incharge = ac_incharge
        self.ac_address = ac_address
class batch_enrollment:
    def __init__(self,batch_rd_year, batch_year_date, batch_type ):
        self.batch_rd_year = batch_rd_year
        self.batch_year_date=batch_year_date
        self.batch_type=batch_type
class college_review:
    def __init__(self,cr_complain):
        self.cr_complain=cr_complain
class department:
    def __init__(self,dep_name):
        self.dep_name=dep_name
class enrolled_department:
    def __init__(self,edept_batch_size,edept_std_count):
        self.edept_batch_size=edept_batch_size
        self.edept_std_count=edept_std_count
