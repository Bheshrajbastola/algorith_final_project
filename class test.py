from db import *





def main_body():
 ab= insert("admin","admin")
 assert ab=="Pass"


def test_register_student_body():
 pq = show_database_result("ram")
 assert pq == "Pass"

def test_find_student_body():
 rs = show_database_result1("Male", "Ram")
 assert rs == "Pass"

def test_add_course_body(show_database_result=None):
 dt = show_database_result("2058/2/3")
 assert dt == "Pass"

def test_Phone():
 vu = show_database_result("1234567890")
 assert vu == "Pass"
