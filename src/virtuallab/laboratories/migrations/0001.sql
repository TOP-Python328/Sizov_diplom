BEGIN;
--
-- Create model Laboratory
--
CREATE TABLE "laboratories" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(20) NOT NULL UNIQUE);
--
-- Create model Task
--
CREATE TABLE "tasks" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "number" varchar(20) NOT NULL, "description" text NOT NULL, "solution" varchar(200) NOT NULL, "laboratory_id" bigint NOT NULL REFERENCES "laboratories" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model TaskSolution
--
CREATE TABLE "tasks_solution" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "time_start" datetime NOT NULL, "time_end" datetime NOT NULL, "solution" varchar(200) NOT NULL, "status" varchar(20) NOT NULL, "grade" smallint unsigned NOT NULL CHECK ("grade" >= 0), "task_id" bigint NOT NULL REFERENCES "tasks" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "tasks_laboratory_id_c6fddb43" ON "tasks" ("laboratory_id");
CREATE INDEX "tasks_solution_task_id_da1d53e7" ON "tasks_solution" ("task_id");
COMMIT;
