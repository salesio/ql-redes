# -*- coding: utf-8 -*-
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]

HEAD = """<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
  <link rel="icon" href="assets/images/logo.png">
</head>
<body>
  <header id="site-header"></header>
  <main>
"""

FOOT = """
  </main>
  <footer id="site-footer"></footer>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  <script src="assets/js/products.js"></script>
  <script src="assets/js/cart.js"></script>
  <script src="assets/js/main.js"></script>
</body>
</html>
"""

WA = "https://wa.me/258848426310?text=Ol%C3%A1%20QL%20REDES!%20Gostaria%20de%20pedir%20um%20or%C3%A7amento%20gratuito."


def write(name, title, description, body):
    path = ROOT / name
    path.write_text(HEAD.format(title=title, description=description) + body + FOOT, encoding="utf-8", newline="\n")
    print("wrote", name)


# ---------- SERVICOS ----------
services = [
    {
        "id": "redes",
        "label": "01 · Infraestrutura TI",
        "title": "Redes Informáticas",
        "desc": "Projectamos e implementamos redes fiáveis para residências e empresas — desde o cabeamento até à configuração de Wi-Fi e servidores.",
        "items": [
            "Cabeamento estruturado (Cat6 e superiores)",
            "Wi-Fi residencial e empresarial de alta cobertura",
            "Configuração de routers, switches e pontos de acesso",
            "Servidores, partilha de ficheiros e backup básico",
            "Manutenção, diagnóstico e optimização de rede",
            "Consultoria TI e integração com sistemas de segurança",
        ],
        "price": "Preço: sob consulta",
        "wa": "Olá! Quero orçamento de redes informáticas.",
        "img": "assets/images/488415479_17893244067207634_6754080003431670941_n.jpg",
        "reverse": False,
    },
    {
        "id": "electricidade",
        "label": "02 · Energia",
        "title": "Electricidade",
        "desc": "Instalações eléctricas seguras e bem dimensionadas, alinhadas com as necessidades de iluminação, tomadas e automação do seu espaço.",
        "items": [
            "Instalações eléctricas novas e reabilitações",
            "Quadros eléctricos e protecções",
            "Iluminação interior e exterior",
            "Preparação eléctrica para CCTV, portões e automação",
            "Manutenção preventiva e correcção de avarias",
        ],
        "price": "Preço: sob consulta",
        "wa": "Olá! Quero orçamento de electricidade.",
        "img": "assets/images/465740896_17874100107207634_5495886275657190308_n.jpg",
        "reverse": True,
    },
    {
        "id": "seguranca",
        "label": "03 · Protecção",
        "title": "Segurança Electrónica",
        "desc": "Proteja a sua casa ou negócio com videovigilância, alarmes e controlo de acesso — com instalação profissional e orientação no uso.",
        "items": [
            "CCTV com ou sem fio (incluindo câmaras solares Wi-Fi)",
            "Sistemas de alarme residencial e comercial",
            "Controlo de acesso (cartão, código, biometria)",
            "Fechaduras magnéticas e electrónicas",
            "Monitorização remota via aplicação no telemóvel",
            "Soluções para condomínios, lojas e escritórios",
        ],
        "price": "Ex.: câmara solar Wi-Fi a partir de 8.300 MT · kits sob consulta",
        "wa": "Olá! Quero orçamento de CCTV / segurança.",
        "img": "assets/images/440984849_836565345161614_2712887158395915178_n.jpg",
        "reverse": False,
        "extra": True,
    },
    {
        "id": "portoes",
        "label": "04 · Acesso & Exterior",
        "title": "Portões Automáticos, Pérgolas & Metal",
        "desc": "Fabrico, fornecimento e instalação de portões automáticos, motores, pérgolas bioclimáticas, estores e estruturas metálicas sob medida.",
        "items": [
            "Portões deslizantes e basculantes (design personalizado)",
            "Motorização, comandos e sensores de segurança",
            "Pérgolas bioclimáticas e cobertura exterior",
            "Persianas / estores metálicos",
            "Guarda-corpos e trabalhos de metalurgia",
            "Entrega e instalação em Maputo",
        ],
        "price": "Preço: sob consulta (conforme medidas e design)",
        "wa": "Olá! Quero orçamento de portão automático / pérgola.",
        "img": "assets/images/download%20(1).png",
        "reverse": True,
        "portfolio": True,
    },
    {
        "id": "outros",
        "label": "05 · Extra",
        "title": "Fornecimento & Consultoria",
        "desc": "Além da instalação, fornecemos equipamentos e aconselhamos a melhor solução para o seu orçamento e nível de segurança desejado.",
        "items": [
            "Fornecimento de equipamentos de rede e segurança",
            "Consultoria técnica e dimensionamento de projectos",
            "Integrações entre sistemas (rede + CCTV + acesso)",
            "Manutenção e suporte após instalação",
        ],
        "price": "",
        "wa": "",
        "img": "assets/images/465706527_17874100092207634_6894705478359609218_n.jpg",
        "reverse": False,
        "products": True,
    },
]

