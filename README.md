# Laboratorio 1 - Señales y Sistemas

Este repositorio contiene el trabajo realizado para el Laboratorio 1 de la materia Señales y Sistemas, enfocado en el análisis de audio mediante Series de Fourier.

## Estructura del Proyecto

```
Laboratorio 1 - S&S/
├── Actividad 1/
│   ├── Codigo1_Problema 1.py
│   └── Codigo2_Problema 2.py
├── Actividad 2/
│   ├── Codigo3_Problema 1.py
│   ├── Codigo4_Problema 3.py
│   └── Extra/
│       └── Error_vs_k.py
├── Actividad 3/
│   └── Problema 1/
│       ├── Problema1_do.py
│       ├── Problema1_la.py
│       ├── Problema2_acorde_do_mayor.py
│       ├── Problema2_acorde_si_menor.py
│       ├── acorde-de-guitarra-do-mayor_.mp3
│       ├── acorde-de-guitarra-si-menor_.mp3
│       ├── nota_do_1_octava.mp3
│       └── nota_la_2_octava.mp3
├── Referencias/
│   ├── A Study of The Gibbs Phenomenon in Fourier Series and Wavelets.pdf
│   └── Señales y sistemas (Alan V. Oppenheim, Alan S. Willsky etc.).pdf
└── Laboratorio 1.docx
```

## Descripción de las Actividades

### Actividad 1
Análisis básico de señales y sistemas.

### Actividad 2
Implementación de algoritmos de procesamiento de señales.

### Actividad 3 - Problema 1
**Análisis de Audio como Serie de Fourier**

Este módulo contiene scripts para analizar archivos de audio MP3 y representarlos como series de Fourier, mostrando:
- Frecuencia fundamental
- Armónicos
- Espectro completo del audio

#### Archivos principales:
- `Problema1_do.py` - Análisis de nota Do
- `Problema1_la.py` - Análisis de nota La
- `Problema2_acorde_do_mayor.py` - Análisis de acorde Do mayor
- `Problema2_acorde_si_menor.py` - Análisis de acorde Si menor

## Requisitos

- Python 3.7+
- numpy
- matplotlib
- scipy
- librosa

## Instalación

```bash
pip install numpy matplotlib scipy librosa
```

## Uso

Para ejecutar el análisis de un archivo de audio:

```python
python Problema2_acorde_do_mayor.py
```

## Características

- Carga de archivos MP3
- Análisis de frecuencia fundamental
- Identificación de armónicos
- Visualización del espectro completo
- Representación como serie de Fourier

## Referencias

- Oppenheim, A. V., & Willsky, A. S. (1997). *Señales y sistemas*
- Estudio del fenómeno de Gibbs en series de Fourier y wavelets

## Autor

Bruno - Estudiante de Ingeniería

