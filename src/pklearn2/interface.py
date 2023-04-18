from .utils import multwo

def mulfour(x):
    return multwo(multwo(x))

def main():
    print("[DEBUG] interface.main is executed")
    B = 1
    print("[DEBUG] B = 1")
    print(f"[DEBUG] mulfour(B) --> {mulfour(B)}")

if __name__=="__main__":
    main()
