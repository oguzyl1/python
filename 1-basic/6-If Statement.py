age = int(input("How old are you?: "))

    #şart bloğu bu şart sağlanıyorsa altındaki işlem gerçekleşir
if age == 100:
    print("You are a century old")
    #if bloğundaki şart gerçekleşmezse bu bloğa bakılır , if sağlanıyorsa buna bakılmaz
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("You haven't been born yet!")
    #if ve elif sağlanmadığı durumlarda bu blok çalışır
else:
    print("You are a child")
