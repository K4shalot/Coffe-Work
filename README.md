# ☕ Work Friendly Cafes

**Work Friendly Cafes** is a Django-based web application that showcases cafes suitable for working or studying.  
Each cafe has its own dedicated page with details like **descriptions**, **images**, **map location**, and **user reviews**.  

🛠️ Admins can easily:
- Manage cafes
- Upload photos
- Moderate reviews

The site includes:
- A gallery of images for each cafe
- Static information like total reviews and average rating
- Clean, responsive UI
- Django templating with custom styling

This app is ideal for anyone looking for cozy, productive spots to work or study.

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/work-friendly-cafes.git
cd work-friendly-cafes
```
2.Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
```

3.Install dependencies
```bash
pip install -r requirements.txt
```

4.Apply migrations
```bash
python manage.py migrate
```

5.Create a superuser to access the admin panel
```bash
python manage.py createsuperuser
```

6.Run the development server
```bash
python manage.py runserver
```

🌐 Access the App 
Visit the homepage: http://127.0.0.1:8000/
Admin panel: http://127.0.0.1:8000/admin/

