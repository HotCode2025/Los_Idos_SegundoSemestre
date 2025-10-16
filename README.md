# Los_Idos_SegundoSemestre


## Comandos útiles de Git:
-------------------------------------------------------------------------------------------------------------------------
## Ayuda Memoria - Comandos Esenciales.

### ***📁 NAVEGACIÓN BÁSICA ENTRE DOCUMENTOS***

**Ver carpetas y archivos**

    ls
    ls -la

**Crear carpeta**
 
    mkdir nombre_carpeta

**Entrar en carpeta**

    cd nombre_carpeta

 **Volver atrás**

    cd ..

 **Ver dónde estoy**

    pwd

 ### ***📄 MANEJO DE ARCHIVOS***


 **Crear archivo vacío**

    touch archivo.txt

 **Ver contenido**

    cat archivo.txt

 **Eliminar archivo**

    rm archivo.txt

 **Eliminar CARPETA _(¡CUIDADO!)_**

    rm -rf nombre_carpeta

 ### ***🐙 GIT - COMANDOS BÁSICOS***

🔄 Flujo Diario

 **Actualizar desde main _(¡SIEMPRE!)_**

    git pull origin main

 **Ver en qué rama estoy**

    git branch -a

 **Cambiar a mi rama**

    git checkout mi_rama

 **Subir mis cambios**

    git add .

    git commit -m "mensaje claro"

    git push origin mi_rama


 ### ***📋 Ver Información***


    git status       *->Ver estado actual*

    git log --oneline  *->Ver historial*

 ## ***🎯 REGLAS DE ORO***

✅ **NUNCA** hacer push a main

✅ **SIEMPRE** hacer **pull origin main** antes de trabajar y antes de hacer Pull Request

✅ **CADA UNO** en su propia rama

✅ **SÓLO** merge a main por **Pull Request** en GitHub


-------------------------------------------------------------------------------------------------------------------------

 ## Metodología de trabajo RESUMIDA: 


1- Clonar el repositorio de Los Idos en una carpeta llamada 

    git clone https://github.com/HotCode2025/Los_Idos_SegundoSemestre.git 
    
    Los_Idos_SegundoSemestre 
    
    cd Los_Idos_SegundoSemestre


2- Crear una rama nueva con el nombre de quien la está trabajando 

    git checkout -b rama_JuanPerez


3- Comando para ver las ramas disponibles

    git branch -a


4- Cambiar a tu rama
   
    git checkout rama_JuanPerez


## Para subir cambios: 

1- Traer el contenido más reciente y para evitar conflictos:

    git pull origin main

2- Agregar cambios y confirmarlos en tu propia rama: 

    git add . 
    
    git commit -m "Mensaje con información sobre el cambio"

3- Subir cambios a la rama (No a MAIN)

    git push origin **rama_JuanPerez**

4- Ir a github y aprobar Pull Request de la rama, luego de aprobarlo, desde Git Bash CAMBIAR A LA RAMA MAIN:

    git checkout main
    git pull origin main

5- Crear el tag anotado:

    git tag -a v0.1.0 -m "v0.1.0: estructura base del proyecto X"

6- Verificar el tag: 

    git tag
    git show v0.1.0

7- Subir el tag:

    git push origin v0.1.0
    # (opcional) subir todos los tags locales:
    # git push --tags

8- Usar el tag (para lectura o para hotfix): 

    git checkout v0.1.0            # detached HEAD (solo lectura)
    git checkout -b hotfix/v0.1.1 v0.1.0  # rama desde el tag

9- SI FUE UN ERROR, para borrar el tag: 

    git tag -d v0.1.0
    git push origin :refs/tags/v0.1.0

*RESUMEN FÁCIL:*

    git checkout main
    git pull origin main
    git tag -a v1.0.0 -m "v1.0.0: entrega final"
    git push origin v1.0.0


**Para más comandos sobre tags, leer guía al final.**

-------------------------------------------------------------------------------------------------------------------------

 ## METODOLOGÍA DE TRABAJO COMPLETA 
 

 ### 🚀 CONFIGURACIÓN INICIAL
 

1. Clonar el repositorio

       git clone https://github.com/HotCode2025/los_Idos_SegundoSemestre.git los_Idos_SegundoSemestre

2. Entrar a la carpeta

       cd Los_Idos_SegundoSemestre

3. Crear tu rama personal

       git checkout -b rama_JuanPerez

4. Verificar ramas disponibles

       git branch -a

5. Cambiar a tu rama (si no estás en ella)

       git checkout rama_JuanPerez

 ### 🔄 CICLO DIARIO DE TRABAJO
 

