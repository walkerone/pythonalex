# -*- coding: utf-8 -*-

def auth(auth_type):
    def outwrapper(func):
        def wrapper(*args, **kwargs):
            _usenrname = "walker"
            _password = "walker123"
            username = input("yourname:").strip()
            password = input("password:").strip()
            print(*args)
            print(**kwargs)
            if auth_type == "local":
                if username == _usenrname and password == _password:
                    print("right")
                    func()
                else:
                    print("valid zccount or name")
            elif auth_type == "reomto":
                _usename = "remoteusename"
                _password = "remotepassword"
                username = input("yourname:").strip()
                password = input("password:").strip()
                if auth_type == "local":
                    if username == _usenrname and password == _password:
                        print("right")
                        func()
                    else:
                        print("valid zccount or name")

        return wrapper

    return outwrapper


@auth(auth_type="local")
def home(*args, **kwargs):
    print("welcome to home page")


@auth(auth_type="reomto")
def index():
    print("welcome to index")


home("walker", "walker123")
print("-----")
index()

