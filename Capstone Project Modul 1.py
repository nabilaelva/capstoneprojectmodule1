from prettytable import PrettyTable

x = PrettyTable()

data = {
  1: {
    "Category": "Design",
    "Business Name": "Stane & Felice Interior Design",
    "Address": "The Oak Tower Apartment",
    "Phone": "081584020146",
    "Website": "stanefelice.com"
  },
  2: {
    "Category": "Restaurant",
    "Business Name": "Canting Restaurant",
    "Address": "Galeria Mall",
    "Phone": "08158992390",
    "Website": "canting.com"
  },
  3: {
    "Category": "Hotel",
    "Business Name": "Clear Hotel",
    "Address": "Jl. Malioboro",
    "Phone": "088978675645",
    "Website": "clearhotel.com"
  },
  4: {
    "Category": "Electronics",
    "Business Name": "Home Living Electronics",
    "Address": "Tunjungan Mall",
    "Phone": "081231378380",
    "Website": "homeliving.com"
  },
  5: {
    "Category": "Property",
    "Business Name": "Fleekhaus Residence",
    "Address": "BSD City",
    "Phone": "080895041095",
    "Website": "felekhaus.com"
  }
}

keys = [n for n in data.keys()]
for in_key in keys:
  innerKey = list(data[in_key].keys())
  # print(innerKey)


def showAllData():
  # values = [n for n in data.values()]
  x = PrettyTable()
  allValues = []
  for n in list(data.keys()):
    innerValues = list(data[n].values())
    allValues.append(innerValues)
  # print(allValues)

  x.field_names = innerKey
  x.add_rows(allValues)
  print(x)


def showSpecificData(in_key):
  x = PrettyTable()
  allValues = []
  innerValues = list(data[in_key].values())
  allValues.append(innerValues)
  # print(allValues)

  x.field_names = innerKey
  x.add_rows(allValues)
  print(x)


def main_menu():
  print("========= Aplikasi Yellow Pages =========")
  print("1. Akses Data Yellow Page")
  print("2. Add Data Yellow Page")
  print("3. Update/Edit Data Yellow Page")
  print("4. Delete Data Yellow Page")
  print("5. Exit")

  pilihan_menu = int(input("\nSilakan Pilih Menu (1-5) : "))

  if (pilihan_menu == 1):
    access_data()
  elif (pilihan_menu == 2):
    add_data()
  elif (pilihan_menu == 3):
    update_data()
  elif (pilihan_menu == 4):
    delete_data()
  elif (pilihan_menu == 5):
    print("\nApakah Anda yakin akan keluar dari aplikasi?")
    print("1. Ya")
    print("2. Tidak")
    pilihan_exit = int(input("Silakan masukkan pilihan Anda (1-2): "))
    if (pilihan_exit == 1):
      print("\nTerima kasih dan sampai jumpa kembali.")
    elif (pilihan_exit == 2):
      print("\nAnda akan kembali ke Menu Utama\n")
      main_menu()
    else:
      print(
        "\nPilihan yang Anda masukkan salah. Anda akan kembali ke Menu Utama\n"
      )
      main_menu()
  else:
    # clear_screen()
    print("\n********* Pilihan yang anda masukkan Salah *********\n")
    main_menu()


# mau data tertentu atau semuanya?
def access_data():
  print("\n========= Anda akan mengakses data pada Yellow Pages =========")
  print("1. Akses Seluruh Data")
  print("2. Akses Data Tertentu")
  print("3. Kembali ke Menu Utama")
  access_request = int(input("Silakan Pilih Sub Menu Akses Data (1-3): "))
  if (access_request == 1):
    print("\nSeluruh Data Yellow Page\n")
    showAllData()
  elif (access_request == 2):
    print("\nBagaimana Anda akan mengakses data?")
    print("1. Melalui Kategori")
    print("2. Melalui Business Name")
    print("3. Kembali ke Menu Sebelumnya")
    access_by = int(input("\nPilihan akses data (1-3): "))

    if (access_by == 3):
      access_data()
    elif (access_by == 1):
      print("\nPilihan kategori data")
      print("1. Design")
      print("2. Restaurant")
      print("3. Hotel")
      print("4. Elektronik")
      print("5. Property")
      input_cat = int(input("\nMasukkan Pilihan Kategori: "))
      if input_cat in data.keys():
        showSpecificData(input_cat)
      else:
        print("********** Pilihan yang Anda masukkan salah **********")
        access_data()

    elif (access_by == 2):
      input_bizname = input(
        "\nMasukkan Business Name yang Anda cari: ").lower()
      biz_names = [n["Business Name"].lower() for n in data.values()]
      if (input_bizname in biz_names):
        index_bizname_access = biz_names.index(input_bizname)
        showSpecificData((index_bizname_access + 1))
      else:
        print(
          "********** Data yang Anda cari tidak ada dalam Database **********")
        access_data()

    else:
      print("********** Pilihan yang Anda masukkan salah **********")
      access_data()

  elif (access_request == 3):
    print("\nAnda akan kembali ke Menu Utama\n")
    main_menu()
  else:
    print("********** Pilihan yang Anda masukkan salah **********")
    access_data()


