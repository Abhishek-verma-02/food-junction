from database.mongodb import db

categories = db["categories"]

if categories.count_documents({}) == 0:

    categories.insert_many([
        {
            "name": "Pizza",
            "image": "pizza_category.jpg"
        },
        {
            "name": "Burger",
            "image": "burger_category.jpg"
        },
        {
            "name": "Chinese",
            "image": "chinese_category.jpg"
        },
        {
            "name": "Drinks",
            "image": "drinks_category.jpg"
        }
    ])

    print("Categories inserted.")

else:

    print("Categories already exist.")