import zipfile
import os

project_name = "dpsmultiservices"
assets_dir = f"{project_name}/assets"
os.makedirs(assets_dir, exist_ok=True)

index_html_content = """<!DOCTYPE html>
<html lang="pt">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>DPS Multiservices - Agência de Serviços Migratórios</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <header>
    <div class="header-top">
      <div class="logo">
        <img src="assets/logo.png" alt="DPS Multiservices" />
      </div>
      <div class="welcome">
        <h1 id="welcomeText">Bem-vindo à DPS Multiservices</h1>
      </div>
    </div>
    <nav>
      <label for="languageSelect">🌐 Idioma:</label>
      <select id="languageSelect">
        <option value="pt">Português 🇧🇷</option>
        <option value="en">English 🇺🇸</option>
        <option value="fr">Français 🇫🇷</option>
        <option value="es">Español 🇪🇸</option>
      </select>
    </nav>
  </header>

  <main>
    <section id="services">
      <h2>Nossos Serviços</h2>
      <ul>
        <li>Consultoria para imigração</li>
        <li>Assistência com vistos</li>
        <li>Traduções juramentadas</li>
        <li>Apoio jurídico</li>
      </ul>
    </section>

    <section id="about">
      <h2>Sobre Nós</h2>
      <p>A DPS Multiservices é uma agência especializada em serviços migratórios com foco no atendimento personalizado para cada cliente.</p>
    </section>

    <section id="contact">
      <h2>Contato</h2>
      <p>Email: contato@dpsmultiservices.com</p>
      <p>Telefone: +55 (11) 99999-9999</p>
    </section>
  </main>

  <footer>
    <p>&copy; 2025 DPS Multiservices. Todos os direitos reservados.</p>
  </footer>

  <script>
    const translations = {
      pt: {
        welcomeText: "Bem-vindo à DPS Multiservices",
        servicesTitle: "Nossos Serviços",
        servicesList: [
          "Consultoria para imigração",
          "Assistência com vistos",
          "Traduções juramentadas",
          "Apoio jurídico"
        ],
        aboutTitle: "Sobre Nós",
        aboutText: "A DPS Multiservices é uma agência especializada em serviços migratórios com foco no atendimento personalizado para cada cliente.",
        contactTitle: "Contato",
        emailText: "Email: contato@dpsmultiservices.com",
        phoneText: "Telefone: +55 (11) 99999-9999",
        footerText: "© 2025 DPS Multiservices. Todos os direitos reservados."
      },
      en: {
        welcomeText: "Welcome to DPS Multiservices",
        servicesTitle: "Our Services",
        servicesList: [
          "Immigration consulting",
          "Visa assistance",
          "Certified translations",
          "Legal support"
        ],
        aboutTitle: "About Us",
        aboutText: "DPS Multiservices is an agency specialized in immigration services, focused on providing personalized support to each client.",
        contactTitle: "Contact",
        emailText: "Email: contact@dpsmultiservices.com",
        phoneText: "Phone: +55 (11) 99999-9999",
        footerText: "© 2025 DPS Multiservices. All rights reserved."
      },
      fr: {
        welcomeText: "Bienvenue chez DPS Multiservices",
        servicesTitle: "Nos Services",
        servicesList: [
          "Consultation en immigration",
          "Assistance pour les visas",
          "Traductions assermentées",
          "Soutien juridique"
        ],
        aboutTitle: "À propos de nous",
        aboutText: "DPS Multiservices est une agence spécialisée dans les services migratoires, offrant un accompagnement personnalisé à chaque client.",
        contactTitle: "Contact",
        emailText: "Email : contact@dpsmultiservices.com",
        phoneText: "Téléphone : +55 (11) 99999-9999",
        footerText: "© 2025 DPS Multiservices. Tous droits réservés."
      },
      es: {
        welcomeText: "Bienvenido a DPS Multiservices",
        servicesTitle: "Nuestros Servicios",
        servicesList: [
          "Consultoría de inmigración",
          "Asistencia de visas",
          "Traducciones juradas",
          "Apoyo legal"
        ],
        aboutTitle: "Sobre Nosotros",
        aboutText: "DPS Multiservices es una agencia especializada en servicios migratorios, enfocada en un servicio personalizado para cada cliente.",
        contactTitle: "Contacto",
        emailText: "Correo: contacto@dpsmultiservices.com",
        phoneText: "Teléfono: +55 (11) 99999-9999",
        footerText: "© 2025 DPS Multiservices. Todos los derechos reservados."
      }
    };

    const languageSelect = document.getElementById("languageSelect");

    languageSelect.addEventListener("change", () => {
      const lang = languageSelect.value;
      const t = translations[lang];

      document.getElementById("welcomeText").textContent = t.welcomeText;
      document.getElementById("services").querySelector("h2").textContent = t.servicesTitle;

      const servicesList = document.getElementById("services").querySelector("ul");
      servicesList.innerHTML = "";
      t.servicesList.forEach(service => {
        const li = document.createElement("li");
        li.textContent = service;
        servicesList.appendChild(li);
      });

      document.getElementById("about").querySelector("h2").textContent = t.aboutTitle;
      document.getElementById("about").querySelector("p").textContent = t.aboutText;

      document.getElementById("contact").querySelector("h2").textContent = t.contactTitle;
      document.getElementById("contact").querySelectorAll("p")[0].textContent = t.emailText;
      document.getElementById("contact").querySelectorAll("p")[1].textContent = t.phoneText;

      document.querySelector("footer p").textContent = t.footerText;
    });
  </script>
</body>
</html>
"""

style_css_content = """body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f5f7fa;
  color: #333;
}

header {
  background-color: #004080;
  color: white;
  padding: 20px 10px;
}

.header-top {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 20px;
  padding-bottom: 10px;
}

.logo img {
  height: 60px;
}

.welcome h1 {
  font-size: 1.8rem;
  margin: 0;
  color: white;
}

nav {
  text-align: center;
  margin-top: 10px;
}

nav select {
  font-size: 1rem;
  padding: 5px;
}

main {
  max-width: 1000px;
  margin: auto;
  padding: 40px 20px;
}

section {
  margin-bottom: 40px;
}

h2 {
  color: #004080;
}

footer {
  background-color: #003366;
  color: white;
  text-align: center;
  padding: 1rem;
}
"""

with open(f"{project_name}/index.html", "w", encoding="utf-8") as f:
    f.write(index_html_content)

with open(f"{project_name}/style.css", "w", encoding="utf-8") as f:
    f.write(style_css_content)

with open(f"{assets_dir}/logo.png", "wb") as f:
    f.write(b"\x89PNG\r\n\x1a\n")  # En-tête PNG minimal

zip_filename = f"{project_name}.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for folder, _, files in os.walk(project_name):
        for file in files:
            file_path = os.path.join(folder, file)
            arcname = os.path.relpath(file_path, project_name)
            zipf.write(file_path, arcname)

print(f"Projet compressé dans {zip_filename}")
