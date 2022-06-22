## **Project Overview**

Anime adalah animasi dalam Bahasa Indonesia yang digambar baik menggunakan tangan maupun komputer. Kata [anime](https://dspace.uii.ac.id/bitstream/handle/123456789/31670/14321083%20Muhammad%20Malik%20Hamka%20Sukarman.pdf?sequence=1&isAllowed=y) merupakan singkatan dari "*animation*" dalam Bahasa Inggris, yang merujuk pada semua jenis animasi. Di luar Jepang, istilah ini digunakan secara spesifik untuk menyebutkan segala animasi yang diproduksi di Jepang. Meskipun demikian, tidak menutup kemungkinan bahwa anime dapat diproduksi di luar Jepang.

Di Indosesia sendiri, penggiat anime tidaklah sedikit. Dari mulai anak-anak hingga orang dewasa masih banyak yang menikmati karya dari negara/negeri matahari terbit tersebut. Dari banyaknya antusias masyarakat Indonesia terhadap anime, tidak menutup kemungkinan hal tersebut dapat diimplementasikan terhadap peluang dalam ranah bisnis. Merujuk dari hal tersebut, sebut saja contohnya iQIYI yang merupakan salah satu platform video daring asal Tiongkok, yang mana menyertakan berbagai anime dalam platformnya.

Sebagai penikmat anime, kita juga perlu memilah serta memilih anime dengan genre yang kita suka. Tentunya dengan memilah serta memilih genre anime yang kita suka, hal tersebut dapat memudahkan kita untuk lebih mendapatkan hiburan dari anime tersebut. Namun, dengan memilah serta memilih anime dengan genre yang kita suka secara manual, hal tersebut tentunya dapat membuang waktu kita yang seharusnya dapat lebih bisa digunakan untuk menonton anime dengan genre yang kita suka. Masalah tersebut tentunya harus diperhatikan oleh platform-platform penyedia anime seperti iQIYI untuk memudahkan penggunanya dalam memilah serta memilih anime-anime berdasarkan genre yang mereka suka. Salah satu solusi yang dapat diberikan adalah dengan menerapkan sistem rekomendasi berdasarkan model content-based filtering. Sistem rekomendasi tersebut akan memberikan beberapa rekomendasi anime berdasarkan genre yang mempunyai relevansi dengan anime yang telah ditonton atau disukai oleh pengguna. Dengan menerapkan sistem rekomendasi tersebut, diharapkan pengguna dapat lebih mudah dalam menikmati anime pada platform penyedia anime, sedangkan platform penyedia anime bisa lebih mendapatkan keuntungan dari bertambah banyaknya pengguna yang menggunakan platformnya karena menerapkan sistem rekomendasi.

Dalam proyek kali ini, akan dibuat suatu sistem rekomendasi berdasarkan model content-based filtering dengan tahapan yang sistematis mulai dari Business Understanding sampai ke Evaluation.

## **Business Understanding**

Seperti yang sudah disampaikan sebelumnya, baik platform penyedia maupun pengguna sangat ingin mendapatkan keuntungan dari aspek masing-masing. Pengguna ingin mendapatkan efisiensi dalam memilah serta memilih anime yang relevan terhadap anime yang telah ditonton atau disukai, sedangkan platform penyedia ingin mendapatkan keuntungan melalui bertambah banyaknya pengguna yang menggunakan platformnya karena menerapkan sistem rekomendasi.

### **Problem Statements**

Berdasarkan kondisi yang telah diuraikan sebelumnya, membuat sebuah sistem rekomendasi anime didasari oleh permasalahan berikut.

- Dari serangkaian variabel yang ada, variabel apa yang paling penting dalam membuat rekomendasi anime dengan model content-based filtering?
- Rekomendasi anime apa saja yang didapatkan berdasarkan genre anime yang telah ditonton atau disukai?

### **Goals**

Berdasarkan kondisi yang telah diuraikan sebelumnya, membuat sebuah sistem rekomendasi anime mempunyai tujuan sebagai berikut.

- Membuat platform penyedia anime mendapatkan lebih banyak pengguna karena menerapkan sistem rekomendasi berdasarkan genre.
- Membuat pengguna dapat mengefisiensikan waktu memilah serta memilih anime berdasarkan genre karena sistem rekomendasi yang diterapkan oleh platform penyedia anime.

### **Solution approach**

Berdasarkan kondisi serta permasalahan yang telah diuraikan sebelumnya, pada proyek ini akan dilakukan penyelesaian masalah yang relevan terhadap tujuan dengan membuat suatu sistem rekomendasi anime berdasarkan genre dengan model content-based filtering.

- **Content-based Filtering**

Sistem rekomendasi dengan content-based filtering
merekomendasikan item yang mirip dengan item sebelumnya
yang disukai atau dipilih oleh pengguna. Kemiripan item
dihitung berdasarkan pada fitur-fitur yang ada pada item
yang dibandingkan. Metode ini bersifat user
independence, tidak bergantung pada situasi apakah item
tersebut merupakan item baru (yang belum pernah dipilih
oleh pengguna manapun) maupun bukan item baru. Jika
seorang pengguna telah memesan suatu menu hidangan pada
kategori tertentu maka sistem akan mencoba
merekomendasikan menu hidangan dengan kategori serupa
yang juga tersedia di restoran lain yang mungkin akan
disukai juga oleh pengguna tersebut.

Kelemahan dari metode content-based filtering adalah
terbatasnya rekomendasi hanya pada item-item yang mirip
sehingga tidak ada kesempatan untuk mendapatkan item
yang tidak terduga.

Dalam content-based filtering diterapkan cosine similarity yang digunakan untuk menghitung kemiripan diantara item-item. Secara umum, fungsi similarity adalah fungsi yang
menerima dua buah obyek berupa bilangan riil (0 dan 1) dan
mengembalikan nilai kemiripan (similarity) antara kedua
obyek tersebut berupa bilangan riil.

Cosine similarity merupakan salah satu metode pengukuran
kemiripan yang populer. Metode ini digunakan untuk menghitung nilai kosinus sudut antara dua vektor dan
biasanya digunakan untuk mengukur kemiripan antara dua item.

## **Data Understanding**

Dataset yang akan digunakan untuk membuat sistem rekomendasi dengan model content-based filtering pada kasus ini adalah dataset yang diunduh dari kaggle yaitu [Anime Recommendations Database](https://www.kaggle.com/CooperUnion/anime-recommendations-database) dengan penggunaan penuh terhadap anime.csv.

| **Jenis** |   **Keterangan**   |
| --------- | --------------     |
|  Sumber   | [Anime Recommendations Database](https://www.kaggle.com/CooperUnion/anime-recommendations-database) |
| Lisensi   | CC0: Public Domain |
| Rating Penggunaan | 8.2 |
| Jenis dan Ukuran Berkas | CSV (112 MB) |

Untuk mengunduh dataset yang diperlukan dari kaggle dilakukan tahapan-tahapan berikut:

1. Mengunduh kaggle.json dari API token pada profil kaggle
2. Upload file kaggle.json yang telah diunduh pada colab
3. Install library kaggle
4. Membuat direktori dengan nama ".kaggle"
5. Copy "kaggle.json" ke dalam direktori yang telah dibuat
6. Mengalokasikan izin yang diperlukan untuk file tersebut
7. Mendownload dataset Anime Recommendations Database

Setelah dataset dapat diunduh, lakukan proses ekstraksi pada file dengan ekstensi zip agar dataset yang diperlukan dapat digunakan. Kemudian lakukan proses konversi dataset menjadi dataframe pada anime.csv dan tampilkan dataframe.

![dtFrm](https://github.com/GhifSmile/Anime-Recommendation-with-Content-based-Filtering/blob/master/images/Dataset.PNG)

Deskripsi dari variabel-variabel yang ada pada Anime Recommendations Database spesifik pada anime.csv adalah sebagai berikut:

- anime_id: myanimelist unik id yang mengidentifikasi sebuah anime
- nama: nama lengkap dari sebuah anime
- genre: genre dari sebuah anime
- type: tipe dari anime berdasarkan jenis anime
- episodes: banyak episode dari sebuah anime(1 jika merupakan sebuah movie)
- rating: rata-rata rating dari sebuah anime dengan skala sampai 10
- members: jumlah anggota dari komunitas pada sebuah anime

Pada tahap ini diperlukan juga analisis terhadap dataset untuk optimalisasi penggunaan yang mana langkah-langkahnya adalah sebagai berikut:

1. Melihat informasi yang ada pada dataset.

2. Melihat ada atau tidaknya nilai yang hilang pada dataset.

3. Melakukan proses analisis data dengan teknik Univariate EDA

4. Melakukan visualisasi pada variabel genre untuk mendapatkan informasi. Hal tersebut dilakukan karena variabel genre merupakan variabel penting yang akan digunakan pada model.

![vis_genre](https://github.com/GhifSmile/Anime-Recommendation-with-Content-based-Filtering/blob/master/images/vis_gen.PNG)

Dapat dilihat dari visualisasi bahwasanya jumlah genre anime comedy merupakan jumlah yang terbanyak dibanding dengan genre anime lainnya. Terlihat pula dalam visualisasi terdapat genre None yang nantinya akan didrop pada Data Preparation, karena genre tersebut hanya representasi nilai yang hilang pada genre.

## **Data Preparation**

Pada tahap ini dilakukan beberapa optimalisasi terhadap penggunaan dataset yang ada. Hal tersebut salah satunya dilakukan dengan menerapkan teknik one hot encoding pada variabel genre untuk keperluan model. Teknik one hot encoding diperlukan untuk menjadi masukan dalam fungsi cosine_similarity dari library sklearn untuk menghitung derajat kesamaan antar anime berdasarkan genre. Dalam penerapannya, akan dibuat beberapa kolom berdasarkan genre yang spesifik dengan nilai 0 atau 1 sesuai relevansi nama anime dengan tiap genrenya. Selain penerapan one hot encoding, pada tahap ini juga akan dilakukan beberapa langkah data preparation, seperti memilih variabel yang relevan dengan model dan sorting dataset berdasarkan suatu variabel.

1. Melakukan drop pada variabel yang tidak diperlukan untuk model. Drop tipe Music pada variabel type diperlukan untuk relevansi pada kasus ini yang merupakan rekomendasi anime. Kemudian lakukan drop pada variabel episodes, members, type, dan rating, karena variabel tersebut juga tidak diperlukan untuk model.

![anim_dropRslt](https://github.com/GhifSmile/Anime-Recommendation-with-Content-based-Filtering/blob/master/images/anim_dropRslt.PNG)

2. Melakukan sorting dataset dan drop duplikasi dataset berdasarkan variabel anime_id.

![dup_animDrop](https://github.com/GhifSmile/Anime-Recommendation-with-Content-based-Filtering/blob/master/images/dup_animDrop.PNG)

Setelah dilakukan beberapa tahap preparation, kini jumlah sampel tersisa 11744 dari sebelumnya berjumlah 12294.

3. Menerapkan teknik One Hot Encoding pada variabel genre untuk keperluan model dengan melakukan split pada variabel genre kemudian dibentuk suatu list, mengimplementasikan One Hot Encoding pada variabel genre, dan mengisi nan pada kolom dengan nilai 0.

![gen_splt](https://github.com/GhifSmile/Anime-Recommendation-with-Content-based-Filtering/blob/master/images/gen_valSplt.PNG)

![one_ht](https://github.com/GhifSmile/Anime-Recommendation-with-Content-based-Filtering/blob/master/images/on_htEcd.PNG)

4. Melakukan drop pada variabel yang tidak diperlukan untuk model.

![one_htFix](https://github.com/GhifSmile/Anime-Recommendation-with-Content-based-Filtering/blob/master/images/on_htEcdfix.PNG)

Setelah dilakukan preparation, kini dataset siap melalui proses modeling.

## **Modeling**

Pada tahap ini akan dibuat sistem rekomendasi berdasarkan content-based filtering dengan menerapkan fungsi cosine_similarity dari library sklearn untuk menghitung derajat kesamaan antar anime berdasarkan genre. Pada tahap ini juga akan disajikan top-N recommendation sebagai solusi.

Tahapan-tahapan yang dilakukan adalah sebagai berikut:

1. Mengambil nilai yang menjadi genre anime pada dataset.

2. Menghitung derajat kesamaan antar anime dengan teknik cosine similarity.

![cos_metrk](https://github.com/GhifSmile/Anime-Recommendation-with-Content-based-Filtering/blob/master/images/cos_metrk.PNG)

3. Melihat matriks kesamaan setiap anime.

![cos_matrx](https://github.com/GhifSmile/Anime-Recommendation-with-Content-based-Filtering/blob/master/images/sim_2.PNG)

4. Mendapatkan rekomendasi anime melalui tahapan-tahapan berikut.

    1. Membuat fungsi anime_recommendations.

        Deskripsi dari parameter fungsi anime_recommendations adalah sebagai berikut:
        
        nama_anime : nama anime (index kemiripan dataframe), tipe data string (str).
        
        similarity_data : kesamaan dataframe, simetrik, dengan name sebagai indeks dan kolom, tipe data pd.DataFrame (object).
        
        items : mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan, tipe data pd.DataFrame (object).
        
        k : banyaknya jumlah rekomendasi yang diberikan, tipe data integer (int).

    2. Melihat informasi yang ada pada nama anime untuk melihat relevansi rekomendasi. Pada tahap ini akan digunakan nama anime Pokemon sebagai rujukan.

    ![pok_rel](https://github.com/GhifSmile/Anime-Recommendation-with-Content-based-Filtering/blob/master/images/pok_rel.PNG)

    3.  Mendapatkan rekomendasi anime berdasarkan nama anime yang menjadi rujukan.

    ![rek_anim](https://github.com/GhifSmile/Anime-Recommendation-with-Content-based-Filtering/blob/master/images/rek_anim.PNG)


## **Evaluation**

![rek_anim](https://github.com/GhifSmile/Anime-Recommendation-with-Content-based-Filtering/blob/master/images/rek_anim.PNG)

Pada tahap ini hasil rekomendasi akan diuji oleh metrik Precission. Metrik Precission merupakan metrik yang mengukur presisi atau kesesuaian yang dalam kasus ini merupakan presisi dari jumlah anime relevan yang direkomendasikan terhadap jumlah anime yang direkomendasikan.

Formula dari metrik Precission:

Precission = (Jumlah rekomendasi item yang relevan)/(Jumlah item yang direkomendasikan)

Precission (dalam persen) = (5/5) * 100

Precission = 100%

Dari lima rekomendasi anime yang diberikan terdapat lima anime yang bervariasi serta relevan dengan anime yang menjadi rujukan, hal ini tentunya menginterpretasikan bahwasanya kinerja dari model cukup optimal. Dengan implementasi metrik Precission juga didapat hasil yang cukup optimal yaitu 100% rekomendasi relevan.
