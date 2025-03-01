from typing import Tuple

class crear_cuenta:
    def __init__(self, user: str, password: str, name_player: str,list_users:list[str] = [], list_name_player: list[str]  = [] ):
        self.user = user
        self.password = password
        self.name_player = name_player
        self.list_name_player = list_name_player
        self.list_users = list_users
    
    def validar_user (self) -> Tuple [str, list[str]]:
        if self.user not in self.list_users:
            self.list_users.append(self.user)
            return (self.user, self.list_users)
        while self.user in self.list_users:
            print("Este nombre de usuario ya existe, cámbialo por otro.")
            user_change = input("Introduce otro nombre de usuario:")
            if user_change not in self.list_name_player:
                self.user = user_change
                return (self.user, self.list_users)


    def validar_name(self) -> Tuple[str, list[str]]:

        if self.name_player not in self.list_name_player:
            self.list_name_player.append(self.name_player)
            return (self.name_player, self.list_name_player)

        while self.name_player in self.list_name_player:
            print("Este nombre de usuario ya existe, cámbialo por otro.")
            name_change = input("Introduce otro nombre de usuario:")
            if name_change not in self.list_name_player:
                self.name_player = name_change
                return (self.name_player, self.list_name_player)


prueba = crear_cuenta("camilo", "mateo", "julian")
print(prueba.validar_user())
print(prueba.validar_name())

