CREATE TABLE `files` (
  file_id INT AUTO_INCREMENT,
  session_id INT,
  path_parts VARCHAR(128),
  stem VARCHAR(64),
  ext VARCHAR(6),
  PRIMARY KEY(file_id)
);

CREATE TABLE `sessions` (
  session_id INT AUTO_INCREMENT,
  file_name VARCHAR(36) NOT NULL UNIQUE,
  name VARCHAR(72) NOT NULL,
  description VARCHAR(144),
  PRIMARY KEY(session_id)
);

/*INSERT INTO `files` (session_id, path_parts, stem, ext) VALUES(1, "\\test\\t3\\t3.2\\", "testing", ".txt"), (1, "\\test\\t2\\t2.1\\", "doc", ".pdf");
INSERT INTO `files` (session_id, path_parts, stem, ext) VALUES(2, "\\test\\t5\\t5.6\\", "virus", ".exe"), (2, "\\test\\t1\\t1.3\\", "word_doc", ".docx");
INSERT INTO `sessions` (file_name, name, description)
    VALUES ("session1", "session-1", "copy to dropbox"),
("session2", "session-2", "copy to gdrive");*/


/* http://www.sqlfiddle.com/#!9/bbae6a/6 */
/* JOIN TABLES BY session_id key */
SELECT f.file_id, f.session_id, f.path_parts, f.stem, f.ext
FROM files f
INNER JOIN sessions s ON s.session_id = f.session_id;

SELECT s.session_id, s.file_name, s.name, s.description FROM sessions as s;
