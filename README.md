# Creador de menús de un archivo Markdown a HTML

## Resumen
- El objetivo de este proyecto es desarrollar un compilador capaz de recibir un archivo Markdown y convertir su contenido en un menú HTML, ideal para representar menús de restaurantes o servicios en una página web de manera estructurada y estéticamente agradable.

## Motivación y Problema a Resolver
- **Descripción del problema:** 
    Muchos restaurantes y servicios necesitan una manera rápida y eficiente de crear y actualizar menús en formato web. Markdown es un formato de texto ligero que permite a los usuarios crear contenido estructurado sin necesidad de conocimientos avanzados de HTML. Sin embargo, convertir automáticamente este contenido en un menú HTML bien estructurado y visualmente atractivo puede ser algo mas complicado si no tienes conocimientos de programacion en este lenguaje.
- **Importancia:** 
    La automatización de la creación de menús en HTML a partir de archivos Markdown permite a los usuarios sin conocimientos de programación gestionar sus contenidos de forma eficiente, mejorando la accesibilidad y la rapidez en la actualización de sus menús en línea.
- **Casos de uso:**
    Restaurantes que desean mantener su menú actualizado en su página web.
    Servicios de catering o eventos que necesitan presentar diferentes opciones de menú para sus clientes.
    Cualquier negocio que ofrezca productos o servicios y necesite mostrar listas de manera clara y estructurada en línea. 

## Objetivos del Proyecto
- **Objetivo 1: Desarrollar un compilador que interprete el contenido de un archivo Markdown y lo convierta en un menú HTML estructurado.**
- **Objetivo 2: Crear un compilador que transforme un archivo Markdown en un menú HTML básico.**
- **Objetivo 3: Asegurar que el compilador genere un menú HTML que sea fácil de leer y navegar.**
- **Objetivo 4: Garantizar que el compilador maneje correctamente casos especiales, como menús con subcategorías o ítems con descripciones detalladas.**

## Revisión del Estado del Arte
- **Compiladores similares:**
    Existen herramientas y librerías que permiten convertir Markdown a HTML, como Pandoc o Markdown-it. Sin embargo, estas herramientas no están específicamente diseñadas para la creación de menús o carecen de personalización avanzada para este propósito.
- **Limitaciones de soluciones actuales:**
    La mayoría de los compiladores genéricos de Markdown a HTML generan una estructura básica sin considerar las necesidades específicas de un menú, como la agrupación de categorías, la inclusión de descripciones o precios, y la personalización del diseño.
- **Justificación del nuevo compilador:**
    Un compilador especializado en la creación de menús a partir de Markdown permitirá a los usuarios generar contenido más adaptado a sus necesidades, con un diseño atractivo y funcional que no requieren edición manual adicional en HTML.

## Arquitectura y Diseño del Compilador
- **Diagrama de bloques:**
  ![Archivo Markdown (1)](https://github.com/user-attachments/assets/c199f72d-94d9-4052-9d18-dcc25407302f)

- **Explicación del flujo de datos:**
    El flujo de datos en este proyecto comienza con la entrada de un archivo Markdown, que pasa por un análisis léxico para identificar y tokenizar elementos clave del documento. Estos tokens luego son analizados sintácticamente para formar un Árbol de Sintaxis Abstracta (AST), que organiza la estructura lógica del documento. A continuación, se realiza un análisis semántico para asegurar la coherencia del contenido. Con el AST validado, se procede a la generación de código HTML, donde cada elemento de Markdown se convierte en su equivalente HTML, resultando en un menú o servicio representado en HTML listo para ser utilizado en una página web.
- **Decisiones de diseño:**
    Se optó por un diseño modular que permite la fácil adición de nuevas funcionalidades, como plantillas personalizadas o soporte para otros formatos de entrada. Se priorizó la eficiencia y la claridad en la generación del código HTML, manteniendo la simplicidad en el uso.

## Análisis Léxico
- **Análisis léxico:**
![Automata DFA](https://github.com/user-attachments/assets/37414cce-2f53-4d6e-80cf-8a64eadcb874)

  - Durante el análisis léxico, el compilador identificará tokens como encabezados (para categorías del menú), listas (para ítems del menú), y texto en línea (para descripciones y precios). Operadores y delimitadores como #, *, y - serán reconocidos y transformados en elementos HTML correspondientes.
- **Ejemplos:**
    Markdown
    # Entradas
    - Ensalada César - $10.00
    - Sopa de tomate - $8.50
    
    HTML
    <h2>Entradas</h2>
    <ul>
      <li>Ensalada César - $10.00</li>
      <li>Sopa de tomate - $8.50</li>
    </ul>
