
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField,DateField
from wtforms.validators import Length, EqualTo, Email, DataRequired,ValidationError
from market.models import Users

class RegisterForm(FlaskForm):
    
    def validate_username(self,username_to_check):
        user = Users.query.filter_by(User_name = username_to_check.data).first()
        if user:
            raise ValidationError("Username already exists, Please try a different username")
        
    def validate_email_address(self,email_address_to_check):
        user = Users.query.filter_by(User_Email = email_address_to_check.data).first()
        if user:
            raise ValidationError("Email_address already exists, Please try a different Email_address")
         
    username = StringField(label = "Username", validators = [Length(min = 3, max= 30),DataRequired()])
    email_address = StringField(label = "Email Address", validators = [Email(),DataRequired()])
    password_1 = PasswordField(label = "Password 1",validators = [Length(min = 6, max= 40),DataRequired()])
    password_2 =  PasswordField(label = "Password 2",validators = [EqualTo('password_1'), DataRequired()])
    submit = SubmitField(label = "Submit") 


class LoginForm(FlaskForm):
    username = StringField(label = "Username", validators =[DataRequired()])
    
    password = PasswordField(label = "Password 1",validators =[DataRequired()])
    
    submit = SubmitField(label = "Sign In") 
    
class addToCartForm(FlaskForm):
    submit = SubmitField(label = "Add to Cart") 
    
class CheckOut(FlaskForm):
    submit = SubmitField(label = "Check Out")


class paymentForm(FlaskForm):
    # Order = IntegerField(lable = "Order_id",validators =[DataRequired()])
    CardNumber = IntegerField( label = "Card Number",validators =[DataRequired()])
    Name_on_Card = StringField( label = "Name on Card",validators =[Length(min = 3, max= 50),DataRequired()])
    Expiry_date = DateField( label = "Expiry Date",validators =[DataRequired()])
    CVV = IntegerField( label = "CVV",validators =[DataRequired()])
    submit = SubmitField(label = "Check Out")