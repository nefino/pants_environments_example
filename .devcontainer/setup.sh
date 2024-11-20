sudo chown -R $USER:$USER /tmp/pants
./install_pants.sh
pants --no-dynamic-ui --version
pants complete >> ~/.bashrc
echo 'PS1="${PS1}\n> "' >> ~/.bashrc
