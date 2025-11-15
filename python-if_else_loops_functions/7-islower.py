#!/usr/bin/python3
def islower(c):
    """Checks if a character is lowercase"""
    num = ord(c)
    if 97 <= num <= 122:
        return True
    return False

# Test bloku (sınaq üçün, lazım deyilsə silinə bilər)
if __name__ == "__main__":
    char = input("Bir simvol daxil et: ")
    if islower(char):
        print(f"{char} => lower")
    else:
        print(f"{char} => not lower")

