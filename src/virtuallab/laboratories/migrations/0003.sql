BEGIN;
--
-- Add field img to laboratory
--
CREATE TABLE "new__laboratories" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "img" varchar(20) NOT NULL, "title" varchar(20) NOT NULL UNIQUE);
INSERT INTO "new__laboratories" ("id", "title", "img") SELECT "id", "title", 'lab_1.jpg' FROM "laboratories";
DROP TABLE "laboratories";
ALTER TABLE "new__laboratories" RENAME TO "laboratories";
COMMIT;