svc_blocks = []
for s in services:
    items = "".join(f'<li><i class="bi bi-check2-circle"></i><span>{x}</span></li>' for x in s["items"])
    order_text = "order-lg-2" if s["reverse"] else ""
    order_img = "order-lg-1" if s["reverse"] else ""
    btns = ""
    if s.get("products"):
        btns = '<a href="produtos.html" class="btn btn-primary">Explorar produtos</a>'
    elif s.get("extra"):
        btns = f'''<div class="d-flex flex-wrap gap-2">
              <a href="https://wa.me/258848426310?text={quote(s["wa"])}" class="btn btn-primary" target="_blank" rel="noopener">Pedir orçamento</a>
              <a href="produtos.html" class="btn btn-outline-primary">Ver equipamentos</a>
            </div>'''
    elif s.get("portfolio"):
        btns = f'''<div class="d-flex flex-wrap gap-2">
              <a href="https://wa.me/258848426310?text={quote(s["wa"])}" class="btn btn-primary" target="_blank" rel="noopener">Pedir orçamento</a>
              <a href="portfolio.html" class="btn btn-outline-primary">Ver projectos</a>
            </div>'''
    else:
        btns = f'<a href="https://wa.me/258848426310?text={quote(s["wa"])}" class="btn btn-primary" target="_blank" rel="noopener">Pedir orçamento</a>'
    price = f'<p class="fw-bold text-primary mb-3">{s["price"]}</p>' if s["price"] else ""
    svc_blocks.append(f'''
        <article class="service-detail" id="{s["id"]}">
          <div class="row g-4 g-lg-5 align-items-center">
            <div class="col-lg-6 {order_text} reveal">
              <span class="section-label">{s["label"]}</span>
              <h2 class="section-title">{s["title"]}</h2>
              <p class="text-muted">{s["desc"]}</p>
              <ul class="check-list">{items}</ul>
              {price}
              {btns}
            </div>
            <div class="col-lg-6 {order_img} reveal reveal-delay-2">
              <div class="visual-frame"><img src="{s["img"]}" alt="{s["title"]}" loading="lazy"></div>
            </div>
          </div>
        </article>''')

write(
    "servicos.html",
    "Serviços | Redes, Electricidade, CCTV e Portões — QL REDES Maputo",
    "Serviços QL REDES em Maputo: redes informáticas, Wi-Fi, electricidade, CCTV, alarmes, controlo de acesso, portões automáticos e pérgolas.",
    f"""
    <section class="page-hero">
      <div class="parallax-bg" data-parallax="0.2" style="background-image:url('assets/images/download.png')"></div>
      <div class="parallax-overlay"></div>
      <div class="container">
        <nav aria-label="breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Início</a></li><li class="breadcrumb-item active">Serviços</li></ol></nav>
        <h1 class="display-5 fw-bold">Os nossos serviços</h1>
        <p>Soluções técnicas completas para casas, empresas e espaços comerciais em Maputo. Preços sob consulta.</p>
      </div>
    </section>
    <section class="section"><div class="container">{''.join(svc_blocks)}</div></section>
    <section class="cta-band">
      <div class="parallax-overlay"></div>
      <div class="container reveal">
        <h2 class="display-6 mb-3">Não sabe por onde começar?</h2>
        <p class="mb-4">Descreva o seu projecto no WhatsApp — ajudamos a escolher a solução certa.</p>
        <a href="{WA}" class="btn btn-light btn-lg me-2" target="_blank" rel="noopener">Falar no WhatsApp</a>
        <a href="contacto.html" class="btn btn-outline-light btn-lg">Formulário</a>
      </div>
    </section>
""",
)

