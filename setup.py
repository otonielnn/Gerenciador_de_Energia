from sys import platform
from cx_Freeze import setup, Executable

base = None
if platform == 'win32':
    base = 'Win32Gui'

setup(
    name='Gerenciador de Energia',
    version='1.0',
    description='Gerenciador de Energia',
    options={
        'build_exe': {
            'includes': ['tkinter', 'ttkbootstrap'],
            'packages': ['tkinter', 'ttkbootstrap'],
            'include_files': ['dados.csv']
        }
    },
    executables=[
        Executable('main.py', base=base)
    ]
)