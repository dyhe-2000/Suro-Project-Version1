from wsgiref.simple_server import make_server           # web server we use
from pyramid.config import Configurator                 # Pyramid configuration

from pyramid.renderers import render_to_response        # Render an HTML page from a template (Jinja2)
from pyramid.httpexceptions import HTTPFound            # Perform redirects from the backend to other routes

# NOTE: this is unencrypted but signed session stored in client cookies. It isn't the most secure, but at least it's baked into Pyramid. Shame on Pyramid!
from pyramid.session import SignedCookieSessionFactory  # The default session factory to generate session objects

import mysql.connector as mysql                         # Library to connect to the MySQL database
import os                                               # To perform OS-level operations (get environment variables)

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from datetime import datetime

import mysql.connector as mysql
import os
import smtplib, ssl

db_user = os.environ['MYSQL_USER']
db_pass = os.environ['MYSQL_PASSWORD']
db_name = os.environ['MYSQL_DATABASE']
db_host = os.environ['MYSQL_HOST']

def get_home(req):
  count_customers_in_Customers_Tb()
  News_DB_To_File()
  # Connect to the database and retrieve the users
  # db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  # cursor = db.cursor()
  # cursor.execute("select first_name, last_name, email from Users;")
  # records = cursor.fetchall()
  # db.close()
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  if len(req.session) == 0:
    query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
    values = [
      ('guest', '/', '1', datetime.now())
    ]
    cursor.executemany(query, values)
    db.commit()
  elif len(req.session) >= 0:
    cursor.execute("select * from visits where session_id ='%s' and route_name = '/';" % req.session['user'])
    records = cursor.fetchall()
    count = 0
    for record in records:
      count = count + 1
    if count == 0:
      query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
      values = [
        (req.session['user'], '/', '0', datetime.now())
      ]
      cursor.executemany(query, values)
      db.commit()
    elif count >= 0:
      query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
      values = [
        (req.session['user'], '/', '1', datetime.now())
      ]
      cursor.executemany(query, values)
      db.commit()
  return render_to_response('templates/Home_Page.html', {}, request=req)
  
def get_post_user(req):
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  if len(req.session) == 0:
    query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
    values = [
      ('guest', '/signup', '1', datetime.now())
    ]
    cursor.executemany(query, values)
    db.commit()
  elif len(req.session) >= 0:
    cursor.execute("select * from visits where session_id ='%s' and route_name = '/signup';" % req.session['user'])
    records = cursor.fetchall()
    count = 0
    for record in records:
      count = count + 1
    if count == 0:
      query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
      values = [
        (req.session['user'], '/signup', '0', datetime.now())
      ]
      cursor.executemany(query, values)
      db.commit()
    elif count >= 0:
      query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
      values = [
        (req.session['user'], '/signup', '1', datetime.now())
      ]
      cursor.executemany(query, values)
      db.commit()
  return render_to_response('templates/post_user.html', {}, request=req)
  
def get_about(req):
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  if len(req.session) == 0:
    query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
    values = [
      ('guest', '/about', '1', datetime.now())
    ]
    cursor.executemany(query, values)
    db.commit()
  elif len(req.session) >= 0:
    cursor.execute("select * from visits where session_id ='%s' and route_name = '/about';" % req.session['user'])
    records = cursor.fetchall()
    count = 0
    for record in records:
      count = count + 1
    if count == 0:
      query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
      values = [
        (req.session['user'], '/about', '0', datetime.now())
      ]
      cursor.executemany(query, values)
      db.commit()
    elif count >= 0:
      query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
      values = [
        (req.session['user'], '/about', '1', datetime.now())
      ]
      cursor.executemany(query, values)
      db.commit()
  return render_to_response('templates/About.html', {}, request=req)
  
def get_about_us(req):
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  if len(req.session) == 0:
    query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
    values = [
      ('guest', '/team', '1', datetime.now())
    ]
    cursor.executemany(query, values)
    db.commit()
  elif len(req.session) >= 0:
    cursor.execute("select * from visits where session_id ='%s' and route_name = '/team';" % req.session['user'])
    records = cursor.fetchall()
    count = 0
    for record in records:
      count = count + 1
    if count == 0:
      query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
      values = [
        (req.session['user'], '/team', '0', datetime.now())
      ]
      cursor.executemany(query, values)
      db.commit()
    elif count >= 0:
      query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
      values = [
        (req.session['user'], '/team', '1', datetime.now())
      ]
      cursor.executemany(query, values)
      db.commit()
  return render_to_response('templates/About_Us.html', {}, request=req)
  
