# EventHub 🎉

EventHub is a web application built with Django that allows users to create, manage, and explore events.

---

## 🚀 Features

- Custom User Model
- User Authentication (Register, Login, Logout)
- User Profile Page
- Create, Edit, Delete Events
- Event Categories (Many-to-Many relationship)
- Permissions (only event creator can edit/delete)
- Class-Based Views (CBV)
- REST API with Django REST Framework
- Date formatting and validation

---

## 🛠️ Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- HTML (Templates)

---

## 📦 Installation

1. Clone the repository:

git clone https://github.com/bazarr32/Eventhub.git  
cd Eventhub

2. Create virtual environment:

python -m venv venv

3. Activate it:

Windows:  
venv\Scripts\activate  

Mac/Linux:  
source venv/bin/activate  

4. Install dependencies:

pip install -r requirements.txt

5. Apply migrations:

python manage.py migrate

6. Run the server:

python manage.py runserver

7. Open in browser:

http://127.0.0.1:8000/

---

## 🔑 Admin Panel

Create superuser:

python manage.py createsuperuser

Access admin panel:

http://127.0.0.1:8000/admin/

---

## 🌐 API Endpoints

- All events:  
/api/events/

- Single event:  
/api/events/<id>/

---

## 📁 Project Structure

eventhub_project/  
│  
├── accounts/  
├── events/  
├── core/  
├── api/  
├── templates/  
│  
├── manage.py  
└── db.sqlite3  

---

## 👤 Author

- Martin Hristov

---

## 📌 Notes

- Only logged-in users can create events  
- Only the organizer can edit or delete events  
- API returns JSON data  
- Project uses Class-Based Views  

---

## ⭐ Project Status

✔️ Completed  
✔️ Fully functional  
✔️ Ready for submission