# ---------- PORTFOLIO ----------
gallery = [
    ("portoes", "assets/images/download%20(1).png", "Portão automático · lâminas"),
    ("portoes", "assets/images/download.png", "Portão painel fechado"),
    ("portoes", "assets/images/489694084_1071761274975352_932475664368770287_n.jpg", "Portão design geométrico"),
    ("portoes", "assets/images/465706527_17874100092207634_6894705478359609218_n.jpg", "Estruturas de portão"),
    ("obra", "assets/images/595662529_1269319441886200_6300626288040576835_n.jpg", "Entrega em Maputo"),
    ("estrutura", "assets/images/488411407_17893244058207634_6765023642434450324_n.jpg", "Montagem de estrutura"),
    ("estrutura", "assets/images/488415479_17893244067207634_6754080003431670941_n.jpg", "Estrutura em obra"),
    ("estrutura", "assets/images/488461347_17893244079207634_6514942602438994313_n.jpg", "Projecto metálico"),
    ("exterior", "assets/images/675813361_1370522625099214_4137454648823396842_n.jpg", "Pérgola bioclimática"),
    ("exterior", "assets/images/537672052_17909713176207634_3423635583355580655_n.jpg", "Estore metálico"),
    ("exterior", "assets/images/537854418_17909713164207634_5212236259825119144_n.jpg", "Persiana · detalhe"),
    ("exterior", "assets/images/623455006_1303841571767320_6077619064415629963_n.jpg", "Guarda-corpo"),
    ("seguranca", "assets/images/440984849_836565345161614_2712887158395915178_n.jpg", "CCTV solar Wi-Fi"),
    ("seguranca", "assets/images/488255805_1067932538691559_5812239850081575222_n.jpg", "Fechadura magnética"),
    ("obra", "assets/images/489916806_1073899878094825_4968900551692884290_n.jpg", "Trabalho de campo"),
    ("obra", "assets/images/489621144_1073068654844614_6216180250187644097_n.jpg", "Instalação em cliente"),
    ("portoes", "assets/images/489381118_1073068441511302_9083164109398043210_n.jpg", "Fabrico de portão"),
    ("obra", "assets/images/490265752_1073068651511281_2369352954484785169_n.jpg", "Obra em curso"),
    ("portoes", "assets/images/490216954_1073899784761501_5346479991168201272_n.jpg", "Detalhe de portão"),
    ("estrutura", "assets/images/488424019_17893356468207634_2783157432092291362_n.jpg", "Estrutura galvanizada"),
    ("obra", "assets/images/515482374_17903605911207634_2851947202045297087_n.jpg", "Projecto concluído"),
    ("exterior", "assets/images/537628200_17909713155207634_5354485175340717890_n.jpg", "Sistema de lâminas"),
    ("portoes", "assets/images/489894644_1073068774844602_8355826637176777445_n.jpg", "Portão instalado"),
    ("obra", "assets/images/597720960_1269319208552890_1106978884828405609_n.jpg", "Logística & entrega"),
]

gal_html = "".join(
    f'''
          <div class="col-6 col-md-4 col-lg-3">
            <div class="gallery-item" data-category="{cat}">
              <img src="{src}" alt="{alt}" loading="lazy">
              <div class="gallery-overlay"><span>{alt}</span></div>
            </div>
          </div>'''
    for cat, src, alt in gallery
)

write(
    "portfolio.html",
    "Portfólio | Projectos QL REDES em Maputo",
    "Galeria de projectos reais da QL REDES: portões automáticos, estruturas metálicas, CCTV, pérgolas e instalações em Maputo.",
    f"""
    <section class="page-hero">
      <div class="parallax-bg" data-parallax="0.2" style="background-image:url('assets/images/download%20(1).png')"></div>
      <div class="parallax-overlay"></div>
      <div class="container">
        <nav aria-label="breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Início</a></li><li class="breadcrumb-item active">Portfólio</li></ol></nav>
        <h1 class="display-5 fw-bold">Portfólio de projectos</h1>
        <p>Trabalhos reais da equipa QL REDES em Maputo — fabrico, entrega e instalação.</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="gallery-filters text-center mb-4 reveal">
          <button type="button" class="btn btn-primary active" data-filter="all">Todos</button>
          <button type="button" class="btn btn-outline-primary" data-filter="portoes">Portões</button>
          <button type="button" class="btn btn-outline-primary" data-filter="estrutura">Estruturas</button>
          <button type="button" class="btn btn-outline-primary" data-filter="seguranca">Segurança</button>
          <button type="button" class="btn btn-outline-primary" data-filter="exterior">Exterior</button>
          <button type="button" class="btn btn-outline-primary" data-filter="obra">Obra / Entrega</button>
        </div>
        <div class="row g-3" id="gallery-grid">{gal_html}</div>
        <p class="text-center text-muted small mt-4">Clique numa imagem para ampliar. Mais projectos no <a href="https://www.facebook.com/joaquimlleao" target="_blank" rel="noopener">Facebook</a> e <a href="https://www.instagram.com/ql_group_/" target="_blank" rel="noopener">Instagram @ql_group_</a>.</p>
      </div>
    </section>
    <section class="cta-band">
      <div class="parallax-overlay"></div>
      <div class="container reveal">
        <h2 class="display-6 mb-3">Quer um projecto como estes?</h2>
        <p class="mb-4">Envie medidas, fotos do local ou ideias — preparamos o orçamento.</p>
        <a href="{WA}" class="btn btn-light btn-lg me-2" target="_blank" rel="noopener">Pedir orçamento</a>
        <a href="produtos.html" class="btn btn-outline-light btn-lg">Ver produtos</a>
      </div>
    </section>
""",
)

