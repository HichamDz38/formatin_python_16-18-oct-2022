
users = []

def deco(func):
    def wraper(*args):
        status = check_login(users)
        if status:
            func(*args)
        else:
            print("you must login")
    return wraper

def check_login(users):
    if users:
        return True
    return False

@deco
def download(link):
    print("commance le telechatement")
    
@deco
def play(link, start, qutliy , speed):
    print("lecture du video")


download("https://n import quoi")
play("https://n import quoi", 60, 720, 1.5)

users = users + ["user123"]

download("https://n import quoi")
play("https://n import quoi", 60, 720, 1.5)