from smartphone import Smartphone

Smartphone1 = Smartphone('Samsung', 'G10', '+79173737173')
Smartphone2 = Smartphone('Xiomi', 'Note 8 pro','+795412654')
Smartphone3 = Smartphone('Nokia', '3310', '+789521466665')
Smartphone4 = Smartphone('Iphone', '11', '+79456314')
Smartphone5 = Smartphone('Galaxy','12', '+719371931')

catalog = [Smartphone1, Smartphone2, Smartphone3, Smartphone4, Smartphone5]

for i in catalog:
    print (i)