# ---------- PRODUTOS ----------
write(
    "produtos.html",
    "Produtos | Equipamentos e Orçamento — QL REDES Maputo",
    "Catálogo QL REDES: CCTV, portões, fechaduras, redes e mais. Adicione ao carrinho e peça orçamento via WhatsApp.",
    f"""
    <section class="page-hero">
      <div class="parallax-bg" data-parallax="0.2" style="background-image:url('assets/images/440984849_836565345161614_2712887158395915178_n.jpg')"></div>
      <div class="parallax-overlay"></div>
      <div class="container">
        <nav aria-label="breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Início</a></li><li class="breadcrumb-item active">Produtos</li></ol></nav>
        <h1 class="display-5 fw-bold">Produtos &amp; equipamentos</h1>
        <p>Explore soluções e monte a sua lista de interesse. No final, envie um pedido de orçamento — sem pagamento online.</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="quote-note d-flex gap-3 align-items-start mb-4 reveal">
          <i class="bi bi-lightbulb fs-4 text-primary"></i>
          <div><strong class="text-primary">Como funciona:</strong> adicione produtos ao pedido de orçamento (ícone da mala). Depois envie a lista pelo WhatsApp. Os valores assinalados são <em>referência</em> e podem variar.</div>
        </div>
        <div class="row g-3 align-items-center mb-4 reveal">
          <div class="col-md-5">
            <div class="input-group">
              <span class="input-group-text bg-white border-end-0"><i class="bi bi-search"></i></span>
              <input type="search" id="product-search" class="form-control border-start-0" placeholder="Pesquisar produtos…" autocomplete="off">
            </div>
          </div>
          <div class="col-md-7"><div class="d-flex flex-wrap gap-2" id="product-cats"></div></div>
        </div>
        <div class="row g-4" id="product-grid"></div>
        <div class="text-center mt-5 reveal">
          <button type="button" class="btn btn-whatsapp btn-lg" data-open-cart><i class="bi bi-bag-check me-1"></i> Ver pedido de orçamento</button>
        </div>
      </div>
    </section>
    <section class="section section-soft">
      <div class="container">
        <div class="text-center mb-5 reveal">
          <span class="section-label">Apoio</span>
          <h2 class="section-title">Precisa de ajuda a escolher?</h2>
        </div>
        <div class="row g-4">
          <div class="col-md-4 reveal"><div class="card ql-card h-100"><div class="card-body p-4"><div class="card-icon"><i class="bi bi-house"></i></div><h3 class="h5">Residencial</h3><p class="text-muted small mb-0">CCTV, alarme, portão e Wi-Fi — dimensionamos conforme o espaço.</p></div></div></div>
          <div class="col-md-4 reveal reveal-delay-2"><div class="card ql-card h-100"><div class="card-body p-4"><div class="card-icon"><i class="bi bi-building"></i></div><h3 class="h5">Empresarial</h3><p class="text-muted small mb-0">Redes, controlo de acesso e vigilância para escritórios e lojas.</p></div></div></div>
          <div class="col-md-4 reveal reveal-delay-3"><div class="card ql-card h-100"><div class="card-body p-4"><div class="card-icon"><i class="bi bi-chat-dots"></i></div><h3 class="h5">Consulta rápida</h3><p class="text-muted small">Envie fotos no WhatsApp e receba orientação antes do orçamento.</p><a href="{WA}" class="fw-semibold" target="_blank" rel="noopener">Falar agora <i class="bi bi-arrow-right"></i></a></div></div></div>
        </div>
      </div>
    </section>
""",
)

