/* QL REDES — main interactions */
const SITE = {
  phone: "+258 84 842 6310",
  phone2: "+258 87 249 7969",
  whatsapp: "258848426310",
  email: "qlredes@gmail.com",
  address: "Rua Irmãos Rubbi 2250, Maputo",
  facebook: "https://www.facebook.com/joaquimlleao",
  instagram: "https://www.instagram.com/ql_group_/"
};

function waLink(text) {
  const t = text ? `?text=${encodeURIComponent(text)}` : "";
  return `https://wa.me/${SITE.whatsapp}${t}`;
}

function logoSVG() {
  return `<svg class="logo-mark" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <rect width="48" height="48" rx="12" fill="#0B1F3A"/>
    <circle cx="24" cy="24" r="8" stroke="#0B9ED9" stroke-width="2.5"/>
    <circle cx="24" cy="24" r="3" fill="#0B9ED9"/>
    <circle cx="12" cy="14" r="2.5" fill="#0B9ED9"/>
    <circle cx="36" cy="14" r="2.5" fill="#0B9ED9"/>
    <circle cx="12" cy="34" r="2.5" fill="#0B9ED9"/>
    <circle cx="36" cy="34" r="2.5" fill="#0B9ED9"/>
    <path d="M14 15.5L19 20M34 15.5L29 20M14 32.5L19 28M34 32.5L29 28" stroke="#0B9ED9" stroke-width="1.5" stroke-linecap="round"/>
  </svg>`;
}

function currentPage() {
  const path = window.location.pathname.replace(/\\/g, "/");
  const file = path.split("/").pop() || "index.html";
  return file === "" ? "index.html" : file;
}

function navLink(href, label, current) {
  const active = current === href ? " active" : "";
  return `<a href="${href}" class="${active.trim()}">${label}</a>`;
}

function injectHeader() {
  const header = document.getElementById("site-header");
  if (!header) return;
  const c = currentPage();

  header.innerHTML = `
    <div class="container header-inner">
      <a href="index.html" class="logo" aria-label="QL REDES — início">
        ${logoSVG()}
        <span class="logo-text">
          <strong>QL<span>REDES</span></strong>
          <small>Tecnologia &amp; Soluções</small>
        </span>
      </a>
      <nav class="nav-desktop" aria-label="Principal">
        ${navLink("index.html", "Início", c)}
        ${navLink("sobre.html", "Sobre", c)}
        ${navLink("servicos.html", "Serviços", c)}
        ${navLink("portfolio.html", "Portfólio", c)}
        ${navLink("produtos.html", "Produtos", c)}
        ${navLink("blog.html", "Blog", c)}
        ${navLink("contacto.html", "Contacto", c)}
      </nav>
      <div class="header-actions">
        <button type="button" class="cart-btn" data-open-cart aria-label="Pedido de orçamento">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6h15l-1.5 9h-12z"/><circle cx="9" cy="20" r="1"/><circle cx="18" cy="20" r="1"/><path d="M6 6L5 3H2"/></svg>
          <span class="cart-count" data-count="0"></span>
        </button>
        <a href="${waLink("Olá QL REDES! Gostaria de pedir um orçamento gratuito.")}" class="btn btn-whatsapp btn-sm btn-cta-desktop" target="_blank" rel="noopener">WhatsApp</a>
        <button type="button" class="menu-toggle" id="menu-toggle" aria-label="Abrir menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
    <nav class="nav-mobile" id="nav-mobile" aria-label="Menu móvel">
      ${navLink("index.html", "Início", c)}
      ${navLink("sobre.html", "Sobre Nós", c)}
      ${navLink("servicos.html", "Serviços", c)}
      ${navLink("portfolio.html", "Portfólio", c)}
      ${navLink("produtos.html", "Produtos / Orçamento", c)}
      ${navLink("blog.html", "Blog", c)}
      ${navLink("faq.html", "FAQ", c)}
      ${navLink("contacto.html", "Contacto", c)}
      <a href="${waLink("Olá QL REDES! Gostaria de pedir um orçamento gratuito.")}" class="btn btn-whatsapp" target="_blank" rel="noopener">Pedir Orçamento WhatsApp</a>
    </nav>`;

  const toggle = document.getElementById("menu-toggle");
  const mobile = document.getElementById("nav-mobile");
  toggle?.addEventListener("click", () => {
    const open = mobile.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.style.overflow = open ? "hidden" : "";
  });
  mobile?.querySelectorAll("a").forEach((a) => {
    a.addEventListener("click", () => {
      mobile.classList.remove("open");
      toggle?.setAttribute("aria-expanded", "false");
      document.body.style.overflow = "";
    });
  });
}

