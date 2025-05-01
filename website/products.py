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
    #Rings ID: 41-50
    {
        "id": 41,
        "name": "Golden Heart Ring",
        "price": 50,
        "desc": "Ring covered in gold with an incrusted heart-shaped gem.",
        "image": "images/Golden Heart Ring.png"
    },
    {
        "id": 42,
        "name": "Golden Heart Ring",
        "price": 90,
        "desc": "Silver coated with an incrusted Sapphire gem.",
        "image": "images/Sapphire Ring.png"
    },
    {
        "id": 43,
        "name": "Emerald Moss Green Ring",
        "price": 65,
        "desc": "Silver coated with an incrusted Emerald gem.",
        "image": "images/Emerald Ring.png"
    },
    {
        "id": 44,
        "name": "Ruby Ring",
        "price": 200,
        "desc": "A sophisticated ring made with a Ruby gem.",
        "image": "images/Ruby Ring.png"
    },
    {
        "id": 45,
        "name": "Tri-Colored Ring",
        "price": 30,
        "desc": "A simple yet elegant ring made with 3 different gems combined.",
        "image": "images/Tri Color Ring.png"
    },
    {
        "id": 46,
        "name": "Dark Amethyst Ring",
        "price": 120,
        "desc": "A dark contrast to enhance the color of the amethyst. For special occassions.",
        "image": "images/Dark Amethyst Ring.png"
    },
    {
        "id": 47,
        "name": "Pink Ring",
        "price": 45,
        "desc": "Made with granite and pink pearls.",
        "image": "images/Pink Ring.png"
    },
    {
        "id": 48,
        "name": "Diamond Ring",
        "price": 1000,
        "desc": "Authentic incrusted diamonds imported from our affiliated gold mines.",
        "image": "images/Diamond Ring.png"
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
    },
    # Dresses ID: 61-70
    {
        "id": 61,
        "name": "Red Goth Victorian Dress",
        "price": 50,
        "desc": "An elaborated cotton dress based on the Victorian Goth era.",
        "image": "images/Dress Red.png"
    },
    {
        "id": 62,
        "name": "Blue Floral Vintage Dress",
        "price": 45,
        "desc": "A breathable floral cotton dress.",
        "image": "images/Dress Blue.png"
    },
    {
        "id": 63,
        "name": "Waist Strapped Winter Brown Dress",
        "price": 100,
        "desc": "A winter warm with mixed fabric to keep warm and elegance.",
        "image": "images/Dress Brown.png"
    },
    {
        "id": 64,
        "name": "Navy Buttoned Dress",
        "price": 40,
        "desc": "Navy Long Skirt Single-piece Bow Strapped Dress.",
        "image": "images/Dress Navy.png"
    },
    {
        "id": 65,
        "name": "Yellow Ribbon Dress",
        "price": 30,
        "desc": "A summer-spring yellow cotton dress with a ribbon on front.",
        "image": "images/Dress Yellow.png"
    },
    {
        "id": 66,
        "name": "Cherry Blossom Bloom Dress",
        "price": 90,
        "desc": "A pink dress with designs resembling a blossom cherry tree..",
        "image": "images/Dress Blossom.png"
    },
    {
        "id": 67,
        "name": "Peach Floral Dress",
        "price": 75,
        "desc": "A light peach color dress.",
        "image": "images/Dress Peach.png"
    },
    {
        "id": 68,
        "name": "Sleeveless Closed Black Skirt Dress",
        "price": 120,
        "desc": "Black Sleeveless dress made with polyester.",
        "image": "images/Dress Black.png"
    },
    # Women Tops IDs 71-80
    {
        "id": 71,
        "name": "Red Long Sleeve Casual Floral Top",
        "price": 10,
        "desc": "Casual Feminine shirt with a floral design.",
        "image": "images/Red Top.png"
    },
    {
        "id": 72,
        "name": "Green Long Sleeve Casual Floral Top",
        "price": 10,
        "desc": "Casual Feminine shirt with a floral design.",
        "image": "images/Green Top.png"
    },
    {
        "id": 73,
        "name": "Yellow Long Sleeve Casual Floral Top",
        "price": 10,
        "desc": "Casual Feminine shirt with a floral design.",
        "image": "images/Yellow Top.png"
    },
    {
        "id": 74,
        "name": "Blue Long Sleeve Casual Floral Top",
        "price": 10,
        "desc": "Casual Feminine shirt with a floral design.",
        "image": "images/Blue Top.png"
    },
    {
        "id": 75,
        "name": "Black Long Sleeve Casual Floral Top",
        "price": 10,
        "desc": "Casual Feminine shirt with a floral design.",
        "image": "images/Black Top.png"
    },
    {
        "id": 76,
        "name": "Burgandy Formal Top",
        "price": 30,
        "desc": "Burgandy Formal Silk Top for all ocassions.",
        "image": "images/Burgandy Top.png"
    },
    {
        "id": 77,
        "name": "Wool Top",
        "price": 20,
        "desc": "A light top made from wool.",
        "image": "images/Wool Top.png"
    },
    {
        "id": 78,
        "name": "Ruffled Top",
        "price": 50,
        "desc": "Ruffled white top made of silk.",
        "image": "images/White Top.png"
    },
]