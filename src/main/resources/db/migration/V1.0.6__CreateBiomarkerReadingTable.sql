CREATE TABLE "dwh-4chealth-db"."public"."biomarkerreadingtype" (
    BR_ID int NOT NULL identity(1, 1),
    BR_READINGTYPEID int,
    BR_BIOMARKERID int,
    BR_ISACTIVE boolean,
    BR_CREATEDDATE datetime,
    BR_MODIFIEDDATE datetime,
    FOREIGN KEY (BR_READINGTYPEID) REFERENCES "dwh-4chealth-db"."public"."readingtype" (R_READINGTYPEID),
    FOREIGN KEY (BR_BIOMARKERID) REFERENCES "dwh-4chealth-db"."public"."biomarker" (D_BIOMARKERID)
    )
diststyle all;