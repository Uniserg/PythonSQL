from sqlalchemy import create_engine, MetaData, SmallInteger, Table, \
    Column, Integer, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.exc import IntegrityError
from MyDate import MyDate
import csv
import pathlib


engine = create_engine('sqlite:///BD_primer.db')

metadata = MetaData()

students = Table(
    'students', metadata,
    Column('student_id', Integer, primary_key=True),
    Column('surname', String(60), nullable=False, index=True),
    Column('name', String(60), nullable=False),
    Column('stipend', Integer, nullable=False),
    Column('kurs', SmallInteger, nullable=False),
    Column('city', String(60), nullable=False),
    Column('birthday', MyDate),
    Column('univ_id', Integer, ForeignKey('universities.univ_id')),
    extend_existing=True
)

subjects = Table(
    'subjects', metadata,
    Column('subj_id', Integer, primary_key=True),
    Column('subj_name', String(80), nullable=False, index=True),
    Column('hour', Integer),
    Column('semester', SmallInteger, nullable=False),
    extend_existing=True
)

lecturers = Table(
    'lecturers', metadata,
    Column('lecturer_id', Integer, primary_key=True),
    Column('surname', String(60), nullable=False, index=True),
    Column('name', String(60), nullable=False),
    Column('city', String(60), nullable=False),
    Column('univ_id', Integer(), ForeignKey('universities.univ_id')),
    extend_existing=True
)

exam_marks = Table(
    'exams_marks', metadata,
    Column('exam_id', Integer, primary_key=True),
    Column('student_id', Integer, ForeignKey('students.student_id'), nullable=False),
    Column('subj_id', Integer, ForeignKey('subjects.subj_id'), nullable=False),
    Column('mark', SmallInteger, nullable=False),
    Column('exam_date', MyDate, nullable=False),
    extend_existing=True
)

universities = Table(
    'universities', metadata,
    Column('univ_id', Integer(), primary_key=True),
    Column('univ_name', String(150), nullable=False, index=True),
    Column('rating', Integer, nullable=False),
    Column('city', String(60), nullable=False),
    extend_existing=True
)

lec_subj = Table(
    "lec_subj", metadata,
    Column('lecturer_id', Integer, ForeignKey('lecturers.lecturer_id'), nullable=False),
    Column('subj_id', Integer, ForeignKey('subjects.subj_id'), nullable=False),
    PrimaryKeyConstraint('lecturer_id', 'subj_id', name='lec_subj_pk'),
    extend_existing=True
)

metadata.create_all(engine)

connection = engine.connect()

files = sorted(pathlib.Path('SCV').iterdir())
tables = [exam_marks, lec_subj, lecturers, students, subjects, universities]
ind = 0

for file in files:
    with open(file, 'r', encoding='utf-8') as scv_file:
        reader_csv = csv.reader(scv_file, delimiter=';')
        print(next(reader_csv))
        change_type = None
        for i in reader_csv:
            ins = tables[ind].insert().values(i)

            try:
                connection.execute(ins)
            except IntegrityError:
                print('Эти данные уже были добавлены!')
        ind += 1
