BEGIN;
--
-- Add field teacher to tasksolution
--
CREATE TABLE "new__tasks_solution" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "teacher_id" integer NOT NULL REFERENCES "teachers" ("user_id") DEFERRABLE INITIALLY DEFERRED, "time_start" datetime NOT NULL, "time_end" datetime NOT NULL, "solution" varchar(200) NOT NULL, "status" varchar(20) NOT NULL, "grade" smallint unsigned NOT NULL CHECK ("grade" >= 0), "task_id" bigint NOT NULL REFERENCES "tasks" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__tasks_solution" ("id", "time_start", "time_end", "solution", "status", "grade", "task_id", "teacher_id") SELECT "id", "time_start", "time_end", "solution", "status", "grade", "task_id", NULL FROM "tasks_solution";
DROP TABLE "tasks_solution";
ALTER TABLE "new__tasks_solution" RENAME TO "tasks_solution";
CREATE INDEX "tasks_solution_teacher_id_0718e8f8" ON "tasks_solution" ("teacher_id");
CREATE INDEX "tasks_solution_task_id_da1d53e7" ON "tasks_solution" ("task_id");
--
-- Add field user to tasksolution
--
CREATE TABLE "new__tasks_solution" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "time_start" datetime NOT NULL, "time_end" datetime NOT NULL, "solution" varchar(200) NOT NULL, "status" varchar(20) NOT NULL, "grade" smallint unsigned NOT NULL CHECK ("grade" >= 0), "task_id" bigint NOT NULL REFERENCES "tasks" ("id") DEFERRABLE INITIALLY DEFERRED, "teacher_id" integer NOT NULL REFERENCES "teachers" ("user_id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "schoolboys" ("user_id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__tasks_solution" ("id", "time_start", "time_end", "solution", "status", "grade", "task_id", "teacher_id", "user_id") SELECT "id", "time_start", "time_end", "solution", "status", "grade", "task_id", "teacher_id", NULL FROM "tasks_solution";
DROP TABLE "tasks_solution";
ALTER TABLE "new__tasks_solution" RENAME TO "tasks_solution";
CREATE INDEX "tasks_solution_task_id_da1d53e7" ON "tasks_solution" ("task_id");
CREATE INDEX "tasks_solution_teacher_id_0718e8f8" ON "tasks_solution" ("teacher_id");
CREATE INDEX "tasks_solution_user_id_2bb1b502" ON "tasks_solution" ("user_id");
COMMIT;
