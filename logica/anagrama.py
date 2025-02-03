def is_anagrama(palabra1: str, palabra2: str)  -> bool:
    if palabra1 == palabra2:
        return False
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    return sorted(palabra1) == sorted(palabra2)


print(is_anagrama("rmoa", "roma"))