# ---------- BLOG ----------
posts = [
    ("cctv-casa", "assets/images/440984849_836565345161614_2712887158395915178_n.jpg", "Segurança · 4 min", "Como proteger a sua casa com CCTV em Maputo", "A videovigilância deixou de ser só para empresas. Com câmaras Wi-Fi e modelos solares, monitorize a entrada e o quintal pelo telemóvel.", "Cubra pontos cegos da entrada; prefira visão noturna; combine com boa iluminação; use detecção de movimento. A QL REDES dimensiona o kit ideal."),
    ("wifi-maputo", "assets/images/488415479_17893244067207634_6754080003431670941_n.jpg", "Redes · 3 min", "Dicas para redes Wi-Fi rápidas em Maputo", "Internet lenta nem sempre é culpa do ISP. Posição do router, interferências e falta de APs degradam a experiência.", "Coloque o router em local central; use mesh em espaços grandes; faça cabeamento quando a estabilidade for crítica."),
    ("manutencao-electrica", "assets/images/465740896_17874100107207634_5495886275657190308_n.jpg", "Electricidade · 3 min", "Manutenção eléctrica preventiva: porquê importa", "Quadros sobrecarregados e ligações soltas são causas comuns de falhas e riscos em residências e comércios.", "Inspeccione o quadro periodicamente; prepare a electricidade para portão motor, CCTV e novas cargas."),
    ("portao-automatico", "assets/images/download%20(1).png", "Portões · 4 min", "Portão automático: o que considerar antes de instalar", "O sucesso depende de medidas correctas, tipo de motor e instalação profissional.", "Avalie deslizante vs basculante, peso, alimentação e sensores. Peça orçamento com fotos e medidas do vão."),
    ("controlo-acesso", "assets/images/488255805_1067932538691559_5812239850081575222_n.jpg", "Acesso · 3 min", "Controlo de acesso: cartão, código ou biometria?", "Escritórios e condomínios ganham com registo de entradas e menos chaves físicas.", "Códigos PIN são simples; cartões para equipas; biometria eleva a segurança. Dimensionamos conforme o fluxo."),
    ("solucoes-integradas", "assets/images/675813361_1370522625099214_4137454648823396842_n.jpg", "QL REDES · 2 min", "Porquê unir redes, luz e segurança no mesmo parceiro", "Quando tudo é planeado em conjunto, evita-se retrabalho e falhas de compatibilidade.", "A QL REDES actua no cruzamento tecnologia + electricidade + segurança — um só contacto em Maputo."),
]

blog_cards = "".join(
    f'''
          <div class="col-md-6 col-lg-4 reveal reveal-delay-{(i%3)+1}">
            <article class="card ql-card h-100" id="{pid}">
              <div class="card-img-wrap"><img src="{img}" class="card-img-top" alt="{title}" loading="lazy"></div>
              <div class="card-body">
                <div class="blog-meta">{meta}</div>
                <h3 class="h5 text-navy">{title}</h3>
                <p class="text-muted small">{lead}</p>
                <p class="text-muted small">{body}</p>
              </div>
            </article>
          </div>'''
    for i, (pid, img, meta, title, lead, body) in enumerate(posts)
)

write(
    "blog.html",
    "Blog | Dicas de Segurança, Redes e Electricidade — QL REDES",
    "Artigos e dicas da QL REDES: CCTV, Wi-Fi em Maputo, manutenção eléctrica e portões automáticos.",
    f"""
    <section class="page-hero">
      <div class="parallax-bg" data-parallax="0.2" style="background-image:url('assets/images/488415479_17893244067207634_6754080003431670941_n.jpg')"></div>
      <div class="parallax-overlay"></div>
      <div class="container">
        <nav aria-label="breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Início</a></li><li class="breadcrumb-item active">Blog</li></ol></nav>
        <h1 class="display-5 fw-bold">Blog &amp; dicas</h1>
        <p>Conteúdo prático sobre segurança, redes e electricidade para Maputo e Moçambique.</p>
      </div>
    </section>
    <section class="section"><div class="container"><div class="row g-4">{blog_cards}</div></div></section>
    <section class="cta-band">
      <div class="parallax-overlay"></div>
      <div class="container reveal">
        <h2 class="display-6 mb-3">Tem uma dúvida técnica?</h2>
        <p class="mb-4">Pergunte-nos no WhatsApp — respondemos em português, com foco em soluções locais.</p>
        <a href="{WA}" class="btn btn-light btn-lg me-2" target="_blank" rel="noopener">Perguntar no WhatsApp</a>
        <a href="faq.html" class="btn btn-outline-light btn-lg">Ver FAQ</a>
      </div>
    </section>
""",
)

