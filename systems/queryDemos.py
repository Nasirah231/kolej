#***(1)Returns all students from student table
student = Student.objects.all()

#(2)Returns first student in table
firstStudent = Student.objects.first()

#(3)Returns last student in table
lastStudent = Student.objects.last()

#(4)Returns single student by name
studentByName = Student.objects.get(name='Peter Piper')

#***(5)Returns single student by name
studentById = Student.objects.get(id=4)

#***(6)Returns all orders related to student (firstStudent variable set above)
firstStudent.order_set.all()

#(7)***Returns orders student name: (Query parent model values)
order = Order.objects.first() 
parentName = order.student.name

#(8)***Returns products from products table with value of "Out Door" in category attribute
products = Product.objects.filter(category="Out Door")

#(9)***Order/Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id') 
greatestToLeast = Product.objects.all().order_by('-id') 


#(10) Returns all products with tag of "Sports": (Query Many to Many Fields)
productsFiltered = Product.objects.filter(tags__name="Sports")

'''
(11)Bonus
Q: If the student has more than 1 ball, how would you reflect it in the database?
A: Because there are many different products and this value changes constantly you would most 
likly not want to store the value in the database but rather just make this a function we can run
each time we load the students profile
'''

#Returns the total count for number of time a "Ball" was ordered by the first student
ballOrders = firstStudent.order_set.filter(product__name="Ball").count()

#Returns total count for each product orderd
allOrders = {}

for order in firstStudent.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] += 1
	else:
		allOrders[order.product.name] = 1

#Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


#RELATED SET EXAMPLE
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(Student)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()