def get_product(req):
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  if len(req.session) == 0:
    query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
    values = [
      ('guest', '/product', '1', datetime.now())
    ]
    cursor.executemany(query, values)
    db.commit()
  elif len(req.session) >= 0:
    cursor.execute("select * from visits where session_id ='%s' and route_name = '/product';" % req.session['user'])
    records = cursor.fetchall()
    count = 0
    for record in records:
      count = count + 1
    if count == 0:
      query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
      values = [
        (req.session['user'], '/product', '0', datetime.now())
      ]
      cursor.executemany(query, values)
      db.commit()
    elif count >= 0:
      query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
      values = [
        (req.session['user'], '/product', '1', datetime.now())
      ]
      cursor.executemany(query, values)
      db.commit()
  return render_to_response('templates/Product.html', {}, request=req)
  
def post_user(req):
  # x = datetime.datetime.utcnow()+datetime.timedelta(hours=-7)+datetime.timedelta(minutes=-12)+datetime.timedelta(seconds=30)
  # Connect to the database
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  # get user info
  firstname = req.params['firstname']
  lastname = req.params['lastname']
  email = req.params['email']
  phonenumber = req.params['phonenumber']
  password = req.params['password']
  # print(check(userId))
  # print(check(password))
  print(firstname)
  print(lastname)
  print(email)
  print(password)
  tempStr = ''
  if firstname != tempStr and lastname != tempStr and email != tempStr:
    # Insert Records
    query = "insert into Customers (first_name, last_name, email, password, created_at) values (%s, %s, %s, %s, %s)"
    values = [
      (firstname, lastname, email, password, datetime.now())
    ]
    cursor.executemany(query, values)
    db.commit()
    print('post_user finished inserting into Customers')
    count_customers_in_Customers_Tb()
    return render_to_response('templates/Home_Page.html', {}, request=req)
  else:
    return render_to_response('templates/try_again.html', {}, request=req)
    
def count_customers_in_Customers_Tb():
  Lines = []
  # Connect to the database and retrieve the student
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select * from Customers;")
  records = cursor.fetchall()
  count = 0
  for record in records:
    count = count + 1
  file2 = open('templates/public/count_customers.txt', 'w') 
  file2.write('current customers get started count: ')
  file2.write(str(int(count)))
  file2.close()
  
def get_enter_progress(req):
  return render_to_response('templates/enter_progress_page.html', {}, request=req)
  
def write_progress_to_file(req):
  # x = datetime.datetime.utcnow()+datetime.timedelta(hours=-7)+datetime.timedelta(minutes=-12)+datetime.timedelta(seconds=30)
  # Connect to the database
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  # get user info
  progress = req.params['progress_percent']
  print(progress)
  print('checking all numbers')
  print(check(progress))
  if check(progress) == False or len(progress) == 0:
    return render_to_response('templates/try_again.html', {}, request=req)
  elif int(progress) > 100 or int(progress) < 0:
    return render_to_response('templates/try_again.html', {}, request=req)
  else:
    percentage = int(progress)
    file2 = open('templates/public/percentage.txt', 'w') 
    file2.write('MVP progress percentage: ')
    file2.write(str(percentage))
    file2.write('%')
    file2.close()
  return render_to_response('templates/success.html', {}, request=req)
  
def check(test_str):
  import re
    #http://docs.python.org/library/re.html
    #re.search returns None if no position in the string matches the pattern
    #pattern to search for any character other then . a-z 0-9
  pattern = r'[^\.0-9]'
  if re.search(pattern, test_str):
        #Character other then . a-z 0-9 was found
        #print 'Invalid : %r' % (test_str,)
        return False
  else:
        #No character other then . a-z 0-9 was found
        #print 'Valid   : %r' % (test_str,)
      return True
      
def get_enter_news(req):
  #print('in get_enter_news function')
  return render_to_response('templates/enter_news.html', {}, request=req)
  
def write_news_to_db(req):
  # x = datetime.datetime.utcnow()+datetime.timedelta(hours=-7)+datetime.timedelta(minutes=-12)+datetime.timedelta(seconds=30)
  # Connect to the database
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  # get user info
  title = req.params['news_title']
  time = req.params['news_time']
  content = req.params['news_content']
  print(title)
  print(time)
  print(content)
  query = "insert into News (title, time, content) values (%s, %s, %s)"
  values = [
    (title,time,content)
  ]
  cursor.executemany(query, values)
  db.commit()
  News_DB_To_File()
  return render_to_response('templates/success.html', {}, request=req)
  
