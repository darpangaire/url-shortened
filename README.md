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

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/a9751c45-e4a3-4747-b74c-be61955f6bae" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/500cbb4b-69c9-4e29-8c56-188eafcab26c" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/83095328-6f66-4776-89d7-060bbb110845" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/0c04e020-c348-4720-9987-6de7b6546ab9" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/bd05d0c5-a35e-4a7d-9000-510e4ea157d6" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/be09a4d7-a635-43f5-9921-ac63479ec045" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/b04702ea-2015-4066-b9f9-cb6ebb6eb539" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/f4fb2a56-65af-47b7-bbe6-6bb24855f592" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/fe6085d6-fabe-49cc-a451-df5429225f39" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/36d21bff-93ba-4ae9-a2c0-bc21939483a1" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/ed25c739-6526-4777-9041-63e82cdca443" />

<img width="1366" height="768" alt="Image" src="https://github.com/user-attachments/assets/0ed03803-2806-460d-9e16-fc759f47b3aa" />
