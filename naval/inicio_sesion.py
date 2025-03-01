from cuenta import crear_cuenta

class inicio_sesion:
    def __init__(self,user:str, password:str):
        self.user = user
        self.password = password

    def sesion(self):