function injectFooter() {
  const footer = document.getElementById("site-footer");
  if (!footer) return;
  const year = new Date().getFullYear();

  footer.innerHTML = `
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="logo">
            ${logoSVG()}
            <span class="logo-text">
              <strong>QL<span style="color:var(--primary)">REDES</span></strong>
              <small>Tecnologia &amp; Soluções</small>
            </span>
          </a>
          <p>Empresa moçambicana em Maputo especializada em redes informáticas, electricidade e segurança electrónica.</p>
          <div class="footer-social">
            <a href="${SITE.facebook}" target="_blank" rel="noopener" aria-label="Facebook">f</a>
            <a href="${SITE.instagram}" target="_blank" rel="noopener" aria-label="Instagram">IG</a>
            <a href="${waLink()}" target="_blank" rel="noopener" aria-label="WhatsApp">WA</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Navegação</h4>
          <a href="index.html">Início</a>
          <a href="sobre.html">Sobre Nós</a>
          <a href="servicos.html">Serviços</a>
          <a href="portfolio.html">Portfólio</a>
          <a href="produtos.html">Produtos</a>
          <a href="blog.html">Blog</a>
        </div>
        <div class="footer-col">
          <h4>Serviços</h4>
          <a href="servicos.html#redes">Redes Informáticas</a>
          <a href="servicos.html#electricidade">Electricidade</a>
          <a href="servicos.html#seguranca">Segurança Electrónica</a>
          <a href="servicos.html#portoes">Portões &amp; Pérgolas</a>
          <a href="produtos.html">Equipamentos</a>
          <a href="faq.html">Perguntas Frequentes</a>
        </div>
        <div class="footer-col">
          <h4>Contactos</h4>
          <div class="f-contact"><span>📍</span><span>${SITE.address}</span></div>
          <div class="f-contact"><span>📞</span><a href="tel:+258848426310">${SITE.phone}</a></div>
          <div class="f-contact"><span>💬</span><a href="tel:+258872497969">${SITE.phone2}</a></div>
          <div class="f-contact"><span>✉️</span><a href="mailto:${SITE.email}">${SITE.email}</a></div>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© ${year} QL REDES / QL Group. Todos os direitos reservados.</span>
        <span>
          <a href="privacidade.html">Privacidade</a> ·
          <a href="contacto.html">Contacto</a>
        </span>
      </div>
    </div>`;
}

function injectFab() {
  if (document.querySelector(".fab-whatsapp")) return;
  const a = document.createElement("a");
  a.href = waLink("Olá QL REDES! Vim do site e gostaria de mais informações.");
  a.className = "fab-whatsapp";
  a.target = "_blank";
  a.rel = "noopener";
  a.setAttribute("aria-label", "Contactar no WhatsApp");
  a.innerHTML = `<svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.85 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>`;
  document.body.appendChild(a);
}

