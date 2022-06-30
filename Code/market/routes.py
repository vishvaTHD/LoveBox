

from market import app
from flask import render_template,redirect,url_for,flash,get_flashed_messages,request
from market.models import Products,Users,Cart,CartItem,Orders,OrderDetails,Payment
from market.forms import RegisterForm,LoginForm,addToCartForm,CheckOut,paymentForm
from market import db
from datetime import date

from flask_login import login_user,logout_user,login_required, current_user

@app.route('/')
def landingpage():
   return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/testimonial')
def testimonial():
    return render_template('testimonial.html')

@app.route('/FAQ')
def FAQ():
    return render_template('FAQ.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/chooseBox')
def chooseBox():
    return render_template('choosebox.html')

@app.route('/NormalDate')
def NormalDate():
    return render_template('NormalDate.html')


@app.route('/ProductDetails/<Prod_id>', methods = ["POST" , "GET"])
def ProductDetails(Prod_id):
    form = addToCartForm()
    if request.method == "POST":
        if current_user.is_authenticated:
            User_id = current_user.User_id
            Prod_id = request.form.get('Prod_id')
            Prod_qty = request.form.get('Prod_qty')
            existing_cart = Cart.query.filter_by(Cart_User_id = User_id).first()
            if existing_cart:
                existing_product = CartItem.query.filter_by(CartItem_Prod_id =Prod_id).first()
                if existing_product:
                    print("I Have found product")
                    existing_product.CartItem_quanitity = existing_product.CartItem_quanitity + 1
                    db.session.commit()
                print("I have not found product")
                productDetails_in_cartDetails = CartItem(CartItem_Cart_id = existing_cart.Cart_id ,CartItem_Prod_id =Prod_id, CartItem_quanitity=Prod_qty)
                db.session.add(productDetails_in_cartDetails)
                db.session.commit()
            else:
                user_cart = Cart(Cart_User_id = Users.query.filter_by(User_id = User_id).first().User_id)
                db.session.add(user_cart)
                db.session.commit()
                productDetails_in_cartDetails = CartItem(CartItem_Cart_id = user_cart.Cart_id ,CartItem_Prod_id =Prod_id, CartItem_quanitity=Prod_qty)
                db.session.add(productDetails_in_cartDetails)
                db.session.commit()
            
            flash('Item Has been added to your Cart', category='success')
        else:
            flash('Please Login to add item in your cart', category='info') 
    ProductDetails = Products.query.filter_by(Prod_id = Prod_id).first()
    return render_template('ProductDetails.html',ProductDetails=ProductDetails, form =form)









@app.route("/Product",methods = ["POST" , "GET"])
def Product():
    form = addToCartForm()
    if request.method == "POST":
        if current_user.is_authenticated:
            User_id = current_user.User_id
            Prod_id = request.form.get('Prod_id')
            Prod_qty = request.form.get('Prod_qty')
            existing_cart = Cart.query.filter_by(Cart_User_id = User_id).first()
            if existing_cart:
                existing_product = CartItem.query.filter_by(CartItem_Prod_id =Prod_id).first()
                if existing_product:
                    print("I Have found product")
                    existing_product.CartItem_quanitity = existing_product.CartItem_quanitity + 1
                    db.session.commit()
                print("I have not found product")
                productDetails_in_cartDetails = CartItem(CartItem_Cart_id = existing_cart.Cart_id ,CartItem_Prod_id =Prod_id, CartItem_quanitity=Prod_qty)
                db.session.add(productDetails_in_cartDetails)
                db.session.commit()
            else:
                user_cart = Cart(Cart_User_id = Users.query.filter_by(User_id = User_id).first().User_id)
                db.session.add(user_cart)
                db.session.commit()
                productDetails_in_cartDetails = CartItem(CartItem_Cart_id = user_cart.Cart_id ,CartItem_Prod_id =Prod_id, CartItem_quanitity=Prod_qty)
                db.session.add(productDetails_in_cartDetails)
                db.session.commit()
            
        
           
            flash('Item Has been added to your Cart', category='success')
        else:
            flash('Please Login to add item in your cart', category='info') 
        
        
    productData = Products.query.filter_by(Prod_cat = "single")
     
    return render_template('product.html',productData = productData, form =form)