def News_DB_To_File():
  Lines = []
  # Connect to the database and retrieve the student
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  cursor.execute("select * from News;")
  records = cursor.fetchall()
  count = 0
  for record in records:
    tempStr = ''
    for x in range(0, 4): #0 - 3, total 4 times
      tempStr += str(record[x])
      tempStr += ' '
    tempStr += '\n'
    print(tempStr)
    Lines.append(tempStr)
  file2 = open('templates/public/News.txt', 'w') 
  file2.writelines(Lines)
  file2.close()

# Route to retrieve the LOGGED-IN homepage
def get_admin(req):
  print_dash_board_in_file()
  if 'user' in req.session: # logged in
    print(req.session)
    print(req.session['user'])
    #print(req.session[1])
    print(len(req.session))
    return render_to_response('templates/admin.html',{'user':req.session['user']})
  else: # not logged in
    return HTTPFound(req.route_url("get_login"))
  
# Route to retrieve the login page
def get_login(req):
  error = req.session.pop_flash('login_error')
  error = error[0] if error else ''
  db = mysql.connect(user=db_user, password=db_pass, host=db_host, database=db_name)
  cursor = db.cursor()
  if len(req.session) == 0:
    query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
    values = [
      ('guest', '/login', '1', datetime.now())
    ]
    cursor.executemany(query, values)
    db.commit()
  elif len(req.session) >= 0:
    cursor.execute("select * from visits where session_id ='%s' and route_name = '/login';" % req.session['user'])
    records = cursor.fetchall()
    count = 0
    for record in records:
      count = count + 1
    if count == 0:
      query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
      values = [
        (req.session['user'], '/login', '0', datetime.now())
      ]
      cursor.executemany(query, values)
      db.commit()
    elif count >= 0:
      query = "insert into visits (session_id, route_name, previous_has_signed_in, timestamp) values (%s, %s, %s, %s)"
      values = [
        (req.session['user'], '/login', '1', datetime.now())
      ]
      cursor.executemany(query, values)
      db.commit()
  return render_to_response('templates/login.html', {'error': error})


# Route to handle login form submissions coming from the login page
def post_login(req):
  email = None
  password = None
  if req.method == "POST":
    email = req.params['email']
    password = req.params['password']

  # Connect to the database and try to retrieve the user
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  query = "SELECT email, password FROM Customers WHERE email='%s';" % email
  cursor.execute(query)
  user = cursor.fetchone() # will return a tuple (email, password) if user is found and None otherwise
  db.close()

  # If user is found and the password is valid, store in session, and redirect to the homepage
  # Otherwise, redirect back to the login page with a flash message
  # Note: passwords should be hashed and encrypted in actual production solutions!
  if user is not None and user[1] == password:
    req.session['user'] = user[0] # set the session variable
    return HTTPFound(req.route_url("get_admin"))
  else:
    req.session.invalidate() # clear session
    req.session.flash('Invalid login attempt. Please try again.', 'login_error')
    return HTTPFound(req.route_url("get_login"))
    
