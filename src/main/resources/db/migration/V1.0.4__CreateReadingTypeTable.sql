CREATE TABLE "dwh-4chealth-db"."public"."readingtype" (
    R_READINGTYPEID int NOT NULL identity(1, 1),
    R_NAME varchar(25),
    R_DESCRIPTION varchar(152),
    R_ISACTIVE boolean,
    R_CREATEDDATE datetime,
    R_MODIFIEDDATE datetime
    )
diststyle all;