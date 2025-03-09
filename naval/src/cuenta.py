from typing import Tuple

class crear_cuenta:
    def __init__(self, user: str, password: str):
        self.user = user
        self.password = password
        self.list_users:list[str] = []
    
    def validar_user (self) -> Tuple [str, list[str]]:
        if self.user not in self.list_users:
            self.list_users.append(self.user)
            return (self.user, self.list_users)
        while self.user in self.list_users:
            print("Este nombre de usuario ya existe, cámbialo por otro.")
            user_change = input("Introduce otro nombre de usuario:")
            if user_change not in self.list_users:
                self.user = user_change
                return (self.user, self.list_users)


