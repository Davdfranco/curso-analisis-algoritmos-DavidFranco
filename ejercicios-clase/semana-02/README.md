# Semana 02 - Configuracion del entorno de trabajo

Este directorio contiene los ejercicios del Laboratorio 02: refactorizacion con PEP 8 y el clasificador de anios bisiestos.

## Entorno virtual

El entorno virtual se crea y se activa desde la **raiz del repositorio** (no desde esta carpeta), con:

```bash
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
```

Con el entorno activado (se ve el prefijo `(venv)` en la terminal), se instalan las dependencias y se generan con:

```bash
pip install matplotlib
pip freeze > requirements.txt
```

## Reproducir el entorno

Otra persona puede reproducir exactamente este entorno ejecutando, desde la raiz del repositorio:

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