1- **SIEMPRE SIEMPRE SIEMPRE empezar actualizando desde main**

    git pull origin main

 *Trabajar en tus archivos...*
 *(hacés tus modificaciones)*

2- Agregar cambios al staging

    git add .

3- Hacer commit con mensaje descriptivo

    git commit -m "feat: agregar funcionalidad de login con validación"

4- Subir cambios a **TU RAMA**, **NO a main**

    git push origin rama_JuanPerez

### 📋 BUENAS PRÁCTICAS PARA COMMITS

 **Ejemplos de mensajes claros para features, fixes, documentación, refactorización:**
 
    git commit -m "feat: implementar sistema de autenticación para login"

    git commit -m "fix: corregir error en página de bienvenida"

    git commit -m "docs: actualizar documentación del API-Reference"

    git commit -m "refactor: optimizar función de búsqueda"


### 🔍 COMANDOS ADICIONALES ÚTILES


**- Ver estado de los archivos**

    git status


**- Ver cambios específicos**

    git diff


**- Ver historial de commits**

    git log --oneline --graph


**- Si necesitas descartar cambios locales**

    git checkout -- nombre_archivo.py


**Si te equivocaste de rama al hacer commit**

    git checkout rama_correcta

    git cherry-pick commit_hash


### ⚠️ **REGLAS DE ORO PARA EL EQUIPO**

NUNCA hacer push directamente a main

SIEMPRE hacer pull origin main antes de empezar a trabajar y antes de subir cambios

CADA PERSONA trabaja en su rama personal

SOLO merge a main via Pull Request aprobado

COMUNICAR cuando se van a subir cambios


### 🎯 EJEMPLO PRÁCTICO DE TRABAJO

**Lunes**

git pull origin main
*Trabajo en la clase 3 de python...*

    git add .

    git commit -m "clase 3 de python"

    git push origin rama_JuanPerez


**Martes - continuar trabajo**

    git pull origin main  ***¡Importante actualizar!***

*Más trabajo...*


    git add .

    git commit -m "clase 4 de python"

    git push origin rama_JuanPerez


 
 *GESTIÓN DE PULL REQUESTS*
 
**Cuando termines una funcionalidad completa:**

*Ir a GitHub → Pull Requests → New Pull Request*

Comparar: rama_JuanPerez → main

Solicitar review de 1 compañero

Esperar aprobación antes de merge


 ## **FLUJO PARA LLEVAR LA RAMA A MAIN**
 

**--Paso 1: PREPARAR tu rama local**


*Asegurate de tener todo actualizado*


    git checkout rama_JuanPerez

    git pull origin main  # ¡CRUCIAL!

    git push origin rama_JuanPerez  # subir últimos cambios



**--Paso 2: IR A GITHUB y crear Pull Request**


Abrir el repositorio en GitHub

Ir a la pestaña "Pull Requests"

Click en "New Pull Request"

Configurar:

  base: main (hacia dónde va)
  
  compare: rama_JuanPerez (tu rama)
  

**--Paso 3: REVISIÓN y APPROVAL**

Agregar reviewers (1 compañero mínimo)

Esperar que revisen y aprueben

Resolver comentarios si los hay


**--Paso 4: MERGE a main**


Una vez aprobado, click en "Merge pull request"

NO usar "Squash and merge" a menos que el equipo lo decida

SÍ usar "Create a merge commit"


**--Paso 5: LIMPIEZA posterior**


*Actualizar tu local main*

    git checkout main

    git pull origin main


*Eliminar tu rama local (opcional)*

    git branch -d rama_JuanPerez


*Eliminar rama remota (opcional)*

    git push origin --delete rama_JuanPerez


## 🚨 ¿POR QUÉ NO git push origin main?


### **¡NUNCA HAGAN ESTO!**

    git push origin main   ❌ **PROHIBIDO**



 Razones:
  
 1. Omite el proceso de revisión
 
 2. Puede romper el código de otros
 
 3. No deja historial de quién aprobó
 
 4. Elimina la trazabilidad



    
## 📊 COMANDOS PARA VER ESTADO ANTES DEL PR (Pull Request)


**Ver diferencias con main**

    git diff main..rama_JuanPerez



**Ver commits que se van a mergear**

    git log main..rama_JuanPerez



**Ver estado del working directory**

    git status



### 🎯 **EJEMPLO PRÁCTICO DE PULL REQUEST**



**1. Preparar mi rama**

    git checkout rama_JuanPerez

    git pull origin main



*Resolver conflictos si los hay*



    git add .

    git commit -m "merge: actualizar con main"

    git push origin rama_JuanPerez



