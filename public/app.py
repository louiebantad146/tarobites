from datetime import datetime
from html import escape
from js import document

products = [
    {
        "id": 1,
        "name": "Classic Taro Chips",
        "description": "Crispy, golden, perfectly salted.",
        "price": 79,
        "emoji": "🥔",
        "tag": "BESTSELLER",
    },
    {
        "id": 2,
        "name": "Sweet Taro Bites",
        "description": "A little sweetness in every bite.",
        "price": 89,
        "emoji": "🍠",
        "tag": "FAN FAVORITE",
    },
    {
        "id": 3,
        "name": "Taro Crunch Mix",
        "description": "Extra crunch for snack lovers.",
        "price": 99,
        "emoji": "🍿",
        "tag": "MUST TRY",
    },
    {
        "id": 4,
        "name": "Golden Taro Box",
        "description": "A shareable box full of goodness.",
        "price": 149,
        "emoji": "🎁",
        "tag": "GREAT TO SHARE",
    },
    {
        "id": 5,
        "name": "Spicy Taro Twists",
        "description": "A crispy kick with a little heat.",
        "price": 99,
        "emoji": "🌶️",
        "tag": "SPICY PICK",
    },
    {
        "id": 6,
        "name": "Taro Cheese Puffs",
        "description": "Fluffy crunch with cheesy goodness.",
        "price": 109,
        "emoji": "🧀",
        "tag": "CHEESY CRUNCH",
    },
    {
        "id": 7,
        "name": "Taro Cookie Bites",
        "description": "Sweet, buttery bites with a taro twist.",
        "price": 119,
        "emoji": "🍪",
        "tag": "SWEET TREAT",
    },
    {
        "id": 8,
        "name": "Taro Party Pack",
        "description": "A big mix made for sharing.",
        "price": 199,
        "emoji": "🍬",
        "tag": "PARTY FAVORITE",
    },
]

cart = []
cart_open = False


def format_price(value):
    return f"₱{value:.2f}"


def get_count():
    return sum(item["quantity"] for item in cart)


def get_total():
    return sum(item["price"] * item["quantity"] for item in cart)


def get_order_summary():
    lines = ["Hi Taro Bites! I'd like to place this order:"]
    for item in cart:
        item_total = item["price"] * item["quantity"]
        lines.append(
            f"- {item['name']} x {item['quantity']} — {format_price(item_total)}"
        )
    lines.extend(
        [
            f"Estimated subtotal: {format_price(get_total())}",
            "Please confirm final prices, delivery availability and fee, pickup options, and expected timing.",
            "Name:",
            "Delivery address or pickup preference:",
        ]
    )
    return escape("\n".join(lines))


def toggle_cart():
    global cart_open
    cart_open = not cart_open
    render_app()
    if cart_open:
        close_button = document.querySelector(".close-button")
        if close_button is not None:
            close_button.focus()
    else:
        cart_button = document.querySelector(".cart-button")
        if cart_button is not None:
            cart_button.focus()


def close_cart():
    global cart_open
    cart_open = False
    render_app()
    cart_button = document.querySelector(".cart-button")
    if cart_button is not None:
        cart_button.focus()


def scroll_to_menu():
    menu = document.getElementById("menu")
    if menu is not None:
        menu.scrollIntoView({"behavior": "smooth"})


def add_to_cart(product_id):
    global cart
    product = next((item for item in products if item["id"] == product_id), None)
    if not product:
        return

    existing = next((item for item in cart if item["id"] == product_id), None)
    if existing:
        existing["quantity"] += 1
    else:
        cart.append({**product, "quantity": 1})

    global cart_open
    cart_open = True
    render_app()
    close_button = document.querySelector(".close-button")
    if close_button is not None:
        close_button.focus()


def change_quantity(product_id, amount):
    global cart
    updated = []
    for item in cart:
        if item["id"] == product_id:
            next_quantity = item["quantity"] + amount
            if next_quantity > 0:
                item["quantity"] = next_quantity
                updated.append(item)
        else:
            updated.append(item)
    cart = updated
    render_app()


def select_order_summary():
    summary = document.getElementById("order-summary")
    if summary is not None:
        summary.focus()
        summary.select()


def render_product_cards():
    cards = []
    for index, product in enumerate(products, start=1):
        cards.append(
            f"""
            <article class=\"product-card\" key=\"{product['id']}\">
              <div class=\"product-art product-art-{index}\">
                <span class=\"product-tag\">{product['tag']}</span>
                <span class=\"product-emoji\">{product['emoji']}</span>
                <span class=\"product-decoration\">✳</span>
              </div>
              <div class=\"product-info\">
                <div>
                  <h3>{product['name']}</h3>
                  <p>{product['description']}</p>
                </div>
                <div class=\"product-bottom\">
                  <strong>{format_price(product['price'])}</strong>
                  <button class=\"add-button\" data-add-product-id=\"{product['id']}\" aria-label=\"Add {product['name']} to bag\">+ Add</button>
                </div>
              </div>
            </article>
            """
        )
    return "\n".join(cards)


