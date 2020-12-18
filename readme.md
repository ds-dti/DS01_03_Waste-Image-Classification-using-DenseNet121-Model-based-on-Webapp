# Waste Image Classification using Web App based DenseNet121 Model

## Kontributor
1. Iqbal Maulana
2. Alvian Putra pamungkas
3. Ananda Putri Almira
4. Muhamad Hafizh Fajar Perdana

## Latar Belakang
Salah satu penyebab sampah menjadi berbau menyengat adalah proses pembusukan sampah organik yang terperangkap di dalam plastik dan jenis sampah anorganik lainnya, sehingga proses dekomposisi terjadi secara anaerobik dan mengeluarkan gas metana. Apabila jumlah gas metana yang dihasilkan dalam jumlah banyak teroksidasi oleh oksigen, maka dapat menimbulkan ledakan.  Sementara itu, sampah-sampah anorganik yang sebenarnya masih dapat didaur ulang justru tidak dapat didaur ulang atau nilai ekonomisnya menurun karena telah terkotori oleh sampah organik yang mengandung air dan minyak. Akibatnya sampah anorganik tersebut berakhir di Tempat Pemrosesan Akhir (TPA) karena dinilai akan membutuhkan biaya yang lebih besar apabila dilakukan proses daur ulang.

Oleh karena itu, pemilahan dari sumber menjadi sangat penting dilakukan untuk meningkatkan persentase daur ulang sampah dan mengurangi jumlah sampah yang berakhir di TPA. Apabila tiap individu terbiasa memilah sampah sedari rumah walaupun hanya dengan membedakan antara sampah organik dan anorganik, maka proses pengelolaan di TPS ataupun TPST 3R akan menjadi lebih mudah. Berdasarkan Undang-Undang Nomor 32 Tahun 2009 tentang Perlindungan dan Pengelolaan Lingkungan Hidup mengamanatkan bahwa masyarakat bertanggung jawab sebagai produsen timbulan sampah. Diharapkan masyarakat sebagai sumber timbulan yang beresiko sebagai sumber pencemar untuk ikut serta dakam sistem pengelolaan sampah. 

## Tujuan 
Fokus ke nomer 12 UN Sustainable Development "Responsible Consumption and Production" karena dapat membantu pemilahan barang sisa produksi/konsumsi atau sampah menjadi barang yang dapat terdaur ulang atau digunakan kembali sehingga perputaran atau circle limbah menjadi lebih baik. Fokus kedalam nomor 13 yaitu "climate action" karena perputaran circle limbah secara tidak langsung akan membantu pesat kepada lingkungan hidup seperti tanaman2 organik, atau sampah lainya yang dapat mengurangi dampak global warming.

## DenseNet 121
DenseNet (Dense Convolutional Network) adalah arsitektur yang berfokus untuk membuat jaringan Deep Learning menjadi lebih dalam (deep) , tetapi pada saat yang sama membuatnya lebih efisien untuk dilatih, dengan menggunakan koneksi yang lebih pendek antar layer. DenseNet merupakan jaringan neural konvolusional di mana setiap layer terhubung ke semua layer lain yang lebih deep di jaringan, yaitu, layer pertama terhubung ke layer ke-2, ke-3, ke-4 dan seterusnya, layer kedua terhubung ke layer ke-3, 4, 5 dan seterusnya.

![DenseNet 121](https://i.ibb.co/pyWqv59/Whats-App-Image-2020-12-16-at-19-12-46.jpg)


## Urutan Pembuatan
1. Gathering Data ( 3 classes, 29.504 image)
2. Preparation Data (total size image : 3.8 gb)
3. Preprocesing (Augmentation : scaling, rotating) 
4. Splitting Data ( 80 : 20 )
5. Training Data (approx. 12+- hours)
6. Hyper Parameter Tuning
7. Evaluation (82% accuracy)
8. Output (PyTorch Model)


## Implementasi lanjutan
1. Pada mikrokontroler berbentuk kamera, digunakan untuk memilah sampah pada industri daur ulang Terdapat kamera pada sebuah tong sampah untuk mengetahui dimana tempat sampah yang sesuai dengan jenis sampah
2. Aplikasi android yang lebih mobile sehingga pengguna hanya perlu mengakses model serta prediksinya dengan cepat

## Poster

![Poster DTI Klasifikasi2](https://user-images.githubusercontent.com/15316744/102346892-316f6c80-3fd2-11eb-99d8-2786b86803cb.jpg)

## Penggunaan
* Install Requirements
```
pip install -r requirements.txt
```

* Ubah directory pada main.py, app.py, index.py
* Pada python prompt masuk kedalam directory dan setting FLASKK APP

```
set FLASK_APP=index.py
```

* Jalankan flask app

```
flask run
```

## Environment

* [PyTorch](https://pytorch.org/) - The Deep Learning framework used
* [Flask](https://github.com/pallets/flask/) - Webapp Framework
* [Pillow](https://pypi.org/project/Pillow/) - Used to image model

