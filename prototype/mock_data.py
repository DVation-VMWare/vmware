# our imports

# std imports
import json
import random 

# make users (~100)
#   name
#   position
#   org
# make admins (~10)
#   name
#   org
#   tags + points   
# make tickets (~1000)
#   time
#   user
#   title
#   description
#   entered tags
#   generated tags

def make_users():
  pass

def make_admins():
  pass

def make_tickets(users, admins):
  pass

def main():
  users = make_users()
  admins = make_admins()
  tickets = make_tickets(users, admins)
# write to disk 

if __name__ == '__main__':
      main()
