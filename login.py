def student_login(username, password):
    if username == password:
        return True
    return False


def admin_login(username, password):
    if username == "admin" and password == "admin123":
        return True
    return False
