# Family Leave Management Web App

A collaborative web application that helps family members track and plan upcoming leaves/work holidays. Share your schedule with everyone to coordinate family events and travel plans.

## Features

✅ **User Authentication** - Family members can login with their credentials  
✅ **Leave Management** - Add, edit, and delete work holidays  
✅ **Family Dashboard** - See all family members' upcoming leaves in one place  
✅ **Leave Planning** - Plan family events based on everyone's availability  
✅ **Personal Leave View** - Check your own leave history  
✅ **Beautiful UI** - Responsive design with Bootstrap  

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Authentication**: Flask-Login with password hashing

## Project Structure

```
webapp/
├── app.py                    # Main Flask application
├── models.py                 # Database models (FamilyMember, Leave)
├── requirements.txt          # Python dependencies
├── README.md                # Documentation
├── family_leaves.db         # SQLite database (auto-created)
├── hello.py                 # Sample Python script
└── templates/
    ├── login.html           # Login page
    ├── dashboard.html       # Family leave schedule
    ├── add_leave.html       # Add new leave form
    ├── edit_leave.html      # Edit leave form
    ├── my_leaves.html       # View user's leaves
    └── index.html          # Welcome page
```

## Setup & Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/ibrahim642/webapp.git
cd webapp
```

2. **Create a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Open in browser**
Navigate to `http://localhost:5000`

## Default Demo Credentials

The app initializes with 8 family members:
- Alice
- Bob
- Charlie
- Diana
- Eve
- Frank
- Grace
- Henry

**Default Password**: `password123`

## How to Use

### Login
1. Enter a family member's name (e.g., "Alice")
2. Enter the password: `password123`

### Add a Leave
1. Click "Add Leave" from the navigation menu
2. Enter the start and end dates
3. Optionally add a reason (e.g., "Beach vacation", "Visit grandparents")
4. Click "Add Leave"

### View All Leaves
- The Dashboard shows all family members' upcoming leaves
- See who's on leave during specific periods
- Plan family events accordingly

### Edit or Delete Leaves
- View your leaves in "My Leaves" section
- Click "Edit" to modify leave dates or reason
- Click "Delete" to remove a leave entry

## API Endpoints

- `GET /` - Redirect to login/dashboard
- `GET/POST /login` - Login page
- `GET /logout` - Logout user
- `GET /dashboard` - Family leave schedule view
- `GET /my-leaves` - View current user's leaves
- `GET/POST /add-leave` - Add new leave
- `GET/POST /edit-leave/<id>` - Edit leave
- `POST /delete-leave/<id>` - Delete leave
- `GET /api/hello` - Sample API endpoint

## Security Notes

⚠️ **For Development Only**: The current implementation uses:
- SQLite for simplicity
- Simple password hashing (werkzeug)
- Secret key is hardcoded

**For Production**, consider:
- Using PostgreSQL
- Implementing proper authentication (OAuth2, JWT)
- Using environment variables for secrets
- Adding HTTPS
- Implementing role-based access control

## License

MIT

## Contributing

Feel free to submit issues and enhancement requests!

