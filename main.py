"""
    @Describe:main.py
    @Author:BeeBaio
    @Email:2435847739@qq.com
    @Time:2022/7/17-11:44
"""

import sys
from PyQt5.QtWidgets import QApplication
from traveling_salesman_problem_dialog import TravelingSalesmanProblemDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    air = TravelingSalesmanProblemDialog()
    air.show()
    sys.exit(app.exec_())