# ---------- CONTACTO ----------
write(
    "contacto.html",
    "Contacto | QL REDES Maputo — Orçamento e WhatsApp",
    "Contacte a QL REDES em Maputo: +258 84 842 6310, qlredes@gmail.com, Rua Irmãos Rubbi 2250.",
    f"""
    <section class="page-hero">
      <div class="parallax-bg" data-parallax="0.2" style="background-image:url('assets/images/595662529_1269319441886200_6300626288040576835_n.jpg')"></div>
      <div class="parallax-overlay"></div>
      <div class="container">
        <nav aria-label="breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Início</a></li><li class="breadcrumb-item active">Contacto</li></ol></nav>
        <h1 class="display-5 fw-bold">Contacto &amp; orçamentos</h1>
        <p>Fale connosco por WhatsApp, telefone, e-mail ou formulário. Respondemos com rapidez.</p>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="row g-4 g-lg-5">
          <div class="col-lg-5 reveal">
            <div class="contact-panel">
              <h3 class="h4 mb-2">QL REDES / QL Group</h3>
              <p class="opacity-75 mb-4">Sediados em Maputo — atendimento residencial e empresarial.</p>
              <div class="d-flex gap-3 mb-3"><div class="contact-row-icon"><i class="bi bi-geo-alt"></i></div><div><strong class="d-block small">Endereço</strong><span class="small opacity-75">Rua Irmãos Rubbi 2250, Maputo, Moçambique</span></div></div>
              <div class="d-flex gap-3 mb-3"><div class="contact-row-icon"><i class="bi bi-telephone"></i></div><div><strong class="d-block small">Telefone / WhatsApp</strong><a href="tel:+258848426310" class="small">+258 84 842 6310</a></div></div>
              <div class="d-flex gap-3 mb-3"><div class="contact-row-icon"><i class="bi bi-chat-dots"></i></div><div><strong class="d-block small">Telefone alternativo</strong><a href="tel:+258872497969" class="small">+258 87 249 7969</a></div></div>
              <div class="d-flex gap-3 mb-3"><div class="contact-row-icon"><i class="bi bi-envelope"></i></div><div><strong class="d-block small">E-mail</strong><a href="mailto:qlredes@gmail.com" class="small">qlredes@gmail.com</a></div></div>
              <div class="d-flex gap-3 mb-3"><div class="contact-row-icon"><i class="bi bi-clock"></i></div><div><strong class="d-block small">Horário</strong><span class="small opacity-75">Seg–Sáb · 08:00–17:30</span></div></div>
              <div class="d-flex gap-3 mb-4"><div class="contact-row-icon"><i class="bi bi-share"></i></div><div><strong class="d-block small">Redes sociais</strong><span class="small"><a href="https://www.facebook.com/joaquimlleao" target="_blank" rel="noopener">Facebook</a> · <a href="https://www.instagram.com/ql_group_/" target="_blank" rel="noopener">Instagram</a></span></div></div>
              <a href="{WA}" class="btn btn-whatsapp w-100" target="_blank" rel="noopener"><i class="bi bi-whatsapp me-1"></i> Abrir WhatsApp directo</a>
            </div>
          </div>
          <div class="col-lg-7 reveal reveal-delay-2">
            <div class="card border-0 shadow-ql rounded-ql">
              <div class="card-body p-4 p-md-5">
                <h3 class="h4 text-navy mb-2">Pedido de orçamento</h3>
                <p class="text-muted small mb-4">Preencha o formulário e enviaremos a mensagem para o WhatsApp. Produtos no carrinho serão incluídos automaticamente.</p>
                <form id="contact-form" class="needs-validation" novalidate>
                  <div class="row g-3">
                    <div class="col-md-6">
                      <label class="form-label" for="name">Nome completo *</label>
                      <input type="text" class="form-control" id="name" name="name" required placeholder="O seu nome" autocomplete="name">
                      <div class="invalid-feedback">Indique o seu nome.</div>
                    </div>
                    <div class="col-md-6">
                      <label class="form-label" for="phone">Telefone / WhatsApp *</label>
                      <input type="tel" class="form-control" id="phone" name="phone" required placeholder="+258 8X XXX XXXX" autocomplete="tel">
                      <div class="invalid-feedback">Indique o telefone.</div>
                    </div>
                    <div class="col-12">
                      <label class="form-label" for="service">Serviço pretendido</label>
                      <select class="form-select" id="service" name="service">
                        <option value="">Seleccione…</option>
                        <option>Redes Informáticas</option>
                        <option>Electricidade</option>
                        <option>CCTV / Segurança</option>
                        <option>Portões Automáticos</option>
                        <option>Pérgolas / Estores</option>
                        <option>Controlo de Acesso</option>
                        <option>Vários / Integrado</option>
                        <option>Outro</option>
                      </select>
                    </div>
                    <div class="col-12">
                      <label class="form-label" for="message">Mensagem *</label>
                      <textarea class="form-control" id="message" name="message" rows="4" required placeholder="Descreva o projecto, localização, medidas ou dúvidas…"></textarea>
                      <div class="invalid-feedback">Escreva a sua mensagem.</div>
                    </div>
                    <div class="col-12">
                      <button type="submit" class="btn btn-whatsapp btn-lg w-100"><i class="bi bi-whatsapp me-1"></i> Enviar via WhatsApp</button>
                      <p class="small text-muted text-center mt-3 mb-0">Ao enviar, abre o WhatsApp com a mensagem pronta. Ver <a href="privacidade.html">política de privacidade</a>.</p>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
        <div class="map-wrap mt-5 reveal">
          <iframe title="Mapa — Maputo, Moçambique" src="https://maps.google.com/maps?q=Rua%20Irm%C3%A3os%20Rubbi%202250%2C%20Maputo&t=&z=15&ie=UTF8&iwloc=&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
        </div>
      </div>
    </section>
""",
)

