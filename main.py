# This is a sample Python script.
from account_type import Account, Customer, Person
from cinema import Cinema, CinemaHall
from constants import ManagerType
from dao.db import FakeNoSQLDB
from managers.movie_manager import MovieManager
from show import Show

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    db = FakeNoSQLDB()
#    hall = CinemaHall("esenlerhall",123,12,"")
#    cinema = Cinema("starwars","12","istanbul/esenler", None)
#    db.insertAll(ManagerType.CINEMA,{
#        "name":"siperman"
#    })
#    print(db.get(ManagerType.CINEMA))
#Account.reset_password(Account)    
user = Person(name="Sila",address="ist",email="sbk@",phone="000",account="sdasd")
print(user)
