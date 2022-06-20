from baha import Baha, Baha_auto_signin
from accounts_system import Accounts_system
import sys

accounts_system = Accounts_system()
args = sys.argv[1:]
tmp_accounts = [{"uid": args[0],"passwd": args[1]}]
accounts_system.save_accounts(tmp_accounts)
baha_auto_signin = Baha_auto_signin()
baha_auto_signin.run()

