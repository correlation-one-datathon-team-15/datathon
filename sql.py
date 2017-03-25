
import psycopg2

# Drop and recreate table    
def ts_sql_table_drop_create(db_conn, table_name, create_sql_cols, drop=True):
    cur = db_conn.cursor()
    if (drop):
        try:
            cur.execute("DROP TABLE %s" % table_name)
        except psycopg2.Error:
            # Ignore the error
            db_conn.commit()
        
    cur.execute("CREATE TABLE %s (%s)" % (table_name, create_sql_cols));
    db_conn.commit();
    cur.close();
    
# Load table from file 
# TODO: Optimize loading
def ts_sql_load_table_from_file(db_conn, table_name, col_fmt, file_name, delim):
    cur = db_conn.cursor()
    
    cur.execute("COPY %s(%s) FROM '%s' DELIMITER AS '%s' CSV" % (table_name, col_fmt, file_name, delim))
        
    db_conn.commit()
    cur.close()
    print "Loaded data from %s" % (file_name)

connect_str = "dbname='testdata' user='haichen' host='localhost' " + \
                  "password='qwert'"
# use our connection values to establish a connection
db_conn = psycopg2.connect(connect_str)

demographics_colname = 'nta_name,borough,nta_code,population,under_5_years,' + \
    'f5_9_years,f10_14_years,f15_19_years,f20_24_years,f25_29_years,f30_34_years,' + \
    'f35_39_years,f40_44_years,f45_49_years,f50_54_years,f55_59_years,f60_64_years,' + \
    'over_65_years,median_age,people_per_acre,households,less_than_10000,' + \
    'f10000_to_14999,f15000_to_24999,f25000_to_34999,f35000_to_49999,f50000_to_74999,' + \
    'f75000_to_99999,f100000_to_149999,f150000_to_199999,f200000_or_more,' + \
    'median_income,mean_income'
demographics_coltype = 'nta_name text, borough text, nta_code text,' + \
    'population integer,under_5_years integer, f5_9_years integer,' + \
    'f10_14_years integer,f15_19_years integer,f20_24_years integer,' + \
    'f25_29_years integer,f30_34_years integer,f35_39_years integer,' + \
    'f40_44_years integer,f45_49_years integer,f50_54_years integer,' + \
    'f55_59_years integer,f60_64_years integer,over_65_years integer' + \
    ',median_age integer,people_per_acre float,households integer,' + \
    'less_than_10000 integer,f10000_to_14999 integer,f15000_to_24999 integer,' + \
    'f25000_to_34999 integer,f35000_to_49999 integer,f50000_to_74999 integer,' + \
    'f75000_to_99999 integer,f100000_to_149999 integer,f150000_to_199999 integer,' + \
    'f200000_or_more integer,median_income integer,mean_income integer'

ts_sql_table_drop_create(db_conn, 'demographics', demographics_coltype)
ts_sql_load_table_from_file(db_conn, 'demographics', demographics_colname,
    '/home/haichen/datathon/csv/demographics.csv', ',')

uber_2014_colname = 'pickup_datetime, pickup_latitude, pickup_longitude, base'
uber_2014_coltype = 'pickup_datetime text, pickup_latitude float, pickup_longitude float, base text'
ts_sql_table_drop_create(db_conn, 'uber_2014', uber_2014_coltype)
ts_sql_load_table_from_file(db_conn, 'uber_2014', uber_2014_colname,
    '/home/haichen/datathon/csv/uber_trips_2014.csv', ',')

uber_2015_colname = 'pickup_datetime, pickup_location_id, dispatch_base, affiliate_base'
uber_2015_coltype = 'pickup_datetime text, pickup_location_id integer, dispatch_base text, affiliate_base text'
ts_sql_table_drop_create(db_conn, 'uber_2015', uber_2015_coltype)
ts_sql_load_table_from_file(db_conn, 'uber_2015', uber_2015_colname,
    '/home/haichen/datathon/csv/uber_trips_2015.csv', ',')
