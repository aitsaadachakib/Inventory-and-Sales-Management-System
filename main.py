"""
This is the runner file of the application
It creates the login widget
"""
import sys
from PySide6.QtWidgets import QApplication
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from SuperMarket.database import Base,User,PasswordType

from widgets import LoginWidget


# runner
engine = create_engine('sqlite:///dataFiles/yourdatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create tables in the database if they don't exist
Base.metadata.create_all(engine)

# Function to add admin user if not exists
def add_default_admin_user(session):
    # Check if an admin user already exists
    admin_user = session.query(User).filter_by(name="admin").first()
    if not admin_user:
        # If no admin exists, create the admin user
        admin_user = User(name="admin")
        admin_user.password = "admin"  # Password will be hashed automatically
        admin_user.type=PasswordType.admin
        session.add(admin_user)
        session.commit()
        print("Admin user created: username = 'admin', password = 'admin'")
    else:
        print("Admin user already exists.")

# Call the function to ensure admin user exists
add_default_admin_user(session)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = LoginWidget(session=session)
    window.show()
    app.exec()

