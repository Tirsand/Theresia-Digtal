class Wallet:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []

    def view_balance(self):
        print(f"\nSaldo Anda saat ini: ${self.balance}")

    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Menambah saldo: +${amount}")
            print(f"\nSaldo berhasil ditambahkan sebesar ${amount}")
        else:
            print("\nJumlah yang dimasukkan harus positif.")

    def send_money(self, amount, recipient):
        if amount <= 0:
            print("\nJumlah pengiriman harus positif.")
        elif amount > self.balance:
            print("\nSaldo tidak mencukupi untuk transaksi ini.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Pengiriman ke {recipient}: -${amount}")
            print(f"\nUang sebesar ${amount} berhasil dikirim ke {recipient}.")

    def view_transaction_history(self):
        print("\nRiwayat Transaksi:")
        if not self.transaction_history:
            print("Belum ada transaksi.")
        else:
            for transaction in self.transaction_history:
                print(f" - {transaction}")


def main():
    wallet = Wallet()

    while True:
        print("\nSelamat datang di Aplikasi Dompet Digital!")
        print("1. Lihat Saldo")
        print("2. Tambah Saldo")
        print("3. Kirim Uang")
        print("4. Lihat Riwayat Transaksi")
        print("5. Keluar")
        
        choice = input("\nPilih menu (1-5): ")

        if choice == "1":
            wallet.view_balance()
        elif choice == "2":
            try:
                amount = float(input("\nMasukkan jumlah saldo yang ingin ditambahkan: $"))
                wallet.add_balance(amount)
            except ValueError:
                print("\nHarap masukkan angka yang valid.")
        elif choice == "3":
            try:
                amount = float(input("\nMasukkan jumlah uang yang akan dikirim: $"))
                recipient = input("Masukkan nama penerima: ")
                wallet.send_money(amount, recipient)
            except ValueError:
                print("\nHarap masukkan angka yang valid.")
        elif choice == "4":
            wallet.view_transaction_history()
        elif choice == "5":
            print("\nTerima kasih telah menggunakan aplikasi dompet digital ini!")
            break
        else:
            print("\nPilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()class Wallet:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []

    def view_balance(self):
        print(f"\nSaldo Anda saat ini: ${self.balance}")

    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Menambah saldo: +${amount}")
            print(f"\nSaldo berhasil ditambahkan sebesar ${amount}")
        else:
            print("\nJumlah yang dimasukkan harus positif.")

    def send_money(self, amount, recipient):
        if amount <= 0:
            print("\nJumlah pengiriman harus positif.")
        elif amount > self.balance:
            print("\nSaldo tidak mencukupi untuk transaksi ini.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Pengiriman ke {recipient}: -${amount}")
            print(f"\nUang sebesar ${amount} berhasil dikirim ke {recipient}.")

    def view_transaction_history(self):
        print("\nRiwayat Transaksi:")
        if not self.transaction_history:
            print("Belum ada transaksi.")
        else:
            for transaction in self.transaction_history:
                print(f" - {transaction}")


def main():
    wallet = Wallet()

    while True:
        print("\nSelamat datang di Aplikasi Dompet Digital!")
        print("1. Lihat Saldo")
        print("2. Tambah Saldo")
        print("3. Kirim Uang")
        print("4. Lihat Riwayat Transaksi")
        print("5. Keluar")
        
        choice = input("\nPilih menu (1-5): ")

        if choice == "1":
            wallet.view_balance()
        elif choice == "2":
            try:
                amount = float(input("\nMasukkan jumlah saldo yang ingin ditambahkan: $"))
                wallet.add_balance(amount)
            except ValueError:
                print("\nHarap masukkan angka yang valid.")
        elif choice == "3":
            try:
                amount = float(input("\nMasukkan jumlah uang yang akan dikirim: $"))
                recipient = input("Masukkan nama penerima: ")
                wallet.send_money(amount, recipient)
            except ValueError:
                print("\nHarap masukkan angka yang valid.")
        elif choice == "4":
            wallet.view_transaction_history()
        elif choice == "5":
            print("\nTerima kasih telah menggunakan aplikasi dompet digital ini!")
            break
        else:
            print("\nPilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main() class Wallet:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []

    def view_balance(self):
        print(f"\nSaldo Anda saat ini: ${self.balance}")

    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Menambah saldo: +${amount}")
            print(f"\nSaldo berhasil ditambahkan sebesar ${amount}")
        else:
            print("\nJumlah yang dimasukkan harus positif.")

    def send_money(self, amount, recipient):
        if amount <= 0:
            print("\nJumlah pengiriman harus positif.")
        elif amount > self.balance:
            print("\nSaldo tidak mencukupi untuk transaksi ini.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Pengiriman ke {recipient}: -${amount}")
            print(f"\nUang sebesar ${amount} berhasil dikirim ke {recipient}.")

    def view_transaction_history(self):
        print("\nRiwayat Transaksi:")
        if not self.transaction_history:
            print("Belum ada transaksi.")
        else:
            for transaction in self.transaction_history:
                print(f" - {transaction}")


def main():
    wallet = Wallet()

    while True:
        print("\nSelamat datang di Aplikasi Dompet Digital!")
        print("1. Lihat Saldo")
        print("2. Tambah Saldo")
        print("3. Kirim Uang")
        print("4. Lihat Riwayat Transaksi")
        print("5. Keluar")
        
        choice = input("\nPilih menu (1-5): ")

        if choice == "1":
            wallet.view_balance()
        elif choice == "2":
            try:
                amount = float(input("\nMasukkan jumlah saldo yang ingin ditambahkan: $"))
                wallet.add_balance(amount)
            except ValueError:
                print("\nHarap masukkan angka yang valid.")
        elif choice == "3":
            try:
                amount = float(input("\nMasukkan jumlah uang yang akan dikirim: $"))
                recipient = input("Masukkan nama penerima: ")
                wallet.send_money(amount, recipient)
            except ValueError:
                print("\nHarap masukkan angka yang valid.")
        elif choice == "4":
            wallet.view_transaction_history()
        elif choice == "5":
            print("\nTerima kasih telah menggunakan aplikasi dompet digital ini!")
            break
        else:
            print("\nPilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()
 import as at 
import 

class Wallet:
    def __init__(self):
        self.balance = 0
        self.transaction_history = []

    def view_balance(self):
        print(f"\nSaldo Anda saat ini: ${self.balance}")

    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Menambah saldo: +${amount}")
            print(f"\nSaldo berhasil ditambahkan sebesar ${amount}")
        else:
            print("\nJumlah yang dimasukkan harus positif.")

    def send_money(self, amount, recipient):
        if amount <= 0:
            print("\nJumlah pengiriman harus positif.")
        elif amount > self.balance:
            print("\nSaldo tidak mencukupi untuk transaksi ini.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Pengiriman ke {recipient}: -${amount}")
            print(f"\nUang sebesar ${amount} berhasil dikirim ke {recipient}.")

    def view_transaction_history(self):
        print("\nRiwayat Transaksi:")
        if not self.transaction_history:
            print("Belum ada transaksi.")
        else:
            for transaction in self.transaction_history:
                print(f" - {transaction}")


def main():
    wallet = Wallet()

    while True:
        print("\nSelamat datang di Aplikasi Dompet Digital!")
        print("1. Lihat Saldo")
        print("2. Tambah Saldo")
        print("3. Kirim Uang")
        print("4. Lihat Riwayat Transaksi")
        print("5. Keluar")
        
        choice = input("\nPilih menu (1-5): ")

        if choice == "1":
            wallet.view_balance()
        elif choice == "2":
            try:
                amount = float(input("\nMasukkan jumlah saldo yang ingin ditambahkan: $"))
                wallet.add_balance(amount)
            except ValueError:
                print("\nHarap masukkan angka yang valid.")
        elif choice == "3":
            try:
                amount = float(input("\nMasukkan jumlah uang yang akan dikirim: $"))
                recipient = input("Masukkan nama penerima: ")
                wallet.send_money(amount, recipient)
            except ValueError:
                print("\nHarap masukkan angka yang valid.")
        elif choice == "4":
            wallet.view_transaction_history()
        elif choice == "5":
            print("\nTerima kasih telah menggunakan aplikasi dompet digital ini!")
            break
        else:
            print("\nPilihan tidak valid, silakan coba lagi.")


if __name__ == "__main__":
    main()
