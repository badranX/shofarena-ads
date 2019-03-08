from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

from wtforms.fields.html5 import TelField
from wtforms.validators import DataRequired,InputRequired,Email,Length, Regexp



class SignUp(FlaskForm):
    
    #Name
    first_name=StringField('الإسم',validators=[DataRequired()])
    father_name=StringField('إسم الأب',validators=[DataRequired()])
    family=StringField('إسم العائلة',validators=[DataRequired()])
    
    #ID Number
    id=StringField('id',
        render_kw={"pattern": "^\d{9}$",
        "type":"tel"},
        validators=[InputRequired(),
        
        Regexp("^\d{9}$",message='ID is wrong')])

    #Mobile Number  
    mobile=StringField('Mobile',
        render_kw= {
            "pattern":"^\+?\d{10,14}$",
            "type":"tel"},
        validators=[InputRequired(), Regexp("^\+?\d{10,14}$",message='number is wrong')])

    #Email
    email=StringField('Email',
        render_kw= {
            "type":"email"}
        )
#validators=[Email(message=u'That\'s not a valid email address.')]
    #home_adress
    home_city = SelectField(u'المدينة', 
        choices=[('', 'المحافظة'),
            ('اريحا', 'اريحا'), 
            ('الخليل', 'الخليل'),
            ('القدس', 'القدس'),
            ('بيت لحم', 'بيت لحم'),
            ('جنين', 'جنين'),
            ('رام الله والبيرة ', 'رام الله والبيرة'),
            ('قلقيلية', 'قلقيلية'),
            ('نابلس', 'نابلس'),
            ('قطاع غزة', 'قطاع غزة')
         ],
        validators = [DataRequired()])
    #home_town = SelectField(u'بلدة السكن') #TODO check on the browser

    #work_adress
    work_city = SelectField(u'مدينة العمل', 
        choices=[('', 'المحافظة'),
            ('اريحا', 'اريحا'), 
            ('الخليل', 'الخليل'),
            ('القدس', 'القدس'),
            ('بيت لحم', 'بيت لحم'),
            ('جنين', 'جنين'),
            ('رام الله والبيرة ', 'رام الله والبيرة'),
            ('قلقيلية', 'قلقيلية'),
            ('نابلس', 'نابلس'),
            ('قطاع غزة', 'قطاع غزة')
         ],
        validators = [DataRequired()])
    #work_town = SelectField(u'بلدة العمل')#check on the browser
    #car_taxi_private
    car_type = SelectField(u'نوع السيارة', 
        choices=[
            ("",'نوع السيارة'),
            ('private', 'خاصة'),
            ('taxi', 'تكسي'),
            ('van', 'شاحنة'),
         ],
        validators = [DataRequired()])

    #car_year
    car_year = SelectField(u'السنة', 
        choices=[('', 'السنة'),
            ('2016', '2016'),
            ('2015', '2015'),
            ('2014', '2014'),
            ('2013', '2013'),
            ('2012', '2012'),
            ('2011', '2011'),
            ('2010', '2010'),
            ('2009', '2009'),
            ('2008', '2008'),
            ('2007', '2007'),
            ('2006', '2006'),
            ('2005', '2005'),
            ('2004', '2004')
          ],
        validators = [DataRequired()])

    #car_company #car_model
    car_company = SelectField(u'نوع السيارة', 
        choices=[('', 'اختار'), 
            ('dodge', 'Dodge'),
            ('اوبل', 'اوبل'),
            ('اودي', 'اودي'),
            ('ايسوزو', 'ايسوزو'),
            ('باص', 'باص'),
            ('بي ام دبليو BMW', 'بي ام دبليو BMW'),
            ('بيجو', 'بيجو'),
            ('تويوتا', 'تويوتا'),
            ('جي ام سي', 'جي ام سي'),
            ('جيب jeep', 'جيب Jeep'),
            ('داتشيا', 'داتشيا'),
            ('داف', 'داف'),
            ('دايو', 'دايو'),
            ('دراجة نارية', 'دراجة نارية'),
            ('ديهاتسو', 'ديهاتسو'),
            ('روفر', 'روفر'),
            ('رينو', 'رينو'),
            ('سانغ يونغ', 'سانغ يونغ'),
            ('ستروين', 'ستروين'),
            ('سكودا', 'سكودا'),
            ('سوبارو', 'سوبارو'),
            ('سوزوكي', 'سوزوكي'),
            ('سيت', 'سيت'),
            ('شاحنة', 'شاحنة'),
            ('شفرليت', 'شفرليت'),
            ('فورد', 'فورد'),
            ('فولفو', 'فولفو'),
            ('فولكسفاجن', 'فولكسفاجن'),
            ('كاديلاك', 'كاديلاك'),
            ('كرايسلر', 'كرايسلر'),
            ('kia', 'كيا Kia'),
            ('لاندروفر', 'لاندروفر'),
            ('مازدا', 'مازدا'),
            ('مرسيدس', 'مرسيدس'),
            ('ميتسوبيشي', 'ميتسوبيشي'),
            ('نيسان', 'نيسان'),
            ('هوندا', 'هوندا'),
            ('هونداي', 'هونداي')],
        validators = [DataRequired()])

    
    #car_model = SelectField(u'موديل السيارة')
    #car_color
    car_color = SelectField(u'لون السيارة', 
        choices=[('','اللون'),
            ('أسود', 'أسود'),
            ('فضي', 'فضي'),
            ('أبيض', 'أبيض'),
            ('أزرق', 'أزرق'),
            ('أحمر', 'أحمر'),
            ('أصفر', 'أصفر'),
            ('أخرى', 'أخرى')],
        validators = [DataRequired()])

    #car_condition
    car_condition =  SelectField(u'حالة السيارة', 
        choices=[('', 'الحالة'),
            ('ممتازة', 'ممتازة'),
            ('جيدة', 'جيدة'),
            ('سيئة', 'سيئة')
         ],
        validators = [DataRequired()])
    #SUBMIT
    submit = SubmitField('تسجيل')

    