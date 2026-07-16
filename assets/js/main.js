/* QL REDES — Bootstrap UI, parallax, reveal, gallery */
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

function logoImg(extraClass = "") {
  const cls = extraClass ? `logo-img ${extraClass}` : "logo-img";
  return `<img src="assets/images/logo.png" alt="QL REDES — Tecnologias & Soluções Informáticas" class="${cls}" width="220" height="56" decoding="async">`;
}

function currentPage() {
  const path = window.location.pathname.replace(/\\/g, "/");
  const file = path.split("/").pop() || "index.html";
  return file === "" ? "index.html" : file;
}

function navItem(href, label, current) {
  const active = current === href ? " active" : "";
  return `<li class="nav-item"><a class="nav-link${active}" href="${href}">${label}</a></li>`;
}

function injectHeader() {
  const header = document.getElementById("site-header");
  if (!header) return;
  const c = currentPage();

  header.className = "navbar navbar-expand-lg site-navbar fixed-top";
  header.innerHTML = `
    <div class="container">
      <a class="navbar-brand" href="index.html" aria-label="QL REDES — início">${logoImg()}</a>
      <div class="d-flex align-items-center gap-2 order-lg-3">
        <button type="button" class="cart-btn" data-open-cart aria-label="Pedido de orçamento">
          <i class="bi bi-bag"></i>
          <span class="cart-count" data-count="0"></span>
        </button>
        <a href="${waLink("Olá QL REDES! Gostaria de pedir um orçamento gratuito.")}" class="btn btn-whatsapp btn-sm d-none d-md-inline-flex" target="_blank" rel="noopener">
          <i class="bi bi-whatsapp me-1"></i> WhatsApp
        </a>
        <button class="navbar-toggler border-0 shadow-none" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav" aria-controls="mainNav" aria-expanded="false" aria-label="Menu">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>
      <div class="collapse navbar-collapse order-lg-2" id="mainNav">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0 align-items-lg-center gap-lg-1">
          ${navItem("index.html", "Início", c)}
          ${navItem("sobre.html", "Sobre", c)}
          ${navItem("servicos.html", "Serviços", c)}
          ${navItem("portfolio.html", "Portfólio", c)}
          ${navItem("produtos.html", "Produtos", c)}
          ${navItem("blog.html", "Blog", c)}
          ${navItem("contacto.html", "Contacto", c)}
          <li class="nav-item d-lg-none mt-2">
            <a class="btn btn-whatsapp w-100" href="${waLink("Olá QL REDES! Gostaria de pedir um orçamento gratuito.")}" target="_blank" rel="noopener">
              <i class="bi bi-whatsapp me-1"></i> Pedir Orçamento
            </a>
          </li>
        </ul>
      </div>
    </div>`;

  const onScroll = () => header.classList.toggle("is-scrolled", window.scrollY > 12);
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
}

function injectFooter() {
  const footer = document.getElementById("site-footer");
  if (!footer) return;
  const year = new Date().getFullYear();

  footer.className = "site-footer";
  footer.innerHTML = `
    <div class="container">
      <div class="row g-4">
        <div class="col-lg-4 col-md-6">
          <a href="index.html" class="d-inline-block mb-3">${logoImg("logo-img-footer")}</a>
          <p class="mb-3 pe-lg-3">Empresa moçambicana em Maputo especializada em redes informáticas, electricidade e segurança electrónica.</p>
          <div class="footer-social">
            <a href="${SITE.facebook}" target="_blank" rel="noopener" aria-label="Facebook"><i class="bi bi-facebook"></i></a>
            <a href="${SITE.instagram}" target="_blank" rel="noopener" aria-label="Instagram"><i class="bi bi-instagram"></i></a>
            <a href="${waLink()}" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="bi bi-whatsapp"></i></a>
          </div>
        </div>
        <div class="col-6 col-md-3 col-lg-2">
          <h6>Navegação</h6>
          <a href="index.html">Início</a>
          <a href="sobre.html">Sobre Nós</a>
          <a href="servicos.html">Serviços</a>
          <a href="portfolio.html">Portfólio</a>
          <a href="produtos.html">Produtos</a>
          <a href="blog.html">Blog</a>
        </div>
        <div class="col-6 col-md-3 col-lg-3">
          <h6>Serviços</h6>
          <a href="servicos.html#redes">Redes Informáticas</a>
          <a href="servicos.html#electricidade">Electricidade</a>
          <a href="servicos.html#seguranca">Segurança Electrónica</a>
          <a href="servicos.html#portoes">Portões &amp; Pérgolas</a>
          <a href="produtos.html">Equipamentos</a>
          <a href="faq.html">FAQ</a>
        </div>
        <div class="col-md-6 col-lg-3">
          <h6>Contactos</h6>
          <p class="mb-2 small"><i class="bi bi-geo-alt me-2 text-primary"></i>${SITE.address}</p>
          <p class="mb-2 small"><i class="bi bi-telephone me-2 text-primary"></i><a href="tel:+258848426310" class="d-inline p-0">${SITE.phone}</a></p>
          <p class="mb-2 small"><i class="bi bi-chat-dots me-2 text-primary"></i><a href="tel:+258872497969" class="d-inline p-0">${SITE.phone2}</a></p>
          <p class="mb-0 small"><i class="bi bi-envelope me-2 text-primary"></i><a href="mailto:${SITE.email}" class="d-inline p-0">${SITE.email}</a></p>
        </div>
      </div>
      <div class="footer-bottom d-flex flex-wrap justify-content-between gap-2">
        <span>© ${year} QL REDES / QL Group. Todos os direitos reservados.</span>
        <span><a href="privacidade.html" class="d-inline p-0">Privacidade</a> · <a href="contacto.html" class="d-inline p-0">Contacto</a></span>
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
  a.innerHTML = `<i class="bi bi-whatsapp"></i>`;
  document.body.appendChild(a);
}

/* Parallax backgrounds */
function initParallax() {
  const layers = document.querySelectorAll("[data-parallax]");
  if (!layers.length) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  let ticking = false;
  const update = () => {
    const scrollY = window.scrollY || window.pageYOffset;
    layers.forEach((el) => {
      const speed = parseFloat(el.dataset.parallax) || 0.25;
      const rect = el.parentElement?.getBoundingClientRect();
      if (!rect) return;
      // only animate when near viewport
      if (rect.bottom < -100 || rect.top > window.innerHeight + 100) return;
      const offset = (scrollY - (el.parentElement.offsetTop - window.innerHeight * 0.3)) * speed * 0.35;
      el.style.transform = `translate3d(0, ${offset}px, 0) scale(1.12)`;
    });
    ticking = false;
  };

  window.addEventListener(
    "scroll",
    () => {
      if (!ticking) {
        requestAnimationFrame(update);
        ticking = true;
      }
    },
    { passive: true }
  );
  update();
}

/* Scroll reveal */
function initReveal() {
  const els = document.querySelectorAll(".reveal");
  if (!els.length) return;
  if (!("IntersectionObserver" in window)) {
    els.forEach((el) => el.classList.add("is-visible"));
    return;
  }
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
  );
  els.forEach((el) => io.observe(el));
}

/* Portfolio filters + Bootstrap modal lightbox */
function initGallery() {
  const grid = document.getElementById("gallery-grid");
  const items = document.querySelectorAll(".gallery-item");
  if (!items.length) return;

  document.querySelectorAll("[data-filter]").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll("[data-filter]").forEach((b) => {
        b.classList.remove("active", "btn-primary");
        b.classList.add("btn-outline-primary");
      });
      btn.classList.add("active", "btn-primary");
      btn.classList.remove("btn-outline-primary");
      const cat = btn.dataset.filter;
      const scope = grid || document;
      scope.querySelectorAll(".gallery-item").forEach((item) => {
        const show = cat === "all" || item.dataset.category === cat;
        item.classList.toggle("hidden", !show);
        item.closest("[class*='col']")?.classList.toggle("d-none", !show);
      });
    });
  });

  let modalEl = document.getElementById("galleryModal");
  if (!modalEl) {
    modalEl = document.createElement("div");
    modalEl.id = "galleryModal";
    modalEl.className = "modal fade";
    modalEl.tabIndex = -1;
    modalEl.setAttribute("aria-hidden", "true");
    modalEl.innerHTML = `
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content bg-dark border-0">
          <div class="modal-header border-0">
            <h5 class="modal-title text-white fs-6" id="galleryModalLabel"></h5>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Fechar"></button>
          </div>
          <div class="modal-body p-0">
            <img src="" alt="" class="w-100" id="galleryModalImg" style="max-height:80vh;object-fit:contain">
          </div>
        </div>
      </div>`;
    document.body.appendChild(modalEl);
  }

  const modal = typeof bootstrap !== "undefined" ? new bootstrap.Modal(modalEl) : null;
  const imgEl = document.getElementById("galleryModalImg");
  const titleEl = document.getElementById("galleryModalLabel");

  items.forEach((item) => {
    item.addEventListener("click", () => {
      const img = item.querySelector("img");
      const label = item.querySelector(".gallery-overlay span")?.textContent || img?.alt || "";
      if (!img) return;
      imgEl.src = img.src;
      imgEl.alt = img.alt || label;
      titleEl.textContent = label;
      modal?.show();
    });
  });
}

/* Products page — Bootstrap cards */
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
      const qOk = !q || p.name.toLowerCase().includes(q) || p.description.toLowerCase().includes(q);
      return catOk && qOk;
    });

    if (!list.length) {
      grid.innerHTML = `<div class="col-12 text-center text-muted py-5">Nenhum produto encontrado.</div>`;
      return;
    }

    grid.innerHTML = list
      .map(
        (p, i) => `
      <div class="col-sm-6 col-lg-4 col-xl-3 reveal reveal-delay-${(i % 4) + 1}">
        <article class="card ql-card product-card h-100">
          <div class="card-img-wrap position-relative">
            <img src="${p.image}" class="card-img-top" alt="${p.name}" loading="lazy" onerror="this.src='assets/images/download%20(1).png'">
            <span class="cat-tag">${PRODUCT_CATEGORIES[p.category] || p.category}</span>
          </div>
          <div class="card-body d-flex flex-column">
            <h3 class="h6 card-title text-navy">${p.name}</h3>
            <p class="card-text text-muted small flex-grow-1">${p.description}</p>
            <div class="d-flex justify-content-between align-items-end gap-2 mb-3">
              <div class="price">${formatPrice(p)}${p.price != null ? "<small>preço de referência</small>" : ""}</div>
            </div>
            <button type="button" class="btn btn-primary btn-sm w-100" data-add="${p.id}">
              <i class="bi bi-plus-lg me-1"></i> Adicionar ao orçamento
            </button>
          </div>
        </article>
      </div>`
      )
      .join("");

    grid.querySelectorAll("[data-add]").forEach((btn) => {
      btn.addEventListener("click", () => {
        if (typeof Cart !== "undefined") Cart.add(btn.dataset.add);
      });
    });
    initReveal();
  }

  if (cats && typeof PRODUCT_CATEGORIES !== "undefined") {
    cats.innerHTML = Object.entries(PRODUCT_CATEGORIES)
      .map(
        ([key, label], idx) =>
          `<button type="button" class="btn btn-sm ${key === "all" ? "btn-primary active" : "btn-outline-primary"}" data-cat="${key}">${label}</button>`
      )
      .join("");
    cats.querySelectorAll("[data-cat]").forEach((btn) => {
      btn.addEventListener("click", () => {
        cats.querySelectorAll("[data-cat]").forEach((b) => {
          b.classList.remove("active", "btn-primary");
          b.classList.add("btn-outline-primary");
        });
        btn.classList.add("active", "btn-primary");
        btn.classList.remove("btn-outline-primary");
        activeCat = btn.dataset.cat;
        render();
      });
    });
  }

  search?.addEventListener("input", render);
  render();
}

function initContactForm() {
  const form = document.getElementById("contact-form");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    if (!form.checkValidity()) {
      e.stopPropagation();
      form.classList.add("was-validated");
      return;
    }
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
  initParallax();
  initReveal();
  initGallery();
  initProductsPage();
  initContactForm();
  if (typeof Cart !== "undefined") Cart.updateUI();
});