def print_dash_board_in_file():
  Lines = []
  # Connect to the database and retrieve the student
  db = mysql.connect(host=db_host, database=db_name, user=db_user, passwd=db_pass)
  cursor = db.cursor()
  #======================================================================================================
  cursor.execute("select * from visits where route_name = '/';")
  records = cursor.fetchall()
  home_total_visit_count = 0
  for record in records:
    home_total_visit_count = home_total_visit_count + 1
    
  cursor.execute("select * from visits where route_name = '/' and session_id = 'guest';")
  records = cursor.fetchall()
  home_total_guest_visit_count = 0
  for record in records:
    home_total_guest_visit_count = home_total_guest_visit_count + 1
    
  cursor.execute("select * from visits where route_name = '/' and previous_has_signed_in = '0';")
  records = cursor.fetchall()
  home_unique_user_visit_count = 0
  for record in records:
    home_unique_user_visit_count = home_unique_user_visit_count + 1
  #======================================================================================================
  cursor.execute("select * from visits where route_name = '/about';")
  records = cursor.fetchall()
  about_total_visit_count = 0
  for record in records:
    about_total_visit_count = about_total_visit_count + 1
    
  cursor.execute("select * from visits where route_name = '/about' and session_id = 'guest';")
  records = cursor.fetchall()
  about_total_guest_visit_count = 0
  for record in records:
    about_total_guest_visit_count = about_total_guest_visit_count + 1
    
  cursor.execute("select * from visits where route_name = '/about' and previous_has_signed_in = '0';")
  records = cursor.fetchall()
  about_unique_user_visit_count = 0
  for record in records:
    about_unique_user_visit_count = about_unique_user_visit_count + 1
  #======================================================================================================
  cursor.execute("select * from visits where route_name = '/team';")
  records = cursor.fetchall()
  team_total_visit_count = 0
  for record in records:
    team_total_visit_count = team_total_visit_count + 1
    
  cursor.execute("select * from visits where route_name = '/team' and session_id = 'guest';")
  records = cursor.fetchall()
  team_total_guest_visit_count = 0
  for record in records:
    team_total_guest_visit_count = team_total_guest_visit_count + 1
    
  cursor.execute("select * from visits where route_name = '/team' and previous_has_signed_in = '0';")
  records = cursor.fetchall()
  team_unique_user_visit_count = 0
  for record in records:
    team_unique_user_visit_count = team_unique_user_visit_count + 1
  #======================================================================================================
  cursor.execute("select * from visits where route_name = '/product';")
  records = cursor.fetchall()
  product_total_visit_count = 0
  for record in records:
    product_total_visit_count = product_total_visit_count + 1
    
  cursor.execute("select * from visits where route_name = '/product' and session_id = 'guest';")
  records = cursor.fetchall()
  product_total_guest_visit_count = 0
  for record in records:
    product_total_guest_visit_count = product_total_guest_visit_count + 1
    
  cursor.execute("select * from visits where route_name = '/product' and previous_has_signed_in = '0';")
  records = cursor.fetchall()
  product_unique_user_visit_count = 0
  for record in records:
    product_unique_user_visit_count = product_unique_user_visit_count + 1
  #======================================================================================================
  cursor.execute("select * from visits where route_name = '/signup';")
  records = cursor.fetchall()
  signup_total_visit_count = 0
  for record in records:
    signup_total_visit_count = signup_total_visit_count + 1
    
  cursor.execute("select * from visits where route_name = '/signup' and session_id = 'guest';")
  records = cursor.fetchall()
  signup_total_guest_visit_count = 0
  for record in records:
    signup_total_guest_visit_count = signup_total_guest_visit_count + 1
    
  cursor.execute("select * from visits where route_name = '/signup' and previous_has_signed_in = '0';")
  records = cursor.fetchall()
  signup_unique_user_visit_count = 0
  for record in records:
    signup_unique_user_visit_count = signup_unique_user_visit_count + 1
  #======================================================================================================
  cursor.execute("select * from visits where route_name = '/login';")
  records = cursor.fetchall()
  login_total_visit_count = 0
  for record in records:
    login_total_visit_count = login_total_visit_count + 1
    
  cursor.execute("select * from visits where route_name = '/login' and session_id = 'guest';")
  records = cursor.fetchall()
  login_total_guest_visit_count = 0
  for record in records:
    login_total_guest_visit_count = login_total_guest_visit_count + 1
    
  cursor.execute("select * from visits where route_name = '/login' and previous_has_signed_in = '0';")
  records = cursor.fetchall()
  login_unique_user_visit_count = 0
  for record in records:
    login_unique_user_visit_count = login_unique_user_visit_count + 1
  #======================================================================================================
  file2 = open('templates/public/Dashboard.txt', 'w') 
  file2.write('Route  |  Total visitors  |  Guest total visitors  |  Unique signed in visitors\n')
  file2.write('/' + '              ' + str(int(home_total_visit_count)) + '                       ' + str(int(home_total_guest_visit_count)) + '                       ' + str(int(home_unique_user_visit_count)) + '\n')
  file2.write('/about' + '         ' + str(int(about_total_visit_count)) + '                       ' + str(int(about_total_guest_visit_count)) + '                       ' + str(int(about_unique_user_visit_count)) + '\n')
  file2.write('/team' + '          ' + str(int(team_total_visit_count)) + '                       ' + str(int(team_total_guest_visit_count)) + '                       ' + str(int(team_unique_user_visit_count)) + '\n')
  file2.write('/product' + '       ' + str(int(product_total_visit_count)) + '                       ' + str(int(product_total_guest_visit_count)) + '                       ' + str(int(product_unique_user_visit_count)) + '\n')
  file2.write('/signup' + '        ' + str(int(signup_total_visit_count)) + '                       ' + str(int(signup_total_guest_visit_count)) + '                       ' + str(int(signup_unique_user_visit_count)) + '\n')
  file2.write('/login' + '         ' + str(int(login_total_visit_count)) + '                       ' + str(int(login_total_guest_visit_count)) + '                       ' + str(int(login_unique_user_visit_count)) + '\n')
  file2.close()
  
