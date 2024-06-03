import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from PyQt6 import uic
import iniwork

class giaoDienChinh(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gddangnhap.ui', self)

        self.buttonKetNoi.setStyleSheet("""
            background-color: #4CAF50;
            border: none;
            color: white;
            padding: 15px 32px;
            border-radius: 10px;
            height: 50px;
        """)

        self.buttonKetNoi.clicked.connect(self.hienThongBaoDangNhap)

    def moGiaoDienBaiTap(self):
        self.window = giaoDienBaiTap()
        self.window.show()
        self.hide()
        
    
    def hienThongBaoDangNhap(self):
        taiKhoanDung = "loptruong"
        matKhauDung = "123456"
        if self.inputTen.text() == taiKhoanDung and self.inputPassword.text() == matKhauDung:
            msgBox = QMessageBox()
            msgBox.setText("Xin chào, bạn đã đăng nhập thành công!")
            msgBox.exec()
            self.moGiaoDienBaiTap()

        else:
            msgBox = QMessageBox()
            msgBox.setText("Đăng nhập thất bại!")
            msgBox.exec()

class giaoDienBaiTap(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gdxembaitap.ui', self)
        self.buttonLuu.clicked.connect(self.luuNoiDung)

    def luuNoiDung(self):
        noiDung = self.textEditNoiDung.toPlainText()
        iniwork.write_data_to_ini(noiDung)
        msgBox = QMessageBox()
        msgBox.setText("Nội dung mới đã được lưu lại!")
        msgBox.exec()
    

khoiChayHeThong = QApplication(sys.argv)
phanMem = giaoDienChinh()
phanMem.show()
chayPhanMem = khoiChayHeThong.exec()
sys.exit(chayPhanMem)