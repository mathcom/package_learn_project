from .utils import addone

def addtwo(x):
    return addone(addone(x))

def main():
    print("[DEBUG] interface.main is executed")
    B = 1
    print("[DEBUG] B = 1")
    print(f"[DEBUG] addtwo(B) --> {addtwo(B)}")

if __name__=="__main__":
    main()