# ---------- FAQ ----------
faqs = [
    ("O site vende produtos com pagamento online?", "Não. A página de produtos serve para <strong>mostrar equipamentos</strong> e montar uma lista de interesse. Depois envia um <strong>pedido de orçamento</strong> (WhatsApp)."),
    ("Os preços no catálogo são finais?", "Os valores indicados (quando existem) são <strong>preços de referência</strong> e podem variar consoante o modelo, quantidade e complexidade da instalação."),
    ("Em que zonas trabalham?", "Estamos sediados em <strong>Maputo</strong> (Rua Irmãos Rubbi 2250) e atendemos o Grande Maputo. Para outras localidades, contacte-nos."),
    ("Quanto tempo demora um orçamento?", "Pedidos simples via WhatsApp têm resposta rápida. Projectos com visita técnica podem precisar de avaliação no local."),
    ("Instalam e só fornecem equipamento?", "Fazemos <strong>fornecimento e instalação</strong>. Em muitos casos a instalação profissional é essencial."),
    ("Que informação enviar para orçamento de portão?", "Idealmente: <strong>fotos do vão</strong>, medidas aproximadas e se pretende motorização."),
    ("As câmaras CCTV funcionam sem internet?", "Sistemas com gravador local podem gravar sem internet. A visualização remota normalmente precisa de ligação."),
    ("Oferecem garantia?", "Sim — a garantia depende do equipamento e do serviço. Detalhamos condições no orçamento."),
    ("Como acompanhar projectos da empresa?", 'Siga no <a href="https://www.facebook.com/joaquimlleao" target="_blank" rel="noopener">Facebook</a> e no <a href="https://www.instagram.com/ql_group_/" target="_blank" rel="noopener">Instagram (@ql_group_)</a>.'),
]

faq_items = "".join(
    f'''
            <div class="accordion-item">
              <h2 class="accordion-header" id="faq{i}">
                <button class="accordion-button{" collapsed" if i else ""}" type="button" data-bs-toggle="collapse" data-bs-target="#c{i}" aria-expanded="{str(i==0).lower()}" aria-controls="c{i}">{q}</button>
              </h2>
              <div id="c{i}" class="accordion-collapse collapse{" show" if i==0 else ""}" data-bs-parent="#faqAccordion" aria-labelledby="faq{i}">
                <div class="accordion-body text-muted">{a}</div>
              </div>
            </div>'''
    for i, (q, a) in enumerate(faqs)
)

