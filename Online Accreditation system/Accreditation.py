from flask import Flask,redirect,url_for
from flask import request
from flask import flash
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kg@localhost/accreditation'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

@app.route('/')
def login():
  return render_template('login.html')
  
@app.route('/login')
def loginn():
  return render_template('login.html')

@app.route('/about')
def about():
  return render_template('about.html')
  
 
@app.route('/login_reg',methods=['GET','POST'])
def login_reg():
		if request.method == 'GET':
			return render_template('login.html')
		user_name=request.form['user_name']
		password=request.form['password']
		
		if request.form['user_name'] == 'admin' and request.form['password'] == 'admin':
			return redirect(url_for('home'))
		else:
			return render_template('login.html')
		
@app.route('/home')
def home():
  return render_template('home.html')
  
  	  
@app.route('/staffreport')
def staffreport():
  return render_template('staffreport.html',staff=staff.query.all())
  
  
  
@app.route('/timetablereport')
def timetablereport():
  return render_template('timetablereport.html',timetable=timetable.query.all())
  
  
  
@app.route('/eventsreport')
def eventsreport():
  return render_template('eventsreport.html',events=events.query.all())
  

  
@app.route('/staff')
def staff():
  return render_template('staff.html')
  
  
@app.route('/college')
def college():
  return render_template('college.html')
  
  
@app.route('/acollege')
def acollege():
  return render_template('acollege.html')
    
@app.route('/timetable')
def timetable():
  return render_template('timetable.html')

@app.route('/events')
def events():
  return render_template('events.html')
  

  
@app.route('/vtimetable')
def vtimetable():
	return render_template('vtimetable.html')
	
	
	
@app.route('/ctimetable')
def ctimetable():
	return render_template('ctimetable.html')

@app.route('/vevents')
def vevents():
	return render_template('vevents.html')


	
	
@app.route('/at_reports',methods = ['POST' , 'GET'])
def at_reports():
	if request.method == 'POST':
		cmp_ref_num = request.form['cmp_ref_num']
		return redirect(url_for('atstatus',name = cmp_ref_num))
	else:
		cmp_ref_num = request.form['cmp_ref_num']	
		return redirect(url_for('atstatus',name = cmp_ref_num))
		
@app.route('/atstatus/<int:name>')
def atstatus(name):
	return render_template('atstatus.html',timetable=timetable.query.filter_by(sid='%d'%name))
	
	
	
	
	
@app.route('/ct_reports',methods = ['POST' , 'GET'])
def ct_reports():
	if request.method == 'POST':
		cmp_ref_num = request.form['cmp_ref_num']
		return redirect(url_for('ctstatus',name = cmp_ref_num))
	else:
		cmp_ref_num = request.form['cmp_ref_num']	
		return redirect(url_for('ctstatus',name = cmp_ref_num))
		
@app.route('/ctstatus/<int:name>')
def ctstatus(name):
	return render_template('ctstatus.html',timetable=timetable.query.filter_by(college='%d'%name))
	
	
	

@app.route('/et_reports',methods = ['POST' , 'GET'])
def et_reports():
	if request.method == 'POST':
		cmp_ref_num = request.form['cmp_ref_num']
		return redirect(url_for('etstatus',name = cmp_ref_num))
	else:
		cmp_ref_num = request.form['cmp_ref_num']	
		return redirect(url_for('etstatus',name = cmp_ref_num))
		
@app.route('/etstatus/<int:name>')
def etstatus(name):
	return render_template('etstatus.html',events=events.query.filter_by(college='%d'%name))
	
	
	
class staff(db.Model):
	id = db.Column('staff_id', db.Integer, primary_key = True )
	name = db.Column(db.String(40))
	gender = db.Column(db.String(10))
	adhaar = db.Column(db.String(50))
	address = db.Column(db.String(500))
	mobile = db.Column(db.String(15))
	email = db.Column(db.String(50))
	feedback = db.Column(db.String(500))
	
		
	def __init__(self,name,gender,adhaar,address,mobile,email,feedback):
		self.name=name
		self.gender=gender
		self.adhaar=adhaar
		self.address=address
		self.mobile=mobile
		self.email=email
		self.feedback=feedback
		
	@app.route('/db_staff', methods = ['GET', 'POST'])
	def db_staff():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['gender'] or not request.form['adhaar'] or not request.form['address'] or not request.form['mobile']  or not request.form['email'] or not request.form['feedback']:
				flash('Please enter all the fields', 'error')
			else:
				feedbackid= staff(request.form['name'],request.form['gender'],request.form['adhaar'],request.form['address'],request.form['mobile'],request.form['email'],request.form['feedback'])          
				db.session.add(feedbackid)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('staff'))
			return render_template('staff.html')		
		
		
		

	
	
	
class events(db.Model):
	id = db.Column('eventsid_id', db.Integer, primary_key = True )
	ename = db.Column(db.String(30))
	edate = db.Column(db.String(50))
	edetails = db.Column(db.String(500))
	university = db.Column(db.String(100))
	college = db.Column(db.String(100))
	syear = db.Column(db.String(50))
	
	
		
	def __init__(self,ename,edate,edetails,university,college,syear):
		self.ename=ename
		self.edate=edate
		self.edetails=edetails
		self.university=university
		self.college=college
		self.syear=syear
		
	@app.route('/db_events', methods = ['GET', 'POST'])
	def db_events():
		if request.method == 'POST':
			if not request.form['ename'] or not request.form['edate'] or not request.form['edetails'] or not request.form['university']  or not request.form['college'] or not request.form['syear']:
				flash('Please enter all the fields', 'error')
			else:
				feedbackid= events(request.form['ename'],request.form['edate'],request.form['edetails'],request.form['university'],request.form['college'],request.form['syear'])          
				db.session.add(feedbackid)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('events'))
			return render_template('events.html')		
	
	
class timetable(db.Model):
	id = db.Column('timetableid_id', db.Integer, primary_key = True )
	sid = db.Column(db.String(10))
	name = db.Column(db.String(30))
	tdate = db.Column(db.String(50))
	dorder= db.Column(db.String(50))
	university = db.Column(db.String(100))
	college = db.Column(db.String(100))
	syear = db.Column(db.String(20))
	subject = db.Column(db.String(200))
	shour = db.Column(db.String(50))
	
		
	def __init__(self,sid,name,tdate,dorder,university,college,syear,subject,shour):
		self.sid=sid
		self.name=name
		self.tdate=tdate
		self.dorder=dorder
		self.university=university
		self.college=college
		self.syear=syear
		self.subject=subject
		self.shour=shour	
		
	@app.route('/db_timetable', methods = ['GET', 'POST'])
	def db_timetable():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['sid'] or not request.form['tdate'] or not request.form['dorder'] or not request.form['university']  or not request.form['college'] or not request.form['syear'] or not request.form['subject'] or not request.form['shour']:
				flash('Please enter all the fields', 'error')
			else:
				feedbackid= timetable(request.form['sid'],request.form['name'],request.form['tdate'],request.form['dorder'],request.form['university'],request.form['college'],request.form['syear'],request.form['subject'],request.form['shour'])          
				db.session.add(feedbackid)
				db.session.commit()
				flash('Record was successfully added')
				return redirect(url_for('timetable'))
			return render_template('timetable.html')			
		
if __name__ == '__main__':
   db.create_all()
   app.run(debug=True)
