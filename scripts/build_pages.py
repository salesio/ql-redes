# -*- coding: utf-8 -*-
"""Build modern Bootstrap HTML pages for QL REDES (UTF-8)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

HEAD = """<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  {extra_meta}
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


def page(title, description, body, extra_meta=""):
    return HEAD.format(title=title, description=description, extra_meta=extra_meta) + body + FOOT


def write(name, content):
    path = ROOT / name
    path.write_text(content, encoding="utf-8", newline="\n")
    print("wrote", name, "bytes", path.stat().st_size)


# ---------- INDEX ----------
index_body = f"""
    <section class="hero-parallax">
      <div class="parallax-bg" data-parallax="0.35" style="background-image:url('assets/images/download%20(1).png')"></div>
      <div class="parallax-overlay"></div>
      <div class="container hero-content">
        <div class="row align-items-center">
          <div class="col-lg-8 col-xl-7 reveal">
            <span class="hero-badge"><i class="bi bi-geo-alt-fill me-1"></i> Maputo · Moçambique · 10+ anos de experiência</span>
            <h1 class="display-5">Soluções Integradas em <em>Redes</em>, Electricidade e <em>Segurança</em></h1>
            <p class="lead mb-4">
              A QL REDES (QL Group) projecta, instala e mantém infraestrutura tecnológica e de segurança
              para casas e empresas em Maputo — com atendimento rápido e orçamento sem compromisso.
            </p>
            <div class="d-flex flex-wrap gap-2 mb-2">
              <a href="{WA}" class="btn btn-whatsapp btn-lg" target="_blank" rel="noopener"><i class="bi bi-whatsapp me-1"></i> Pedir Orçamento Gratuito</a>
              <a href="servicos.html" class="btn btn-outline-light btn-lg">Ver Serviços</a>
              <a href="produtos.html" class="btn btn-light btn-lg">Ver Produtos</a>
            </div>
            <div class="hero-stats">
              <div><strong>10+</strong><span>Anos de experiência</span></div>
              <div><strong>B2B &amp; B2C</strong><span>Casas e empresas</span></div>
              <div><strong>3 em 1</strong><span>Redes · Luz · Segurança</span></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="text-center mb-5 reveal">
          <span class="section-label">O que fazemos</span>
          <h2 class="section-title">Serviços em destaque</h2>
          <p class="text-muted mx-auto" style="max-width:36rem">Soluções práticas e integradas para residências, escritórios e indústrias em Maputo.</p>
        </div>
        <div class="row g-4">
          <div class="col-md-6 col-xl-3 reveal reveal-delay-1">
            <article class="card ql-card h-100">
              <div class="card-img-wrap"><img src="assets/images/488415479_17893244067207634_6754080003431670941_n.jpg" class="card-img-top" alt="Redes informáticas" loading="lazy"></div>
              <div class="card-body">
                <div class="card-icon"><i class="bi bi-router"></i></div>
                <h3 class="h5 text-navy">Redes Informáticas</h3>
                <p class="text-muted small">Cabeamento estruturado, Wi-Fi empresarial, servidores e manutenção de infraestrutura TI.</p>
                <a href="servicos.html#redes" class="stretched-link text-decoration-none fw-semibold">Saber mais <i class="bi bi-arrow-right"></i></a>
              </div>
            </article>
          </div>
          <div class="col-md-6 col-xl-3 reveal reveal-delay-2">
            <article class="card ql-card h-100">
              <div class="card-img-wrap"><img src="assets/images/465740896_17874100107207634_5495886275657190308_n.jpg" class="card-img-top" alt="Electricidade" loading="lazy"></div>
              <div class="card-body">
                <div class="card-icon"><i class="bi bi-lightning-charge"></i></div>
                <h3 class="h5 text-navy">Electricidade</h3>
                <p class="text-muted small">Instalações eléctricas, quadros, iluminação e automação com segurança e conformidade.</p>
                <a href="servicos.html#electricidade" class="stretched-link text-decoration-none fw-semibold">Saber mais <i class="bi bi-arrow-right"></i></a>
              </div>
            </article>
          </div>
          <div class="col-md-6 col-xl-3 reveal reveal-delay-3">
            <article class="card ql-card h-100">
              <div class="card-img-wrap"><img src="assets/images/440984849_836565345161614_2712887158395915178_n.jpg" class="card-img-top" alt="CCTV e segurança" loading="lazy"></div>
              <div class="card-body">
                <div class="card-icon"><i class="bi bi-camera-video"></i></div>
                <h3 class="h5 text-navy">Segurança Electrónica</h3>
                <p class="text-muted small">CCTV, alarmes, controlo de acesso e vigilância para casas e espaços comerciais.</p>
                <a href="servicos.html#seguranca" class="stretched-link text-decoration-none fw-semibold">Saber mais <i class="bi bi-arrow-right"></i></a>
              </div>
            </article>
          </div>
          <div class="col-md-6 col-xl-3 reveal reveal-delay-4">
            <article class="card ql-card h-100">
              <div class="card-img-wrap"><img src="assets/images/download.png" class="card-img-top" alt="Portões automáticos" loading="lazy"></div>
              <div class="card-body">
                <div class="card-icon"><i class="bi bi-door-open"></i></div>
                <h3 class="h5 text-navy">Portões &amp; Pérgolas</h3>
                <p class="text-muted small">Portões automáticos, motores, pérgolas bioclimáticas e soluções metálicas sob medida.</p>
                <a href="servicos.html#portoes" class="stretched-link text-decoration-none fw-semibold">Saber mais <i class="bi bi-arrow-right"></i></a>
              </div>
            </article>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container">
        <div class="row g-5 align-items-center">
          <div class="col-lg-6 reveal">
            <span class="section-label">Porquê a QL REDES</span>
            <h2 class="section-title">Experiência local, soluções integradas</h2>
            <p class="text-muted mb-4">Diferenciamo-nos por unir redes, electricidade e segurança num só parceiro — menos fornecedores, mais responsabilidade e entrega coordenada.</p>
            <div class="row g-3">
              <div class="col-md-6"><div class="feature-item"><div class="fi"><i class="bi bi-check2-circle"></i></div><div><h4 class="h6 mb-1">10+ anos no terreno</h4><p class="small text-muted mb-0">Projectos residenciais e empresariais em Maputo.</p></div></div></div>
              <div class="col-md-6"><div class="feature-item"><div class="fi"><i class="bi bi-lightning"></i></div><div><h4 class="h6 mb-1">Atendimento rápido</h4><p class="small text-muted mb-0">WhatsApp, visitas técnicas e orçamentos claros.</p></div></div></div>
              <div class="col-md-6"><div class="feature-item"><div class="fi"><i class="bi bi-shield-check"></i></div><div><h4 class="h6 mb-1">Qualidade e garantia</h4><p class="small text-muted mb-0">Instalação profissional e suporte pós-venda.</p></div></div></div>
              <div class="col-md-6"><div class="feature-item"><div class="fi"><i class="bi bi-geo"></i></div><div><h4 class="h6 mb-1">Foco em Moçambique</h4><p class="small text-muted mb-0">Soluções adaptadas à realidade de Maputo.</p></div></div></div>
            </div>
          </div>
          <div class="col-lg-6 reveal reveal-delay-2">
            <div class="visual-frame">
              <img src="assets/images/595662529_1269319441886200_6300626288040576835_n.jpg" alt="Entrega de equipamentos QL REDES em Maputo" loading="lazy">
              <div class="visual-badge"><strong>Maputo</strong><span class="small text-muted">Instalação &amp; entrega local</span></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="parallax-band">
      <div class="parallax-bg" data-parallax="0.2" style="background-image:url('assets/images/download%20(1).png')"></div>
      <div class="parallax-overlay"></div>
      <div class="container text-center py-5 reveal">
        <h2 class="display-6 fw-bold mb-3">Mais de uma década a proteger e conectar Maputo</h2>
        <p class="mb-4 mx-auto" style="max-width:32rem;opacity:.9">Redes, electricidade e segurança electrónica — num só parceiro de confiança.</p>
        <a href="portfolio.html" class="btn btn-light btn-lg me-2">Ver portfólio</a>
        <a href="{WA}" class="btn btn-outline-light btn-lg" target="_blank" rel="noopener">Falar no WhatsApp</a>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="text-center mb-5 reveal">
          <span class="section-label">Portfólio</span>
          <h2 class="section-title">Projectos recentes</h2>
          <p class="text-muted">Trabalhos reais da equipa — portões, estruturas, segurança e mais.</p>
        </div>
        <div class="row g-3">
          {"".join(f'''
          <div class="col-6 col-md-4 reveal reveal-delay-{(i%4)+1}">
            <div class="gallery-item">
              <img src="{src}" alt="{alt}" loading="lazy">
              <div class="gallery-overlay"><span>{alt}</span></div>
            </div>
          </div>''' for i,(src,alt) in enumerate([
            ("assets/images/download%20(1).png","Portão automático"),
            ("assets/images/489694084_1071761274975352_932475664368770287_n.jpg","Portão design"),
            ("assets/images/488411407_17893244058207634_6765023642434450324_n.jpg","Estrutura metálica"),
            ("assets/images/465706527_17874100092207634_6894705478359609218_n.jpg","Preparação de instalação"),
            ("assets/images/675813361_1370522625099214_4137454648823396842_n.jpg","Pérgola bioclimática"),
            ("assets/images/download.png","Portão painel fechado"),
          ]))}
        </div>
        <div class="text-center mt-4 reveal"><a href="portfolio.html" class="btn btn-outline-primary btn-lg">Ver portfólio completo</a></div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container">
        <div class="text-center mb-5 reveal">
          <span class="section-label">Clientes</span>
          <h2 class="section-title">O que dizem sobre nós</h2>
        </div>
        <div class="row g-4">
          <div class="col-md-4 reveal reveal-delay-1">
            <div class="card testimonial-card h-100"><div class="card-body p-4">
              <div class="stars mb-2">★★★★★</div>
              <p class="text-muted fst-italic">“Instalaram o portão automático e o sistema de CCTV na nossa casa. Trabalho limpo, prazos cumpridos e excelente comunicação no WhatsApp.”</p>
              <div class="d-flex align-items-center gap-2 mt-3"><div class="avatar-circle">CM</div><div><strong class="d-block small text-navy">Cliente Residencial</strong><span class="small text-muted">Maputo</span></div></div>
            </div></div>
          </div>
          <div class="col-md-4 reveal reveal-delay-2">
            <div class="card testimonial-card h-100"><div class="card-body p-4">
              <div class="stars mb-2">★★★★★</div>
              <p class="text-muted fst-italic">“Precisávamos de rede Wi-Fi estável no escritório e controlo de acesso. A QL REDES resolveu tudo de forma integrada — recomendo.”</p>
              <div class="d-flex align-items-center gap-2 mt-3"><div class="avatar-circle">ES</div><div><strong class="d-block small text-navy">Empresa Local</strong><span class="small text-muted">Maputo</span></div></div>
            </div></div>
          </div>
          <div class="col-md-4 reveal reveal-delay-3">
            <div class="card testimonial-card h-100"><div class="card-body p-4">
              <div class="stars mb-2">★★★★★</div>
              <p class="text-muted fst-italic">“Equipa técnica experiente. Explicaram as opções de segurança e o orçamento foi transparente. Voltaremos a chamar.”</p>
              <div class="d-flex align-items-center gap-2 mt-3"><div class="avatar-circle">AM</div><div><strong class="d-block small text-navy">Comércio</strong><span class="small text-muted">Grande Maputo</span></div></div>
            </div></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="text-center mb-5 reveal">
          <span class="section-label">Processo</span>
          <h2 class="section-title">Como pedir o seu orçamento</h2>
        </div>
        <div class="row g-4">
          {"".join(f'''
          <div class="col-6 col-lg-3 reveal reveal-delay-{i}">
            <div class="step-card"><div class="step-num">{i}</div><h4 class="h6 text-navy">{t}</h4><p class="small text-muted mb-0">{d}</p></div>
          </div>''' for i,t,d in [
            (1,"Contacte-nos","WhatsApp, telefone ou formulário no site."),
            (2,"Avaliação","Visitamos o local e analisamos a melhor solução."),
            (3,"Orçamento","Proposta clara com equipamentos e prazos."),
            (4,"Instalação","Execução profissional e suporte após entrega."),
          ])}
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="parallax-bg" data-parallax="0.15" style="background-image:url('assets/images/675813361_1370522625099214_4137454648823396842_n.jpg')"></div>
      <div class="parallax-overlay"></div>
      <div class="container reveal">
        <h2 class="display-6 mb-3">Pronto para proteger e modernizar o seu espaço?</h2>
        <p class="mb-4">Peça um orçamento gratuito hoje. Respondemos rapidamente via WhatsApp.</p>
        <div class="d-flex flex-wrap justify-content-center gap-2">
          <a href="{WA}" class="btn btn-light btn-lg" target="_blank" rel="noopener"><i class="bi bi-whatsapp me-1"></i> +258 84 842 6310</a>
          <a href="contacto.html" class="btn btn-outline-light btn-lg">Formulário de contacto</a>
          <a href="produtos.html" class="btn btn-outline-light btn-lg">Montar lista de produtos</a>
        </div>
      </div>
    </section>
"""

