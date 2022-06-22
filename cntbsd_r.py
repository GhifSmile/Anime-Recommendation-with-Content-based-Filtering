# -*- coding: utf-8 -*-
"""cntBsd_R.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gl69t8slfhiwQhhVsyLBrrOcy7EvwnKK

# Sistem Rekomendasi: Rekomendasi Anime Berdasarkan Model Content-based Filtering

*Oleh : Ghifari Ismail*

*Proyek Submission 2 - Machine Learning Terapan Dicoding*

## 1. Mempersiapkan dataset

### 1.1 Menyiapkan kredensial akun Kaggle
"""

# Install library kaggle
! pip install kaggle

# Membuat direktori dengan nama ".kaggle"
! mkdir ~/.kaggle

# Copy "kaggle.json" ke dalam direktori yang telah dibuat
! cp kaggle.json ~/.kaggle/

# Mengalokasikan izin yang diperlukan untuk file tersebut
! chmod 600 ~/.kaggle/kaggle.json

"""### 1.2 Mengunduh dan menyiapkan dataset

![SS](https://github.com/GhifSmile/content_based_filtering/blob/main/Capture.PNG?raw=true)

| **Jenis** |   **Keterangan**   |
| --------- | --------------     |
|  Sumber   | [Anime Recommendations Database](https://www.kaggle.com/CooperUnion/anime-recommendations-database) |
| Lisensi   | CC0: Public Domain |
| Rating Penggunaan | 8.2 |
| Jenis dan Ukuran Berkas | CSV (112 MB) |
"""

# Mengunduh dan menyiapkan dataset 
! kaggle datasets download CooperUnion/anime-recommendations-database

# Mengekstrak zip file
import zipfile

local_zip = '/content/anime-recommendations-database.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/content')
zip_ref.close()

"""## 2. Data Understanding

### 2.1 Mengubah dataset menjadi dataframe dan melihat beberapa informasi yang ada
"""

# Mengubah dataset menjadi dataframe
import pandas as pd

anim = pd.read_csv('/content/anime.csv')

anim

"""Deskripsi dari variabel-variabel yang ada pada Anime Recommendations Database adalah sebagai berikut:

- anime_id: myanimelist unik id yang mengidentifikasi sebuah anime
- nama: nama lengkap dari sebuah anime
- genre: genre dari sebuah anime
- type: tipe dari anime berdasarkan jenis anime
- episodes: banyak episode dari sebuah anime(1 jika merupakan sebuah movie)
- rating: rata-rata rating dari sebuah anime dengan skala sampai 10
- members: jumlah anggota dari komunitas pada sebuah anime

"""

# Melihat informasi yang ada pada dataset
anim.info()

# Melihat ada tidaknya nilai yang hilang pada dataset
anim.isnull().sum()

"""### 2.2 Univariate Exploratory Data Analysis"""

# Mengetahui jumlah serta beberapa nilai yang unik pada variabel anime_id
print('Banyak anime id', len(anim.anime_id.unique()))
print('Anime id:', anim.anime_id.unique())

# Mengetahui jumlah serta beberapa nilai yang unik pada variabel name
print('Banyak nama anime', len(anim.name.unique()))
print('Nama anime:', anim.name.unique())

# Mengetahui jumlah serta beberapa nilai yang unik pada variabel genre
print('Banyak genres', len(anim.genre.unique()))
print('Genres', anim.genre.unique())

# Melakukan visualisasi pada variabel genre untuk mendapatkan informasi

import seaborn as sns
import matplotlib.pyplot as plt 
plt.style.use('ggplot')
import itertools
from collections import Counter 


anim.genre = anim.genre.fillna('None') # Mengisi nilai yang hilang pada variabel genre dengan None
genre_anime = anim.genre.apply(lambda x: x.split(', ')).values.tolist()
genre = itertools.chain(*genre_anime)
genre_count = Counter(genre)

genre_df = pd.DataFrame.from_dict(genre_count,orient='index').reset_index()
genre_df.columns = ["genre","count"]
genre_df = genre_df.sort_values('count', ascending=False)
plt.figure(figsize=(9,12))
sns.barplot(x=genre_df["count"], y=genre_df["genre"])

"""Dapat dilihat dari visualisasi bahwasanya jumlah genre anime comedy merupakan jumlah yang terbanyak dibanding dengan genre anime lainnya. Terlihat pula dalam visualisasi terdapat genre None yang nantinya akan didrop pada Data Preparation, karena genre tersebut hanya representasi nilai yang hilang pada genre."""

# Mengetahui jumlah serta beberapa nilai yang unik pada variabel type
print('Banyak tipe', len(anim['type'].unique()))
print('tipe', anim['type'].unique())

# Mengetahui jumlah serta beberapa nilai yang unik pada variabel episodes
print('Banyak akumulasi episodes', len(anim.episodes.unique()))
print('episodes', anim.episodes.unique())

# Mengetahui jumlah serta beberapa nilai yang unik pada variabel rating
print('Banyak akumulasi rating', len(anim.rating.unique()))
print('rating', anim.rating.unique())

# Mengetahui jumlah serta beberapa nilai yang unik pada variabel members
print('Banyak akumulasi members', len(anim.members.unique()))
print('members', anim.members.unique())

"""## 3. Data Preparation

### 3.1 Melakukan drop pada variabel yang tidak diperlukan untuk model
"""

# Melihat jumlah tipe Music pada variabel type untuk didrop
msc = (anim['type']=='Music').sum()
# Melihat jumlah genre None pada variabel genre untuk didrop
genr = (anim['genre']=='None').sum()

print(msc)
print(genr)

