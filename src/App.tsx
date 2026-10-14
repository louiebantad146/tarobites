
import { useState } from "react";
import "./App.css";

const products = [
  {
    id: 1,
    name: "Classic Taro Chips",
    description: "Crispy, golden, perfectly salted.",
    price: 79,
    emoji: "🥔",
    tag: "BESTSELLER",
  },
  {
    id: 2,
    name: "Sweet Taro Bites",
    description: "A little sweetness in every bite.",
    price: 89,
    emoji: "🍠",
    tag: "FAN FAVORITE",
  },
  {
    id: 3,
    name: "Taro Crunch Mix",
    description: "Extra crunch for snack lovers.",
    price: 99,
    emoji: "🍿",
    tag: "MUST TRY",
  },
  {
    id: 4,
    name: "Golden Taro Box",
    description: "A shareable box full of goodness.",
    price: 149,
    emoji: "🎁",
    tag: "GREAT TO SHARE",
  },
];

type CartItem = (typeof products)[number] & { quantity: number };

function App() {
  const [cart, setCart] = useState<CartItem[]>([]);
  const [cartOpen, setCartOpen] = useState(false);

  const count = cart.reduce((sum, item) => sum + item.quantity, 0);
  const total = cart.reduce(
    (sum, item) => sum + item.price * item.quantity,
    0
  );

  function addToCart(product: (typeof products)[number]) {
    setCart((current) => {
      const found = current.find((item) => item.id === product.id);
      if (found) {
        return current.map((item) =>
          item.id === product.id
            ? { ...item, quantity: item.quantity + 1 }
            : item
        );
      }
      return [...current, { ...product, quantity: 1 }];
    });
  }

  function changeQuantity(id: number, amount: number) {
    setCart((current) =>
      current
        .map((item) =>
          item.id === id
            ? { ...item, quantity: item.quantity + amount }
            : item
        )
        .filter((item) => item.quantity > 0)
    );
  }

  return (
    <div className="site-shell">
      <div className="announcement">
        A LITTLE CRUNCH, A LOT OF LOVE 💜
      </div>

      <header className="navbar">
        <a className="brand" href="#home" aria-label="Taro Bites home">
          <img src="/taro-bites-logo.svg" alt="Taro Bites" />
        </a>

        <nav className="nav-links">
          <a href="#home">Home</a>
          <a href="#menu">Our Snacks</a>
          <a href="#story">Our Story</a>
        </nav>

        <button className="cart-button" onClick={() => setCartOpen(!cartOpen)}>
          Bag <span>{count}</span>
        </button>
      </header>

      <main>
        <section className="hero" id="home">
          <div className="hero-copy">
            <span className="eyebrow">YOUR NEW FAVORITE SNACK ✨</span>
            <h1>
              Good days
              <br />
              start with a
              <br />
              <span>little crunch.</span>
            </h1>
            <p>
              Meet your new snack obsession. Made for happy
              munching, sharing with friends, and treating yourself.
            </p>
            <div className="hero-actions">
              <a className="primary-button" href="#menu">
                Shop our snacks <span>↗</span>
              </a>
              <a className="text-button" href="#story">
                Get to know us
              </a>
            </div>
            <div className="hero-note">
              <span>💜</span> Small bites, big happy moments.
            </div>
          </div>

          <div className="hero-art">
            <div className="sunburst" />
            <div className="hero-sticker sticker-top">MADE FOR<br />MUNCHING!</div>
            <div className="snack-circle">
              <div className="snack-emoji">🍠</div>
              <div className="floating-chip chip-one">🥔</div>
              <div className="floating-chip chip-two">✨</div>
              <div className="floating-chip chip-three">💜</div>
            </div>
            <div className="hero-sticker sticker-bottom">
              SNACK HAPPY
              <br />
              EVERY DAY!
            </div>
            <span className="sparkle sparkle-one">✳</span>
            <span className="sparkle sparkle-two">✦</span>
          </div>
        </section>

        <div className="perks">
          <div><span>🌱</span><p>Rooted in goodness</p></div>
          <div><span>💜</span><p>Made for happy moments</p></div>
          <div><span>✨</span><p>Seriously snack-worthy</p></div>
        </div>

        <section className="menu-section" id="menu">
          <div className="section-heading">
            <div>
              <span className="eyebrow">THE SNACK LINEUP</span>
              <h2>Little bites.<br /><span>Big delight.</span></h2>
            </div>
            <p>
              Crunchy, craveable, and ready for snack time.
              Find your new go-to below.
            </p>
          </div>

          <div className="product-grid">
            {products.map((product, index) => (
              <article className="product-card" key={product.id}>
                <div className={`product-art product-art-${index + 1}`}>
                  <span className="product-tag">{product.tag}</span>
                  <span className="product-emoji">{product.emoji}</span>
                  <span className="product-decoration">✳</span>
                </div>
                <div className="product-info">
                  <div>
                    <h3>{product.name}</h3>
                    <p>{product.description}</p>
                  </div>
                  <div className="product-bottom">
                    <strong>₱{product.price.toFixed(2)}</strong>
                    <button
                      className="add-button"
                      onClick={() => addToCart(product)}
                      aria-label={`Add ${product.name} to bag`}
                    >
                      + Add
                    </button>
                  </div>
                </div>
              </article>
            ))}
          </div>
          <p className="menu-footnote">
            Prices are sample prices. Product availability may vary.
          </p>
        </section>

        <section className="story-section" id="story">
          <div className="story-art">
            <div className="story-blob">
              <span>💜</span>
              <strong>SNACK<br />HAPPY!</strong>
              <small>GOODNESS IN EVERY BITE</small>
            </div>
            <span className="story-star">✳</span>
          </div>
          <div className="story-copy">
            <span className="eyebrow">A LITTLE ABOUT US</span>
            <h2>Life is better<br />with <span>good snacks.</span></h2>
            <p>
              Taro Bites is all about making everyday moments a
              little more delicious. Whether you're taking a study
              break, hanging out with friends, or simply craving
              something fun, there's always room for a little bite
              of happiness.
            </p>
            <a className="primary-button" href="#menu">
              Find your favorite <span>↗</span>
            </a>
          </div>
        </section>

        <section className="cta-section">
          <span>💜 ✨ 💜</span>
          <h2>Your next favorite snack<br />is waiting for you.</h2>
          <a href="#menu" className="light-button">Let's get snacking ↗</a>
        </section>
      </main>

      <footer className="footer">
        <a href="#home" className="footer-brand">Taro Bites<span>®</span></a>
        <p>Made for munching. Shared with love.</p>
        <span>© {new Date().getFullYear()} Taro Bites</span>
      </footer>

      {cartOpen && (
        <div className="cart-overlay" onClick={() => setCartOpen(false)}>
          <aside
            className="cart-panel"
            onClick={(event) => event.stopPropagation()}
          >
            <div className="cart-heading">
              <div>
                <span className="eyebrow">YOUR SNACK STASH</span>
                <h2>Your bag <span>({count})</span></h2>
              </div>
              <button
                className="close-button"
                onClick={() => setCartOpen(false)}
                aria-label="Close shopping bag"
              >
                ×
              </button>
            </div>

            {cart.length === 0 ? (
              <div className="empty-cart">
                <span>🛍️</span>
                <h3>Your bag needs some bites!</h3>
                <p>Add a snack or two to get things rolling.</p>
                <button
                  className="primary-button"
                  onClick={() => {
                    setCartOpen(false);
                    document.getElementById("menu")?.scrollIntoView({
                      behavior: "smooth",
                    });
                  }}
                >
                  Explore snacks ↗
                </button>
              </div>
            ) : (
              <>
                <div className="cart-items">
                  {cart.map((item) => (
                    <div className="cart-item" key={item.id}>
                      <div className="cart-item-emoji">{item.emoji}</div>
                      <div className="cart-item-details">
                        <h3>{item.name}</h3>
                        <p>₱{item.price.toFixed(2)} each</p>
                        <div className="quantity-control">
                          <button onClick={() => changeQuantity(item.id, -1)}>
                            −
                          </button>
                          <span>{item.quantity}</span>
                          <button onClick={() => changeQuantity(item.id, 1)}>
                            +
                          </button>
                        </div>
                      </div>
                      <strong>
                        ₱{(item.price * item.quantity).toFixed(2)}
                      </strong>
                    </div>
                  ))}
                </div>
                <div className="cart-total">
                  <div><span>Subtotal</span><strong>₱{total.toFixed(2)}</strong></div>
                  <p>Delivery fees, if applicable, are not included.</p>
                  <button
                    className="primary-button checkout-button"
                    onClick={() =>
                      alert("Thanks for loving Taro Bites! Online checkout isn't connected yet.")
                    }
                  >
                    Continue to checkout ↗
                  </button>
                </div>
              </>
            )}
          </aside>
        </div>
      )}
    </div>
  );
}

export default App;