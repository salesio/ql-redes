/* Carrinho de orçamento — localStorage + WhatsApp */
const CART_KEY = "qlredes_quote_cart";
const WHATSAPP_NUMBER = "258848426310";

const Cart = {
  get() {
    try {
      return JSON.parse(localStorage.getItem(CART_KEY)) || [];
    } catch {
      return [];
    }
  },

  save(items) {
    localStorage.setItem(CART_KEY, JSON.stringify(items));
    this.updateUI();
    document.dispatchEvent(new CustomEvent("cart:updated", { detail: items }));
  },

  count() {
    return this.get().reduce((sum, i) => sum + i.qty, 0);
  },

  add(productId, qty = 1) {
    const product = typeof getProductById === "function" ? getProductById(productId) : null;
    if (!product) return;

    const items = this.get();
    const existing = items.find((i) => i.id === productId);
    if (existing) {
      existing.qty += qty;
    } else {
      items.push({
        id: product.id,
        name: product.name,
        price: product.price,
        priceLabel: product.priceLabel,
        image: product.image,
        qty
      });
    }
    this.save(items);
    this.toast(`"${product.name}" adicionado ao orçamento`);
  },

  setQty(productId, qty) {
    let items = this.get();
    if (qty <= 0) {
      items = items.filter((i) => i.id !== productId);
    } else {
      const item = items.find((i) => i.id === productId);
      if (item) item.qty = qty;
    }
    this.save(items);
  },

  remove(productId) {
    this.save(this.get().filter((i) => i.id !== productId));
  },

  clear() {
    this.save([]);
  },

  updateUI() {
    const count = this.count();
    document.querySelectorAll(".cart-count").forEach((el) => {
      el.textContent = count > 0 ? String(count) : "";
      el.dataset.count = String(count);
    });
    this.renderDrawer();
  },

  toast(msg) {
    let el = document.getElementById("toast");
    if (!el) {
      el = document.createElement("div");
      el.id = "toast";
      el.className = "toast-ql";
      document.body.appendChild(el);
    }
    el.textContent = msg;
    el.classList.add("show");
    clearTimeout(el._t);
    el._t = setTimeout(() => el.classList.remove("show"), 2600);
  },

  open() {
    document.getElementById("cart-overlay")?.classList.add("open");
    document.getElementById("cart-drawer")?.classList.add("open");
    document.body.style.overflow = "hidden";
  },

  close() {
    document.getElementById("cart-overlay")?.classList.remove("open");
    document.getElementById("cart-drawer")?.classList.remove("open");
    document.body.style.overflow = "";
  },

  renderDrawer() {
    const body = document.getElementById("cart-body");
    if (!body) return;

    const items = this.get();
    if (!items.length) {
      body.innerHTML = `
        <div class="cart-empty">
          <p style="font-size:2rem;margin-bottom:0.5rem">🛒</p>
          <p>O seu pedido de orçamento está vazio.</p>
          <p style="font-size:0.85rem;margin-top:0.5rem">Adicione produtos na <a href="produtos.html">loja</a>.</p>
        </div>`;
      return;
    }

    body.innerHTML = items
      .map(
        (item) => `
      <div class="cart-item" data-id="${item.id}">
        <img src="${item.image}" alt="${item.name}" loading="lazy" onerror="this.style.background='#e2e8f0'">
        <div class="cart-item-info">
          <h4>${item.name}</h4>
          <div class="price">${item.price != null ? `ref. ${item.price.toLocaleString("pt-MZ")} MT` : item.priceLabel || "Sob consulta"}</div>
          <div class="cart-qty">
            <button type="button" data-action="dec" aria-label="Diminuir">−</button>
            <span>${item.qty}</span>
            <button type="button" data-action="inc" aria-label="Aumentar">+</button>
          </div>
        </div>
        <button type="button" class="cart-item-remove" data-action="remove" aria-label="Remover">✕</button>
      </div>`
      )
      .join("");

    body.querySelectorAll(".cart-item").forEach((row) => {
      const id = row.dataset.id;
      row.querySelector('[data-action="inc"]')?.addEventListener("click", () => {
        const item = this.get().find((i) => i.id === id);
        if (item) this.setQty(id, item.qty + 1);
      });
      row.querySelector('[data-action="dec"]')?.addEventListener("click", () => {
        const item = this.get().find((i) => i.id === id);
        if (item) this.setQty(id, item.qty - 1);
      });
      row.querySelector('[data-action="remove"]')?.addEventListener("click", () => this.remove(id));
    });
  },

  buildWhatsAppMessage(extra = {}) {
    const items = this.get();
    let msg = "Olá QL REDES! 👋\n\nGostaria de solicitar um *orçamento*";
    if (extra.name) msg += `\n\n*Nome:* ${extra.name}`;
    if (extra.phone) msg += `\n*Telefone:* ${extra.phone}`;
    if (extra.service) msg += `\n*Serviço:* ${extra.service}`;

    if (items.length) {
      msg += "\n\n*Produtos / equipamentos de interesse:*\n";
      items.forEach((item, i) => {
        const price =
          item.price != null
            ? ` (ref. ${item.price.toLocaleString("pt-MZ")} MT)`
            : item.priceLabel
              ? ` (${item.priceLabel})`
              : "";
        msg += `${i + 1}. ${item.name} × ${item.qty}${price}\n`;
      });
    }

    if (extra.message) msg += `\n*Mensagem:*\n${extra.message}\n`;
    msg += "\nAguardo o vosso contacto. Obrigado!";
    return msg;
  },

  sendQuote(extra = {}) {
    const items = this.get();
    if (!items.length && !extra.message && !extra.service) {
      this.toast("Adicione produtos ou preencha a mensagem");
      return;
    }
    const text = encodeURIComponent(this.buildWhatsAppMessage(extra));
    window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${text}`, "_blank");
  }
};

function initCartUI() {
  // Drawer shell if missing
  if (!document.getElementById("cart-drawer")) {
    const overlay = document.createElement("div");
    overlay.id = "cart-overlay";
    overlay.className = "cart-overlay";
    overlay.addEventListener("click", () => Cart.close());

    const drawer = document.createElement("aside");
    drawer.id = "cart-drawer";
    drawer.className = "cart-drawer";
    drawer.setAttribute("aria-label", "Carrinho de orçamento");
    drawer.innerHTML = `
      <div class="cart-header">
        <h3>Pedido de Orçamento</h3>
        <button type="button" class="cart-close" id="cart-close" aria-label="Fechar">✕</button>
      </div>
      <div class="cart-body" id="cart-body"></div>
      <div class="cart-footer">
        <p class="hint">Não é uma loja online — enviaremos um orçamento personalizado sem compromisso.</p>
        <button type="button" class="btn btn-whatsapp btn-block" id="cart-send-wa">
          Enviar orçamento via WhatsApp
        </button>
        <button type="button" class="btn btn-outline btn-block btn-sm" id="cart-clear">Limpar lista</button>
      </div>`;

    document.body.appendChild(overlay);
    document.body.appendChild(drawer);

    document.getElementById("cart-close")?.addEventListener("click", () => Cart.close());
    document.getElementById("cart-send-wa")?.addEventListener("click", () => Cart.sendQuote());
    document.getElementById("cart-clear")?.addEventListener("click", () => {
      Cart.clear();
      Cart.toast("Lista limpa");
    });
  }

  document.querySelectorAll("[data-open-cart]").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      Cart.open();
    });
  });

  Cart.updateUI();
}

document.addEventListener("DOMContentLoaded", initCartUI);
