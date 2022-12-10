CREATE TABLE "dwh-4chealth-db"."public"."biomarker" (
    D_BIOMARKERID int NOT NULL identity(1, 1),
    D_NAME varchar(25),
    D_DESCRIPTION varchar(152),
    D_ISACTIVE boolean,
    D_CREATEDDATE datetime,
    D_MODIFIEDDATE datetime)
diststyle all;