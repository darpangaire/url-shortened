# Django JWT Channel System

A modern Django project featuring channel-based discussions, JWT authentication, feedback with email notifications, and a clear separation of admin and user capabilities.

---

## Features

- **JWT Authentication**:  
  - User registration with email verification link sent to their Gmail.
  - Secure login system using JWT tokens.
- **Environment Configuration**:  
  - Uses a `.env` file for configuration (see [Setup](#setup) below).
- **Channel Management**:  
  - Only authenticated users can create channels.
  - Each channel has an admin (creator).
- **Feedback & Comments**:  
  - Anonymous users can leave feedback/comments on admin posts in any channel.
  - When feedback is submitted, an email notification is sent to the channel's admin.
- **Pagination**:  
  - All channel and post listings are paginated for scalability.
- **Admin Controls**:  
  - Admins can create and delete posts.
  - Admins can delete feedback/comments on their posts.
  - Admin dashboard available from their profile page.
- **API Authentication**:  
  - All API endpoints are secured with JWT authentication.

---

## Quick Start

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/your-django-jwt-channel-app.git
cd your-django-jwt-channel-app
```

### 2. Python & Virtualenv

```sh
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Variables (`.env`)

Create a `.env` file in your project root:

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_gmail@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password
EMAIL_USE_TLS=True
JWT_SECRET=your_jwt_secret
```

- **EMAIL_HOST_USER**/**EMAIL_HOST_PASSWORD**: Use [Gmail App Passwords](https://support.google.com/accounts/answer/185833) for better security.
- **SECRET_KEY**/**JWT_SECRET**: Generate strong random secrets.

### 4. Migrate & Create Superuser

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run the Development Server

```sh
python manage.py runserver
```

---

## How it Works

### Registration & Login

- Users register with their email.  
- An email verification link is sent (check your Gmail).
- Only verified users can log in and create channels.
- JWT tokens are used for API authentication.

### Channels & Admins

- Only logged-in users can create channels.
- The creator becomes the channel admin.
- Admins can:
  - Create posts in their channels.
  - Delete any post or feedback in their channels.
  - Access an admin dashboard from their profile.

### Feedback/Comments

- Anonymous users can leave feedback on posts.
- When feedback is added, an email is sent to the channel's admin.
- Admins can delete any feedback on their posts.

### Pagination

- Channel and post lists are paginated for better UX and scalability.

### API Authentication

- All API endpoints require JWT authentication.
- Example usage (with `Authorization: Bearer <JWT>` header):

```http
POST /api/create-channel/
Authorization: Bearer <your_jwt_token>
Content-Type: application/json
```

---

## Project Structure

```
your-django-jwt-channel-app/
├── channels/          # Channel, Post, Feedback models & views
├── users/             # JWT Auth, Registration, Profile, Admin dashboard
├── core/              # Settings, Middlewares, .env config
├── templates/         # HTML templates
├── static/            # Static files (CSS/JS)
├── manage.py
├── .env.example
└── README.md
```

---

## Customization

- **Email Backend**: You may swap out Gmail for another SMTP backend as needed.
- **Frontend**: Templates use [Tailwind CSS](https://tailwindcss.com/) for a modern UI.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

[MIT](LICENSE)

---

## Credits

- Django
- djangorestframework
- SimpleJWT
- Tailwind CSS
- [django-environ](https://github.com/joke2k/django-environ)

---

**Happy coding!**
