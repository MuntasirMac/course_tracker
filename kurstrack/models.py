# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime
from django.utils import timezone


class Awardingbody(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'awardingbody'
        verbose_name_plural = 'Awarding Bodies'
    
    def __str__(self):
        return f"{self.name}"


class WhoCourseFor(models.Model):
    who_course_id = models.IntegerField(primary_key=True)
    who_course_for = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'who_course_for'
        verbose_name_plural = 'Who Course For'

    def __str__(self):
        return f"{self.who_course_for}"


class WhyChoose(models.Model):
    whychoose_id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'why_choose'
        verbose_name_plural = 'Why Should Choose'

    def __str__(self):
        return f"{self.whychoose_id}"


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return f"{self.category}"


class Level(models.Model):
    level_id = models.IntegerField(primary_key=True)
    level_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'level'
        verbose_name_plural = 'Levels'
    
    def __str__(self):
        return f"{self.level_name}"


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    profession = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=45, null=True)
    website = models.CharField(max_length=45, blank=True, null=True)
    social_media = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(unique=True, max_length=45, null=True)

    class Meta:
        db_table = 'student'
        ordering = ("last_name", "first_name")
        verbose_name_plural = 'Students'
    
    def __str__(self):
        return f"{self.first_name}" + ' ' + f"{self.last_name}"

    def show_address(self):
        return f"{self.address}"


class Instructorinfo(models.Model):
    instructor_id = models.IntegerField(db_column='Instructor_id', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    designation = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    website = models.CharField(max_length=45, blank=True, null=True)
    social_media = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'instructorinfo'
        verbose_name_plural = 'Instructors Info'
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Registerinfo(models.Model):
    register_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    designation = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=45, blank=True, null=True)
    website = models.CharField(max_length=45, blank=True, null=True)
    social_media = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'registerinfo'
        verbose_name_plural = 'Register Info'

    def __str__(self):
        return f"{self.first_name}" + ' ' + f"{self.last_name}"


class CertificateType(models.Model):
    type_id = models.IntegerField(primary_key=True)
    price = models.FloatField()
    type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'certificate_type'
        verbose_name_plural = 'Certificate Types'

    def __str__(self):
        return f"{self.type}"


class Coursedesign(models.Model):
    design_id = models.IntegerField(primary_key=True)
    design_type = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'coursedesign'
        verbose_name_plural = 'Course Designs'

    def __str__(self):
        return f"{self.design_type}"


