import re  

def run(mgmt_email, sbx_email):
  if not re.match('^[a-z0-9\+]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', mgmt_email.lower()) or not re.match(
            '^[a-z0-9\+]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', sbx_email.lower()):
        error_reason = error_reason + "Invalid Email in the input parameters" + " | "
        error_flag = True


run("p.e.t.e.rgrainger2000@gmail.com", "p.e.tergrainger@gmail.com")