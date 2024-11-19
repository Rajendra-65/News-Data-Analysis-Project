use role accountadmin;

create database news_api;

USE news_api;

CREATE FILE FORMAT parquet_format TYPE=parquet;

CREATE OR REPLACE STORAGE INTEGRATION news_data_gcs_integration
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = GCS
ENABLED = TRUE
STORAGE_ALLOWED_LOCATIONS = ('gcs://snowflake_projects_all/news_data_analysis/parquet_files/');

desc integration news_data_gcs_integration;

CREATE OR REPLACE STAGE gcs_raw_data_stage
URL = 'gcs://snowflake_projects_all/news_data_analysis/parquet_files/'
STORAGE_INTEGRATION = news_data_gcs_integration
FILE_FORMAT = (TYPE = 'PARQUET');

show stages;

select * from news_api_data;

select count(*) from news_api_data;