class Cart(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    description = models.TextField(blank=True, null=True)
    stud_id = models.ForeignKey('Student', on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart'
        verbose_name_plural = 'Cart'

    def __str__(self):
        return f"{self.description}"


class Certification(models.Model):
    certification_id = models.IntegerField(primary_key=True)
    certificate_name = models.CharField(max_length=50, blank=True, null=True)
    type = models.ForeignKey(CertificateType, on_delete=models.CASCADE)

    class Meta:
        db_table = 'certification'
        verbose_name_plural = 'Certification'

    def __str__(self):
        return f"{self.certificate_name}"


class Webcourseinfo(models.Model):
    w_course_id = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=1000)
    subtite = models.CharField(max_length=5000, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    access = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    original_price = models.FloatField(blank=True, null=True)
    offer_price = models.FloatField(blank=True, null=True)
    no_modules = models.IntegerField(blank=True, null=True)
    no_quizzes = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    regular_specialization = models.IntegerField(blank=True, null=True)
    manipulated_or_not = models.IntegerField(blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    method_assesment = models.TextField(blank=True, null=True)
    prerequisite = models.TextField(blank=True, null=True)
    career_path = models.TextField(blank=True, null=True)
    learning_outcomes = models.TextField(blank=True, null=True)
    quality = models.CharField(max_length=45, blank=True, null=True)
    quaity_type = models.CharField(max_length=1, blank=True, null=True)
    whychoose = models.ForeignKey('WhyChoose', on_delete=models.CASCADE)
    who_course = models.ForeignKey('WhoCourseFor', on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)

    class Meta:
        db_table = 'webcourseinfo'
        verbose_name_plural = 'Course Info'
    
    def __str__(self):
        return f"{self.w_course_id}"
    

class Coursecategory(models.Model):
    cat = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey('Webcourseinfo', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'coursecategory'
        verbose_name_plural = 'Category Of Courses'
    
    def __str__(self):
        return f"{self.course}, {self.cat}"


class Coursedesignhaswebcoursesinfo(models.Model):
    course = models.ForeignKey('Webcourseinfo', on_delete=models.CASCADE)
    w_design = models.ForeignKey(Coursedesign, on_delete=models.CASCADE)

    class Meta:
        db_table = 'coursedesignhaswebcoursesinfo'
        verbose_name_plural = 'Delivery Mode'


class Coursemodule(models.Model):
    module_type = models.CharField(primary_key=True, max_length=100)
    module = models.ForeignKey('Module', on_delete=models.CASCADE, blank=True, null=True)
    register = models.ForeignKey('Registerinfo', on_delete=models.CASCADE)
    w_course = models.ForeignKey('Webcourseinfo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'coursemodule'
        verbose_name_plural = 'Courses Module'
    
    def __str__(self):
        return f"{self.module}"


class Courseorder(models.Model):
    order_no = models.AutoField(primary_key=True)
    details = models.TextField()
    quantity = models.IntegerField()
    total_price = models.FloatField()
    shipping_method = models.CharField(max_length=50)
    payment_method = models.CharField(max_length=50)
    gift_or_not = models.IntegerField()
    address = models.TextField(blank=True, null=True)
    coupon_code = models.CharField(max_length=10, blank=True, null=True)
    id = models.OneToOneField(Cart, on_delete=models.CASCADE, db_column='id')
    w_course = models.ForeignKey('Webcourseinfo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'courseorder'
        verbose_name_plural = 'Orders'
    
    def __str__(self):
        return f"{self.order_no}, {self.w_course}, {self.quantity}, {self.shipping_method}, {self.payment_method}"


class Courseslevel(models.Model):
    level = models.ForeignKey('Level', on_delete=models.CASCADE, blank=True, null=True)
    w_course = models.ForeignKey('Webcourseinfo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'courseslevel'
        verbose_name_plural = 'Level Of Courses'

    def __str__(self):
        return f"{self.w_course}, {self.level}"


class Grouponcoursesinfo(models.Model):
    course_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    subtitle = models.CharField(max_length=1000, blank=True, null=True)
    offer_price = models.FloatField(blank=True, null=True)
    original_price = models.FloatField(blank=True, null=True)
    unit_sold = models.IntegerField(blank=True, null=True)
    saving_percent = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=150, blank=True, null=True)
    web_course = models.ForeignKey('Webcourseinfo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'grouponcoursesinfo'
        verbose_name_plural = 'GroupOn Courses'

    def __str__(self):
        return f"{self.course_id}, {self.title}"


class Groupondailysale(models.Model):
    date = models.DateField(primary_key=True)
    order_id = models.IntegerField(blank=True, null=True)
    course_id = models.IntegerField(blank=True, null=True)
    unit_sold = models.IntegerField(blank=True, null=True)
    revenue = models.FloatField(blank=True, null=True)
    g_course = models.ForeignKey(Grouponcoursesinfo, on_delete=models.CASCADE)
    stn = models.ForeignKey('Student', on_delete=models.CASCADE)

    class Meta:
        db_table = 'groupondailysale'
        verbose_name_plural = 'GroupOn Sales'
    
    def __str__(self):
        return f"{self.date}, {self.course_id}, {self.unit_sold}, {self.revenue}"


class Log(models.Model):
    log_id = models.IntegerField(primary_key=True)
    log_table = models.CharField(max_length=45, blank=True, null=True)
    field = models.CharField(max_length=45, blank=True, null=True)
    field_id = models.IntegerField(blank=True, null=True)
    change_reason = models.CharField(max_length=45, blank=True, null=True)
    old_value = models.CharField(max_length=200, blank=True, null=True)
    add_date = models.DateTimeField(blank=True, null=True)
    add_by = models.CharField(max_length=45, blank=True, null=True)
    log_register = models.ForeignKey('Registerinfo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'log'
        verbose_name_plural = 'Logs'

    def __str__(self):
        return f"{self.add_date}, {self.log_table}, {self.field}, {self.old_value}"


class Module(models.Model):
    module_id = models.IntegerField(primary_key=True)
    module_name = models.CharField(max_length=5000, blank=True, null=True)
    module_id_from = models.IntegerField()
    question = models.ForeignKey('Quizes', on_delete=models.CASCADE)

    class Meta:
        db_table = 'module'
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'
    
    def __str__(self):
        return f"{self.module_name}"


class Quizes(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    register = models.ForeignKey('Registerinfo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'quizes'
        verbose_name_plural = 'Quizes'

    def __str__(self):
        return f"{self.question}"


class Reedcoursesinfo(models.Model):
    r_course_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    link = models.CharField(max_length=500, blank=True, null=True)
    subtitle = models.CharField(max_length=1000, blank=True, null=True)
    offer_price = models.FloatField(blank=True, null=True)
    original_price = models.FloatField(blank=True, null=True)
    savings_percent = models.FloatField(blank=True, null=True)
    broad_category1 = models.CharField(max_length=100, blank=True, null=True)
    broad_category2 = models.CharField(max_length=100, blank=True, null=True)
    sub_category1 = models.CharField(max_length=100, blank=True, null=True)
    sub_category2 = models.CharField(max_length=100, blank=True, null=True)
    have_cpd = models.IntegerField(blank=True, null=True)
    cpd_point = models.IntegerField(blank=True, null=True)
    cpd_provider = models.CharField(max_length=1000, blank=True, null=True)
    qual_name = models.CharField(max_length=1000, blank=True, null=True)
    is_regulated = models.IntegerField(blank=True, null=True)
    sold_enq = models.IntegerField(blank=True, null=True)
    single_bundle = models.IntegerField(blank=True, null=True)
    awardingbody = models.ForeignKey(Awardingbody, on_delete=models.CASCADE, db_column='AwardingBody_id')  # Field name made lowercase.
    w_course = models.ForeignKey('Webcourseinfo', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reedcoursesinfo'
        verbose_name_plural = 'REED Courses'

    def __str__(self):
        return f"{self.title}"


class Reeddailysale(models.Model):
    date = models.DateField(primary_key=True)
    order_id = models.IntegerField(blank=True, null=True)
    course_id = models.IntegerField(blank=True, null=True)
    unit_sold = models.IntegerField(blank=True, null=True)
    revenue = models.FloatField(blank=True, null=True)
    r_course = models.ForeignKey(Reedcoursesinfo, on_delete=models.CASCADE)
    st = models.ForeignKey('Student', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reeddailysale'
        verbose_name_plural = 'REED Sales'

    def __str__(self):
        return f"{self.date}" + ' ' + f"{self.order_id}" + ' ' + f"{self.unit_sold}" + ' ' + f"{self.revenue}"


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_text = models.TextField(blank=True, null=True)
    reviewed_course = models.ForeignKey('Webcourseinfo', on_delete=models.CASCADE)
    rating = models.FloatField(blank=True, null=True)
    st = models.ForeignKey('Student', on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.reviewed_course}" + ' '  + f"{self.review_text}"


class Unit(models.Model):
    unit_id = models.IntegerField(primary_key=True)
    unit_name = models.CharField(max_length=100)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'unit'
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
    
    def __str__(self):
        return f"{self.unit_name}"


class WebCourseQuiz(models.Model):
    course = models.ForeignKey(Webcourseinfo, on_delete=models.CASCADE)
    question = models.ForeignKey(Quizes, on_delete=models.CASCADE)

    class Meta:
        db_table = 'webcoursesinfo_has_quizzes'
        verbose_name = 'Quiz Of Course'
        verbose_name_plural = 'Quizes of Courses'
    
    def __str__(self):
        return f"{self.course}"


class WebSale(models.Model):
    date = models.DateField(primary_key=True)
    course_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    unit_sold = models.IntegerField(blank=True, null=True)
    revenue = models.FloatField(blank=True, null=True)
    sold_course = models.ForeignKey(Webcourseinfo, on_delete=models.CASCADE)
    stu = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        db_table = 'webdailysale'
        verbose_name_plural = 'Sales of Courses'
    
    def __str__(self):
        return f"{self.date}, {self.order_id}, {self.sold_course}, {self.unit_sold}, {self.revenue}"



