from database.mongodb import db

foods = db["foods"]

if foods.count_documents({}) == 0:

    foods.insert_many([
        {
            "name": "Margherita Pizza",
            "category": "Pizza",
            "price": 299,
            "rating": 4.8,
            "image": "pizza.jpg",
            "description": "Fresh mozzarella with tomato sauce."
        },
        {
            "name": "Cheese Burger",
            "category": "Burger",
            "price": 199,
            "rating": 4.6,
            "image": "burger.jpg",
            "description": "Loaded with cheese and veggies."
        },
        {
            "name": "Veg Hakka Noodles",
            "category": "Chinese",
            "price": 249,
            "rating": 4.7,
            "image": "noodles.jpg",
            "description": "Delicious Chinese noodles."
        }
    ])

    print("✅ Sample food inserted successfully!")

else:
    print("⚡ Sample data already exists.")