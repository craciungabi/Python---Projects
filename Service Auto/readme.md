
              Here is the requirement of the project

1. CRUD car: id, model, year of purchase, no. km, under warranty. Km and the year of manufacture to be
strictly positive.
2. CRUD client card: id, name, surname, CNP, date of birth (dd.mm.yyyy), date of registration
(Dd.mm.yyyy). The CNP must be unique.
3. CRUD transaction: id, machine_id, customer_card_id (can be null), parts amount, amount
labor, date and time. If there is a customer card, then apply a 10% discount
for labor. If the car is under warranty, then the parts are free. It is printed
the price paid and the discounts granted.
4. Search for cars and customers by model, year of manufacture, first name, CNP, etc. Full text search.
5. Show all transactions with the amount within a given range.
6. Display of cars in descending order by the amount obtained per labor.
7. Show customer cards ordered in descending order by the level of discounts obtained.
8. Delete all transactions within a certain number of days.
9. Warranty update on each car: a car is under warranty if and only if
has a maximum of 3 years and a maximum of 60,000 km.
