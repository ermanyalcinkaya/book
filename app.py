from flask import Flask,request,jsonify,flash
from flask import render_template
from flask_pymongo import PyMongo
import hashlib
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/bookStore'
mongo = PyMongo(app)
usermail = ""
category = ""
openchart = False

@app.route('/')
def home():
    collectionuserdetails=mongo.db.UserDetails
    collectionbooks=mongo.db.Bookss
    collectionorders=mongo.db.Orders
    collectioncharts=mongo.db.ShoppingCharts
    return render_template('user/index.html', title='Home')

@app.route('/signIn')
def signin():
    return render_template('signin.html',title='Signing')

@app.route('/register')
def register():
    return render_template('register.html',title="Registering")

@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'address': request.form['address'],
            'password': hashlib.sha256(request.form['password'].encode()).hexdigest()
        }

        collection = mongo.db.UserDetails
        checkUser=collection.find_one({'email':data.get("email") })
        if(checkUser):
            giveAlert=True
            return render_template('register.html',giveAlert=giveAlert)
        else:
            result = collection.insert_one(data)
            return render_template("user/index.html" , uname=data.get("name"), umail=data.get("email"))

@app.route('/checkuserindb',methods=['POST'])
def checkuserindb():
    global usermail
    if request.method =='POST':
        username=request.form.get('email')
        userpassword=request.form.get('password')
    
        hashed_password = hashlib.sha256(userpassword.encode()).hexdigest()

        collectionuserdetails=mongo.db.UserDetails
        user=collectionuserdetails.find_one({'email':username , 'password':hashed_password })
        if not user:
            givealert=True
            return render_template('signin.html',givealert=givealert)
        else:
            if user.get("email") == "admin@vinbook.com":
                usermail = user.get("email")
                return render_template('admin/adminmain.html',uname=user.get("name"), umail=user.get("email"))
            else:
                usermail = user.get("email")
                return render_template('user/index.html',uname=user.get("name"), umail=user.get("email"))

@app.route('/logout')
def logout():
    return render_template('user/index.html')


# Books Route 

@app.route('/poetry')
def poetry():
    global category
    category = "poetry_books"
    collectionbooks = mongo.db.Books
    booksdata = collectionbooks.find({'category': "poetry_books"})
    books = [book for book in booksdata] 
    for book in books:
        if '_id' in book:
            book['_id'] = str(book['_id'])
    if not books:
        return "Data Not Found"

    collectioncharts = mongo.db.ShoppingCharts
    data = collectioncharts.find({'email': usermail})
    chartsarr = [chart for chart in data] 
    for chart in chartsarr:
        if '_id' in chart:
            chart['_id'] = str(chart['_id'])   

    return render_template("book/viewed.html", arr=books, category="poetry_books", charts=chartsarr)

@app.route('/novel')
def novel():
    global category
    category = "novels"
    collectionbooks = mongo.db.Books
    booksdata = collectionbooks.find({'category': "novels"})
    books = [book for book in booksdata] 
    for book in books:
        if '_id' in book:
            book['_id'] = str(book['_id'])
    if not books:
        return "Data Not Found"

    collectioncharts = mongo.db.ShoppingCharts
    data = collectioncharts.find({'email': usermail})
    chartsarr = [chart for chart in data] 
    for chart in chartsarr:
        if '_id' in chart:
            chart['_id'] = str(chart['_id']) 

    return render_template("book/viewed.html", arr=books ,category="novels", charts=chartsarr)

@app.route('/comic')
def comic():
    global category
    category = "comic_books"
    collectionbooks = mongo.db.Books
    booksdata = collectionbooks.find({'category': "comic_books"})
    books = [book for book in booksdata] 
    for book in books:
        if '_id' in book:
            book['_id'] = str(book['_id'])
    if not books:
        return "Data Not Found"

    collectioncharts = mongo.db.ShoppingCharts
    data = collectioncharts.find({'email': usermail})
    chartsarr = [chart for chart in data] 
    for chart in chartsarr:
        if '_id' in chart:
            chart['_id'] = str(chart['_id']) 

    return render_template("book/viewed.html", arr=books,category="comic_books", charts=chartsarr)


@app.route('/child')
def child():
    global category
    category = "children_books"
    collectionbooks = mongo.db.Books
    booksdata = collectionbooks.find({'category': "children_books"})
    books = [book for book in booksdata] 
    for book in books:
        if '_id' in book:
            book['_id'] = str(book['_id'])
    if not books:
        return "Data Not Found"

    collectioncharts = mongo.db.ShoppingCharts
    data = collectioncharts.find({'email': usermail})
    chartsarr = [chart for chart in data] 
    for chart in chartsarr:
        if '_id' in chart:
            chart['_id'] = str(chart['_id']) 

    return render_template("book/viewed.html", arr=books ,category="children_books", charts=chartsarr)