@app.route("/login", methods = ["POST" , "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = Users.query.filter_by(User_name=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.User_name}', category='success')
            return redirect(url_for('landingpage'))
        else:
            flash('Username and password are not match! Please try again', category='danger')
            
    return render_template('login.html', form = form)


@app.route("/Register" , methods = ["POST" , "GET"])
def Register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = Users(
            User_name =form.username.data,
            User_Email = form.email_address.data,
            password = form.password_1.data )
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Success! Your account has been created and you are logged in as: {user_to_create.User_name}', category='success')
        return redirect(url_for('landingpage'))
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error creating a user: {err_msg}', category='danger')
        
    return render_template('Register.html' , form = form)


@app.route('/logout')
def logout():
    logout_user()
    flash(f'Success! You are logged out', category='success')
    return redirect(url_for('landingpage'))

@login_required
@app.route('/CartScreen', methods = ["POST" , "GET"])
def CartScreen():
    form = CheckOut()
    
    

        
        
    locations = [
        {"location" : "Germany", 'Charges': 3.79},
        {"location" : "Within EU", 'Charges': 4.89},
        {"location" : "Switzerland", 'Charges': 8.89},
        {"location" : "Britain", 'Charges': 8.89},
        {"location" : "Europe", 'Charges': 8.89},
        {"location" : "China", 'Charges': 8.89},
        {"location" : "Eastern Countries", 'Charges': 8.89},
        {"location" : "Northern Africa", 'Charges': 8.89},
        {"location" : "Rest of the world", 'Charges': 8.89},
    ]
    cart = Cart.query.filter_by(Cart_User_id = current_user.User_id).first().Cart_id
    prodIDs = []


    for item in CartItem.query.filter_by(CartItem_Cart_id =str(cart)):
        a = {"Prod_id":item.CartItem_Prod_id, "CartItem_id": item.CartItem_id }
        prodIDs.append(a)

    
    cart_data = []
    for i in prodIDs:
        for j in Products.query.filter_by(Prod_id = i['Prod_id']):
            a = {"CartItem_id" : i['CartItem_id'],"Prod_name":j.Prod_name,"Prod_desc" :  j.Prod_desc,"Prod_Price" : j.Prod_Price,"Prod_URl":j.Prod_URl}
            cart_data.append(a)
            
	
    if request.method == "POST":
        Orders_User_id = current_user.User_id
        Order_location = request.form.get('Order_location')
        for i in locations:
            if i['location'] == Order_location:
                Order_Shipment_price = (i['Charges'])
        
        Order_price = request.form.get('Order_price')
        Order_date = date.today()
        
        Order = Orders(Orders_User_id=Orders_User_id,Order_location =Order_location,Order_price=Order_price,Order_Shipment_price=Order_Shipment_price,Order_date=Order_date)
        db.session.add(Order)
        db.session.commit()
        for i in prodIDs:
            orderDetails = OrderDetails(OrderDetails_Prod_id = i['Prod_id'] , OrderDetails_Prod_quantity = 1 , OrderDetails_Order_id = Order.Order_id)
            db.session.add(orderDetails)
            db.session.commit()
        
        return redirect(url_for('Payment_Screen', Order = Order))
     
    return render_template('CartScreen.html', cart_data = cart_data ,locations= locations,form=form )

@app.route('/DeleteCartItem/<CartItemId>')
def DeleteCartItem(CartItemId):
    item_to_delete = CartItem.query.get_or_404(CartItemId) 
    db.session.delete(item_to_delete)
    db.session.commit()
    
	
    return redirect(url_for('CartScreen'))

@app.route("/Payment_Screen",  methods = ["POST" , "GET"])
def Payment_Screen():
    form = paymentForm()
    Payment_Order_id = request.args.get('Order')
    
    order_Price = Orders.query.filter_by(Order_id = Payment_Order_id).first().Order_price
    Order_Shipment_price = Orders.query.filter_by(Order_id = Payment_Order_id).first().Order_Shipment_price
    if form.validate_on_submit():
        if request.method == 'POST':
            Payment_total= request.form.get('Payment_total')
            payment = Payment(
            Payment_Order_id = Payment_Order_id,
            Payment_card_No = form.CardNumber.data,
            Payment_card_Name = form.Name_on_Card.data,
            Payment_card_Expiry=form.Expiry_date.data,
            Payment_card_VCC = form.CVV.data,
            Payment_total= Payment_total
            )
            
            db.session.add(payment)
            db.session.commit()
            
            cart_id =  Cart.query.filter_by(Cart_User_id = current_user.User_id).first().Cart_id
            for item in CartItem.query.filter_by(CartItem_Cart_id =str(cart_id)):
                db.session.delete(item)
                db.session.commit()
            
            # flash(f'Success! Your Order has been Placed! Happy shoping!!', category='success')
            
            return redirect(url_for('Confirmation'))
        
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error in payment form: {err_msg}', category='danger')
    
    return render_template('PaymentScreen.html', form=form , order_Price = order_Price,Order_Shipment_price=Order_Shipment_price)



@app.route('/Confirmation')
def Confirmation():
    return render_template('confirmation.html')