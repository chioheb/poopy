meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "GYATT":"singkatan dari goddamn yang sering digunakan sebagai reaksi spontan atau pujian terhadap penampilan fisik seseorang.",
            "RIZZ": "penampilan atau gaya seseorang yang dianggap keren atau stylish"
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
    # Apa yang harus kita lakukan jika kata itu ditemukan?
else:
    print("kata yang anda cari tidak ada")
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
