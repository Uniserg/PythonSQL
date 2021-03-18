--1 +
SELECT student_id || ';' ||
       UPPER(surname) || ';' ||
       UPPER(name) || ';' ||
       STRFTIME('%d/%m/%Y') || ';' ||
       univ_id || '.'
    AS [ROWS1]
FROM student;

--2 +
SELECT
       SUBSTR(name, 1, 1) || '.' ||
       UPPER(surname) ||
       '; место жительства - ' || UPPER(city) || '; ' ||
       'родился - ' || STRFTIME('%d.%m.%Y', birthday) || '.'
AS [ROWS2]
FROM student;

--3 +
SELECT
       LOWER(SUBSTR(name, 1, 1)) || '.' ||
       LOWER(surname) ||
       '; место жительства - ' || LOWER(city) || '; ' ||
       'родился - ' || STRFTIME('%d-%m-%Y', birthday) || '.'
AS [ROWS3]
FROM student;
--4 +
SELECT
       name|| ' ' ||
       surname ||
       ' родился в ' || STRFTIME('%Y', birthday) || '.'
AS "Bithday Info"
FROM student;
--5 +
SELECT surname, name, stipend * 100
FROM student;
--6 +
SELECT UPPER(surname), UPPER(name), stipend * 100
FROM student
WHERE kurs IN (1, 2, 4);

--7 +
SELECT 'Код - ' || univ_id ||
       '; ' || univ_name ||
       ' - г. ' || city ||
       '; Рейтинг=' || rating || '.'
AS "Univesity Info"
FROM university;

--8 +
SELECT 'Код - ' || univ_id ||
       '; ' || univ_name ||
       ' - г. ' || city ||
       '; Рейтинг=' || ROUND(rating, LENGTH(rating) - 1) || '.'
AS "Univesity Info (ROUND)"
FROM university;

--9 +
SELECT COUNT(DISTINCT student_id)
FROM exam_marks
WHERE subj_id = 20;

--10 +
SELECT COUNT(DISTINCT subj_id)
FROM exam_marks;

--11 +
SELECT student_id, MIN(mark)
FROM exam_marks
GROUP BY student_id;

--12 +
SELECT student_id, MAX(mark)
FROM exam_marks
GROUP BY student_id;

--13 +
SELECT surname
FROM student
WHERE surname LIKE 'И%'
ORDER BY surname
LIMIT 1;

--14 +
SELECT subj_name, MAX(semester)
FROM subject
GROUP BY subj_name;

--15 +
SELECT STRFTIME('%d.%m.%Y', exam_date) AS "Date", COUNT(student_id)
FROM exam_marks
GROUP BY exam_date;

--16 +
SELECT stud.kurs, subj.subj_name, AVG(em.mark)
FROM exam_marks em
    JOIN student stud on stud.student_id = em.student_id
    JOIN subject subj on em.subj_id = subj.subj_id
GROUP BY stud.kurs, subj.subj_name;

--17 +
SELECT st.student_id, surname || ' ' || name as "Full Name", AVG(mark)
FROM student st
    JOIN exam_marks em on st.student_id = em.student_id
GROUP BY st.student_id;

--18 +
SELECT exam_id, subj_name, AVG(mark)
FROM exam_marks
    JOIN subject s on s.subj_id = exam_marks.subj_id
GROUP BY exam_id;

--19 +
SELECT subj.subj_name, COUNT(DISTINCT stud.student_id)
FROM exam_marks
    JOIN subject subj on subj.subj_id = exam_marks.subj_id
    JOIN student stud on stud.student_id = exam_marks.student_id
GROUP BY subj.subj_name;

--20 +
SELECT st.kurs, COUNT(DISTINCT em.subj_id)
FROM student AS st
    JOIN exam_marks AS em ON st.student_id = em.student_id
GROUP BY st.kurs;
