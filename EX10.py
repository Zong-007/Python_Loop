"""
เขียนโปรแกรม คำนวณการแลกเปลี่ยนเงิน โดย input จำนวนเงิน “12345”

Input
Amount

Output
Enter the amount you want to exchange: 12345
1000 baht =  12
100 baht =  3
20 baht =  2
5 baht =  1
 
เติม code ให้สมบูรณ์ตามเงื่อนไข

"""

denominations = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
amount = _(input("Enter the amount you want to exchange: "))

for x in _:
    count = amount // _
    if _ > 0:
        print(x ,"baht = ",count)
    amount = _ % x