**2. Crear PR en GitHub (desde la web)**



**3. Esperar approval de 1 compañero**



**4. Después del merge en GitHub:**

    git checkout main

    git pull origin main  *->traer los cambios mergeados*



**5. Opcional: eliminar rama**

    git branch -d rama_JuanPerez

    git push origin --delete rama_JuanPerez



======================== **GUÍA Y TIPS SOBRE TAGS** ========================


> Los **tags** marcan puntos específicos del historial (versiones, entregas, hitos).
> Se usan para identificar **versiones estables** del proyecto, normalmente en `main` **después** de mergear un Pull Request.

---

## 1) ¿Qué es un tag?

* Un **tag** es una etiqueta inmutable que “apunta” a un commit.
* Sirve para **versionar** (ej.: `v1.0.0`) o marcar **hitos** (ej.: `entrega-parcial-1`).
* En GitHub, los tags pueden convertirse en **Releases** con notas de cambios (*changelog*), binarios, etc.

---

## 2) Tipos de tags

| Tipo                      | Comando                          | Cuándo usar                          | Pros                                             | Contras                                     |
| ------------------------- | -------------------------------- | ------------------------------------ | ------------------------------------------------ | ------------------------------------------- |
| **Anotado (recomendado)** | `git tag -a v1.0.0 -m "mensaje"` | Releases, entregas formales          | Guarda autor, fecha, mensaje; base para Releases | Un poco más de tipeo                        |
| **Lightweight**           | `git tag v1.0.0`                 | Marcadores rápidos y temporales      | Simple y veloz                                   | No guarda metadatos; no ideal para releases |
| **Firmado (GPG)**         | `git tag -s v1.0.0 -m "mensaje"` | Proyectos que requieren autenticidad | Verificable criptográficamente                   | Requiere configurar GPG                     |

> **Recomendación del equipo:** usar **anotados** (`-a -m`) para todas las entregas/versiones.

---

## 3) Convención SemVer (Semántica de versiones)

Formato: `vMAJOR.MINOR.PATCH`

* **MAJOR**: cambios incompatibles (breaking changes).
* **MINOR**: nuevas features compatibles.
* **PATCH**: fixes sin romper compatibilidad.

**Ejemplos (Los_Idos):**

* `v0.1.0` – Estructura base del proyecto.
* `v0.2.0` – Módulo Login completo.
* `v0.2.1` – Fix de validaciones de login.
* `v1.0.0` – Entrega final del semestre.

---

## 4) Cuándo crear un tag (flujo de equipo)

1. **Trabajás en tu rama** y hacés PR → *no taggear aquí*.
2. **Se aprueba el PR y se mergea a `main`**.
3. **Ahora sí**: en `main`, crear el **tag** de versión y pushearlo a GitHub.
4. (Opcional) Crear **Release** en GitHub a partir del tag.

> Regla de oro: **NUNCA** taggear en tu rama personal ni antes del merge a `main`.

---

## 5) Comandos esenciales

### 5.1 Crear tag (anotado)

```
git checkout main
git pull origin main

git tag -a v1.0.0 -m "v1.0.0: entrega final del semestre"
git push origin v1.0.0
# (opcional) subir todos los tags locales pendientes
# git push --tags
```

### 5.2 Crear tag sobre un commit anterior

```
git log --oneline       # copiate el hash, ej: a1b2c3d
git tag -a v0.2.0 a1b2c3d -m "v0.2.0: módulo login completo"
git push origin v0.2.0
```

### 5.3 Listar y ver información

```
git tag                 # lista todos los tags
git tag -l "v1.*"       # filtra por patrón
git show v1.0.0         # detalles del tag/commit
```

### 5.4 Checkout de un tag (modo lectura)

```
git checkout v1.0.0     # detached HEAD (no es una rama)
```

> Para trabajar desde un tag (p. ej. hotfix):

```
git checkout -b hotfix/v1.0.1 v1.0.0
# ... hacés el fix, PR → merge → tag nuevo v1.0.1 en main
```

### 5.5 Borrar tags

```
# Local:
git tag -d v1.0.0

# Remoto (GitHub):
git push origin :refs/tags/v1.0.0
```

### 5.6 Renombrar un tag (técnica segura)

> No existe “rename” directo; recrealo. Si el tag ya estaba en remoto, borrarlo también.

```
# Crear uno nuevo apuntando al mismo commit
git tag -a v1.0.1 -m "rename desde v1.0.0"

# Borrar el viejo local y remoto
git tag -d v1.0.0
git push origin :refs/tags/v1.0.0

# Subir el nuevo
git push origin v1.0.1
```

