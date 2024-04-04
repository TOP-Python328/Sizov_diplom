BEGIN;
--
-- Create model Group
--
CREATE TABLE "groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL);
--
-- Create model Teacher
--
CREATE TABLE "teachers" ("user_id" integer NOT NULL PRIMARY KEY REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "last_name" varchar(30) NOT NULL, "first_name" varchar(30) NOT NULL, "patr_name" varchar(30) NOT NULL, "uid" varchar(10) NOT NULL UNIQUE, "organization" varchar(50) NOT NULL, "post" varchar(100) NOT NULL);
--
-- Create model Schoolboy
--
CREATE TABLE "schoolboys" ("user_id" integer NOT NULL PRIMARY KEY REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "last_name" varchar(30) NOT NULL, "first_name" varchar(30) NOT NULL, "patr_name" varchar(30) NOT NULL, "uid" varchar(10) NOT NULL UNIQUE, "organization" varchar(50) NOT NULL, "group_id" bigint NOT NULL REFERENCES "groups" ("id") DEFERRABLE INITIALLY DEFERRED, "teacher_id" integer NOT NULL REFERENCES "teachers" ("user_id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field teacher to group
--
CREATE TABLE "new__groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(10) NOT NULL, "teacher_id" integer NOT NULL REFERENCES "teachers" ("user_id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__groups" ("id", "title", "teacher_id") SELECT "id", "title", NULL FROM "groups";
DROP TABLE "groups";
ALTER TABLE "new__groups" RENAME TO "groups";
CREATE INDEX "schoolboys_group_id_b57d1bf9" ON "schoolboys" ("group_id");
CREATE INDEX "schoolboys_teacher_id_f4eb63d9" ON "schoolboys" ("teacher_id");
CREATE INDEX "groups_teacher_id_f297e8a3" ON "groups" ("teacher_id");
COMMIT;
