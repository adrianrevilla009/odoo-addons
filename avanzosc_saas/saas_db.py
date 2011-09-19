from osv import osv
from osv import fields

class saas_db(osv.osv):
    _name = 'saas.db'
 
    _columns = {
        'name': fields.char('Database Name', size=64),
        'db_user': fields.char('Database User', size=64),
        'db_password': fields.char('Database Password', size=64),
        'server_id':fields.many2one('saas.server', 'Server'),        
    }
saas_db()