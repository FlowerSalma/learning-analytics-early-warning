-- A) Full modeling dataset
SELECT
  s.student_id,
  s.school,
  s.sex,
  s.age,
  s.address,
  s.parent_edu_max,
  e.travel_time,
  e.study_time,
  e.failures,
  e.absences,
  e.schoolsup,
  e.famsup,
  e.paid,
  e.activities,
  e.higher,
  e.internet,
  o.g1,
  o.g2,
  o.g3,
  o.pass_fail
FROM students s
JOIN engagement e ON s.student_id = e.student_id
JOIN outcomes o ON s.student_id = o.student_id;

-- B) KPI: overall pass rate
SELECT AVG(pass_fail) AS pass_rate, COUNT(*) AS n
FROM outcomes;

-- C) KPI: pass rate by school
SELECT s.school, AVG(o.pass_fail) AS pass_rate, COUNT(*) AS n
FROM students s
JOIN outcomes o ON s.student_id = o.student_id
GROUP BY s.school
ORDER BY n DESC;

-- D) KPI: pass rate by sex
SELECT s.sex, AVG(o.pass_fail) AS pass_rate, COUNT(*) AS n
FROM students s
JOIN outcomes o ON s.student_id = o.student_id
GROUP BY s.sex;

-- E) KPI: average G3 by absence band
SELECT
  CASE
    WHEN e.absences BETWEEN 0 AND 5 THEN '0-5'
    WHEN e.absences BETWEEN 6 AND 10 THEN '6-10'
    WHEN e.absences BETWEEN 11 AND 20 THEN '11-20'
    ELSE '21+'
  END AS absence_band,
  AVG(o.g3) AS avg_g3,
  COUNT(*) AS n
FROM engagement e
JOIN outcomes o ON e.student_id = o.student_id
GROUP BY absence_band
ORDER BY n DESC;
