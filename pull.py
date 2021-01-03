import psycopg2
import connection_info
#connect
con = psycopg2.connect(database='postgres', user=connection_info.USER, password=connection_info.PASSWORD, host=connection_info.HOST, port='5432')
cur=con.cursor()
print('Database opened successfully')

def extract(table_name, file_name):
    #write my query
    query = 'SELECT * FROM {}'.format(table_name)
    #write the command to transform to csv
    query_for_csv = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)
    #filename
    filename = '{}.csv'.format(file_name)
    #load data
    with open(filename, 'w') as f_output: 
        cur.copy_expert(query_for_csv, f_output)

#pull the tweets
extract('tweets', 'tweets')
#pull the stock data
extract('stock_data', 'stock_data')

#close connection
con.close()