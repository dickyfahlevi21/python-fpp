def Trim(val, limit):
    info = (val[:limit] + "...") if limit > 7 else val
    return info

tulisan_panjang = Trim("ini adalah tulisan yang sangat panjang",8)
print(tulisan_panjang)