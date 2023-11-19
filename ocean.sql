-- auto-generated definition
create table ocean_all
(
    sea_area                    varchar(10),
    shore_line                  integer,
    zenith                      integer,
    shor_line_and_zhnith        text,
    latitude                    numeric,
    longitude                   numeric,
    observation_time            text,
    observed_depth              integer,
    water_temperature           numeric,
    "water_temperature_QC_flag" integer,
    salinity                    numeric,
    "salinity_QC_flag"          integer,
    dissolved_oxygen            numeric,
    "dissolved_oxygen_QC_flag"  integer,
    "QC_level"                  integer,
    phosphate                   numeric,
    nitrous_acid                numeric,
    nitric_acid                 numeric,
    sillicic_acid               numeric,
    ph                          text,
    transparency                numeric,
    atmospheric_pressure        numeric,
    screen_line                 text
);

comment on table ocean_all is '정선해양정보';

comment on column ocean_all.sea_area is '해역 ';

comment on column ocean_all.shore_line is '정선';

comment on column ocean_all.zenith is '정점';

comment on column ocean_all.shor_line_and_zhnith is '정선-정점';

comment on column ocean_all.latitude is '위도(˚N)';

comment on column ocean_all.longitude is '경도(˚E)';

comment on column ocean_all.observation_time is '관측일시(KST)';

comment on column ocean_all.observed_depth is '관측수심(m)';

comment on column ocean_all.water_temperature is '수온(℃)';

comment on column ocean_all."water_temperature_QC_flag" is '수온 QC Flag';

comment on column ocean_all.salinity is '염분(psu)';

comment on column ocean_all."salinity_QC_flag" is '염분 QC Flag';

comment on column ocean_all.dissolved_oxygen is '용존산소(ml/L)';

comment on column ocean_all."dissolved_oxygen_QC_flag" is '용존산소 QC Flag';

comment on column ocean_all.phosphate is '인산염인  (ug-at/L)';

comment on column ocean_all.nitrous_acid is '아질산질소 (ug-at/L)';

comment on column ocean_all.nitric_acid is '질산질소 (ug-at/L)';

comment on column ocean_all.sillicic_acid is '규산규소 (ug-at/L)';

comment on column ocean_all.ph is '폐하';

comment on column ocean_all.transparency is '투명도(m)';

comment on column ocean_all.atmospheric_pressure is '기압(hPa)';

comment on column ocean_all.screen_line is '조사선';

alter table ocean_all
    owner to postgres;



-- auto-generated definition
create table waterline_marine_information
(
    observation_date             date,
    temperature                  numeric,
    salinity                     numeric,
    dissolved_oxygen             numeric,
    phosphate_phosphorus         numeric,
    nitrous_acid_nitrogen        numeric,
    nitric_acid_nitrogen         numeric,
    silicic_acid_silicon         numeric,
    harmful_algal_bloom_presence integer,
    probability                  numeric
);

comment on table waterline_marine_information is '정선해양정보 및 유해적조발생여부';

alter table waterline_marine_information
    owner to postgres;



