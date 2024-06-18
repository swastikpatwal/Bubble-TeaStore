# Bubble-Tea-Store
You are required to implement a program for a bubble tea store. Your solution must exemplify
aspects of object-oriented programming and principles. You are required to include at least one
abstract class, dictionary or set, and are even permitted to use multiple inheritance. With the
abstraction, you must include polymorphism. Finally, you will write tests to compliment your
program.
All classes must include a string conversion method which eloquently describes and displays
their details.
Due to the nature of assignment 1, you are being tested not only on your ability to problem solve
and develop a solution to the given problem, but further emphasis is placed on perfecting your
solution with correct and object-oriented code.
Bubble Tea
This class represents a bubble tea object which includes what you might find in most bubble tea
stores. It has a name, size, level of ice, level of sugar, whether it is green or black tea, any toppings
it might include, and a price.
Furthermore, you can add and remove toppings and should be able to store more than one of the
same toppings. Your choice of data structure is key to good object-oriented code.
A method for calculating the price of tea is required. This price is based on the many factors that
make up a tea (See Pricing section for tea prices). This method must be well-implemented, and
all children of bubble tea are required to override this method.
Fruit Tea & Milk Tea
These classes represent different types of tea. If they are selected, their cost increases based
on the fruit or flavour.
Sparkling Tea & Hot Tea
These classes represent different types of tea. They differ greatly in that they are opposing teas.
A hot tea cannot be a sparkling tea and vice versa. Only certain kinds of teas should be sparkling,
and others are hot teas.
Frozen Tea
This type of tea can be both fruity and milky. Depending on what tea is ordered, you will need to
adjust the price accordingly. This is either both milky and fruity, just milky, or just fruity.
Topping
A simple object which stores the name and price of a topping. These are stored in bubble teas
when ordering.
4
Store
This is the main hub for ordering bubble tea. It will have an attribute to store its earnings and all
the order history. Furthermore, the store contains all prices of different sizes of tea, different fruit
selections, flavours, and toppings.
The store is responsible for ordering and creating teas. Once this process is complete, your
earnings increase, and the created tea is stored in the orders. You can view your order history in
a polished and organised way showing the tea and how you your increase in profit.
Testing
Tests should be written using Pytest and at least 5 methods should be tested. Only 10 pytests are
required and a method could have at most 4 tests relating to it. This does not include getter and
setter methods. Your tests should reflect week 12 tutorial examples and/or week 13 workshop.
Milestones
Aim to complete these tasks by the given week. Always isolate and test your code while you work
in-between. Comments and your git repository should be updated throughout the entire
assignment.
Hints
Design & Structure
• Classes should be split into their own modules.
o Testa should be a single module.
o Main code which runs the program should be in its own module.
• Main code should include ordering at least 10 different teas and then showing the order
history with the correct prices calculated. Ordering should only happen within the store
class. No Teas should be instantiated within the main module unless through an order.
• You must include at least one abstract class and implement polymorphic objects.
Week Tasks
11 • Initialise a local git repository. (Practical 7)
• Outline your design and start implementing classes, attributes, and
methods.
• Implement method logic and optimise your design.
12 • Your abstract class and inheritance structure should be completely
implemented.
• Understand Testing with Pytest (Tutorial)
13 • Complete the implementation of your program.
• Finalise your Testing module. (Workshop 9)
• Make sure your design and implementation meets object-oriented
standards including SOLID principles, encapsulation, inheritance,
abstraction, etc.
SWOTVAC • Remove TODOs, unused code, and/or unnecessary comments.
• Rename and compress folder.
• Submit the assignment.
5
• You should include multiple inheritance where possible.
• Your inheritance structure should capture a capable and complete design.
Pricing
• Each tea will be priced differently based on factors such as Tea types, sizes, fruits,
flavours, and toppings.
• Teas have a base price which does not change. This is the cost of the service for making
tea. This price is $ 4.5
• The following differences also increase the cost:
