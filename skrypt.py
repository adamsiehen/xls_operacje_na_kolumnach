import pandas as pd

#wybor pliku
data = pd.read_excel (r'wpisz sciezke pliku', dtype = {'Name':'Umowa','Value': 'string'}) 
#wymien kolumny w kolejnosci
df = pd.DataFrame(data, columns= ['Konto','R.','Umowa','Kontrahent', 'Skrót', 'Dok. księgowy', 'Typ', 'Tytułem', 'D. wystaw.', 'D. księgow.', 'D. płatności', 'Stan na dzień', 'Ilość dni', 'Rozterminowanie', 'Przeterminowanie', 'Wal.', 'Kwota WAL', 'Reszta WAL', 'Kwota PLN', 'Reszta PLN'])
print (df)
#sciezka docelowa
df.to_excel(r'tu wpisz sciezke docelowa', index = False)
