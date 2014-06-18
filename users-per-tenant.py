import sys, MySQLdb, json

host = 'localhost'
user = 'root'
password = 'root'

def PrintTenantId(database, table, tenant):
    """ Connects to the table specified by the user and prints out its fields in HTML format used by Ben's wiki. """
    conn = MySQLdb.Connection(db=database, host=host, user=user, passwd=password)
    mysql = conn.cursor()
    sql = """ SELECT id FROM %s WHERE name=\"%s\" """ % (table, tenant)
    print sql
    mysql.execute(sql)
    fields=mysql.fetchall()
    for field in fields:
        id = field[0]
    
    mysql.close()
    conn.close()

    return id


def PrintEmailUsersPerTenant(database, table, tenantId):
    conn = MySQLdb.Connection(db=database, host=host, user=user, passwd=password)
    mysql = conn.cursor()
    sql = """ SELECT extra FROM %s """" % (table)
    print sql
    mysql.execute(sql)
    fields=mysql.fetchall()
    for field in fields:
        print field
        data = json.load(field)
        print data['tenantId']



users_database = sys.argv[1]
users_table = sys.argv[2]
users_tenant = sys.argv[3]
print "Wikified txt for " + users_database + "." + users_table
print "========================"

tenantId = PrintTenantId(users_database, users_table, users_tenant)

print tenantId

PrintEmailsUsersPerTenant(users_database, users_table, tenantId)

