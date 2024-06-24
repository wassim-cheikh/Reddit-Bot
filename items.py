class account() :
    def __init__(self,username,psswd) -> None:
        self.username=username
        self.psswd=psswd
    def __str__(self) -> str:
        return f'Username: {self.username} , password: {self.psswd}'
class vote():
    def __init__(self,url,url2,nacc) -> None:
        self.url=url
        self.url2=url2
        self.nacc=nacc
class comment():
    def __init__(self,url,url2,comment,nacc) -> None:
        self.url=url
        self.url2=url2
        self.comment=comment
        self.nacc=nacc
class join():
    def __init__(self,url,nacc) -> None:
        self.url=url
        self.nacc=nacc