#~ 
bases_colname = 'base, name, dba, dba_category'
bases_coltype = 'base text, name text, dba text, dba_category text'
ts_sql_table_drop_create(db_conn, 'bases', bases_coltype)
ts_sql_load_table_from_file(db_conn, 'bases', bases_colname,
    '/home/haichen/datathon/csv/bases.csv', ',')

zones_colname = 'location_id, borough, zone, service_zone, nta_code'
zones_coltype = 'location_id integer, borough text, zone text, service_zone text, nta_code text'
ts_sql_table_drop_create(db_conn, 'zones', zones_coltype)
ts_sql_load_table_from_file(db_conn, 'zones', zones_colname,
    '/home/haichen/datathon/csv/zones.csv', ',')

ntapos_colname = 'nta_code, latitude, longitude'
ntapos_coltype = 'nta_code text, latitude float, longitude float'
ts_sql_table_drop_create(db_conn, 'ntapos', ntapos_coltype)
ts_sql_load_table_from_file(db_conn, 'ntapos', ntapos_colname,
    '/home/haichen/datathon/csv/ntapos.csv', ',')

cur = db_conn.cursor()

cur.execute("select nt.latitude, nt.longitude " + 
            "from uber_2015 u15, zones z, demographics de, ntapos nt " +
            "where u15.pickup_location_id = z.location_id and z.nta_code = de.nta_code " +
            "and de.nta_code = nt.nta_code " +
            "and 120000 <= de.median_income")
result = cur.fetchall()
for tup in result:
    print tup[0], ',', tup[1]


print result
#~ 
cur.execute("select median_income " +
            "from demographics " +
            "order by median_income ")
print cur.fetchall()
#~ 
for tup in result:
    print tup[0]
#~ 
print len(result)
#~ 
cur.execute("select u15.pickup_location_id " + 
            "from uber_2015 u15, zones z, demographics de " +
            "where u15.pickup_location_id = z.location_id and z.nta_code = de.nta_code " +
            "and de.median_income < 30000 ")
print len(cur.fetchall())

cur.execute("select u15.pickup_location_id " + 
            "from uber_2015 u15, zones z, demographics de " +
            "where u15.pickup_location_id = z.location_id and z.nta_code = de.nta_code " +
            "and 30000 <= de.median_income and de.median_income < 40000 ")
print len(cur.fetchall())

cur.execute("select u15.pickup_location_id " + 
            "from uber_2015 u15, zones z, demographics de " +
            "where u15.pickup_location_id = z.location_id and z.nta_code = de.nta_code " +
            "and 40000 <= de.median_income and de.median_income < 50000 ")
print len(cur.fetchall())

cur.execute("select u15.pickup_location_id " + 
            "from uber_2015 u15, zones z, demographics de " +
            "where u15.pickup_location_id = z.location_id and z.nta_code = de.nta_code " +
            "and 50000 <= de.median_income and de.median_income < 60000 ")
print len(cur.fetchall())

cur.execute("select u15.pickup_location_id " + 
            "from uber_2015 u15, zones z, demographics de " +
            "where u15.pickup_location_id = z.location_id and z.nta_code = de.nta_code " +
            "and 60000 <= de.median_income and de.median_income < 70000 ")
print len(cur.fetchall())

cur.execute("select u15.pickup_location_id " + 
            "from uber_2015 u15, zones z, demographics de " +
            "where u15.pickup_location_id = z.location_id and z.nta_code = de.nta_code " +
            "and 70000 <= de.median_income and de.median_income < 80000 ")
print len(cur.fetchall())

cur.execute("select u15.pickup_location_id " + 
            "from uber_2015 u15, zones z, demographics de " +
            "where u15.pickup_location_id = z.location_id and z.nta_code = de.nta_code " +
            "and 90000 <= de.median_income and de.median_income < 120000")
print len(cur.fetchall())

cur.execute("select u15.pickup_location_id " + 
            "from uber_2015 u15, zones z, demographics de " +
            "where u15.pickup_location_id = z.location_id and z.nta_code = de.nta_code " +
            "and 120000 <= de.median_income ")
print len(cur.fetchall())