def add_data():
  print("\n========== Anda akan menambahkan data pada Yellow Pages ==========")
  print("Ketik 0 untuk kembali ke Menu Utama")
  data_baru_biz_name = input("\nMasukkan Business Name Data Baru: ").lower()
  biz_names = [n["Business Name"].lower() for n in data.values()]
  if (data_baru_biz_name == '0'):
    print("\n")
    main_menu()
  elif (data_baru_biz_name in biz_names):
    print("Data yang Anda masukkan sudah ada dalam database")
    add_data()
  else:
    kategori_baru = input("Masukan kategori data baru: ").title()
    alamat_baru = input("Masukan alamat data baru: ").title()
    telpon_baru = input("Masukan nomor telepon data baru: ")
    website_baru = input("Masukan website data baru: ")

    def data_update():
      data_baru = {
        (len(data) + 1): {
          "Category": kategori_baru,
          "Business Name": data_baru_biz_name.title(),
          "Address": alamat_baru,
          "Phone": telpon_baru,
          "Website": website_baru
        }
      }
      print("\nApakah Anda ingin menyimpan Data?")
      print("1. Ya")
      print("2. Tidak")
      simpan = int(input("Pilihan penyimpanan data:"))
      if (simpan == 1):
        print("\nData Tersimpan\n")
        data.update(data_baru)
        showAllData()
        add_data()
      elif (simpan == 2):
        add_data()
      else:
        print(
          "\n********** Pilihan penyimpanan yang Anda masukkan salah **********"
        )
        data_update()

    data_update()


def update_data():
  print("\n========== Anda akan mengubah data Yellow Pages ==========")
  print("Ketik 0 untuk kembali ke Menu Utama\n")
  biz_names = [n["Business Name"].lower() for n in data.values()]
  biz_name_to_change = input("Masukan Business Name yang mau diubah: ").lower()

  if (biz_name_to_change == '0'):
    main_menu()
  elif (biz_name_to_change not in biz_names):
    print("Data yang Anda cari tidak ada dalam database")
    update_data()

  else:
    print("Anda akan mengubah data", biz_name_to_change)
    # masukin data existing nya dulu
    index_biz_name_to_change = biz_names.index(biz_name_to_change)
    showSpecificData(index_biz_name_to_change + 1)
    print("\nApakah ada akan mengubah data tersebut?")
    print("1. Ya")
    print("2. Tidak")
    decision_update = int(input("Pilihan ubah data: "))
    if (decision_update == 1):

      def proses_update():
        print("\nMasukan jenis data yang mau diubah: ")
        print("1. Kategori")
        print("2. Alamat")
        print("3. Nomor Telepon")
        print("4. Website")
        type_to_change = int(input("Pilihan jenis data (1-4): "))

        if (type_to_change == 1):
          kategori_baru = input(
            "Masukkan kategori baru dari data tersebut: ").title()
          data[index_biz_name_to_change + 1]['Category'] = kategori_baru
        elif (type_to_change == 2):
          alamat_baru = input(
            "Masukkan alamat baru dari data tersebut: ").title()
          data[index_biz_name_to_change + 1]['Address'] = alamat_baru
        elif (type_to_change == 3):
          telepon_baru = input(
            "Masukkan nomor telepon baru dari data tersebut: ")
          data[index_biz_name_to_change + 1]['Phone'] = telepon_baru
        elif (type_to_change == 4):
          website_baru = input("Masukkan website baru dari data tersebut: ")
          data[index_biz_name_to_change + 1]['Website'] = website_baru
        else:
          print("********** Pilihan yang Anda masukkan salah **********")
          proses_update()

        print("\nApakah Anda ingin menyimpan perubahan ini?")
        print("1. Ya")
        print("2. Tidak")
        decision_save = int(input("\nPilihan simpan data: "))
        if (decision_save == 1):
          print("\nData berhasil diubah")
          showAllData()
        elif (decision_save == 2):
          update_data()
        else:
          print("\nPilihan yang Anda masukkan salah")
          update_data()

    elif (decision_update == 2):
      update_data()
    else:
      print("\nPilihan yang Anda masukkan salah")
      update_data()

  proses_update()
  # main_menu()


def delete_data():
  print("\n========== Anda akan menghapus data Yellow Pages ==========")
  print("Ketik 0 untuk kembali ke Menu Utama\n")
  biz_names = [n["Business Name"].lower() for n in data.values()]
  biz_name_to_delete = input(
    "Masukan Business Name yang mau dihapus: ").lower()

  if (biz_name_to_delete == '0'):
    print("\n")
    main_menu()
  elif (biz_name_to_delete not in biz_names):
    print("Data yang Anda cari tidak ada dalam database")
    delete_data()
  else:
    print("Anda akan menghapus data:", biz_name_to_delete)
    # masukin data existing nya dulu
    index_biz_name_to_delete = biz_names.index(biz_name_to_delete)
    showSpecificData(index_biz_name_to_delete + 1)
    print("\nApakah ada akan menghapus data tersebut?")
    print("1. Ya")
    print("2. Tidak")
    decision_delete = int(input("Pilihan ubah data: "))

    if (decision_delete == 1):
      del data[index_biz_name_to_delete + 1]
      print("\n>>>>> Data sudah dihapus >>>>>")
      print("\nAnda akan kembali ke Menu Utama\n")
      # print(data)
      # print(list(data.keys()))
      # values = [n for n in data.values()]
      # allValues = []
      # print(len(values))
      showAllData()
      main_menu()

    elif (decision_delete == 2):
      print("Anda akan kembali ke Submenu Delete Data")
      delete_data()
    else:
      print("********** Pilihan yang Anda masukkan salah **********")
      delete_data()


main_menu()