def render_cart_contents():
    if not cart:
        return f"""
        <div class=\"empty-cart\">
          <span>🛍️</span>
          <h3>Your bag needs some bites!</h3>
          <p>Add a snack or two to get things rolling.</p>
          <button class=\"primary-button\" data-action=\"menu\">Explore snacks ↗</button>
        </div>
        """

    items = []
    for item in cart:
        items.append(
            f"""
            <div class=\"cart-item\" key=\"{item['id']}\">
              <div class=\"cart-item-emoji\" aria-hidden=\"true\">{item['emoji']}</div>
              <div class=\"cart-item-details\">
                <h3>{item['name']}</h3>
                <p>{format_price(item['price'])} each</p>
                <div class=\"quantity-control\">
                  <button data-change-quantity-id=\"{item['id']}\" data-change-quantity-delta=\"-1\" aria-label=\"Remove one {item['name']}\">−</button>
                  <span aria-label=\"Quantity: {item['quantity']}\">{item['quantity']}</span>
                  <button data-change-quantity-id=\"{item['id']}\" data-change-quantity-delta=\"1\" aria-label=\"Add one {item['name']}\">+</button>
                </div>
              </div>
              <strong>{format_price(item['price'] * item['quantity'])}</strong>
            </div>
            """
        )

    return f"""
    <div class=\"cart-items\">{''.join(items)}</div>
    <div class=\"cart-total\">
      <div><span>Subtotal</span><strong>{format_price(get_total())}</strong></div>
      <p>Displayed prices are samples. Confirm final pricing, delivery areas and fees, pickup options, and timing with us in Messenger.</p>
      <label class=\"order-summary-label\" for=\"order-summary\">Your order message</label>
      <textarea class=\"order-summary\" id=\"order-summary\" rows=\"8\" readonly>{get_order_summary()}</textarea>
      <p class=\"order-guidance\">Select and copy these details, then paste them into your Messenger chat.</p>
      <button class=\"order-copy-button\" data-action=\"select-order\">Select order details</button>
      <a class=\"primary-button checkout-button\" href=\"https://m.me/Tarobites\" target=\"_blank\" rel=\"noopener noreferrer\">Continue in Messenger ↗</a>
    </div>
    """


def attach_event_handlers():
    for button in document.querySelectorAll("[data-add-product-id]"):
        product_id = int(getattr(button.dataset, "addProductId"))
        button.onclick = lambda event, product_id=product_id: add_to_cart(product_id)

    for button in document.querySelectorAll("[data-change-quantity-id]"):
        product_id = int(getattr(button.dataset, "changeQuantityId"))
        delta = int(getattr(button.dataset, "changeQuantityDelta"))
        button.onclick = lambda event, product_id=product_id, delta=delta: change_quantity(product_id, delta)

    for button in document.querySelectorAll("[data-action='toggle-cart']"):
        button.onclick = lambda event: toggle_cart()

    for button in document.querySelectorAll("[data-action='close-cart']"):
        button.onclick = lambda event: close_cart()

    for button in document.querySelectorAll("[data-action='menu']"):
        button.onclick = lambda event: (close_cart(), scroll_to_menu())

    for button in document.querySelectorAll("[data-action='select-order']"):
        button.onclick = lambda event: select_order_summary()

    overlay = document.querySelector(".cart-overlay")
    if overlay is not None:
        overlay.onclick = lambda event: close_cart()

    panel = document.querySelector(".cart-panel")
    if panel is not None:
        panel.onclick = lambda event: event.stopPropagation()
        panel.onkeydown = lambda event: close_cart() if event.key == "Escape" else None