"""Menghilangkan tipe Music pada variabel type diperlukan untuk relevansi pada kasus ini yang merupakan rekomendasi anime. """

# Memilih dataset dengan tidak menyertakan tipe Music pada variabel type dan genre None pada variabel genre
anim = anim.loc[(anim['type']!='Music')]
anim = anim.loc[(anim['genre']!='None')]
anim.shape

# Melakukan drop pada variabel yang tidak diperlukan untuk model
anim = anim.drop(columns=['episodes', 'members', 'type', 'rating'])

# Melihat lima sampel awal pada dataset
anim.head()

# Melakukan drop pada sampel dengan nilai yang hilang untuk antisipasi
anim_new = anim.dropna()

# Melihat ada tidaknya nilai yang hilang setelah melakukan drop
anim_new.isnull().sum()

# Melihat dataset pada dataframe setelah memilah serta memilih variabel yang diperlukan untuk model
anim_new

"""Setelah dilakukan beberapa tahap data preparation, kini jumlah sampel tersisa 11744 dari sebelumnya berjumlah 12294.

### 3.2 Melakukan sorting dataset dan drop duplikasi dataset berdasarkan variabel anime_id
"""

# Melakukan sorting pada dataset berdasarkan anime_id
anim_new = anim_new.sort_values('anime_id', ascending=True)

# Melihat dataset pada dataframe setelah disorting
anim_new

# Melakukan drop duplikasi pada dataset berdasarkan anime_id
anim_new = anim_new.drop_duplicates('anime_id')
anim_new

"""### 3.3 Menerapkan teknik One Hot Encoding pada variabel genre untuk keperluan model"""

# Melakukan split pada variabel genre, kemudian dibentuk suatu list
anim_new['genre']=anim_new['genre'].str.split(',')
anim_new.head()

# Mengimplementasikan One Hot Encoding pada variabel genre
for index,row in anim_new.iterrows():
    for genres in row['genre']:
        anim_new.at[index,genres] = 1

# Mengisi nan pada kolom dengan 0
anim_new = anim_new.fillna(0)
anim_new.head()

"""### 3.4 Melakukan drop pada variabel yang tidak diperlukan untuk model"""

# Melakukan drop pada variabel anime_id dan genre
anim_new = anim_new.drop(columns=['anime_id', 'genre'])
anim_new

"""## 4. Modeling

### 4.1 Mengambil nilai yang menjadi genre anime pada dataset
"""

# Mengambil nilai yang menjadi genre anime pada dataset
gen = anim_new.iloc[:,1:].values
gen.shape

"""### 4.2 Menghitung derajat kesamaan antar anime dengan teknik cosine similarity"""

from sklearn.metrics.pairwise import cosine_similarity
 
# Menghitung cosine similarity pada matrix gen
cosine_sim = cosine_similarity(gen) 
cosine_sim

"""### 4.3 Melihat matriks kesamaan setiap anime"""

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama anime
cosine_sim_df = pd.DataFrame(cosine_sim, index=anim_new['name'], columns=anim_new['name'])
print('Shape:', cosine_sim_df.shape)
 
# Melihat similarity matrix pada setiap anime dengan hanya menampilkan beberapa saja
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""### 4.4 Mendapatkan rekomendasi anime

#### 4.4.1 Membuat fungsi anime_recommendations
"""

def anime_recommendations(nama_anime, similarity_data=cosine_sim_df, items=anim[['name', 'genre']], k=5):
    
    """
    Rekomendasi anime berdasarkan kemiripan dataframe
 
    Parameter:
    ---
    nama_anime : tipe data string (str)
                 Nama anime (index kemiripan dataframe)
    similarity_data : tipe data pd.DataFrame (object)
                      Kesamaan dataframe, simetrik, dengan name sebagai 
                      indeks dan kolom
    items : tipe data pd.DataFrame (object)
            Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan
    k : tipe data integer (int)
        Banyaknya jumlah rekomendasi yang diberikan
    ---
 
 
    Pada index ini, kita mengambil k dengan nilai similarity terbesar 
    pada index matrix yang diberikan (i).
    """
 
    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan    
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,nama_anime].to_numpy().argpartition(
        range(-1, -k, -1))
    
    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    
    # Drop nama_anime agar nama anime yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(nama_anime, errors='ignore')
 
    return pd.DataFrame(closest).merge(items).head(k)

"""#### 4.4.2 Melihat informasi yang ada pada nama anime untuk melihat relevansi rekomendasi"""

# Melihat informasi yang ada pada nama anime untuk melihat relevansi rekomendasi
anim[anim.name.eq('Pokemon')]

"""#### 4.4.3 Mendapatkan rekomendasi anime berdasarkan nama anime yang menjadi rujukan"""

# Mendapatkan rekomendasi anime
anime_recommendations('Pokemon')

"""Rekomendasi yang diberikan terhadap anime yang menjadi rujukan bervariasi serta relevan, hal tersebut menginterpretasikan bahwasanya model yang dibuat memiliki kinerja yang cukup baik.

## 5. Evaluation

### 5.1 Penggunaan metrik Precission

Formula dari metrik Precission:

Precission = (Jumlah rekomendasi item yang relevan)/(Jumlah item yang direkomendasikan)

Precission (dalam persen) = (5/5) * 100

Precission = 100%

Dari lima rekomendasi anime yang diberikan terdapat lima anime yang bervariasi serta relevan dengan anime yang menjadi rujukan, hal ini tentunya menginterpretasikan bahwasanya kinerja dari model cukup optimal. Dengan implementasi metrik Precission juga didapat hasil yang cukup optimal yaitu 100% rekomendasi relevan.
"""