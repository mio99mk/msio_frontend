cd msio_frontend
git init
git remote add origin https://github.com/mio99mk/msio_frontend.git
touch requirements.txt
echo "streamlit\nrequests" > requirements.txt
git add .
git commit -m "frontend init"
git push -u origin main