write(
    "faq.html",
    "FAQ | Perguntas Frequentes — QL REDES Maputo",
    "Perguntas frequentes sobre orçamentos, CCTV, portões automáticos, redes e instalação da QL REDES.",
    f"""
    <section class="page-hero">
      <div class="parallax-overlay"></div>
      <div class="container">
        <nav aria-label="breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Início</a></li><li class="breadcrumb-item active">FAQ</li></ol></nav>
        <h1 class="display-5 fw-bold">Perguntas frequentes</h1>
        <p>Respostas rápidas sobre orçamentos, instalação e serviços da QL REDES.</p>
      </div>
    </section>
    <section class="section">
      <div class="container" style="max-width:760px">
        <div class="accordion reveal" id="faqAccordion">{faq_items}</div>
        <div class="text-center mt-5 reveal">
          <p class="text-muted mb-3">Não encontrou a resposta?</p>
          <a href="{WA}" class="btn btn-whatsapp me-2" target="_blank" rel="noopener">Perguntar no WhatsApp</a>
          <a href="contacto.html" class="btn btn-outline-primary">Página de contacto</a>
        </div>
      </div>
    </section>
""",
)

# ---------- PRIVACIDADE ----------
write(
    "privacidade.html",
    "Política de Privacidade | QL REDES",
    "Política de privacidade do website da QL REDES — como tratamos contactos e pedidos de orçamento.",
    """
    <section class="page-hero">
      <div class="parallax-overlay"></div>
      <div class="container">
        <nav aria-label="breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Início</a></li><li class="breadcrumb-item active">Privacidade</li></ol></nav>
        <h1 class="display-5 fw-bold">Política de privacidade</h1>
        <p>Transparência sobre o uso de dados no website da QL REDES.</p>
      </div>
    </section>
    <section class="section">
      <div class="container" style="max-width:760px">
        <p class="text-muted mb-4">Última actualização: Julho 2026. Esta página descreve práticas simples do site estático da QL REDES / QL Group.</p>
        <h3 class="h5 text-navy">1. Quem somos</h3>
        <p class="text-muted mb-4">QL REDES (QL Group), Maputo, Moçambique. Contacto: <a href="mailto:qlredes@gmail.com">qlredes@gmail.com</a> · <a href="tel:+258848426310">+258 84 842 6310</a>.</p>
        <h3 class="h5 text-navy">2. Dados que podemos receber</h3>
        <p class="text-muted mb-4">Quando pede um orçamento (formulário ou WhatsApp), pode partilhar nome, telefone, e-mail, descrição do projecto e lista de produtos. Destinam-se apenas a <strong>responder ao pedido comercial</strong>.</p>
        <h3 class="h5 text-navy">3. Armazenamento no navegador</h3>
        <p class="text-muted mb-4">O carrinho de orçamento usa <strong>localStorage</strong> no seu dispositivo. Estes dados não são enviados a servidores até você partilhá-los (ex.: via WhatsApp).</p>
        <h3 class="h5 text-navy">4. WhatsApp e terceiros</h3>
        <p class="text-muted mb-4">Botões de WhatsApp redireccionam para a Meta/WhatsApp. Mapas (Google Maps) são serviços de terceiros.</p>
        <h3 class="h5 text-navy">5. Cookies e analytics</h3>
        <p class="text-muted mb-4">Esta versão não utiliza cookies de publicidade nem analytics de terceiros por defeito.</p>
        <h3 class="h5 text-navy">6. Partilha de dados</h3>
        <p class="text-muted mb-4">Não vendemos dados pessoais. A informação é usada internamente pela QL REDES para orçamentos e suporte.</p>
        <h3 class="h5 text-navy">7. Os seus direitos</h3>
        <p class="text-muted mb-4">Pode pedir correcção ou eliminação dos seus dados enviando e-mail para <a href="mailto:qlredes@gmail.com">qlredes@gmail.com</a>.</p>
        <h3 class="h5 text-navy">8. Alterações</h3>
        <p class="text-muted mb-4">Podemos actualizar esta página periodicamente.</p>
        <a href="contacto.html" class="btn btn-primary">Contactar-nos</a>
      </div>
    </section>
""",
)

# Verify accents
for f in ROOT.glob("*.html"):
    t = f.read_text(encoding="utf-8")
    assert "charset=\"UTF-8\"" in t
    assert "Ã§" not in t
    assert "bootstrap" in t
print("all pages OK")
