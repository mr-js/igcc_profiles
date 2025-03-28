# -*- mode: python ; coding: utf-8 -*-
import shutil

a = Analysis(
    ['igcc_profiles.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['comtypes.stream'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['config'],
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
    name='igcc_profiles',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['igcc_profiles.ico'],
)

shutil.copy("config.py", "dist/")
