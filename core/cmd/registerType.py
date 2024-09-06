from core.cmd.type import Typecmd

class RegisterTypecmd:
    """
    этот класс не подлежит инициализации\n
    и существует для регистрации всех типов команд в types\n
    и определения их типа с помощью indentify
    """
    types: dict[str, Typecmd] = [
            Typecmd(r"\/\w*(\s+\w+)*", True)
        ]
        
    def __new__(cls) -> None:
        return None
        
    def identify(value: str, handwritten: bool) -> Typecmd | None:
        for type in RegisterTypecmd.types:
            if(type.test(value, handwritten)):
                return type 
        return None