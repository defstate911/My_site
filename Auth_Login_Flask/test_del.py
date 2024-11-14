from app import app, db
from app.models import User

# Создайте приложение Flask и контекст приложения
with app.app_context():
    # Создайте пользователя
    new_user = User(username='testuser', email='test@example.com', password='password')
    db.session.add(new_user)
    db.session.commit()
