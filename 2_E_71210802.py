suhu = float(input("Masukkan suhu tubuh anda:"))

if suhu <= 31.9:
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat!")
elif suhu <= 37.5 and suhu >= 32:
    print (f"suhu Anda normal!")
elif suhu <= 50 and suhu >= 37.6:
    print (f"suhu anda: {suhu}")
    print("Anda demam! Jangan berpergian ke tempat fasilitas Umum")
elif suhu >= 50:
    print (f"suhu anda: {suhu}")
    print("Anda bukan manusia :)")
