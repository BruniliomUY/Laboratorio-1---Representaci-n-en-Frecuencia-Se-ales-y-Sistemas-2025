# Análisis de Audio como Serie de Fourier

#Imports
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fft import fft
from scipy.signal import spectrogram
import librosa

# Función para cargar un archivo MP3 y obtener la transformada de Fourier del audio
def mp3_to_fft(filename):
    # Cargar el archivo MP3 utilizando librosa
    base_dir = os.path.dirname(os.path.abspath(__file__))
    audio_path = filename if os.path.isabs(filename) else os.path.join(base_dir, filename)
    audio, sr = librosa.load(audio_path, sr=None)

    # Calcular la Transformada de Fourier
    fft_result = fft(audio)

    # Calcular las frecuencias correspondientes
    freqs = np.fft.fftfreq(len(fft_result), 1/sr)

    return freqs, np.abs(fft_result), sr

# Esta función simula el análisis de Fourier Series para estudiantes
def analyze_audio_fourier_series(filename, max_harmonics=11):
    """
    Analiza un archivo de audio MP3 y presenta el espectro como si fuera una Serie de Fourier
    mostrando solo la frecuencia fundamental y sus armónicos
    """
    # Analizar el audio y obtener la FFT
    freqs, fft_result, sr = mp3_to_fft(filename)
    magnitude = np.abs(fft_result)

    # Solo considerar frecuencias positivas
    positive_freq_idx = freqs > 0
    freqs_positive = freqs[positive_freq_idx]
    magnitude_positive = magnitude[positive_freq_idx]

    # Encontrar la frecuencia fundamental (pico más prominente en frecuencias bajas)
    # Buscar en el rango de frecuencias típicas de instrumentos musicales (80-1000 Hz)
    low_freq_mask = (freqs_positive >= 80) & (freqs_positive <= 1000)
    low_freq_indices = np.where(low_freq_mask)[0]

    if len(low_freq_indices) > 0:
        # Encontrar el pico más prominente en esta región
        fundamental_idx = low_freq_indices[np.argmax(magnitude_positive[low_freq_mask])]
        fundamental_freq = freqs_positive[fundamental_idx]
    else:
        # Si no se encuentra, usar el pico global
        fundamental_idx = np.argmax(magnitude_positive)
        fundamental_freq = freqs_positive[fundamental_idx]

    print(f"Frecuencia fundamental detectada: {fundamental_freq:.2f} Hz")

    # Calcular las frecuencias de los armónicos
    harmonic_freqs = []
    harmonic_magnitudes = []

    for n in range(1, max_harmonics + 1):
        target_freq = n * fundamental_freq

        # Encontrar la frecuencia más cercana en nuestro espectro
        freq_diff = np.abs(freqs_positive - target_freq)
        closest_idx = np.argmin(freq_diff)
        # Buscar todos los índices dentro del rango de tolerancia (±0.5%)
        tolerance = 0.01  # +-1%
        in_window = np.where(np.abs(freqs_positive - target_freq) / target_freq < tolerance)[0]
        if len(in_window) > 0:
            avg_magnitude = np.max(magnitude_positive[in_window])
            harmonic_freqs.append(target_freq)
            harmonic_magnitudes.append(avg_magnitude)
        else:
            harmonic_freqs.append(target_freq)
            harmonic_magnitudes.append(0)

    return harmonic_freqs, harmonic_magnitudes, fundamental_freq, freqs, fft_result, sr

# Esta función genera una visualización del espectro completo del archivo
def visualizar_acorde(filename, plot_handles=None):
    freqs, fft_result, sr = mp3_to_fft(filename)
    if plot_handles is None:
        plt.figure(figsize=(12, 6))
    else:
        plt.sca(plot_handles)
    plt.title('Espectro Completo del Audio: ' + filename)
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Magnitud')
    plt.plot(freqs[:len(freqs)//2], np.abs(fft_result)[:len(fft_result)//2], 'lightgray', alpha=0.7)
    plt.xlim(0, 2000)
    plt.ylim(5, 10000)
    plt.yscale('log')
    plt.grid(True, alpha=0.3)
    plt.show()

# Esta función genera una visualización estilo Serie de Fourier
def visualizar_nota(filename, plot_handles=None):
    harmonic_freqs, harmonic_mags, f0, freqs, fft_result, sr = analyze_audio_fourier_series(filename)
    if plot_handles is None:
        plt.figure(figsize=(12, 6))
    else:
        plt.sca(plot_handles)
    harmonic_numbers = range(1, len(harmonic_freqs) + 1)

    # Crear gráfico de barras para los armónicos
    (markerline, stemlines, baseline) = plt.stem(harmonic_numbers*f0, harmonic_mags, basefmt=" ")
    plt.setp(markerline, color='steelblue', marker='o', markersize=8)
    plt.setp(stemlines, color='darkblue', linewidth=2, alpha=0.8)

    # Agregar etiquetas con las frecuencias
    for i, (freq, mag) in enumerate(zip(harmonic_freqs, harmonic_mags)):
        if mag > max(harmonic_mags) * 0.1:  # Solo etiquetar armónicos significativos
            plt.text((i+1)*f0, mag + max(harmonic_mags)*0.02, f'{freq:.0f}Hz',
                     ha='center', va='bottom', fontsize=9, rotation=45)

    plt.xlabel('Frecuencia del armónico (Hz)')
    plt.ylabel('Magnitud')
    plt.title(f'Representación como Serie de Fourier (f₀ = {f0:.2f} Hz), archivo: {filename}')
    plt.grid(True, alpha=0.3, axis='y')
    plt.xlim(0, (len(harmonic_freqs) + 0.5)*f0)
    plt.xticks(list(harmonic_numbers*f0))
    plt.ylim(5, 10000)
    plt.yscale('log')
    # Superponer el espectro completo como línea gris claro
    plt.plot(freqs[:len(freqs)//2], np.abs(fft_result)[:len(fft_result)//2], color='lightgray', alpha=0.5, label='Espectro completo')

    # Añadir línea vertical para mostrar la fundamental
    plt.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='Frecuencia fundamental')
    plt.legend()
    plt.xlim(0, 2000)
    plt.show()

# Analizar el archivo de audio
mp3_file = './acorde-organo-do-mayor'

# Visualizar
visualizar_nota('/acorde-organo-do-mayor')
visualizar_acorde(mp3_file)