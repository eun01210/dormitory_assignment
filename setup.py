from cx_Freeze import setup,Executable

setup(name="기숙사 배치 프로그램",
         version="1.0v",
         description="기숙사 배치 프로그램",
         executables=[Executable("dormitory.py")])
