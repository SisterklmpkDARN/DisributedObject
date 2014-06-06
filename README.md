DisributedObject
=================
Praktikum 3: Praktikum Distributed Object


README
=================
File-file di repo ini udah di compile dari idl ke java dan pythonnya.

HOW TO
=================
Java (Java IDL)
Installasi
Pastikan folder bin Java JDK udah ada di PATH (supaya bisa akses javac, java, orbd, idlj global)

Running Program
Compile file idlnya pake idlj
	> idlj -fall Hello.idl
Compile file javanya
	> javac HelloServer.java HelloApp/*.java
Jalanin ORBnya
	> start orbd -ORBInitialPort 1050 -ORBInitialHost localhost
	nanti dia buka cmd console baru buat ORBnya
Jalanin programnya
	> java HelloServer -ORBInitialPort 1050 -ORBInitialHost localhost

Python (OmniORBPy)
Installasi (Windows)
Unzip omniorbpy-4.2.0-win32
Simpan folder di tempat yang diinginkan
Tambah alamat folder omniorb/bin di PATH (supaya bisa akses omniidl, omninames global aja sih)
Merge file sample.reg (klik kanan->merge)

Runnning program
Compile file idlnya pake omniidl
	> omniidl -bpython Hello.idl
Kalo ORBnya pake OmniORB, jalanin omniNames
	> omniNames -start -logdir alamat_folder_valid
Default portnya 2809, kalo mau diganti tambahin nomor port setelah -start
Utk setiap cmd console, set %PYTHONPATH%. Contohnya bisa dilihat di pythonpath.bat. Kalo pythonpath.batnya udah di edit direktorinya, kalo dijalanin ngebuka cmd console yang udah di set %PYTHONPATH% nya.
Jalanin program pythonnya
	> python HelloClient.py -ORBInitRef NameService=corbaloc::localhost:1050/NameService
Dokumentasi omniorb bisa dibuka dari doc/omniORBpy/index.htm