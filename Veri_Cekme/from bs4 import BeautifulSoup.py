import firebase_admin
from firebase_admin import credentials, firestore
import requests
from bs4 import BeautifulSoup
import time

# Firebase ayarları
cred = credentials.Certificate("C:/Users/Kenan/Downloads/scolar-59dd7-firebase-adminsdk-v3lke-3302e5f125.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Google Scholar'dan verileri çekme
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
akademisyen = requests.get("https://scholar.google.com/citations?hl=tr&user=3EiBtZEAAAAJ", headers=headers)
time.sleep(3)

soup = BeautifulSoup(akademisyen.content, 'html.parser')

# Akademisyen bilgilerini çekme
baslik = soup.find(id="gsc_prf_inw").get_text()
atif = soup.find_all(class_="gsc_rsb_std")[0].get_text()
h_indeks = soup.find_all(class_="gsc_rsb_std")[2].get_text()
i10_indeks = soup.find_all(class_="gsc_rsb_std")[4].get_text()

# Firebase Firestore'a verileri ekleme
doc_ref = db.collection("Universiteler").document("Firat Universitesi").collection("Yapay Zeka ve Veri Mühendisligi").document()
doc_ref.set({
    "isim": baslik,
    "alıntı sayısı": atif,
    "h-endeksi": h_indeks,
    "i10-endeksi": i10_indeks
})

print(f"Veriler Firebase'e kaydedildi: {baslik}")