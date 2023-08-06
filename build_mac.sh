#!/bin/bash

nuitka \
  --standalone \
  --onefile \
  --enable-plugin=pyside6 \
  --macos-create-app-bundle \
  --output-dir=build \
  --assume-yes-for-download \
  --macos-app-version=1.0 \
  --macos-app-icon=icon.icns \
  --disable-console \
  main.py

