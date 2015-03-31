sudo -v
echo "Downloading source code..."
sudo wget https://raw.githubusercontent.com/ralphembree/py2048/master/py2048 -O /usr/games/py2048
sudo chmod +x /usr/games/py2048
echo "Downloading icon..."
sudo wget https://raw.githubusercontent.com/ralphembree/py2048/master/2048.png -O /usr/share/icons/hicolor/64x64/apps/py2048.png

echo "Adding menu item..."
echo "[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon[en_US]=/usr/share/icons/hicolor/64x64/apps/py2048.png
Name[en_US]=py2048
Exec=py2048
Name=py2048
Icon=/usr/share/icons/hicolor/64x64/apps/py2048.png
Categories=Game" | sudo tee /usr/share/applications/py2048.desktop >/dev/null
echo "Done"
echo "The application can be run from the terminal by typing 'py2048' and can also be accessed from the start menu in the games section."
