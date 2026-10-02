# Build script for the macOS .app bundle using py2app.
#
# Build it on macOS with:
#     python3 -m pip install -r requirements.txt
#     python3 -m pip install py2app pillow
#     python3 setup.py py2app
#
# The finished bundle is written to dist/SCMD Workshop Downloader 2.app.
# The GitHub Actions workflow in .github/workflows/build-macos.yml does this
# automatically and uploads the zipped app as a build artifact.

import os
from setuptools import setup

APP = ['SCMD Workshop Downloader 2.py']

# Everything the app reads or writes at runtime. When bundled these are copied
# into a per-user folder on first launch (see prepare_runtime() in the app).
DATA_FILES = [
    'resources',
    'data',
    'download lists',
    'generated scripts',
    'SCMD List Manager.py',
]

OPTIONS = {
    'argv_emulation': False,
    'iconfile': os.path.join('resources', 'scmdwd.ico'),
    'packages': ['requests', 'bs4'],
    'includes': ['PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets'],
    'plist': {
        'CFBundleName': 'SCMD Workshop Downloader 2',
        'CFBundleDisplayName': 'SCMD Workshop Downloader 2',
        'CFBundleIdentifier': 'com.berdyalexei.scmdwd2',
        'CFBundleShortVersionString': '2.0.0',
        'CFBundleVersion': '2.0.0',
        'NSHighResolutionCapable': True,
        'LSApplicationCategoryType': 'public.app-category.utilities',
        'LSMinimumSystemVersion': '10.13',
        'NSHumanReadableCopyright': 'SCMD Workshop Downloader 2',
    },
}

setup(
    name='SCMD Workshop Downloader 2',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
)
