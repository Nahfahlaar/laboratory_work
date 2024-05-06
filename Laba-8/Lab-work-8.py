from PIL import Image, ImageDraw, ImageFont

def one():
     img = Image.open("Открытки/Открытка.jpg")

     width, height = img.size
     
     new_img = img.crop((0, 250, width, height))

     name = input("Введите имя кого хотите поздравить: ")
     draw = ImageDraw.Draw(new_img)
     font = ImageFont.truetype("arial.ttf", 50)
     text_color = (255, 0, 0)
     text_position = (340, 620)

     text = f"{name}, поздравляю!"
     draw.text(text_position, text, font=font, fill=text_color, stroke_width=2, stroke_fill="red")

     new_img.save("Открытки/Обрезанная открытка.png")

def two():
     birthday_img = Image.open("Второе задание/ДР.jpg")
     new_year_img = Image.open("Второе задание/НГ.jpg")
     victory_day_img = Image.open("Второе задание/9мая.jpg")

     holidays = {
          "День победы": victory_day_img,
          "Новый год": new_year_img,
          "День рождения": birthday_img
     }

     user_holiday = input("К какому празднику вам нужна открытка?: ")
     
     while user_holiday not in holidays:
          print("Извините, такого праздника нет в списке. Пожалуйста, выберите один из следующих праздников: ")
          for holiday in holidays.keys():
               print(holiday)
          user_holiday = input("К какому празднику вам нужна открытка? ")


     selected_holiday_img = holidays[user_holiday]
     selected_holiday_img.show()

