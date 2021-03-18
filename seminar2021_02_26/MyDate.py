from sqlalchemy import TypeDecorator, Date
import datetime


class MyDate(TypeDecorator):
    impl = Date

    def process_bind_param(self, value, dialect):
        if type(value) is str:
            if value == 'NULL':
                return None
            return datetime.datetime.strptime(value, '%Y-%m-%d')
        return value
