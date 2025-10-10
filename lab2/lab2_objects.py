class UserManager:
    CONST_OBJ = {"name": "Глеб"}
    def __init__(self):
        self.var_obj = {"name": "Иван"}

    def update_names(self):
        self.CONST_OBJ["name"] = "Александр" # все равно обновит значение, так как в Python нету неизменяемых переменных
        self.var_obj["name"] = "Петр"
        self.var_obj = {"name": "Ева"}

    def show_objects(self):
        print("CONST_OBJ:", self.CONST_OBJ)
        print("var_obj:", self.var_obj)

    @staticmethod
    def createUser(name, city):
        return {"name": name, "city": city}


if __name__ == "__main__":
    manager = UserManager()
    manager.update_names()
    manager.show_objects()
    user = UserManager.createUser("Marcus Aurelius", "Roma")
    print("user:", user)
