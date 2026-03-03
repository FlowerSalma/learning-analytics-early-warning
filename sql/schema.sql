DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS engagement;
DROP TABLE IF EXISTS outcomes;

CREATE TABLE students (
  student_id INTEGER PRIMARY KEY,
  school TEXT,
  sex TEXT,
  age INTEGER,
  address TEXT,
  famsize TEXT,
  parent_status TEXT,
  mother_edu INTEGER,
  father_edu INTEGER,
  parent_edu_max INTEGER
);

CREATE TABLE engagement (
  student_id INTEGER,
  travel_time INTEGER,
  study_time INTEGER,
  failures INTEGER,
  absences INTEGER,
  schoolsup TEXT,
  famsup TEXT,
  paid TEXT,
  activities TEXT,
  higher TEXT,
  internet TEXT,
  FOREIGN KEY(student_id) REFERENCES students(student_id)
);

CREATE TABLE outcomes (
  student_id INTEGER,
  g1 INTEGER,
  g2 INTEGER,
  g3 INTEGER,
  pass_fail INTEGER,
  FOREIGN KEY(student_id) REFERENCES students(student_id)
);