write(
    "index.html",
    page(
        "QL REDES | Redes, Electricidade e Segurança Electrónica em Maputo",
        "QL REDES (QL Group) — soluções integradas em redes informáticas, electricidade, CCTV, portões automáticos e segurança electrónica em Maputo, Moçambique.",
        index_body,
        extra_meta="""<meta name="keywords" content="redes informáticas Maputo, instalação CCTV Maputo, segurança electrónica Moçambique, portões automáticos Maputo">
  <meta name="author" content="QL REDES">
  <meta property="og:title" content="QL REDES | Tecnologia & Soluções Integradas">
  <meta property="og:description" content="Redes, electricidade e segurança electrónica em Maputo. Orçamento gratuito via WhatsApp.">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pt_MZ">""",
    ),
)

# ---------- SOBRE ----------
write(
    "sobre.html",
    page(
        "Sobre Nós | QL REDES — QL Group Maputo",
        "Conheça a QL REDES (QL Group): empresa moçambicana em Maputo com 10+ anos em redes, electricidade e segurança electrónica.",
        f"""
    <section class="page-hero">
      <div class="parallax-bg" data-parallax="0.2" style="background-image:url('assets/images/488411407_17893244058207634_6765023642434450324_n.jpg')"></div>
      <div class="parallax-overlay"></div>
      <div class="container">
        <nav aria-label="breadcrumb"><ol class="breadcrumb"><li class="breadcrumb-item"><a href="index.html">Início</a></li><li class="breadcrumb-item active">Sobre Nós</li></ol></nav>
        <h1 class="display-5 fw-bold">Sobre a QL REDES</h1>
        <p>Tecnologia, redes e segurança — uma empresa moçambicana ao serviço de casas e negócios em Maputo.</p>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="row g-5 align-items-center">
          <div class="col-lg-6 reveal">
            <div class="visual-frame"><img src="assets/images/488411407_17893244058207634_6765023642434450324_n.jpg" alt="Equipa QL REDES em obra" loading="lazy"></div>
          </div>
          <div class="col-lg-6 reveal reveal-delay-2">
            <span class="section-label">A nossa história</span>
            <h2 class="section-title">QL REDES / QL Group</h2>
            <p class="text-muted">A <strong>QL REDES</strong> (também conhecida como <strong>QL Group</strong>) é uma empresa moçambicana sediada em Maputo, especializada em <strong>Tecnologia</strong>, <strong>Redes Informáticas</strong>, <strong>Electricidade</strong> e <strong>Segurança Electrónica</strong>.</p>
            <p class="text-muted">Com mais de <strong>10 anos de experiência</strong> no terreno, unimos competências técnicas para entregar soluções integradas — da infraestrutura de rede à videovigilância, passando por instalações eléctricas, portões automáticos e pérgolas.</p>
            <p class="text-muted mb-0">Actuamos nos segmentos <strong>B2C</strong> e <strong>B2B</strong>, com ênfase em soluções práticas e fiáveis para Maputo.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-soft">
      <div class="container">
        <div class="row g-5 align-items-center">
          <div class="col-lg-6 order-lg-2 reveal">
            <div class="visual-frame"><img src="assets/images/595662529_1269319441886200_6300626288040576835_n.jpg" alt="Operações QL REDES" loading="lazy"></div>
          </div>
          <div class="col-lg-6 order-lg-1 reveal reveal-delay-2">
            <span class="section-label">Liderança</span>
            <h2 class="section-title">Joaquim Leão</h2>
            <p class="text-muted"><strong>Proprietário e Director Geral</strong> — engenheiro informático e técnico de redes. Lidera a visão da empresa: oferecer tecnologia e segurança com profissionalismo e proximidade ao cliente.</p>
            <p class="text-muted mb-4">Acompanhe o dia-a-dia dos projectos no Facebook e Instagram (@ql_group_).</p>
            <a href="contacto.html" class="btn btn-primary">Falar connosco</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="text-center mb-5 reveal"><span class="section-label">Missão &amp; Valores</span><h2 class="section-title">O que nos move</h2></div>
        <div class="row g-4">
          <div class="col-md-4 reveal reveal-delay-1"><div class="card ql-card h-100 text-center"><div class="card-body p-4"><div class="card-icon mx-auto"><i class="bi bi-bullseye"></i></div><h3 class="h5">Missão</h3><p class="text-muted small mb-0">Fornecer soluções tecnológicas e de segurança confiáveis, acessíveis e bem executadas em Moçambique.</p></div></div></div>
          <div class="col-md-4 reveal reveal-delay-2"><div class="card ql-card h-100 text-center"><div class="card-body p-4"><div class="card-icon mx-auto"><i class="bi bi-eye"></i></div><h3 class="h5">Visão</h3><p class="text-muted small mb-0">Ser referência em Maputo em soluções integradas de redes, electricidade e segurança electrónica.</p></div></div></div>
          <div class="col-md-4 reveal reveal-delay-3"><div class="card ql-card h-100 text-center"><div class="card-body p-4"><div class="card-icon mx-auto"><i class="bi bi-gem"></i></div><h3 class="h5">Valores</h3><p class="text-muted small mb-0">Profissionalismo, inovação prática, atendimento personalizado e transparência nos orçamentos.</p></div></div></div>
        </div>
      </div>
    </section>

    <section class="cta-band">
      <div class="parallax-overlay"></div>
      <div class="container reveal">
        <h2 class="display-6 mb-3">Vamos trabalhar juntos?</h2>
        <p class="mb-4">Conte-nos o seu projecto. Orçamento gratuito e sem compromisso.</p>
        <a href="{WA}" class="btn btn-light btn-lg me-2" target="_blank" rel="noopener">Contactar no WhatsApp</a>
        <a href="servicos.html" class="btn btn-outline-light btn-lg">Ver serviços</a>
      </div>
    </section>
""",
    ),
)

print("index + sobre done")
