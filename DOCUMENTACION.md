# 📚 Plot & Form - Documentación Completa

## 🎯 ¿Qué es Plot & Form?

Plot & Form es una plataforma web que **genera libros digitales automáticamente** a partir de tus ideas. Puedes crear:

- 📿 Libros de mandalas para colorear
- 🐉 Cuentos de fantasía
- 📖 Historias noveladas
- 🎓 Libros educativos
- ✨ Y mucho más...

**Todo sin pagar por APIs externas** - 100% gratuito y local.

---

## 🚀 Cómo Empezar

### Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/mgdomm/Plot-Form.git
   cd Plot-Form
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Inicia la aplicación:**
   ```bash
   python web/app.py
   ```

4. **Abre tu navegador:**
   ```
   http://127.0.0.1:5000
   ```

---

## 📝 Cómo Usar Plot & Form

### Paso 1: Describe tu Libro

En el campo de texto principal, describe el tipo de libro que quieres crear. Por ejemplo:

- `"Libro de mandalas geométricos para relajación y meditación"`
- `"Cuento de fantasía para niños sobre dragones y héroes"`
- `"Historia novelada sobre la evolución de las mandalas"`
- `"Libro educativo sobre animales con ilustraciones"`

### Paso 2: Configura las Opciones

**Tipo de libro:**
- Mandalas
- Fantasía
- Historia
- Novela
- Educativo
- Cuento
- Otro

**Público objetivo:**
- General
- Niños
- Adultos
- Jóvenes

**¿Incluir texto?**
- Sí (con texto descriptivo)
- No (solo imágenes)

**Número de páginas:**
- De 5 a 200 páginas

**Estilo de ilustración:**
- Geométrico
- Fractal
- Abstracto
- Fantasía
- Histórico
- Animal
- Natural

**Modo de color:**
- A color
- Blanco y negro

### Paso 3: Generar el Libro

1. Haz clic en el botón **"✨ Generar Libro"**
2. Espera mientras se procesa (verás una barra de progreso)
3. El sistema:
   - Interpreta tu prompt
   - Crea la estructura del libro
   - Genera el contenido de cada página
   - Crea las ilustraciones

### Paso 4: Vista Previa

Una vez generado, verás:
- **Información del libro** (título, tipo, páginas)
- **Vista previa de cada página** con ilustración y texto
- **Navegación** entre páginas (botones Anterior/Siguiente)
- **Botones de edición:**
  - ✏️ Editar Página
  - 🔄 Regenerar Ilustración

### Paso 5: Exportar

Cuando estés satisfecho con tu libro:

1. **📄 Exportar PDF** - Descarga un PDF listo para Amazon KDP
2. **📚 Exportar EPUB** - (Próximamente) Formato para libros digitales

---

## 🏗️ Arquitectura del Sistema

### Módulos Principales

#### 1. **plot_engine/** - Motor de Narrativa
- `prompt_interpreter.py` - Interpreta tus ideas
- Genera la estructura del libro
- Crea el texto automáticamente

#### 2. **form_engine/** - Motor Visual
- `mandala_generator.py` - Genera mandalas geométricos
- `illustration_generator.py` - Crea ilustraciones
- Todo generado por código (sin APIs externas)

#### 3. **exporters/** - Exportadores
- `pdf_exporter.py` - Crea PDFs listos para KDP
  - Formato Letter (8.5 x 11 pulgadas)
  - Márgenes correctos (0.5 pulgadas)
  - Portada automática
  - Numeración de páginas
- `epub_exporter.py` - (En desarrollo)

#### 4. **web/** - Interfaz Web
- `app.py` - Servidor Flask
- `templates/` - HTML
- `static/` - CSS y JavaScript
- API REST completa

#### 5. **output/** - Archivos Generados
- Aquí se guardan tus PDFs y EPUBs

---

## 🎨 Características Actuales

### ✅ Implementado

- ✨ **Dashboard profesional** en español
- 📝 **Generación de libros** basada en prompts
- 🎨 **Mandalas geométricos** generados por código
- 📄 **Exportación a PDF** lista para Amazon KDP
- 🖼️ **Vista previa interactiva** con navegación
- ✏️ **Edición de texto** en línea
- 🔄 **Regeneración de ilustraciones**
- 💾 **Descarga directa** de archivos

### 🔄 En Desarrollo

