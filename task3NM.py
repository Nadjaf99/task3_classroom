# Tapşırıq 1: 

# İstifadəçidən boyu ilə bağlı məlumat alan və ona tövsiyə olunan ideal cəki aralığını göstərən proqram hazırlayın. 
 
    
# Əhatə olunan biliklər: İnput, Variables, Float, If...Else.
# note: Body_Mass_Index_(bmi)




weight = float(input("enter in weight: "))
height = float(input("Enter your height in centimeters: "))

bmi = weight / ((height / 100) ** 2)

if bmi < 18.5:
   print("Weak")
elif 18.5 <= bmi < 25:
   print("Normal")
elif 25 <= bmi < 30:
   print("Overweight")
else:
   print("Obese")





# Tapşırıq 2: 

# Tapşırıq: Onlayn mağaza üçün alış-veriş səbəti sistemini simulyasiya edən proqram hazırlayın. İstifadəçilərə səbətinə əşyalar əlavə etməyə, vergilər(18% ədv ümumi qiymetin üzərinə gəlməlidir) daxil olmaqla ümumi dəyəri hesablamağa kömək edir. əgər ümumi qiymət (ədv daxil) 50 azn dən çox olarsa istifadəciyə ən sonra 10 azn lik kupon qazandınız mesajını verin. əgər ümumi qiymət (ədv daxil) 100 azn dən çox olarsa istifadəciyə ən sonra 15 azn lik kupon qazandınız mesajını verin. İstifadəçi səbətə 5 dəfə məhsul əlavə edə bilər.
    
    
# Əhatə olunan biliklər: İnput, Variables, List, Float, Dictionaries, Əsas Operatorlar, If...Else.


basket = [] 
total_price = 0 
coupon = 0 

for _ in range(5): 
        product_name = input("Enter the product name: ")
        product_price = float(input("Enter the price of the product (AZN): "))
        basket.append({"name": product_name, "price": product_price})
        total_price += product_price
        

total_price_with_taxes = total_price * 1.18

if total_price_with_taxes > 100:
        coupon = 15
elif total_price_with_taxes > 50:
        coupon = 10

print("-"*39)
print("basket Contents:")


for mzada in basket:
    print(mzada)
print("-"*39)
print("Total Price (including VAT(ƏDV)):",total_price_with_taxes ,"AZN")

if coupon > 0:
    print(coupon, "AZN lik kupon qazandiniz!(You won a coupon worth AZN!)")

print("-"*70)
print(basket)





# Tapşırıq 3: 

# Müştəriyə səyahətin ümumi dəyərini hesablamaq üçün nəqliyyat şirkətinə Python proqramı yazın. İstifadəçidən səyahət məsafəsini və nəqliyyat vasitəsinin növünü (məsələn, avtomobil, yük maşını, avtobus) daxil etməyi təklif edin. Verilən məsafəyə və nəqliyyat vasitəsinin növünə əsaslanaraq ümumi dəyəri hesablayın (avtomobillərin hər km üçün 0,50 dollar, yük maşınlarının hər km üçün 1,00 dollar, avtobusların hər km üçün qiyməti 2,00 dollar).


# Əhatə olunan biliklər: İnput, Variables, Float, Əsas Operatorlar, If...Else.




distance = float(input("Enter the travel distance in km: "))
vehicle_type = input("Enter the type of vehicle (car, truck, bus): ")

if vehicle_type == "car":
        price_per_km = 0.50
elif vehicle_type == "truck":
        price_per_km = 1.00
elif vehicle_type == "bus":
        price_per_km = 2.00
else:
    print("Please enter the correct vehicle type!")
    
total_cost = distance * price_per_km
print("Total cost of the trip:", total_cost,"$")


