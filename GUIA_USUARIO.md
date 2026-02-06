# 📖 Guía de Usuario - Plot & Form

## ¿Qué es Plot & Form?

Plot & Form es una herramienta que convierte tus ideas en libros digitales. Combina texto (la trama o "plot") con elementos visuales (la forma o "form") para crear publicaciones listas para imprimir o leer digitalmente.

## 🗂️ Estructura del Proyecto

### Carpetas Principales

1. **plot_engine/** 
   - **Qué hace:** Interpreta tus ideas creativas escritas
   - **Ejemplo:** Si escribes "Un viaje místico", esta parte entiende y estructura tu historia

2. **form_engine/**
   - **Qué hace:** Crea mandalas e ilustraciones para tu libro
   - **Ejemplo:** Genera diseños visuales basados en tu historia

3. **exporters/**
   - **Qué hace:** Convierte tu libro en archivos PDF que puedes descargar
   - **Ejemplo:** El archivo final que puedes imprimir o compartir

4. **web/**
   - **Qué hace:** La página web donde interactúas con todo
   - **Ejemplo:** La interfaz visual con botones y formularios

5. **assets/**
   - **Qué hace:** Guarda recursos como fuentes e imágenes
   - **Ejemplo:** Tipografías especiales para tu libro

6. **output/**
   - **Qué hace:** Aquí se guardan los libros que generas
   - **Ejemplo:** Tu libro finalizado en formato PDF

## 🚀 Cómo Usar (Cuando esté Listo)

### Paso 1: Instalar
```bash
# Instalar las herramientas necesarias
pip install -r requirements.txt
```

### Paso 2: Iniciar la Aplicación
```bash
# Arrancar el servidor web
python web/app.py
```

### Paso 3: Abrir en tu Navegador
- Abre tu navegador web (Chrome, Firefox, etc.)
- Ve a: `http://127.0.0.1:5000`

### Paso 4: Crear tu Libro
1. **Escribe tu prompt creativo** - Describe tu idea para el libro
2. **Genera visuales** - Crea mandalas o ilustraciones
3. **Exporta a PDF** - Descarga tu libro terminado

## 📝 Estado Actual

🚧 **En Desarrollo** - La estructura base está creada, pero las funcionalidades completas aún están en proceso.

## ❓ Preguntas Frecuentes

### ¿Por qué no veo las carpetas en GitHub?

Las carpetas están en una "rama" (branch) separada llamada `copilot/create-folder-structure`. 

Para verlas en la página principal de GitHub:
1. Ve a la página de tu repositorio en GitHub
2. Busca el botón que dice "main" o "master"
3. Selecciona la rama `copilot/create-folder-structure`
4. O crea un Pull Request para fusionar los cambios

### ¿Necesito saber programar?

No necesariamente. Una vez que el sistema esté completo, podrás usarlo desde la interfaz web sin escribir código.

### ¿Qué es Flask?

Flask es una herramienta que permite crear páginas web con Python. Es lo que hace funcionar la interfaz visual de Plot & Form.

## 🔒 Seguridad

- El sistema solo funciona en tu computadora local (127.0.0.1)
- No se conecta a internet
- Tus libros se guardan solo en tu computadora

## 📞 Próximos Pasos

Comparte el diseño funcional de lo que quieres que haga la página para continuar con el desarrollo.
