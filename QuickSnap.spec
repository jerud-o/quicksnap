# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

face_models = [
    ('.venv\\Lib\\site-packages\\face_recognition_models\\models\\shape_predictor_68_face_landmarks.dat', 'face_recognition_models/models'),
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=face_models,
    datas=[
        ('package', 'package'),
        ('.env', '.'),
        ('.venv\\Lib\\site-packages\\mediapipe\\modules', 'mediapipe\\modules'),
        
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

a.datas += [('blush_bg.jpg', 'package\\resource\\filter\\background\\blush_bg.jpg', "DATA")]
a.datas += [('grizzly_bg.jpg', 'package\\resource\\filter\\background\\grizzly_bg.jpg', "DATA")]
a.datas += [('pinkheart_bg.jpg', 'package\\resource\\filter\\background\\pinkheart_bg.jpg', "DATA")]

a.datas += [('blush.png', 'package\\resource\\filter\\cheek\\blush.png', "DATA")]
a.datas += [('grizzly.png', 'package\\resource\\filter\\cheek\\grizzly.png', "DATA")]
a.datas += [('pinkheart.png', 'package\\resource\\filter\\cheek\\pinkheart.png', "DATA")]

a.datas += [('blush_icon.jpg', 'package\\resource\\filter\\icon\\blush_icon.jpg', "DATA")]
a.datas += [('grizzly_icon.jpg', 'package\\resource\\filter\\icon\\grizzly_icon.jpg', "DATA")]
a.datas += [('pinkheart_icon.jpg', 'package\\resource\\filter\\icon\\pinkheart_icon.jpg', "DATA")]

a.datas += [('male.png', 'package\\resource\\formal\\male.png', "DATA")]
a.datas += [('female.png', 'package\\resource\\formal\\female.png', "DATA")]

a.datas += [('img.png', 'package\\resource\\img\\temp\\img.png', "DATA")]

a.datas += [('back.png', 'package\\resource\\img\\back.png', "DATA")]
a.datas += [('beauty.png', 'package\\resource\\img\\beauty.png', "DATA")]
a.datas += [('bg_film.jpg', 'package\\resource\\img\\bg_film.jpg', "DATA")]
a.datas += [('bg_film2.png', 'package\\resource\\img\\bg_film2.png', "DATA")]
a.datas += [('bg_film3.png', 'package\\resource\\img\\bg_film3.png', "DATA")]
a.datas += [('bg_gradient.png', 'package\\resource\\img\\bg_gradient.png', "DATA")]
a.datas += [('camera.png', 'package\\resource\\img\\camera.png', "DATA")]
a.datas += [('danger.png', 'package\\resource\\img\\danger.png', "DATA")]
a.datas += [('female.png', 'package\\resource\\img\\female.png', "DATA")]
a.datas += [('formal.png', 'package\\resource\\img\\formal.png', "DATA")]
a.datas += [('intro_bg.png', 'package\\resource\\img\\intro_bg.png', "DATA")]
a.datas += [('main_bg.png', 'package\\resource\\img\\main_bg.png', "DATA")]
a.datas += [('male.png', 'package\\resource\\img\\male.png', "DATA")]
a.datas += [('man.png', 'package\\resource\\img\\man.png', "DATA")]
a.datas += [('null.png', 'package\\resource\\img\\null.png', "DATA")]
a.datas += [('photo_strips-removebg-preview.png', 'package\\resource\\img\\photo_strips-removebg-preview.png', "DATA")]
a.datas += [('photo_strips.jpg', 'package\\resource\\img\\photo_strips.jpg', "DATA")]
a.datas += [('print.png', 'package\\resource\\img\\print.png', "DATA")]
a.datas += [('quicksnap_logo-removebg-preview.png', 'package\\resource\\img\\quicksnap_logo-removebg-preview.png', "DATA")]
a.datas += [('quicksnap_logo.png', 'package\\resource\\img\\quicksnap_logo.png', "DATA")]
a.datas += [('quicksnap.ico', 'package\\resource\\img\\quicksnap.ico', "DATA")]
a.datas += [('tab.png', 'package\\resource\\img\\tab.png', "DATA")]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='QuickSnap',
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
    icon=['package\\resource\\img\\quicksnap.ico'],
)