def get_shower_door_products(req):
  return render_to_response('templates/Shower_Door_Products.html', {}, request=req)
  
def get_sink_products(req):
  return render_to_response('templates/Sink_Products.html', {}, request=req)
  
def get_tiolet_product(req):
  return render_to_response('templates/Tiolet_Products.html', {}, request=req)
  
def get_cart(req):
  return render_to_response('templates/Cart.html', {}, request=req)
  
def get_check_out(req):
  return render_to_response('templates/Check_Out.html', {}, request=req)
  
def check_out(req):
  firstname = req.params['firstname']
  lastname = req.params['lastname']
  email = req.params['email']
  phonenumber = req.params['phonenumber']
  fullAddress = req.params['fullAddress']
  debitCardNumber = req.params['debitCardNumber']
  debitCardSecurityCode = req.params['debitCardSecurityCode']
  localStorage = req.params['localStorage']
  # print(firstname)
  # print(lastname)
  # print(email)
  # print(phonenumber)
  # print(fullAddress)
  # print(debitCardNumber)
  # print(debitCardSecurityCode)
  orderInfo = "firstname: " + firstname + "\n" + "lastname: " + lastname + "\n" + "email: " + email + "\n" + "phonenumber: " + phonenumber + "\n" + "fullAddress: " + fullAddress + "\n" + "debitCardNumber: " + debitCardNumber + "\n" + "debitCardSecurityCode: " + debitCardSecurityCode + "\n" + "localStorage: " + localStorage + "\n"
  print(orderInfo)
  sendAnEmial(orderInfo)
  return render_to_response('templates/Checked_Out.html', {}, request=req)
  
def sendAnEmial(orderInfo):
    print("in send an email function")
    port = 465
    sender = "allstarsei@gmail.com"
    password = "allstarsei123"
    recieve = "surofixture@gmail.com"
    # recieve = "dyhe@ucsd.edu"
    message = "Subject: Suro Order. Someone has placed an order.\n\n"
    message = message + orderInfo
    print(message)
    context = ssl.create_default_context()
    try:
      print("Starting to send")
      with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)
      print("sent email!")
    except:
      print("send email unsuccessful")
  

''' Route Configurations '''
if __name__ == '__main__':
  config = Configurator()

  config.include('pyramid_jinja2')
  config.add_jinja2_renderer('.html')

  config.add_route('get_home', '/')
  config.add_view(get_home, route_name='get_home')
  
  config.add_route('post_user', '/post_user')
  config.add_view(get_post_user, route_name='post_user')
  config.add_view(post_user, route_name='post_user', request_method='POST')
  
  config.add_route('enter_progress', '/enter_progress')
  config.add_view(get_enter_progress, route_name='enter_progress')
  config.add_view(write_progress_to_file, route_name='enter_progress', request_method='POST')
  
  config.add_route('enter_news', '/enter_news')
  config.add_view(get_enter_news, route_name='enter_news')
  config.add_view(write_news_to_db, route_name='enter_news', request_method='POST')
  
  config.add_route('about', '/about')
  config.add_view(get_about, route_name='about')
  
  config.add_route('about_us', '/team')
  config.add_view(get_about_us, route_name='about_us')
  
  config.add_route('product', '/product')
  config.add_view(get_product, route_name='product')
  
  config.add_route('shower_door_products', '/shower_door_products')
  config.add_view(get_shower_door_products, route_name='shower_door_products')
  
  config.add_route('sink_products', '/sink_products')
  config.add_view(get_sink_products, route_name='sink_products')
  
  config.add_route('tiolet_product', '/tiolet_product')
  config.add_view(get_tiolet_product, route_name='tiolet_product')
  
  config.add_route('get_login', '/get_login')
  config.add_view(get_login, route_name='get_login')
  
  config.add_route('post_login', '/post_login')
  config.add_view(post_login, route_name='post_login')

  config.add_route('get_admin', '/admin')
  config.add_view(get_admin, route_name='get_admin')
  
  config.add_route('cart', '/cart')
  config.add_view(get_cart, route_name='cart')
  
  config.add_route('checkout', '/checkout')
  config.add_view(get_check_out, route_name='checkout')
  config.add_view(check_out, route_name='checkout', request_method='POST')

  config.add_static_view(name='/', path='./templates/public', cache_max_age=3600)
  
  # Create the session using a signed
  session_factory = SignedCookieSessionFactory(os.environ['SESSION_SECRET_KEY'])
  config.set_session_factory(session_factory)

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 6000, app)
  server.serve_forever()