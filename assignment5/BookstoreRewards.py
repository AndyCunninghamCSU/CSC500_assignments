'''
@Author Andrew Cunningham
@date 15 Dec 2024
CSC 500 - Critical Thinking Assignment 5

Part 2
The CSU Global Bookstore has a book club that awards points 
to its students based on the number of books purchased each month. 

The points are awarded as follows:

If a customer purchases 0 books, they earn 0 points.
If a customer purchases 2 books, they earn 5 points.
If a customer purchases 4 books, they earn 15 points.
If a customer purchases 6 books, they earn 30 points.
If a customer purchases 8 or more books, they earn 60 points.
'''
def calculate_points(books_purchased):

    # rewards in descending order
    reward_thresholds = [
        (8, 60),
        (6, 30),
        (4, 15),
        (2, 5),
        (0, 0)
    ]

    # since rewards are in descending order, return the points as soon as the criteria is met
    for books, points in reward_thresholds:
        if books_purchased >= books:
            return points

print("input nothing to exit")
# asks the user to enter the number of books that they have purchased this month

# use a walrus operator to loop through books purchased while an input is supplied
while (books_purchased := input("How many books were purchased: ")):
    points = calculate_points(int(books_purchased))

    # display the number of points awarded.

    print(f"{points} awarded for {books_purchased} books.")