@app.route('/cook')
def cook():
    global category
    category = "cooking_books"
    collectionbooks = mongo.db.Books
    booksdata = collectionbooks.find({'category': "cooking_books"})
    books = [book for book in booksdata] 
    for book in books:
        if '_id' in book:
            book['_id'] = str(book['_id'])
    if not books:
        return "Data Not Found"

    collectioncharts = mongo.db.ShoppingCharts
    data = collectioncharts.find({'email': usermail})
    chartsarr = [chart for chart in data] 
    for chart in chartsarr:
        if '_id' in chart:
            chart['_id'] = str(chart['_id']) 

    return render_template("book/viewed.html", arr=books,category="cooking_books", charts=chartsarr)


@app.route('/coffeetable')
def coffeetable():
    global category
    category = "coffee_table_books"
    collection = mongo.db.Books
    booksdata = collection.find({'category': "coffee_table_books"})
    books = [book for book in booksdata] 
    for book in books:
        if '_id' in book:
            book['_id'] = str(book['_id'])
    if not books:
        return "Data Not Found"

    collectioncharts = mongo.db.ShoppingCharts
    data = collectioncharts.find({'email': usermail})
    chartsarr = [chart for chart in data] 
    for chart in chartsarr:
        if '_id' in chart:
            chart['_id'] = str(chart['_id']) 

    return render_template("book/viewed.html", arr=books, category="coffee_table_books", charts=chartsarr)


@app.route('/search',methods=['POST'])
def search():
    print("search")
    if request.method=="POST":
        query=request.form.get("search")
        collectionbooks = mongo.db.Books
        data = collectionbooks.find({
            'name': {"$regex": '^' + query},
            'category': {"$regex": category}
        })
        books = [book for book in data] 
        for book in books:
            if '_id' in book:
                book['_id'] = str(book['_id'])
        if not books:
            return "Data Not Found"
        return render_template("book/viewed.html", arr=books)

#chart route
@app.route('/editchart',methods=['GET'])
def editchart():
    collectioncharts = mongo.db.ShoppingCharts
    
    if request.query_string.decode() =='delete=delete':
        collectioncharts.delete_many({
            'email': usermail
        })
 
    data=collectioncharts.find({'email': usermail})
    chartsarr = [chart for chart in data] 
    for chart in chartsarr:
        if '_id' in chart:
            chart['_id'] = str(chart['_id'])
    if request.query_string.decode() =='buy=buy':
        collectionuser=mongo.db.UserDetails
        tempUser=collectionuser.find_one({'email': usermail })
        return render_template("user/buypage.html",user= tempUser,charts=chartsarr)  


    collectionbooks = mongo.db.Books
    data = collectionbooks.find({'category': category})
    books = [book for book in data] 
    for book in books:
        if '_id' in book:
            book['_id'] = str(book['_id'])
    if not books:
        return "Data Not Found"
    return render_template("book/viewed.html", arr=books, category=category, charts=chartsarr)    

@app.route('/addtochart',methods=['POST'])
def addtochart():
    collectioncharts = mongo.db.ShoppingCharts
    collectionbooks = mongo.db.Books

    findbookdata = collectionbooks.find({'_id': ObjectId(request.form['bookid']) })

    booklist = [booklist for booklist in findbookdata]
    for foundbook in booklist:
        if '_id' in foundbook:
            foundbook['_id'] = str(foundbook['_id'])

    exist = collectioncharts.find_one({
        "$and": [{
            'email': usermail,
        }, {
            'name':foundbook['name'],
        }, {
            'author': foundbook['author'],
        }, {
            'publicationdate': foundbook['publicationdate'],
        }]
    })

    if not exist:
        collectioncharts.insert_one({
            'email': usermail, 
            'name': foundbook['name'],
            'author': foundbook['author'],
            'publisher': foundbook['publisher'],
            'category': foundbook['category'],
            'description': foundbook['description'],
            'publicationdate': foundbook['publicationdate'],
            'price': foundbook['price'],          
        })

    data=collectioncharts.find({'email': usermail})
    chartsarr = [chart for chart in data] 
    for chart in chartsarr:
        if '_id' in chart:
            chart['_id'] = str(chart['_id'])

    data = collectionbooks.find({'category': foundbook['category']})
    books = [book for book in data] 
    for book in books:
        if '_id' in book:
            book['_id'] = str(book['_id'])
    if not books:
        return "Data Not Found"
    return render_template("book/viewed.html", arr=books, category=category, charts=chartsarr)  

#Buy pages
@app.route('/buy',methods=['POST'])
def buy():
    collectiorders = mongo.db.Orders
    collectioncharts = mongo.db.ShoppingCharts
    

    shopchart=collectioncharts.find({'email': usermail})
    chartsarr = [chart for chart in shopchart] 
    for chart in chartsarr:
        if '_id' in chart:
            chart['_id'] = str(chart['_id'])

    collectiorders.insert_one({
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'address': request.form['address'],  
        'orders': chartsarr 
    })
    collectioncharts.delete_many({'email': usermail})
    return render_template('user/index.html', giveBuyAlert = True)

#Admin pages 
@app.route('/adminmain')
def adminmain():
    return render_template("admin/adminmain.html")

@app.route('/adminbook')
def adminbook():
    collection = mongo.db.Books
    data = collection.find()
    books = [book for book in data] 
    for book in books:
        if '_id' in book:
            book['_id'] = str(book['_id'])
    return render_template("admin/adminbook.html", arr=books )

@app.route('/editbook', methods=['POST'] )
def editbook():
    collectionbooks = mongo.db.Books
    data = {
        'name': request.form['name'],
        'author': request.form['author'],
        'publisher': request.form['publisher'],
        'category': request.form['category'],
        'description': request.form['description'],
        'publicationdate': request.form['publicationdate'],
        'price': request.form['price'],
        '_id': request.form['bookid'],          
    }
    if request.form.get('delete'):
        myquery = { "_id": ObjectId(data['_id'])}
        collectionbooks.delete_one(myquery)
    else:
        myquery = { "_id": ObjectId(data['_id'])}
        newvalues = { "$set": {
                'name': request.form['name'],
                'author': request.form['author'],
                'publisher': request.form['publisher'],
                'category': request.form['category'],
                'description': request.form['description'],
                'publicationdate': request.form['publicationdate'],
                'price': request.form['price'],          
            } }
        collectionbooks.update_one(myquery,newvalues)

    data = collectionbooks.find()
    books = [book for book in data] 
    for book in books:
        if '_id' in book:
             book['_id'] = str(book['_id'])
    return render_template("admin/adminbook.html", arr=books )

@app.route('/addbook', methods=['POST'] )
def addbook():
    collectionbooks = mongo.db.Books
    if request.form.get('add'):
        data = {
            'name': request.form['addname'],
            'author': request.form['addauthor'],
            'publisher': request.form['addpublisher'],
            'category': request.form['addcategory'],
            'description': request.form['adddescription'],
            'publicationdate': request.form['addpublicationdate'],
            'price': request.form['addprice'],         
        }
        collectionbooks.insert_one(data)

    data = collectionbooks.find()
    books = [book for book in data] 
    for book in books:
        if '_id' in book:
             book['_id'] = str(book['_id'])
    return render_template("admin/adminbook.html", arr=books )   

@app.route('/adminuser')
def adminuser():
    collectionuser = mongo.db.UserDetails
    data = collectionuser.find()
    usersdetails = [user for user in data] 
    for user in usersdetails:
        if '_id' in user:
             user['_id'] = str(user['_id'])
    return render_template("admin/adminuser.html", arr=usersdetails )   

@app.route('/edituser', methods=['POST'] )
def edituser():
    collectionuser = mongo.db.UserDetails
    data = {
        '_id': request.form['userid'],
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'address': request.form['address'],      
    }
    if request.form.get('delete'):
        myquery = { "_id": ObjectId(data['_id'])}
        collectionuser.delete_one(myquery)
    else:
        myquery = { "_id": ObjectId(data['_id'])}
        newvalues = { "$set": {
            'name': request.form['name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'address': request.form['address'],  
        } }
        collectionuser.update_one(myquery,newvalues)

    data = collectionuser.find()
    usersdetails = [user for user in data] 
    for user in usersdetails:
        if '_id' in user:
             user['_id'] = str(user['_id'])
    return render_template("admin/adminuser.html", arr=usersdetails ) 


@app.route('/adminorder')
def adminorder():
    collectiorders = mongo.db.Orders
    data = collectiorders.find()
    userorders = [order for order in data] 
    for order in userorders:
        if '_id' in order:
             order['_id'] = str(order['_id'])
    if not userorders:
         return "Data Not Found" 
    return render_template("admin/adminorder.html", arr=userorders)


if __name__ == "__main__":
    app.run(debug=True)
    
