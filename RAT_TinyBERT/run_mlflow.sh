echo "export PATH=\"`python3 -m site --user-base`/bin:\$PATH\"" >> ~/.bashrc
source ~/.bashrc
cat ~/.bashrc
mlflow ui -h 0.0.0.0
