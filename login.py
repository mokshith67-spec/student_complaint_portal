def student_login(username, password):
    return username == password

def admin_login(username, password):
    return username == "admin" and password == "admin123"