def render_app():
    count = get_count()
    total = get_total()
    current_year = datetime.now().year
    cart_section = ""
    if cart_open:
        cart_section = f"""
        <div class=\"cart-overlay\">
          <aside id=\"cart-dialog\" class=\"cart-panel\" role=\"dialog\" aria-modal=\"true\" aria-labelledby=\"cart-heading\">
            <div class=\"cart-heading\">
              <div>
                <span class=\"eyebrow\">YOUR SNACK STASH</span>
                <h2 id=\"cart-heading\">Your bag <span>({count})</span></h2>
              </div>
              <button class=\"close-button\" data-action=\"close-cart\" aria-label=\"Close shopping bag\">×</button>
            </div>
            {render_cart_contents()}
          </aside>
        </div>
        """

    app = document.getElementById("app")
    ad_video = app.querySelector(".ad-video")
    app.innerHTML = f"""
    <div class=\"site-shell\">
      <div class=\"announcement\">A LITTLE CRUNCH, A LOT OF LOVE 💜</div>

      <a class=\"skip-link\" href=\"#main-content\">Skip to content</a>
      <header class=\"navbar\">
        <a class=\"brand\" href=\"#home\" aria-label=\"Taro Bites home\">
          <img src=\"/public/taro-bites-logo.svg\" alt=\"Taro Bites\" />
        </a>

        <nav class=\"nav-links\" aria-label=\"Main navigation\">
          <a href=\"#home\">Home</a>
          <a href=\"#menu\">Our Snacks</a>
          <a href=\"#story\">Our Story</a>
        </nav>

        <button class=\"cart-button\" data-action=\"toggle-cart\" aria-expanded=\"{str(cart_open).lower()}\" aria-controls=\"cart-dialog\">
          Bag <span aria-live=\"polite\" aria-label=\"{count} items in bag\">{count}</span>
        </button>
      </header>

      <main id=\"main-content\">
        <section class=\"hero\" id=\"home\">
          <div class=\"hero-copy\">
            <span class=\"eyebrow\">YOUR NEW FAVORITE SNACK ✨</span>
            <h1>
              Good days
              <br />
              start with a
              <br />
              <span>little crunch.</span>
            </h1>
            <p>
              Meet your new snack obsession. Made for happy munching, sharing with friends, and treating yourself.
            </p>
            <div class=\"hero-actions\">
              <a class=\"primary-button\" href=\"#menu\">Shop our snacks <span>↗</span></a>
              <a class=\"text-button\" href=\"#story\">Get to know us</a>
            </div>
            <div class=\"hero-note\">
              <span>💜</span> Small bites, big happy moments.
            </div>
          </div>

          <div class=\"hero-art\">
            <div class=\"sunburst\"></div>
            <div class=\"hero-sticker sticker-top\">MADE FOR<br />MUNCHING!</div>
            <div class=\"snack-circle\">
              <div class=\"snack-emoji\">🍠</div>
              <div class=\"floating-chip chip-one\">🥔</div>
              <div class=\"floating-chip chip-two\">✨</div>
              <div class=\"floating-chip chip-three\">💜</div>
            </div>
            <div class=\"hero-sticker sticker-bottom\">
              SNACK HAPPY
              <br />
              EVERY DAY!
            </div>
            <span class=\"sparkle sparkle-one\">✳</span>
            <span class=\"sparkle sparkle-two\">✦</span>
          </div>
        </section>

        <div class=\"perks\">
          <div><span>🌱</span><p>Rooted in goodness</p></div>
          <div><span>💜</span><p>Made for happy moments</p></div>
          <div><span>✨</span><p>Seriously snack-worthy</p></div>
        </div>

        <section class=\"ad-section\" aria-labelledby=\"ad-heading\">
          <div class=\"ad-copy\">
            <span class=\"eyebrow\">A LITTLE TASTE OF TARO BITES</span>
            <h2 id=\"ad-heading\">Meet your new<br /><span>happy snack.</span></h2>
            <p>Made for snack breaks, shared moments, and one more delicious bite.</p>
          </div>
          <video class=\"ad-video\" autoplay muted loop playsinline preload=\"auto\" aria-label=\"Taro Bites advertisement\">
            <source src=\"/public/taro-bites-ad.mp4\" type=\"video/mp4\" />
            Your browser does not support HTML video.
          </video>
        </section>

        <section class=\"menu-section\" id=\"menu\">
          <div class=\"section-heading\">
            <div>
              <span class=\"eyebrow\">THE SNACK LINEUP</span>
              <h2>Little bites.<br /><span>Big delight.</span></h2>
            </div>
            <p>
              Crunchy, craveable, and ready for snack time. Find your new go-to below.
            </p>
          </div>

          <div class=\"product-grid\">
            {render_product_cards()}
          </div>
          <p class=\"menu-footnote\">
            Prices are sample prices. Product availability may vary.
          </p>
        </section>

        <section class=\"story-section\" id=\"story\">
          <div class=\"story-art\">
            <div class=\"story-blob\">
              <span>💜</span>
              <strong>SNACK<br />HAPPY!</strong>
              <small>GOODNESS IN EVERY BITE</small>
            </div>
            <span class=\"story-star\">✳</span>
          </div>
          <div class=\"story-copy\">
            <span class=\"eyebrow\">A LITTLE ABOUT US</span>
            <h2>Life is better<br />with <span>good snacks.</span></h2>
            <p>
              Taro Bites is all about making everyday moments a little more delicious. Whether you're taking a study break, hanging out with friends, or simply craving something fun, there's always room for a little bite of happiness.
            </p>
            <a class=\"primary-button\" href=\"#menu\">Find your favorite <span>↗</span></a>
          </div>
        </section>

        <section class=\"cta-section\">
          <span>💜 ✨ 💜</span>
          <h2>Your next favorite snack<br />is waiting for you.</h2>
          <a href=\"#menu\" class=\"light-button\">Let's get snacking ↗</a>
        </section>
      </main>

      <footer class=\"footer\">
        <a href=\"#home\" class=\"footer-brand\">Taro Bites<span>®</span></a>
        <p>Made for munching. Shared with love.</p>
        <span>© {current_year} Taro Bites</span>
      </footer>

      {cart_section}
    </div>
    """
    if ad_video is not None:
        video_placeholder = app.querySelector(".ad-video")
        if video_placeholder is not None:
            video_placeholder.replaceWith(ad_video)
    attach_event_handlers()


render_app()
