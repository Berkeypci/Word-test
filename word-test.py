import pandas as pd
import random

# Kelime listesi excel dosyası
file_name = "kelimeler.xlsx"

# Excel dosyasını okuyun
df = pd.read_excel(file_name)

# Toplam puan
score = 0

# Oyun döngüsü
while score < 20:
    # Rastgele kelime seçin
    word = random.choice(df["kelimeler"])
    
    # Ekrana kelimeyi yazdırın ve kullanıcıdan tahmin isteyin
    guess = input(f"What is the English meaning of '{word}'? ")
    
    # Tahmin doğruysa, puanı artırın
    if guess.lower() == df.loc[df["kelimeler"]==word, "anlamlar"].values[0].lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect. Try again.")
    
    # Kullanıcının mevcut puanını yazdırın
    print(f"Score: {score}")
    
# Oyun tamamlandı
print("Daily goal completed!")