- 📚 Exportación a EPUB completa
- 🎨 Más estilos de ilustraciones
- 🤖 Generación de texto más avanzada
- 📊 Galería de libros generados
- 🎨 Editor visual de portadas

---

## 📋 Ejemplos de Uso

### Ejemplo 1: Libro de Mandalas

**Prompt:** `"Libro de mandalas geométricos para colorear y relajación"`

**Configuración:**
- Tipo: Mandalas
- Público: General
- Texto: Sí
- Páginas: 20
- Estilo: Geométrico
- Color: Blanco y negro (para colorear)

**Resultado:** Un PDF con 20 mandalas únicos, cada uno con texto inspirador

### Ejemplo 2: Cuento de Fantasía

**Prompt:** `"Cuento de fantasía para niños sobre un dragón amigable"`

**Configuración:**
- Tipo: Cuento
- Público: Niños
- Texto: Sí
- Páginas: 15
- Estilo: Fantasía
- Color: A color

**Resultado:** Un cuento ilustrado con narrativa y dibujos fantásticos

---

## 🛠️ Especificaciones Técnicas

### Requisitos del Sistema

- Python 3.8 o superior
- Navegador web moderno (Chrome, Firefox, Safari)
- 100 MB de espacio en disco

### Dependencias

```python
Flask==3.0.0        # Servidor web
reportlab==4.0.7    # Generación de PDF
Pillow==10.1.0      # Procesamiento de imágenes
```

### Formatos de Salida

**PDF (Amazon KDP):**
- Tamaño: 8.5 x 11 pulgadas (Letter)
- Márgenes: 0.5 pulgadas (cumple KDP)
- Resolución: Alta calidad
- Formato: PDF 1.3

**EPUB (Próximamente):**
- Versión: EPUB 3.0
- Reflowable: Sí
- Imágenes: Embebidas

---

## ❓ Preguntas Frecuentes

### ¿Es gratis?
**Sí, completamente gratis.** No usa APIs de pago. Todo se genera localmente en tu computadora.

### ¿Necesito internet?
**No después de la instalación.** Una vez instalado, funciona 100% offline.

### ¿Los libros son originales?
**Sí, 100% originales.** Todo el contenido se genera automáticamente. No hay derechos de autor de terceros.

### ¿Puedo vender los libros generados?
**Sí.** Los libros generados son tuyos. Puedes publicarlos en Amazon KDP u otras plataformas.

### ¿Funciona en Windows/Mac/Linux?
**Sí.** Python y Flask funcionan en todos los sistemas operativos.

### ¿Qué es Amazon KDP?
**Amazon Kindle Direct Publishing** - la plataforma de Amazon para auto-publicar libros. Los PDFs generados por Plot & Form cumplen con sus especificaciones.

### ¿Puedo modificar los libros generados?
**Sí.** Puedes editar el texto directamente en la interfaz antes de exportar.

---

## 🔒 Privacidad y Seguridad

- **Todo es local:** Nada se envía a servidores externos
- **Sin tracking:** No recopilamos datos
- **Solo localhost:** El servidor solo acepta conexiones de tu computadora (127.0.0.1)
- **Código abierto:** Puedes revisar todo el código

---

## 📞 Soporte y Contribuciones

### Reportar Problemas
Si encuentras un error, abre un "Issue" en GitHub.

### Sugerencias
¿Ideas para nuevas funcionalidades? ¡Compártelas!

### Contribuir
El proyecto está abierto a contribuciones. Fork el repositorio y envía un Pull Request.

---

## 🗺️ Hoja de Ruta (Roadmap)

### v1.0 - MVP Actual ✅
- [x] Dashboard funcional
- [x] Generación de mandalas
- [x] Exportación a PDF
- [x] Vista previa interactiva

### v1.1 - Próximo (En desarrollo)
- [ ] Exportación a EPUB
- [ ] Más estilos de ilustraciones
- [ ] Generación de texto mejorada
- [ ] Galería de libros creados

### v2.0 - Futuro
- [ ] Integración opcional con APIs (OpenAI, DALL-E)
- [ ] Plantillas de libros predefinidas
- [ ] Editor visual avanzado
- [ ] Soporte para más idiomas

---

## 💝 Agradecimientos

Plot & Form es un proyecto creado para democratizar la creación de libros digitales, haciendo que cualquier persona pueda convertir sus ideas en publicaciones profesionales sin costo alguno.

**¡Gracias por usar Plot & Form!** ✨📚

---

*Última actualización: Febrero 2026*