/* Portfolio gallery filter + lightbox */
function initGallery() {
  const grid = document.getElementById("gallery-grid");
  if (!grid) return;

  document.querySelectorAll(".filter-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".filter-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      const cat = btn.dataset.filter;
      grid.querySelectorAll(".gallery-item").forEach((item) => {
        const show = cat === "all" || item.dataset.category === cat;
        item.classList.toggle("hidden", !show);
      });
    });
  });

  // Lightbox
  let lb = document.getElementById("lightbox");
  if (!lb) {
    lb = document.createElement("div");
    lb.id = "lightbox";
    lb.className = "lightbox";
    lb.innerHTML = `<button type="button" class="lightbox-close" aria-label="Fechar">✕</button><img src="" alt="">`;
    document.body.appendChild(lb);
    lb.querySelector(".lightbox-close").addEventListener("click", () => lb.classList.remove("open"));
    lb.addEventListener("click", (e) => {
      if (e.target === lb) lb.classList.remove("open");
    });
  }

  grid.querySelectorAll(".gallery-item").forEach((item) => {
    item.addEventListener("click", () => {
      const img = item.querySelector("img");
      if (!img) return;
      lb.querySelector("img").src = img.src;
      lb.querySelector("img").alt = img.alt || "";
      lb.classList.add("open");
    });
  });
}

/* Products page */
function initProductsPage() {
  const grid = document.getElementById("product-grid");
  if (!grid || typeof PRODUCTS === "undefined") return;

  const search = document.getElementById("product-search");
  const cats = document.getElementById("product-cats");
  let activeCat = "all";

  function render() {
    const q = (search?.value || "").toLowerCase().trim();
    const list = PRODUCTS.filter((p) => {
      const catOk = activeCat === "all" || p.category === activeCat;
      const qOk =
        !q ||
        p.name.toLowerCase().includes(q) ||
        p.description.toLowerCase().includes(q);
      return catOk && qOk;
    });

    if (!list.length) {
      grid.innerHTML = `<p class="text-center" style="grid-column:1/-1;color:var(--text-muted);padding:2rem">Nenhum produto encontrado.</p>`;
      return;
    }

    grid.innerHTML = list
      .map(
        (p) => `
      <article class="product-card" data-id="${p.id}">
        <div class="img-wrap">
          <img src="${p.image}" alt="${p.name}" loading="lazy" onerror="this.src='assets/images/download (1).png'">
          <span class="cat-tag">${PRODUCT_CATEGORIES[p.category] || p.category}</span>
        </div>
        <div class="body">
          <h3>${p.name}</h3>
          <p class="desc">${p.description}</p>
          <div class="meta">
            <div class="price">${formatPrice(p)}${p.price != null ? "<small>preço de referência</small>" : ""}</div>
          </div>
          <button type="button" class="btn btn-primary btn-block btn-sm" data-add="${p.id}">
            Adicionar ao orçamento
          </button>
        </div>
      </article>`
      )
      .join("");

    grid.querySelectorAll("[data-add]").forEach((btn) => {
      btn.addEventListener("click", () => {
        if (typeof Cart !== "undefined") Cart.add(btn.dataset.add);
      });
    });
  }

  if (cats && typeof PRODUCT_CATEGORIES !== "undefined") {
    cats.innerHTML = Object.entries(PRODUCT_CATEGORIES)
      .map(
        ([key, label]) =>
          `<button type="button" class="filter-btn${key === "all" ? " active" : ""}" data-cat="${key}">${label}</button>`
      )
      .join("");
    cats.querySelectorAll(".filter-btn").forEach((btn) => {
      btn.addEventListener("click", () => {
        cats.querySelectorAll(".filter-btn").forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        activeCat = btn.dataset.cat;
        render();
      });
    });
  }

  search?.addEventListener("input", render);
  render();
}

/* Contact form → WhatsApp */
function initContactForm() {
  const form = document.getElementById("contact-form");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const data = new FormData(form);
    const payload = {
      name: data.get("name") || "",
      phone: data.get("phone") || "",
      service: data.get("service") || "",
      message: data.get("message") || ""
    };

    if (typeof Cart !== "undefined") {
      Cart.sendQuote(payload);
    } else {
      const msg = `Olá QL REDES!\n\n*Nome:* ${payload.name}\n*Telefone:* ${payload.phone}\n*Serviço:* ${payload.service}\n\n*Mensagem:*\n${payload.message}`;
      window.open(waLink(msg), "_blank");
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  injectHeader();
  injectFooter();
  injectFab();
  initGallery();
  initProductsPage();
  initContactForm();
  if (typeof Cart !== "undefined") Cart.updateUI();
});
