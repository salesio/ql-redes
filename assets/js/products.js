/* Catálogo de produtos QL REDES — preços de referência (sob consulta) */
const PRODUCTS = [
  {
    id: "cam-solar-wifi",
    name: "Câmara Solar Wi-Fi Externa",
    category: "cctv",
    price: 8300,
    priceLabel: "a partir de",
    image: "assets/images/440984849_836565345161614_2712887158395915178_n.jpg",
    description: "Câmara de segurança sem fio com painel solar, bateria recarregável, Wi-Fi, detecção de movimento PIR, visão noturna e áudio bidirecional."
  },
  {
    id: "kit-cctv-4",
    name: "Kit CCTV 4 Câmaras HD",
    category: "cctv",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/476376466_17885926239207634_3543768025712323292_n.jpg",
    description: "Sistema completo de videovigilância com 4 câmaras HD, gravador e instalação profissional residencial ou comercial."
  },
  {
    id: "kit-cctv-8",
    name: "Kit CCTV 8 Câmaras + DVR",
    category: "cctv",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/476271729_17885926230207634_4306339768668785807_n.jpg",
    description: "Solução de vigilância alargada para empresas e propriedades maiores, com gravação e acesso remoto."
  },
  {
    id: "fechadura-magnetica",
    name: "Fechadura Magnética Electromagnética",
    category: "acesso",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/488255805_1067932538691559_5812239850081575222_n.jpg",
    description: "Fecho electromagnético de alta força para portas e portões — ideal para controlo de acesso comercial e residencial."
  },
  {
    id: "controlo-acesso",
    name: "Sistema de Controlo de Acesso",
    category: "acesso",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/488257583_1067932535358226_8671181315900120721_n.jpg",
    description: "Leitores de cartão, biometria ou código PIN com registo de entradas e integração com portas e barreiras."
  },
  {
    id: "portao-automatico",
    name: "Portão Automático Deslizante",
    category: "portoes",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/download (1).png",
    description: "Portão metálico automatizado com motor, comando à distância e instalação completa em Maputo."
  },
  {
    id: "portao-painel",
    name: "Portão Automático Painel Fechado",
    category: "portoes",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/download.png",
    description: "Portão de painéis fechados com motor silencioso — privacidade e segurança para residências."
  },
  {
    id: "portao-design",
    name: "Portão Decorativo em Metal",
    category: "portoes",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/489694084_1071761274975352_932475664368770287_n.jpg",
    description: "Portão com design geométrico personalizado, fabricado e instalado pela equipa QL REDES."
  },
  {
    id: "motor-portao",
    name: "Motor para Portão Automático",
    category: "portoes",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/465612243_17874099957207634_3016753067222796926_n.jpg",
    description: "Kit de motorização para portões basculantes ou deslizantes, com comandos e sensores de segurança."
  },
  {
    id: "pergola-bioclimatica",
    name: "Pérgola Bioclimática",
    category: "pergolas",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/675813361_1370522625099214_4137454648823396842_n.jpg",
    description: "Pérgola com lâminas orientáveis para sombra, ventilação e proteção — ideal para esplanadas e jardins."
  },
  {
    id: "estor-enrolavel",
    name: "Estore / Persianas Metálicas",
    category: "pergolas",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/537672052_17909713176207634_3423635583355580655_n.jpg",
    description: "Sistemas de estores e persianas metálicas para proteção solar e segurança de fachadas e aberturas."
  },
  {
    id: "guarda-corpo",
    name: "Guarda-Corpo Metálico",
    category: "metal",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/623455006_1303841571767320_6077619064415629963_n.jpg",
    description: "Guarda-corpos e corrimãos em metal para varandas, escadas e áreas exteriores com acabamento premium."
  },
  {
    id: "alarme-residencial",
    name: "Alarme Residencial / Comercial",
    category: "alarme",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/476388993_17885926278207634_7210792862547623333_n.jpg",
    description: "Sistemas de alarme com sensores de movimento, contacto de portas/janelas e notificação no telemóvel."
  },
  {
    id: "rede-wifi",
    name: "Instalação Rede Wi-Fi Empresarial",
    category: "redes",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/488415479_17893244067207634_6754080003431670941_n.jpg",
    description: "Planeamento e instalação de redes Wi-Fi estáveis para casas, escritórios e espaços comerciais."
  },
  {
    id: "cabeamento",
    name: "Cabeamento Estruturado",
    category: "redes",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/488461347_17893244079207634_6514942602438994313_n.jpg",
    description: "Cabeamento de rede Cat6, pontos de dados, racks e organização profissional de infraestrutura TI."
  },
  {
    id: "quadro-eletrico",
    name: "Instalação Eléctrica / Quadros",
    category: "electricidade",
    price: null,
    priceLabel: "Sob consulta",
    image: "assets/images/465740896_17874100107207634_5495886275657190308_n.jpg",
    description: "Instalações eléctricas residenciais e comerciais, quadros, iluminação e manutenção preventiva."
  }
];

const PRODUCT_CATEGORIES = {
  all: "Todos",
  cctv: "CCTV",
  acesso: "Controlo de Acesso",
  portoes: "Portões",
  pergolas: "Pérgolas & Estores",
  metal: "Metalurgia",
  alarme: "Alarmes",
  redes: "Redes",
  electricidade: "Electricidade"
};

function formatPrice(product) {
  if (product.price == null) return product.priceLabel || "Sob consulta";
  return `${product.priceLabel || ""} ${product.price.toLocaleString("pt-MZ")} MT`.trim();
}

function getProductById(id) {
  return PRODUCTS.find((p) => p.id === id);
}
