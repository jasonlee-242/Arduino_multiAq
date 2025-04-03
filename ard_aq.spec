# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ard_aq.py'],
    pathex=[],
    binaries=[],
    datas=[('/home/john/anaconda3/lib/python3.9/site-packages/pyqtgraph/multiprocess/bootstrap.py', 'pyqtgraph/multiprocess')],
    hiddenimports=['pyqtgraph.multiprocess', 'pyqtgraph.multiprocess.remoteproxy', 'pyi_rth_pyqtgraph_multiprocess'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt5', 'tkinter'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ard_aq',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
