

from market import db,loginManager
from market import bcrypt
from flask_login import UserMixin


    
@loginManager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Users(db.Model,UserMixin):
    User_id = db.Column(db.Integer, primary_key=True)
    User_name = db.Column(db.String(30), unique=True, nullable=False)
    User_Email = db.Column(db.String(40), nullable=False)
    User_pass = db.Column(db.String(40), nullable=False)
    User_cart = db.relationship('Cart', backref='users', lazy = True)
    User_Orders = db.relationship('Orders', backref='users',lazy = True)
    
    def get_id(self):
           return (self.User_id)
    
    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.User_pass = bcrypt.generate_password_hash(plain_text_password).decode("utf_8") 
    
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.User_pass, attempted_password)    


def __repr__(self):
        
        return f"{self.User_id}"
    
class Products(db.Model):
    Prod_id = db.Column(db.Integer, primary_key=True)
    Prod_name = db.Column(db.String(80), unique=True, nullable=False)
    Prod_desc = db.Column(db.String(120), nullable=False)
    Prod_Price = db.Column(db.Integer, nullable=False)
    
    Prod_URl = db.Column(db.String(120), nullable=False)
    Prod_cat = db.Column(db.String(120))
    

    def __repr__(self):
        return f"{self.Prod_id}"


class Cart(db.Model):
    Cart_id = db.Column(db.Integer, primary_key=True)
    Cart_User_id = db.Column(db.Integer, db.ForeignKey('users.User_id') ,nullable=False)
    
    Cart_CartItem = db.relationship("CartItem" ,backref='cart' ,lazy = True)


    def __repr__(self):
        return f'{self.Cart_id}'


class CartItem(db.Model):
    CartItem_id = db.Column(db.Integer, primary_key=True)
    CartItem_Cart_id = db.Column(db.Integer ,db.ForeignKey('cart.Cart_id'),nullable=False )
    CartItem_Prod_id = db.Column(db.Integer, db.ForeignKey('products.Prod_id'),nullable=False)
    CartItem_quanitity = db.Column(db.Integer, nullable=False)
   
    def __repr__(self):
        return f'{self.CartItem_id}'


class Orders(db.Model):
    Order_id = db.Column(db.Integer, primary_key=True)
    Orders_User_id = db.Column(db.Integer, db.ForeignKey('users.User_id'))
    Order_location = db.Column(db.String(120),nullable=False)
    Order_price = db.Column(db.Integer, nullable=False)
    Order_Shipment_price = db.Column(db.Integer, nullable=False)
    Order_date = db.Column(db.DateTime ,nullable=False )
    Order_Details = db.relationship('OrderDetails' , backref='orders',lazy = True)
    Order_payment = db.relationship('Payment' , backref='orders' , uselist=False)
    def __repr__(self):
        return f'{self.Order_id}'
    
class OrderDetails(db.Model):
    OrderDetails_id = db.Column(db.Integer, primary_key=True)
    OrderDetails_Prod_id = db.Column(db.Integer, db.ForeignKey('products.Prod_id'))
    OrderDetails_Prod_quantity = db.Column(db.Integer, nullable=False)
    OrderDetails_Order_id = db.Column(db.Integer, db.ForeignKey('orders.Order_id'))
    def __repr__(self):
        return f'{self.OrderDetails_id}'

class Payment(db.Model):
    Payment_id = db.Column(db.Integer, primary_key=True)
    Payment_Order_id = db.Column(db.Integer, db.ForeignKey('orders.Order_id'))
    Payment_card_No = db.Column(db.Integer,nullable=False)
    Payment_card_Name = db.Column(db.String(120),nullable=False)
    Payment_card_Expiry = db.Column(db.DateTime,nullable=False)
    Payment_card_VCC = db.Column(db.Integer,nullable=False)
    Payment_total = db.Column(db.Integer,nullable=False)
    