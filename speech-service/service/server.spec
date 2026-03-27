# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_dynamic_libs, collect_submodules

block_cipher = None

hiddenimports = collect_submodules("vosk")
binaries = collect_dynamic_libs("vosk")

a = Analysis(
    ["server.py"],
    pathex=["."],
    binaries=binaries,
    datas=[],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="CornerstoneSpeechService",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)

app = BUNDLE(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    name="CornerstoneSpeechService.app",
    bundle_identifier="com.cornerstone.speechservice",
)

coll = COLLECT(
    app,
    a.binaries,
    a.zipfiles,
    a.datas,
    name="CornerstoneSpeechService",
)
