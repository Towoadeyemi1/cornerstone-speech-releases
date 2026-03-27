# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_dynamic_libs, collect_submodules

block_cipher = None

hiddenimports = (
    collect_submodules("vosk")
    + collect_submodules("websockets")
    + collect_submodules("sounddevice")
)

# Put libvosk.dylib under _internal/vosk/
binaries = collect_dynamic_libs("vosk", destdir="vosk")

datas = [
    ("vosk-model-small-en-us-0.15", "model"),
]

a = Analysis(
    ["server.py"],
    pathex=["."],
    binaries=binaries,
    datas=datas,
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
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name="CornerstoneSpeechService",
)
