from api_minuscule.exception.user_not_authenticated_exception import UserNotAuthenticated
from api_minuscule.metier.user import User
from api_minuscule.dao.user_dao import UserDao


class UserService:
    @staticmethod
    def createUser(user: User) -> User:
        return UserDao.createUser(user)

    @staticmethod
    def getUser(user_id: str) -> User:
        return UserDao.getUser(user_id)

    @staticmethod
    def updateUser(user_id: str, user: User) -> User:
        return UserDao.updateUser(user_id, user)

    @staticmethod
    def deleteUser(user_id: str) -> User:
        return UserDao.deleteUser(user_id)

    @staticmethod
    def authenticate_and_get_user(username: str, password: str) -> User:
        if (UserDao.verifyPassword(username, password)):
            return UserDao.getUser(username)
        else:
            raise UserNotAuthenticated(username=username)
