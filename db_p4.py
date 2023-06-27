from sqlite3 import OperationalError
from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import  Mapped
from sqlalchemy.orm import mapped_column
from datetime import date
from sqlalchemy import MetaData
import tkinter
from tkinter import messagebox


window = tkinter.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')

class Base(DeclarativeBase):
    pass

assosiation_table = Table(
    "association_table",
    Base.metadata,
    Column("Scliessfach_ID", Integer, ForeignKey("Schliessfach.SID"), primary_key=True),
    Column("person_id", Integer, ForeignKey("Person.PID"), primary_key=True),
    
)
class Eigentuemer(Base):
    __tablename__ = "Eigentuemer"

    Unternehmensname: Mapped[str] = mapped_column(String(50), primary_key=True)
    Laendercode: Mapped[str] = mapped_column(String(50))
    schliessfach: Mapped[list["Schliessfach"]] = relationship(back_populates="eigentuemer")

    def __int__(self, u_name, l_code):
        self.Unternehmensname = u_name
        self.Laendercode = l_code

class Schliessfach(Base):
    __tablename__ = "Schliessfach"

    SID: Mapped[int] = mapped_column(primary_key=True)
    Erstellungsdatum: Mapped[Date] = mapped_column(Date())
    eigentuemer_name: Mapped[str] = mapped_column(String(50), ForeignKey("Eigentuemer"))
    eigentuemer: Mapped["Eigentuemer"] = relationship(back_populates="schliessfach")
    berechtigter: Mapped[list["Person"]]= relationship(secondary=assosiation_table, back_populates="berechtigte_person")

    def __int__(self, m_date):
        self.Erstellungsdatum = m_date

class Person(Base):
    __tablename__ = "Person"

    PID: Mapped[int] = mapped_column(primary_key=True)
    vorname: Mapped[str] = mapped_column(String(50))
    nachname: Mapped[str] = mapped_column(String(50))
    berechtigte_person: Mapped[Schliessfach] = relationship(secondary=assosiation_table, back_populates="berechtigter")

    def __int__(self, firstname, lastname):
        self.vorname = firstname
        self.nachname = lastname

def print_menu():
    print("Menu:")
    print("1: Ausgabe aller Eigentuemer")
    print("2: Ausgabe aller Schliessfaecher")
    print("3: Ausgabe aller Personen")
    print("4: Ausgabe aller Schliessfaecher eines Berechtigten")
    print("q: Exit")

def ausgabe_eigentuemer():
    pass


def ausgabe_schliessfaecher():
    pass


def ausgabe_personen():
    pass


def ausgabe_schliessfaecher_berechtigte():
    pass

def db_fill():
    pass


def option_auswaehlen():

    while True:
        print_menu()

        choice = input("Option auswaehlen (1-4): ")
        if choice == "1":
            ausgabe_eigentuemer()
        elif choice == "2":
            ausgabe_schliessfaecher()
        elif choice == "3":
            ausgabe_personen()
        elif choice == "4":
            ausgabe_schliessfaecher_berechtigte()
        elif choice == "q":
            exit()
        else:
            print("Ungueltige Eingabe. Versuchen Sie nochmal.")

def login():

    username = username_entry.get()
    password = password_entry.get()

    try:
        engine = create_engine(f"postgresql+psycopg2://{username}:{password}@localhost/{username}", echo=False)
        conncetion = engine.connect()
        messagebox.showinfo("Connected to db")
    except OperationalError:
        messagebox.showerror(title="Error", message="Failed to connect to the database.")
frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_label = tkinter.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tkinter.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()

def main():
    login()

if __name__ == "__main__":
    main()
