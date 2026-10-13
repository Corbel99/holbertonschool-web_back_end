#!/usr/bin/env python3
"""Simuler le téléchargement asynchrone de films."""

import asyncio
import time


async def download_movie(name: str, delay: int) -> str:
    """Simuler le téléchargement d'un film.

    Args:
        name (str): Le nom du film.
        delay (int): La durée simulée du téléchargement en secondes.

    Returns:
        str: Le nom du film téléchargé.
    """
    # Afficher le début du téléchargement et le temps écoulé
    print(
        f"[{time.time() - start_time:.2f}s] "
        f"Début du téléchargement : {name}"
    )

    # Simuler une attente sans bloquer les autres tâches asynchrones
    await asyncio.sleep(delay)

    # Afficher la fin du téléchargement et le temps écoulé
    print(
        f"[{time.time() - start_time:.2f}s] "
        f"Téléchargement terminé : {name}"
    )

    # Renvoyer le nom du film une fois le téléchargement terminé
    return name


async def main() -> None:
    """Gérer les téléchargements des trois films."""
    # Créer le marqueur temporel au début des téléchargements
    global start_time
    start_time = time.time()

    # Programmer les trois téléchargements
    task_1 = asyncio.create_task(
        download_movie("Le Silence Des Agneaux", 3)
    )
    task_2 = asyncio.create_task(
        download_movie("La Chose", 5)
    )
    task_3 = asyncio.create_task(
        download_movie("L'Exorciste", 2)
    )

    # Attendre la fin des trois téléchargements
    results = await asyncio.gather(task_1, task_2, task_3)

    # Afficher les résultats
    print("Films téléchargés :", results)

    # Afficher la durée totale
    print(f"Durée totale : {time.time() - start_time:.2f} secondes")


if __name__ == "__main__":
    # Démarrer la boucle événementielle
    asyncio.run(main())
