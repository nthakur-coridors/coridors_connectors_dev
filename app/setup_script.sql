--Create application roles
CREATE APPLICATION ROLE IF NOT EXISTS app_public;

--Create a versioned schema to hold those UDFs/Stored Procedures
CREATE OR ALTER VERSIONED SCHEMA core;
GRANT USAGE ON SCHEMA core TO APPLICATION ROLE app_public;

CREATE OR ALTER VERSIONED SCHEMA config;
GRANT USAGE ON SCHEMA config TO APPLICATION ROLE app_public;

CREATE OR ALTER VERSIONED SCHEMA confidential;
GRANT USAGE ON SCHEMA confidential TO APPLICATION ROLE app_public;

CREATE OR ALTER VERSIONED SCHEMA salesforce;
GRANT USAGE ON SCHEMA salesforce TO APPLICATION ROLE app_public;

create schema if not exists confidential;
GRANT USAGE ON SCHEMA confidential TO APPLICATION ROLE app_public;

--tables
CREATE table if not exists confidential.connections(id NUMBER AUTOINCREMENT START 1 INCREMENT 1, user VARCHAR(200), connection VARCHAR(50), password VARCHAR(200), secret VARCHAR(200), environment VARCHAR(20), status string(20));
-- INSERT INTO confidential.connections (user, connection, password, environment, secret, status) VALUES ('username1', 'connector', 'hashed_pass_sec', 'environment', 'secret', 'status');
GRANT SELECT ON table confidential.connections TO APPLICATION ROLE app_public;

CREATE table if not exists confidential.ingestion_lookup(id NUMBER AUTOINCREMENT START 1 INCREMENT 1, database string(50), schema string(50), connection_id VARCHAR(50), username VARCHAR(200), environment VARCHAR(20), table_name VARCHAR(100), sobject VARCHAR(100), applied_filter varchar, query string);
-- INSERT INTO confidential.ingestion_lookup(database, schema, connection_id, username, environment, table_name, sobject, applied_filter, query) VALUES ('database','schema', 'connection_id','connection_id', 'environment', 'table', 'table_name', 'True', 'object_query')
GRANT SELECT ON table confidential.ingestion_lookup TO APPLICATION ROLE app_public;


-- references storeprocedure, function, table, external access for single reference
CREATE OR REPLACE PROCEDURE config.register_single_reference(ref_name STRING, operation STRING, ref_or_alias STRING)
  RETURNS STRING
  LANGUAGE SQL
  AS $$
    BEGIN
      CASE (operation)
        WHEN 'ADD' THEN
          SELECT SYSTEM$SET_REFERENCE(:ref_name, :ref_or_alias);
        WHEN 'REMOVE' THEN
          SELECT SYSTEM$REMOVE_REFERENCE(:ref_name);
        WHEN 'CLEAR' THEN
          SELECT SYSTEM$REMOVE_REFERENCE(:ref_name);
      ELSE
        RETURN 'unknown operation: ' || operation;
      END CASE;
      
    END;
  $$;

GRANT USAGE ON PROCEDURE config.register_single_reference(STRING, STRING, STRING)
  TO APPLICATION ROLE app_public;

-- Configuration callback for the `EXTERNAL_ACCESS_REFERENCE` defined in the manifest.yml
-- The procedure returns a json format object containing information about the EAI to be created, that is
-- and show the same information in a popup-window in the UI.
-- There are no allowed_secrets since the API doesn't require authentication.
CREATE OR REPLACE PROCEDURE core.get_configuration(ref_name STRING)
RETURNS STRING
LANGUAGE SQL
AS 
$$
BEGIN
  CASE (UPPER(ref_name))
      WHEN 'EXTERNAL_ACCESS_REFERENCE' THEN
          RETURN OBJECT_CONSTRUCT(
              'type', 'CONFIGURATION',
              'payload', OBJECT_CONSTRUCT(
                  'host_ports', ARRAY_CONSTRUCT('api.coincap.io', 'login.salesforce.com'),
                  'allowed_secrets', 'NONE')                  
          )::STRING;
      ELSE
          RETURN '';
  END CASE;
END;	
$$;

GRANT USAGE ON PROCEDURE core.get_configuration(STRING) TO APPLICATION ROLE app_public;

-- Create stored procedures using the external access reference from the manifest.yml
-- The Stored Procedures needs to be created in runtime because EAI reference needs to be set
-- after installing the application.
CREATE OR REPLACE PROCEDURE core.create_eai_objects()
RETURNS STRING
LANGUAGE SQL
AS 
$$
BEGIN
  CREATE PROCEDURE IF NOT EXISTS core.salesforce()
  RETURNS VARIANT
  LANGUAGE PYTHON
  RUNTIME_VERSION = 3.9
  IMPORTS=('/module-api/salesforce.py')
  EXTERNAL_ACCESS_INTEGRATIONS = (reference('external_access_reference'))
  PACKAGES = ('snowflake-snowpark-python', 'requests', 'simple-salesforce')
  HANDLER = 'salesforce.salesforce_login';

  
  GRANT USAGE ON PROCEDURE core.salesforce() TO APPLICATION ROLE app_public;

  RETURN 'SUCCESS';
END;	
$$;

GRANT USAGE ON PROCEDURE core.create_eai_objects() TO APPLICATION ROLE app_public;

CREATE STREAMLIT core.ui
     FROM '/streamlit/'
     MAIN_FILE = 'Home.py';

-- Grant appropriate privileges over these objects to your application roles. 
GRANT USAGE ON STREAMLIT core.ui TO APPLICATION ROLE app_public;