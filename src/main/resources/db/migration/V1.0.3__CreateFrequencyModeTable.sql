CREATE TABLE "dwh-4chealth-db"."public"."frequencymode" (
    F_FREQUENCYMODEID bigint NOT NULL,
    F_NAME varchar(25),
    F_DESCRIPTION varchar(150),
    F_ISACTIVE boolean,
    F_CREATEDDATE datetime,
    F_MODIFIEDDATE datetime)
diststyle all;