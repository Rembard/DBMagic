import pandas as pd
from clickhouse_driver import Client
connection_params_clickhouse = {'host': '10.144.198.132',
                                'user': "mon_report_bti",
                                'password': "Report_112233",
                                'database': "TestDB"}
cur_clic = Client(**connection_params_clickhouse)
#cur_clic.execute ('CREATE TABLE IF NOT EXISTS  test (Name String, Soname String, Fathername String, Age Int32) ENGINE = Memory')
#cur_clic.execute ('INSERT INTO test (Age) VALUES', [{'Age':12345}])

testfile = pd.read_excel('try_to_import.xlsx')
#table_columns = testfile.columns
print (testfile.head())