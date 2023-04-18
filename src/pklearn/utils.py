def addone(x):
    return x+1

def main():
    print("[DEBUG] utils.main is called")
    A = 1
    print("[DEBUG] A = 1")
    print(f"[DEBUG] addone(A) -> {addone(A)}")

if __name__=="__main__":
    main()
