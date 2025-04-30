'''
products.py
Create by Hien Tran 
Make it so that all the products can store here to be call apon later
'''

products = [
    #watches id 1-10
    {
        "id": 1,
        "name": "Bulova Chronograph",
        "price": 289,
        "desc": "Black stainless steel watch with chronograph functionality.",
        "image": "images/bulova-black.png"
    },
    {
        "id": 2,
        "name": "Sanda Sport Watch",
        "price": 59,
        "desc": "White water-resistant sport watch with LED features.",
        "image": "images/sanda-white.png"
    },
    #shirt id 11-20
    {
        "id": 11,
        "name": "Mens Short Sleeve Crew T-Shirt",
        "price": 30,
        "desc": "Mens Short Sleeve Crew T-Shirt",
        "image": "images/black shirt.png"
    },
    {
        "id": 12,
        "name": "Formal Slim Fit Shirt",
        "price": 63,
        "desc": "Formal Straight Point Slim Fit Shirt",
        "image": "images/slim fit shirt.jpg"
    },
    {
        "id": 13,
        "name": "Long Sleeve Stretch Dress Shirt",
        "price": 40,
        "desc": "Long Sleeve Stretch Dress Shirts Casual Button Down Shirt",
        "image": "images/long sleeve dress shirt.png"
    },
    {
        "id": 14,
        "name": "Summit Flannel Shirt",
        "price": 98,
        "desc": "Navy Blue Summit Flannel Shirt",
        "image": "images/summit flannel shirt.png"
    },
    {
        "id": 15,
        "name": "Polo Cotton Vneck Shirt",
        "price": 30,
        "desc": "Grey Polo Cotton Vneck Shirt",
        "image": "images/Polo Cotton Vneck Shirt.png"
    },
    {
        "id": 16,
        "name": "Cotton Relaxed Fit Long Sleeve Shirt",
        "price": 60,
        "desc": "Medium Blue Cotton Relaxed Fit Long Sleeve Shirt",
        "image": "images/Cotton Relaxed Fit Long Sleeve Shirt.jpg"
    },
    {
        "id": 17,
        "name": "Men's Lightweight Shirt",
        "price": 65,
        "desc": "Iron Lightweight Shirt",
        "image": "images/iron lightweight shirt.png"
    },
    {
        "id": 18,
        "name": "Men's White Long Sleeve Shirt",
        "price": 65,
        "desc": "White Long Sleeve Shirt",
        "image": "images/white long sleeve range shirt.png"
    },
    #mens pants 21-30
    {
        "id": 21,
        "name": "Khaki Pants",
        "price": 50,
        "desc": "Mens Classic Khaki Pants",
        "image": "images/khaki.jpg"
    },
    {
        "id": 22,
        "name": "Chino Officer Pant",
        "price": 250,
        "desc": "Mens Classic Khaki Pants",
        "image": "images/officer chino pant.png"
    },
    {
        "id": 23,
        "name": "Stretch Pants",
        "price": 250,
        "desc": "Beige Stretch Pants",
        "image": "images/stretch pants.png"
    },
    {
        "id": 24,
        "name": "Relax Fit Cargo Pants",
        "price": 90,
        "desc": "Gray Relax Fit Cargo Pants",
        "image": "images/relaxed fit cargo pants.jpg"
    },
    {
        "id": 25,
        "name": "Standard Fit Jeans",
        "price": 85,
        "desc": "Mens Standard Fit Jeans",
        "image": "images/standard fit jeans.jpg"
    },
    {
        "id": 26,
        "name": "Relaxed Fit Cargo Shorts",
        "price": 65,
        "desc": "Relaxed Fit Cargo Shorts",
        "image": "images/relaxed fit cargo shorts.jpg"
    },
    {
        "id": 27,
        "name": "Dress Pants",
        "price": 225,
        "desc": "Wool Dress Pants",
        "image": "images/dress pants.jpg"
    },
    {
        "id": 28,
        "name": "Drawstring Linen Pants",
        "price": 200,
        "desc": "Drawstring Linen Pants",
        "image": "images/drawstring linen pants.jpg"
    },
    #jackets 31-40
    {
        "id": 31,
        "name": "Dri Duck Rambler Jacket",
        "price": 250,
        "desc": "Rambler Jacket",
        "image": "images/rambler jacket.png"
    },
    {
        "id": 32,
        "name": "Suede Trucker Jacket",
        "price": 250,
        "desc": "Suede Trucker Jacket",
        "image": "images/suede jacket.png"
    },
    {
        "id": 33,
        "name": "Mens Rain Jacket",
        "price": 220,
        "desc": "Mens Rain Jacket",
        "image": "images/mens rain jacket.jpg"
    },
    {
        "id": 34,
        "name": "Mens Softshell Jacket",
        "price": 30,
        "desc": "Mens Softshell Jacket",
        "image": "images/softshell jacket.png"
    },
    {
        "id": 35,
        "name": "Bomber Jacket",
        "price": 140,
        "desc": "Bomber Jacket",
        "image": "images/bomber jacket.png"
    },
    {
        "id": 36,
        "name": "Puffer Jacket",
        "price": 170,
        "desc": "Water Repellent Puffer Jacket",
        "image": "images/puffer jacket.jpg"
    },
    {
        "id": 37,
        "name": "Denim Jacket",
        "price": 250,
        "desc": "Mens Denim Jacket",
        "image": "images/denim jacket.jpg"
    },
    {
        "id": 38,
        "name": "Regular Fit Cotton Jacket",
        "price": 70,
        "desc": "Regular Fit Cotton Jacket",
        "image": "images/regular fit cotton jacket.jpg"
    },
    #Necklaces ID: 51-60
    {
        "id": 51,
        "name": "Aquamarine Heart Necklace",
        "price": 120,
        "desc": "Silver Jared Heart-Shaped Jewel glossed in a bright aqua color.",
        "image": "images/Aquamarine Necklace.png"
    },
    {
        "id": 52,
        "name": "Ruby Heart Necklace",
        "price": 220,
        "desc": "Authentic Ruby Jewel imported into a heart shape.",
        "image": "images/Ruby Necklace.png"
    },
    {
        "id": 53,
        "name": "Sapphire Necklace",
        "price": 450,
        "desc": "Navy Blue Sapphire Gem Necklace.",
        "image": "images/Sapphire Necklace.png"
    },
    {
        "id": 54,
        "name": "Teal Tear Drop Necklace",
        "price": 600,
        "desc": "Necklace with an incrusted teal tear-shaped.",
        "image": "images/Teal Necklace.png"
    },
    {
        "id": 55,
        "name": "Blue Flower Necklace",
        "price": 320,
        "desc": "5-Petal Blue Flower-Shaped Necklace.",
        "image": "images/Flower Necklace.png"
    },
    {
        "id": 56,
        "name": "Emerald Heart Necklace",
        "price": 1200,
        "desc": "Authentic Emerald Jewel imported and incrusted into a heart shape.",
        "image": "images/Emerald Necklace.png"
    },
    {
        "id": 57,
        "name": "Golden Heart Necklace",
        "price": 500,
        "desc": "Shiny Gold Yellow Heart-Shaped Necklace.",
        "image": "images/Golden Necklace.png"
    },
    {
        "id": 58,
        "name": "Amethyst Necklace",
        "price": 2200,
        "desc": "Real Purple Amethyst Incrusted Heart-Shaped Necklace.",
        "image": "images/Amethyst Necklace.png"
    }
]