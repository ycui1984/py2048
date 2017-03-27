sudo -v
echo "Downloading source code..."
sudo wget https://raw.githubusercontent.com/ralphembree/py2048/master/py2048 -O /usr/games/py2048
sudo chmod +x /usr/games/py2048
echo "Downloading icon..."
sudo wget https://raw.githubusercontent.com/ralphembree/py2048/master/2048.png -O /usr/share/icons/hicolor/64x64/apps/py2048.png

if [ ! -f /usr/share/mime/packages/application-2048.xml ]; then
    echo "Registering mime type"
    echo '<?xml version="1.0" encoding="UTF-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
  <mime-type type="application/2048">
    <comment>py2048 mime type</comment>
    <glob pattern="*.2048"/>
  </mime-type>
</mime-info>' | sudo tee /usr/share/mime/packages/application-2048.xml >/dev/null
fi

echo "Adding menu item..."
echo "[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon[en_US]=py2048
Name[en_US]=py2048
Exec=py2048
Name=py2048
Description=Play the popular puzzle game of 2048
Icon=py2048
Categories=Game
MimeType=application/2048" | sudo tee /usr/share/applications/py2048.desktop >/dev/null
sudo update-mime-database /usr/share/mime
sudo update-desktop-database /usr/share/applications
echo -e "\033[1;34mThe application can be run from the terminal by typing 'py2048' and can also be accessed from the start menu in the games section.\033[m"


