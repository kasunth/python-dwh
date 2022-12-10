CREATE TABLE "dwh-4chealth-db"."public"."biomarker_value" (
    BV_ID int NOT NULL identity(1, 1),
    BV_UERID bigint NOT NULL,
    BV_BIOMARKERREADINGID bigint NOT NULL,
    BV_DEVICETYPEID bigint NOT NULL,
    BV_FREQUENCYMODEID bigint NOT NULL,
    BV_VALUE varchar(150),
    BV_ISACTIVE boolean,
    BV_READTIME datetime,
    BV_SYNCTIME datetime,
    BV_INSERTEDTIME datetime,
    FOREIGN KEY (BV_BIOMARKERREADINGID) REFERENCES "dwh-4chealth-db"."public"."biomarkerreadingtype" (BR_ID),
    FOREIGN KEY (BV_DEVICETYPEID) REFERENCES "dwh-4chealth-db"."public"."devicetype" (D_DEVICETYPEID),
    FOREIGN KEY (BV_FREQUENCYMODEID) REFERENCES "dwh-4chealth-db"."public"."frequencymode" (F_FREQUENCYMODEID)
    )
diststyle all;