### 5.7 Mover un tag a otro commit (⚠️ con cuidado)

```
git tag -f -a v1.0.0 <nuevo_hash> -m "mover v1.0.0 al commit correcto"
git push -f origin v1.0.0   # puede estar bloqueado si protegen tags
```

---

## 6) Comparaciones y changelog

### 6.1 Diff entre tags

```
git diff v0.2.0..v1.0.0
```

### 6.2 Commits entre tags

```
git log --oneline v0.2.0..v1.0.0
```

### 6.3 Ordenar tags por versión (útil en scripts)

```
git tag --sort=v:refname   # orden natural (v1 < v1.2 < v1.10)
```

---

## 7) Traer tags del remoto y sincronización

```
git fetch --tags                 # trae tags faltantes
git pull --tags                  # (equivalente común en varios setups)
git fetch origin --prune --tags  # limpia referencias obsoletas
```

---

## 8) Releases en GitHub (desde un tag)

1. Pusheá el tag (`git push origin v1.0.0`).
2. En GitHub: **Releases → Draft a new release**.
3. Elegí el **tag** (`v1.0.0`), título y descripción (changelog).
4. (Opcional) Adjuntá binarios/artefactos.
5. **Publish release**.

> Alternativa con CLI de GitHub (`gh`):

```
gh release create v1.0.0 --title "v1.0.0" --notes-file CHANGELOG.md
```

---

## 9) Integración con CI/CD (opcional)

* Muchos pipelines se gatillan **cuando hay un tag nuevo** (ej.: publicar contenedores, compilar artefactos, generar changelog).
* En GitHub Actions, usá disparadores:

```
on:
  push:
    tags:
      - 'v*.*.*'
```

---

## 10) Buenas prácticas del equipo

* **Crear tags solo en `main`** y **después** de mergear PRs aprobados.
* Usar **anotados** (`-a -m`) y **SemVer** (`vMAJOR.MINOR.PATCH`).
* Mantener un **CHANGELOG** (manual o auto-generado).
* Evitar **mover/borrar** tags publicados; si es imprescindible, **comunicar** al equipo.
* Considerar **proteger tags** en GitHub (Settings → Rules → *Tag protection rules*).

---

## 11) Errores comunes y cómo resolverlos

**“¿Por qué no veo el tag?”**

* No lo subiste: `git push origin vX.Y.Z`
* No lo trajiste: `git fetch --tags`

**“Detached HEAD” al hacer checkout del tag**

* Es normal: estás “parado” sobre un commit sin rama.
* Si querés trabajar: `git checkout -b rama-desde-tag vX.Y.Z`

**“No me deja pushear el tag”**

* Puede haber **reglas de protección** de tags en GitHub.
* Consultá con el owner o usá otro nombre/flujo establecido.

**“Quiero cambiar el nombre de un tag publicado”**

* Borrar remoto + local del viejo → crear y pushear el nuevo (ver 5.6).

---

## 12) Plantilla de mensajes para tags

```
v1.2.0: integración de base de datos y reportes
- Nueva: CRUD de clientes y ventas
- Nueva: Reporte mensual PDF
- Fix: validación de email en formulario de registro
- Docs: README actualizado con variables de entorno
```

Guardar como **nota del tag** o **Release notes**.

---

## 13) Ejemplo aplicado (Los_Idos)

**Objetivo:** cerrar la entrega del Módulo Login.

```
# 1) PR aprobado y mergeado → main actualizado
git checkout main
git pull origin main

# 2) Crear tag de versión
git tag -a v0.2.0 -m "v0.2.0: módulo Login completo (validación + tests básicos)"

# 3) Subir tag
git push origin v0.2.0

# 4) (Opcional) Crear Release en GitHub con changelog
```

**Siguientes hitos sugeridos:**

* `v0.3.0` – Integración Base de Datos (migraciones + seed)
* `v0.4.0` – Reportes / UI final
* `v1.0.0` – Entrega final del semestre

---

## 14) Cheklist previo a taggear

* [ ] PRs relevantes **mergeados** en `main`.
* [ ] `main` **compila** y **tests pasan**.
* [ ] Cambios **documentados** (README/CHANGELOG).
* [ ] Nombre **SemVer** elegido (ej.: `v0.3.0`).
* [ ] Crear **tag anotado** y **pushear** a GitHub.
* [ ] (Opcional) Crear **Release** con notas.

---

## 15) Resumen FÁCIL

```
git checkout main
git pull origin main
git tag -a v1.0.0 -m "v1.0.0: entrega final"
git push origin v1.0.0
```


