# Compose2Rancher Enterprise (C2R)

> **Herramienta empresarial para migrar aplicaciones Docker Compose hacia Rancher/Kubernetes de forma inteligente.**

---

## Descripción

Compose2Rancher Enterprise (C2R) es una herramienta diseñada para automatizar la migración de aplicaciones definidas mediante **Docker Compose** hacia **Kubernetes**, con especial enfoque en **Rancher v2.14.x**, **RKE2** y **K3s**.

A diferencia de herramientas tradicionales como **Kompose**, C2R no solo convierte un `docker-compose.yml`, sino que analiza la infraestructura completa de la aplicación para generar manifiestos optimizados y adaptados a entornos empresariales.

---

# Objetivos

* Automatizar la migración de Docker Compose hacia Kubernetes.
* Reducir errores manuales durante la conversión.
* Detectar configuraciones inseguras o incompletas.
* Generar manifiestos listos para Rancher.
* Aplicar buenas prácticas de Kubernetes automáticamente.
* Facilitar la migración de aplicaciones con datos persistentes.

---

# Características

## Análisis del proyecto

* Lectura de `docker-compose.yml`
* Lectura de `.env`
* Validación del Compose
* Inventario completo de servicios
* Inventario de imágenes
* Inventario de redes
* Inventario de volúmenes
* Inventario de puertos

---

## Conversión

* Deployment
* Service
* Namespace
* ConfigMap
* Secret
* PersistentVolumeClaim
* Ingress
* NetworkPolicy (Roadmap)

---

## Inteligencia basada en reglas

La herramienta identifica automáticamente servicios conocidos y aplica configuraciones recomendadas.

Ejemplos:

| Servicio   | Acción                         |
| ---------- | ------------------------------ |
| PostgreSQL | PVC + StartupProbe + Resources |
| MariaDB    | PVC + Resources                |
| Redis      | LivenessProbe + ReadinessProbe |
| NGINX      | Service + Ingress              |
| Apache     | Service + Ingress              |
| MongoDB    | PVC                            |
| RabbitMQ   | PVC + Probes                   |
| MinIO      | PVC + Resources                |

---

## Validaciones

Antes del despliegue se ejecutan automáticamente:

* docker compose config
* yamllint
* kubeconform
* kubectl --dry-run

---

## Reportes

La herramienta podrá generar:

* HTML
* JSON
* Excel

Incluyendo:

* Servicios
* Volúmenes
* Variables
* Riesgos detectados
* Recomendaciones

---

# Arquitectura

```
compose2rancher/

├── docs/
├── examples/
├── tests/
├── src/
│   └── compose2rancher/
│       ├── core/
│       ├── analyzers/
│       ├── converters/
│       ├── rancher/
│       ├── report/
│       ├── migration/
│       ├── templates/
│       ├── models/
│       └── utils/
├── pyproject.toml
└── README.md
```

---

# Flujo de trabajo

```
Docker Compose

↓

Validación

↓

Lectura .env

↓

Inventario

↓

Análisis

↓

Motor de reglas

↓

Conversión

↓

Post-Procesamiento

↓

Validación Kubernetes

↓

Reporte

↓

Deploy en Rancher
```

---

# Instalación

## Requisitos

* Python 3.12 o superior
* Docker Compose v2
* kubectl
* Kompose
* Git

---

## Clonar el repositorio

```bash
git clone https://github.com/ECMSolutions/compose2rancher.git

cd compose2rancher
```

---

## Crear entorno virtual

```bash
python3 -m venv .venv
```

Linux

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

---

## Instalar dependencias

```bash
pip install -U pip

pip install -e ".[dev]"
```

---

# Uso

Consultar ayuda

```bash
compose2rancher --help
```

Analizar un proyecto

```bash
compose2rancher analyze docker-compose.yml
```

Convertir

```bash
compose2rancher convert docker-compose.yml
```

Validar

```bash
compose2rancher validate
```

Generar reporte

```bash
compose2rancher report
```

Desplegar

```bash
compose2rancher deploy
```

---

# Roadmap

## Sprint 1

* Infraestructura
* CLI
* Logger
* Parser
* Inventario

---

## Sprint 2

* Integración con Kompose
* Deployment
* Service
* Namespace

---

## Sprint 3

* Volúmenes
* PersistentVolumeClaim
* StorageClass
* HostPath

---

## Sprint 4

* ConfigMap
* Secret
* Variables de entorno

---

## Sprint 5

* Ingress
* TLS
* Certificados

---

## Sprint 6

* Docker Registry
* Harbor
* ImagePullSecrets

---

## Sprint 7

* Validaciones
* yamllint
* kubeconform
* kubectl

---

## Sprint 8

* Reportes
* HTML
* JSON
* Excel

---

## Sprint 9

* API de Rancher
* GitOps
* Fleet
* ArgoCD

---

## Sprint 10

* CI/CD
* GitHub Actions
* GitLab CI
* Jenkins

---

# Calidad del código

El proyecto utiliza:

* Python 3.12+
* Typer
* Rich
* Loguru
* Pydantic v2
* PyYAML
* Jinja2

Herramientas de calidad:

* Ruff
* Black
* MyPy
* Pytest
* Coverage

---

# Estructura de desarrollo

Cada Sprint produce una versión funcional.

```
v0.1.0

↓

v0.2.0

↓

v0.3.0

↓

v1.0.0
```

El proyecto mantiene compatibilidad hacia atrás siempre que sea posible.

---

# Licencia

Este proyecto se distribuye bajo la licencia Apache 2.0.

---

# Estado del proyecto

**Versión actual**

```
v0.1.0-alpha
```

Estado:

**En desarrollo activo**

---

# Contribuciones

Las contribuciones son bienvenidas.

Antes de enviar un Pull Request:

1. Ejecutar Ruff.
2. Ejecutar Black.
3. Ejecutar MyPy.
4. Ejecutar Pytest.
5. Verificar cobertura mínima del 90%.

---

# Visión del proyecto

Compose2Rancher Enterprise busca convertirse en una plataforma de migración para Kubernetes y Rancher que permita transformar aplicaciones Docker Compose en despliegues empresariales listos para producción, incorporando análisis, validación, automatización y buenas prácticas de infraestructura como código.

